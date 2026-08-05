#!/usr/bin/env python3
"""install.py — deploy the delegation-triage package to a consumer surface.

Targets:
  claude-code   copy knowledge surfaces + checks + probes/ into the skill home and roster
                definitions into the agents dir (default root: ~/.claude). Restart required —
                roster registers at session START.
  cowork        build a plugin zip (dist/delegation-roster-<version>.plugin) from canonical.
                Ships NO volatile state by design: degradation is a rule the skill carries,
                not dates in the artifact (operator direction 2026-07-10). Install via the
                Cowork plugin UI, then stamp agents/MANIFEST.md.
  codex         emit the consumer guidance fragment (AGENTS.md-style), package path resolved.

Every deploy is a recorded deployment: this script prints the sha256 table to paste into
agents/MANIFEST.md — it does not edit the manifest (curated by hand, by design).

Usage:
  python3 install.py claude-code [--root ~/.claude] [--check | --dry-run]
  python3 install.py cowork      [--version 0.3.0] [--check | --dry-run]
  python3 install.py codex       [--dest PATH]     (no --dest: prints to stdout)

Plain stdlib. Zips are deterministic (fixed timestamps), so --check byte-compares honestly.
"""
import argparse
import fnmatch
import hashlib
import io
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

PKG = Path(__file__).resolve().parent
PACKAGE_SPEC = PKG / "adapters" / "claude-code" / "package-spec.json"
PACKAGE_MANIFEST_NAME = "delegation-triage-package-manifest.json"
PLUGIN_NAME = "delegation-roster"
PLUGIN_VERSION_DEFAULT = "0.3.0"
PLUGIN_REFERENCES = ["ROUTES.md", "CONTRACT.md", "EPISTEMICS.md", "WARRANTS.md"]  # no STATE: by design
ZIP_DATE = (2026, 1, 1, 0, 0, 0)  # fixed → deterministic archive → --check is byte-honest


class PackageSpecError(ValueError):
    """The declared Claude package boundary is invalid."""


class DirtySourceError(RuntimeError):
    """Release materialization was requested from a dirty source tree."""


