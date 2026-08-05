#!/usr/bin/env python3
"""check_wids.py — W-ID resolvability + internal-link + forbidden-path pass (P-D7 support).

Exit 1 if: (a) a W-ID cited anywhere in the package is not defined in WARRANTS.md, or a defined
W-record is cited nowhere (orphan → warning only); (b) a relative markdown link inside the
package points at a file that does not exist; (c) any package file contains an absolute
user-specific path or a SEAS-relative path used as a *dependency* (heuristic: outside the
KNOWN-REPOS key and STATE/probes provenance columns, flags `/Users/`, `~/Projects/`,
`~/Development/`). Plain stdlib; run from anywhere: `python3 check_wids.py [package_dir]`.
"""
import argparse
from dataclasses import dataclass, field
import hashlib
import json
import os
import re
import sys
from pathlib import Path, PurePosixPath

WID_DEF_RE = re.compile(r"^### (W-\d{3}) ", re.MULTILINE)
WID_USE_RE = re.compile(r"\bW-\d{3}\b")
LINK_RE = re.compile(r"\]\((?!https?://|#|mailto:)([^)#]+)")
ABS_PATH_RE = re.compile(r"/Users/\w+|(?<![\w.])~/(?:Projects|Development)/")
HEX40_RE = re.compile(r"^[0-9a-f]{40}$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
STAMP_RE = re.compile(
    r"<!-- claude-package-manifest:v1 sha256=([0-9a-f]{64}) "
    r"source_commit=([0-9a-f]{40}) -->"
)


@dataclass
class ValidationResult:
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    extras: list[str] = field(default_factory=list)
    source_only: list[str] = field(default_factory=list)
    checked_files: int = 0

    @property
    def ok(self):
        return not self.failures


def safe_manifest_relative(value, label, failures):
    if not isinstance(value, str) or not value:
        failures.append(f"{label} must be a non-empty string")
        return None
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        failures.append(f"unsafe {label}: {value!r}")
        return None
    return path


def validate_deployment(installation_root, manifest_path, stamp_path):
    result = ValidationResult()
    root = Path(installation_root).resolve()
    manifest_file = Path(manifest_path)
    stamp_file = Path(stamp_path)

    if manifest_file.is_symlink() or not manifest_file.is_file():
        result.failures.append("manifest is missing or is not a regular non-symlink file")
        return result
    raw = manifest_file.read_bytes()
    manifest_digest = hashlib.sha256(raw).hexdigest()
    try:
        manifest = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError):
        result.failures.append("manifest is not valid UTF-8 JSON")
        return result
    if not isinstance(manifest, dict):
        result.failures.append("manifest root must be an object")
        return result

    if manifest.get("schema_version") != 1:
        result.failures.append("unsupported manifest schema_version")
    if manifest.get("dirty_source") is not False:
        result.failures.append("release manifest must declare dirty_source false")
    source_commit = manifest.get("source_commit")
    if not isinstance(source_commit, str) or not HEX40_RE.fullmatch(source_commit):
        result.failures.append("manifest source_commit must be 40 lowercase hex characters")
    spec_digest = manifest.get("package_spec_sha256")
    if not isinstance(spec_digest, str) or not HEX64_RE.fullmatch(spec_digest):
        result.failures.append("manifest package_spec_sha256 must be 64 lowercase hex characters")
    entries = manifest.get("entries")
    links = manifest.get("source_only_links")
    if not isinstance(entries, list):
        result.failures.append("manifest entries must be a list")
        entries = []
    if not isinstance(links, list):
        result.failures.append("manifest source_only_links must be a list")

    if stamp_file.is_symlink() or not stamp_file.is_file():
        result.failures.append("canonical manifest stamp is missing")
    else:
        stamps = STAMP_RE.findall(stamp_file.read_text(encoding="utf-8"))
        if (manifest_digest, source_commit) not in stamps:
            result.failures.append("manifest digest/source commit is not canonically stamped")

    destinations = set()
    sources = set()
    expected_skill = set()
    expected_agents = set()
    markdown_files = {}
    required_keys = {"destination", "source", "size", "mode", "sha256"}
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict) or set(entry) != required_keys:
            result.failures.append(f"manifest entry {index} has invalid fields")
            continue
        destination_value = entry["destination"]
        source_value = entry["source"]
        destination = safe_manifest_relative(
            destination_value, f"entry {index} destination", result.failures
        )
        source = safe_manifest_relative(source_value, f"entry {index} source", result.failures)
        if destination is None or source is None:
            continue
        if destination_value in destinations:
            result.failures.append(f"duplicate manifest destination: {destination_value}")
            continue
        if source_value in sources:
            result.failures.append(f"duplicate manifest source: {source_value}")
            continue
        destinations.add(destination_value)
        sources.add(source_value)
        if destination.parts[:2] == ("skills", "delegation-triage"):
            expected_skill.add(destination_value)
        elif destination.parts[:1] == ("agents",):
            expected_agents.add(destination_value)
        elif destination_value != "delegation.md":
            result.failures.append(f"destination is outside declared package trees: {destination_value}")

        target = root / Path(*destination.parts)
        resolved = target.resolve(strict=False)
        try:
            resolved.relative_to(root)
        except ValueError:
            result.failures.append(f"manifest destination escapes installation root: {destination_value}")
            continue
        if target.is_symlink() or not target.is_file():
            result.failures.append(f"manifest file missing or non-regular: {destination_value}")
            continue
        data = target.read_bytes()
        if destination.suffix.lower() == ".md":
            markdown_files[destination_value] = target
        if not isinstance(entry["size"], int) or entry["size"] < 0 or len(data) != entry["size"]:
            result.failures.append(f"size mismatch: {destination_value}")
        if not isinstance(entry["sha256"], str) or not HEX64_RE.fullmatch(entry["sha256"]):
            result.failures.append(f"invalid sha256 field: {destination_value}")
        elif hashlib.sha256(data).hexdigest() != entry["sha256"]:
            result.failures.append(f"digest mismatch: {destination_value}")
        if entry["mode"] not in ("0644", "0755"):
            result.failures.append(f"invalid mode field: {destination_value}")
        elif f"{os.stat(target, follow_symlinks=False).st_mode & 0o777:04o}" != entry["mode"]:
            result.failures.append(f"mode mismatch: {destination_value}")

    result.checked_files = len(entries)
    skill_root = root / "skills" / "delegation-triage"
    actual_skill = set()
    if skill_root.is_dir():
        for path in skill_root.rglob("*"):
            if path.is_file() or path.is_symlink():
                actual_skill.add(str(path.relative_to(root)))
    for extra in sorted(actual_skill - expected_skill):
        result.failures.append(f"unlisted package file: {extra}")

    agents_root = root / "agents"
    if agents_root.is_dir():
        for path in sorted(agents_root.glob("*.md")):
            relative = str(path.relative_to(root))
            if relative not in expected_agents:
                result.extras.append(relative)

    declarations = set()
    declaration_reasons = {}
    for index, link in enumerate(links):
        if not isinstance(link, dict) or set(link) != {"source", "target", "reason"}:
            result.failures.append(f"source_only_links entry {index} has invalid fields")
            continue
        source = link["source"]
        target = link["target"]
        reason = link["reason"]
        if source not in markdown_files:
            result.failures.append(f"source-only link source is not packaged Markdown: {source}")
            continue
        if not isinstance(target, str) or not target or not isinstance(reason, str) or not reason:
            result.failures.append(f"source_only_links entry {index} has invalid target/reason")
            continue
        edge = (source, target)
        if edge in declarations:
            result.failures.append(f"duplicate source-only edge: {source} -> {target}")
            continue
        declarations.add(edge)
        declaration_reasons[edge] = reason

    observed_edges = set()
    for source, path in sorted(markdown_files.items()):
        text = path.read_text(encoding="utf-8")
        for target_value in LINK_RE.findall(text):
            target_value = target_value.strip()
            if not target_value or target_value.startswith("<"):
                continue
            edge = (source, target_value)
            observed_edges.add(edge)
            target_path = (path.parent / target_value).resolve(strict=False)
            try:
                target_relative = str(target_path.relative_to(root))
            except ValueError:
                result.failures.append(f"link target escapes installation root: {source} -> {target_value}")
                continue
            packaged = target_relative in destinations
            if target_path.is_dir():
                prefix = target_relative.rstrip("/") + "/"
                packaged = any(destination.startswith(prefix) for destination in destinations)
            exists = target_path.exists()
            declared = edge in declarations
            if declared:
                if exists or packaged:
                    result.failures.append(
                        f"declared source-only edge target is present: {source} -> {target_value}"
                    )
                else:
                    result.source_only.append(f"{source} -> {target_value}")
            elif not exists or not packaged:
                result.failures.append(f"undeclared missing package link: {source} -> {target_value}")

        for line_number, line in enumerate(text.splitlines(), 1):
            if ABS_PATH_RE.search(line) and "local hint" not in line and "env-specific" not in line \
                    and not line.strip().startswith("| `"):
                result.failures.append(
                    f"{source}:{line_number}: absolute/user-specific path outside the locator key"
                )

    for source, target in sorted(declarations - observed_edges):
        result.failures.append(f"declared source-only edge is not present: {source} -> {target}")

    warrants_path = markdown_files.get("skills/delegation-triage/WARRANTS.md")
    defined = set()
    if warrants_path:
        defined = set(WID_DEF_RE.findall(warrants_path.read_text(encoding="utf-8")))
    if not defined:
        result.failures.append("no W-records defined in packaged WARRANTS.md")
    used = set()
    for destination, path in markdown_files.items():
        if destination != "skills/delegation-triage/WARRANTS.md":
            used |= set(WID_USE_RE.findall(path.read_text(encoding="utf-8")))
    for wid in sorted(used - defined):
        result.failures.append(f"packaged cited but undefined W-ID: {wid}")
    for wid in sorted(defined - used):
        result.warnings.append(f"packaged defined but never cited (orphan): {wid}")
    return result


def validate_source_declarations(pkg, failures):
    spec_path = pkg / "adapters" / "claude-code" / "package-spec.json"
    if not spec_path.is_file():
        return
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        failures.append("package specification is not valid UTF-8 JSON")
        return
    declarations = spec.get("source_only_links") if isinstance(spec, dict) else None
    if not isinstance(declarations, list):
        failures.append("package specification source_only_links must be a list")
        return
    seen = set()
    for index, declaration in enumerate(declarations):
        if not isinstance(declaration, dict) or set(declaration) != {"source", "target", "reason"}:
            failures.append(f"source-only declaration {index} has invalid fields")
            continue
        source_value = declaration["source"]
        target_value = declaration["target"]
        source_relative = safe_manifest_relative(
            source_value, f"source-only declaration {index} source", failures
        )
        if source_relative is None or not isinstance(target_value, str) or not target_value:
            failures.append(f"source-only declaration {index} has invalid target")
            continue
        edge = (source_value, target_value)
        if edge in seen:
            failures.append(f"duplicate source-only declaration: {source_value} -> {target_value}")
            continue
        seen.add(edge)
        source_path = pkg / Path(*source_relative.parts)
        if source_path.is_symlink() or not source_path.is_file():
            failures.append(f"source-only declaration source is missing: {source_value}")
            continue
        targets = {target.strip() for target in LINK_RE.findall(
            source_path.read_text(encoding="utf-8")
        )}
        if target_value not in targets:
            failures.append(
                f"declared source-only edge is not present: {source_value} -> {target_value}"
            )
            continue
        resolved = (source_path.parent / target_value).resolve(strict=False)
        try:
            resolved.relative_to(pkg.resolve())
        except ValueError:
            failures.append(f"source-only declaration escapes source root: {source_value} -> {target_value}")
            continue
        if not resolved.exists():
            failures.append(f"source-only declaration target is missing in source: {source_value} -> {target_value}")


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("package_dir", nargs="?", type=Path)
    parser.add_argument("--scope", choices=("source", "deployment"), default="source")
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args(argv[1:])
    if args.scope == "deployment" and args.manifest is None:
        parser.error("--manifest is required when --scope deployment")
    if args.scope == "source" and args.manifest is not None:
        parser.error("--manifest is valid only when --scope deployment")
    return args