def require_clean_source(repo: Path):
    try:
        status = subprocess.run(
            ["git", "-C", str(repo), "status", "--porcelain=v1", "-uall"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except subprocess.CalledProcessError as exc:
        raise DirtySourceError("cannot establish clean source state") from exc
    if status:
        count = len(status.splitlines())
        raise DirtySourceError(f"release deployment refused: source tree has {count} change(s)")


def git_file_mode(source: Path):
    relative = str(source.relative_to(PKG))
    try:
        line = subprocess.run(
            ["git", "-C", str(PKG), "ls-files", "-s", "--", relative],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except subprocess.CalledProcessError as exc:
        raise PackageSpecError(f"cannot read tracked mode: {relative}") from exc
    mode = line.split(maxsplit=1)[0] if line else ""
    if mode == "100755":
        return "0755"
    if mode == "100644":
        return "0644"
    raise PackageSpecError(f"unsupported tracked file mode for {relative}: {mode or 'missing'}")


def build_manifest(pairs, spec, source_commit, spec_path):
    installation_root = Path(os.path.commonpath([str(destination) for _, destination in pairs]))
    if installation_root.is_file():
        installation_root = installation_root.parent
    entries = []
    source_destinations = {}
    for source, destination in pairs:
        source_relative = str(source.relative_to(PKG))
        destination_relative = str(destination.relative_to(installation_root))
        source_destinations[source_relative] = destination_relative
        data = source.read_bytes()
        entries.append({
            "destination": destination_relative,
            "source": source_relative,
            "size": len(data),
            "mode": git_file_mode(source),
            "sha256": sha256(data),
        })
    links = []
    for declaration in spec["source_only_links"]:
        if not isinstance(declaration, dict):
            raise PackageSpecError("source_only_links entries must be objects")
        source_relative = declaration.get("source")
        target = declaration.get("target")
        reason = declaration.get("reason")
        if source_relative not in source_destinations:
            raise PackageSpecError(f"source-only link source is not packaged: {source_relative}")
        if not isinstance(target, str) or not target or not isinstance(reason, str) or not reason:
            raise PackageSpecError("source-only link target and reason must be non-empty strings")
        links.append({
            "source": source_destinations[source_relative],
            "target": target,
            "reason": reason,
        })
    return {
        "schema_version": 1,
        "source_commit": source_commit,
        "dirty_source": False,
        "package_spec_sha256": sha256(spec_path.read_bytes()),
        "entries": sorted(entries, key=lambda entry: entry["destination"]),
        "source_only_links": sorted(links, key=lambda link: (link["source"], link["target"])),
    }


def manifest_bytes(manifest):
    return (json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def load_package_spec(path: Path):
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PackageSpecError(f"cannot load package spec: {exc}") from exc
    if not isinstance(spec, dict) or spec.get("schema_version") != 1:
        raise PackageSpecError("unsupported package spec schema_version")
    for key in ("exact_files", "tracked_globs", "forbidden_parts",
                "forbidden_names", "source_only_links", "required_integrity_commands"):
        if not isinstance(spec.get(key), list):
            raise PackageSpecError(f"package spec {key} must be a list")
    if not spec["required_integrity_commands"] or not all(
        isinstance(command, str) and command for command in spec["required_integrity_commands"]
    ):
        raise PackageSpecError("package spec required_integrity_commands must be non-empty strings")
    return spec


def safe_relative_path(value, label):
    if not isinstance(value, str) or not value:
        raise PackageSpecError(f"{label} must be a non-empty string")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise PackageSpecError(f"unsafe {label}: {value!r}")
    return path


def tracked_source_paths():
    try:
        output = subprocess.run(
            ["git", "-C", str(PKG), "ls-files", "-z"],
            capture_output=True,
            check=True,
        ).stdout
    except subprocess.CalledProcessError as exc:
        raise PackageSpecError("cannot enumerate tracked package sources") from exc
    return sorted(path.decode("utf-8") for path in output.split(b"\0") if path)


def validate_source(relative, spec, tracked):
    path = safe_relative_path(relative, "source path")
    if relative not in tracked:
        raise PackageSpecError(f"package source is not tracked: {relative}")
    if any(part in spec["forbidden_parts"] for part in path.parts):
        raise PackageSpecError(f"package source contains forbidden path part: {relative}")
    if path.name in spec["forbidden_names"]:
        raise PackageSpecError(f"package source has forbidden name: {relative}")
    source = PKG / Path(*path.parts)
    if source.is_symlink() or not source.is_file():
        raise PackageSpecError(f"package source is not a regular non-symlink file: {relative}")
    return source


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def agent_files():
    return sorted(p for p in (PKG / "agents").glob("*.md") if p.name != "MANIFEST.md")


def head_commit():
    try:
        return subprocess.run(["git", "-C", str(PKG), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "UNKNOWN"


def full_head_commit():
    try:
        return subprocess.run(
            ["git", "-C", str(PKG), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except Exception as exc:
        raise PackageSpecError("cannot resolve source commit") from exc


def claude_code_plan(root: Path, spec=None):
    """(source, destination) pairs for the claude-code target."""
    if spec is None:
        spec = load_package_spec(PACKAGE_SPEC)

    tracked = tracked_source_paths()
    tracked_set = set(tracked)
    declared = []
    for entry in spec["exact_files"]:
        if not isinstance(entry, dict):
            raise PackageSpecError("exact_files entries must be objects")
        source_rel = entry.get("source")
        destination_rel = entry.get("destination")
        source = validate_source(source_rel, spec, tracked_set)
        destination_path = safe_relative_path(destination_rel, "destination path")
        declared.append((source_rel, source, destination_rel,
                         root / Path(*destination_path.parts)))

    for rule in spec["tracked_globs"]:
        if not isinstance(rule, dict):
            raise PackageSpecError("tracked_globs entries must be objects")
        pattern = rule.get("pattern")
        prefix = safe_relative_path(rule.get("destination_prefix"), "destination prefix")
        excludes = rule.get("exclude", [])
        if not isinstance(pattern, str) or not pattern or not isinstance(excludes, list):
            raise PackageSpecError("invalid tracked_globs entry")
        matches = [path for path in tracked
                   if fnmatch.fnmatchcase(path, pattern) and path not in excludes]
        if not matches:
            raise PackageSpecError(f"tracked_globs pattern matched no files: {pattern}")
        for source_rel in matches:
            source = validate_source(source_rel, spec, tracked_set)
            destination_rel = str(prefix / PurePosixPath(source_rel).name)
            declared.append((source_rel, source, destination_rel,
                             root / Path(*PurePosixPath(destination_rel).parts)))

    sources = [source_rel for source_rel, _, _, _ in declared]
    destinations = [destination_rel for _, _, destination_rel, _ in declared]
    if len(sources) != len(set(sources)):
        raise PackageSpecError("duplicate package source")
    if len(destinations) != len(set(destinations)):
        raise PackageSpecError("duplicate package destination")
    return [(source, destination) for _, source, _, destination in
            sorted(declared, key=lambda item: item[2])]


def in_history(rel: str, digest: str) -> bool:
    """True if `digest` is the sha256 of this path at ANY commit — i.e. the deployed bytes
    were once canonical and the deployment is merely BEHIND."""
    try:
        revs = subprocess.run(["git", "-C", str(PKG), "rev-list", "--all"],
                              capture_output=True, text=True, check=True).stdout.split()
        for rev in revs:
            blob = subprocess.run(["git", "-C", str(PKG), "show", f"{rev}:{rel}"],
                                  capture_output=True, check=False)
            if blob.returncode == 0 and sha256(blob.stdout) == digest:
                return True
    except Exception:
        pass
    return False


def source_dirty(rel: str) -> bool:
    """True if the source file has uncommitted changes. Then 'not in history' CANNOT mean
    hand-edited: a deploy taken mid-edit puts never-committed—but genuinely canonical—bytes in
    the target. Asserting DIVERGED there would name a failure mode the evidence cannot
    distinguish (this fired against itself on 2026-07-24, one commit after the check was
    written). Undecidable is reported as DRIFT?, never as the accusation."""
    try:
        out = subprocess.run(["git", "-C", str(PKG), "status", "--porcelain", "--", rel],
                             capture_output=True, text=True, check=True).stdout.strip()
        return bool(out)
    except Exception:
        return True  # unknown git state ⇒ refuse to accuse


def extra_deployed(root: Path, pairs):
    """Deployed roster definitions the package does not own. --check is otherwise blind to
    these by construction: it only inspects files it would itself write (review D-3)."""
    owned = {dst.name for src, dst in pairs if dst.parent.name == "agents"}
    agents_dir = root / "agents"
    if not agents_dir.is_dir():
        return []
    return sorted(p for p in agents_dir.glob("*.md") if p.name not in owned)


def run_claude_code(args):
    root = Path(args.root).expanduser()
    if not args.check:
        try:
            require_clean_source(PKG)
        except DirtySourceError as exc:
            print(f"FAIL: {exc}")
            return 1
    try:
        spec = load_package_spec(PACKAGE_SPEC)
        pairs = claude_code_plan(root, spec)
    except PackageSpecError as exc:
        print(f"FAIL: {exc}")
        return 1
    manifest_path = root / PACKAGE_MANIFEST_NAME
    if args.check or args.dry_run:
        counts = {"OK": 0, "BEHIND": 0, "DRIFT?": 0, "DIVERGED": 0, "MISSING": 0}
        for src, dst in pairs:
            if not dst.exists():
                state = "MISSING"
            elif sha256(dst.read_bytes()) == sha256(src.read_bytes()):
                state = "OK"
            else:
                rel = str(src.relative_to(PKG))
                if in_history(rel, sha256(dst.read_bytes())):
                    state = "BEHIND"
                elif source_dirty(rel):
                    state = "DRIFT?"     # undecidable: dirty source, direction unknowable
                else:
                    state = "DIVERGED"   # clean source + bytes never in history ⇒ hand-edited
            counts[state] += 1
            print(f"{state:9} {dst}")
        extras = extra_deployed(root, pairs)
        for p in extras:
            print(f"{'EXTRA':9} {p}")
        verb = "would deploy" if args.dry_run else "checked"
        print(f"\n{verb} {len(pairs)} files: "
              + " · ".join(f"{k.lower()} {v}" for k, v in counts.items())
              + f" · extra {len(extras)}")
        if counts["DIVERGED"]:
            print("DIVERGED = clean source, yet deployed bytes never existed in this repo "
                  "(hand-edited). Reconcile deliberately; a plain re-deploy DISCARDS them.")
        if counts["DRIFT?"]:
            print("DRIFT?   = source file is dirty, so 'never in history' proves nothing — the "
                  "deployed copy may be an earlier uncommitted canonical state. Direction is "
                  "UNDECIDABLE until the source is committed; not an accusation.")
        if extras:
            print("EXTRA = deployed roster definitions the package does not own "
                  "(not stamped in agents/MANIFEST.md; a re-deploy will NOT remove them).")
        if args.dry_run:
            try:
                manifest = build_manifest(pairs, spec, full_head_commit(), PACKAGE_SPEC)
            except PackageSpecError as exc:
                print(f"FAIL: {exc}")
                return 1
            data = manifest_bytes(manifest)
            print(f"would write {manifest_path} (sha256 {sha256(data)})")
            return 0

        # Import only after release materialization's clean-source gate. Importing this
        # sibling can create __pycache__, which must not make a clean tree dirty before
        # the gate has established the release source state.
        from check_wids import validate_deployment

        integrity = validate_deployment(root, manifest_path, PKG / "agents" / "MANIFEST.md")
        for failure in integrity.failures:
            print(f"FAIL: {failure}")
        for warning in integrity.warnings:
            print(f"WARN: {warning}")
        for edge in integrity.source_only:
            print(f"SOURCE_ONLY: {edge}")
        print(
            f"deployment integrity: {integrity.checked_files} files · "
            f"{len(integrity.source_only)} SOURCE_ONLY · {len(integrity.extras)} EXTRA · "
            f"{'OK' if integrity.ok else 'FAIL'}"
        )
        # Lag remains informational only while the externally stamped installed manifest
        # validates. Genuine divergence OR any integrity failure is fail-closed.
        return 1 if counts["DIVERGED"] or not integrity.ok else 0

    try:
        manifest = build_manifest(pairs, spec, full_head_commit(), PACKAGE_SPEC)
    except PackageSpecError as exc:
        print(f"FAIL: {exc}")
        return 1
    for src, dst in pairs:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
        dst.chmod(int(git_file_mode(src), 8))
    data = manifest_bytes(manifest)
    manifest_path.write_bytes(data)
    manifest_path.chmod(0o644)
    print(f"deployed {len(pairs)} files under {args.root}")
    print("\nMANIFEST stamp (agents/ rows) — paste-ready:")
    for p in agent_files():
        print(f"  {p.name}: {sha256(p.read_bytes())}")
    print(f"\nsource commit: {manifest['source_commit']}")
    print(f"package manifest: {manifest_path}\nsha256 {sha256(data)}")
    print("paste-ready manifest stamp:")
    print("  <!-- claude-package-manifest:v1 "
          f"sha256={sha256(data)} source_commit={manifest['source_commit']} -->")
    print("NOW: stamp agents/MANIFEST.md, then RESTART the session (roster registers at START).")
    return 0


def render(template: Path, subs: dict) -> str:
    text = template.read_text(encoding="utf-8")
    for key, value in subs.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def build_plugin_bytes(version: str) -> bytes:
    subs = {"VERSION": version, "COMMIT": head_commit()}
    entries = [(".claude-plugin/plugin.json",
                render(PKG / "adapters/cowork-plugin/plugin.json.template", subs).encode())]
    entries += [(f"agents/{p.name}", p.read_bytes()) for p in agent_files()]
    entries.append(("skills/delegation-triage/SKILL.md",
                    render(PKG / "adapters/cowork-plugin/SKILL.template", subs).encode()))
    entries += [(f"skills/delegation-triage/references/{f}", (PKG / f).read_bytes())
                for f in PLUGIN_REFERENCES]
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, data in entries:
            zf.writestr(zipfile.ZipInfo(name, date_time=ZIP_DATE), data)
    return buf.getvalue()


def run_cowork(args):
    out = PKG / "dist" / f"{PLUGIN_NAME}-{args.version}.plugin"
    data = build_plugin_bytes(args.version)
    if args.dry_run:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            for name in zf.namelist():
                print(f"would pack {name}")
        print(f"would write {out} ({len(data)} bytes, sha256 {sha256(data)[:16]}…)")
        return 0
    if args.check:
        if not out.exists():
            print(f"FAIL: {out} not built yet")
            return 1
        ok = sha256(out.read_bytes()) == sha256(data)
        print(f"{'OK: artifact matches canonical' if ok else 'DRIFT: rebuild needed'} ({out.name})")
        return 0 if ok else 1
    out.parent.mkdir(exist_ok=True)
    out.write_bytes(data)
    print(f"built {out}\nsha256 {sha256(data)}\nsource commit {head_commit()}")
    print("NOW: install via the Cowork plugin UI (replaces the fork lineage), "
          "then stamp agents/MANIFEST.md with this hash.")
    return 0


def run_codex(args):
    text = render(PKG / "adapters/codex/AGENTS-fragment.template", {"PACKAGE_HOME": str(PKG)})
    if args.dest:
        dest = Path(args.dest).expanduser()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        print(f"wrote {dest}")
    else:
        print(text)
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="target", required=True)
    cc = sub.add_parser("claude-code")
    cc.add_argument("--root", default="~/.claude")
    cw = sub.add_parser("cowork")
    cw.add_argument("--version", default=PLUGIN_VERSION_DEFAULT)
    cx = sub.add_parser("codex")
    cx.add_argument("--dest")
    for p in (cc, cw):
        p.add_argument("--check", action="store_true")
        p.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])
    return {"claude-code": run_claude_code, "cowork": run_cowork, "codex": run_codex}[args.target](args)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