def main(argv):
    args = parse_args(argv)
    if args.scope == "deployment":
        stamp_path = Path(__file__).resolve().parent / "agents" / "MANIFEST.md"
        result = validate_deployment(
            (args.package_dir or Path.cwd()).resolve(),
            args.manifest.resolve(),
            stamp_path,
        )
        for failure in result.failures:
            print(f"FAIL: {failure}")
        for warning in result.warnings:
            print(f"WARN: {warning}")
        for edge in result.source_only:
            print(f"SOURCE_ONLY: {edge}")
        for extra in result.extras:
            print(f"EXTRA: {extra}")
        print(
            f"{result.checked_files} files · {len(result.source_only)} SOURCE_ONLY · "
            f"{len(result.extras)} EXTRA: {'OK' if result.ok else 'FAIL'}"
        )
        return 0 if result.ok else 1
    pkg = (args.package_dir or Path(__file__).resolve().parent).resolve()
    md_files = sorted(pkg.rglob("*.md"))
    warrants = pkg / "WARRANTS.md"
    failures, warnings = [], []
    validate_source_declarations(pkg, failures)

    defined = set(WID_DEF_RE.findall(warrants.read_text(encoding="utf-8"))) if warrants.is_file() else set()
    if not defined:
        failures.append("no W-records defined in WARRANTS.md")

    used = set()
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(pkg)
        # Stage-2 validation 2026-07-10: archives + deployment stubs exempt.
        # 2026-07-24: vendored EXTERNAL artifacts exempt too — they are byte-copies of
        # third-party evidence, preserved verbatim, whose internal links resolve only in the
        # companion evidence store (see each dir's PROVENANCE.md). Verbatim fidelity of an
        # external record beats internal link resolution; corrections live in the citing W-record.
        if ("references/ARCHIVE" in str(rel)
                or str(rel) == "references/routing-table.md"
                or str(rel).startswith("docs/research/external/")):
            continue
        if f.name != "WARRANTS.md":
            used |= set(WID_USE_RE.findall(text))
        # relative links must resolve
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith("<"):
                continue
            if not (f.parent / target).exists():
                failures.append(f"{rel}: broken relative link -> {target}")
        # forbidden absolute/user paths (allow the marked env-hint column in WARRANTS' repo key)
        for n, line in enumerate(text.splitlines(), 1):
            if ABS_PATH_RE.search(line) and "local hint" not in line and "env-specific" not in line \
                    and not line.strip().startswith("| `"):
                failures.append(f"{rel}:{n}: absolute/user-specific path outside the locator key")

    for wid in sorted(used - defined):
        failures.append(f"cited but undefined W-ID: {wid}")
    for wid in sorted(defined - used):
        warnings.append(f"defined but never cited (orphan): {wid}")

    for f in failures:
        print(f"FAIL: {f}")
    for w in warnings:
        print(f"WARN: {w}")
    print(f"{len(md_files)} md files · {len(defined)} W-records defined · "
          f"{len(used)} cited: {'FAIL' if failures else 'OK'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
