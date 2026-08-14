#!/usr/bin/env python3
"""Fail-loud stale-reference checker for the 2026-08-14 family rename.

Exit criterion for migration P4 (docs/reviews/2026-08-14-family-naming-migration-record.md):
this script exits 0. Before the renames it doubles as the deterministic reference inventory.

Old name -> new name:
  delegation-triage      -> delegate-policy (repo) / delegate-triage (deployed skill act-name)
  delegation-runtime     -> delegate-runtime
  orchestration-learning -> delegate-learn (code plane only; the telemetry data dir keeps its path)
"""
import re
import sys
from pathlib import Path

HOME = Path.home()
REPO = Path(__file__).resolve().parent

OLD_NAMES = re.compile(r"delegation-triage|delegation-runtime|orchestration-learning")
# Data-plane exception: the telemetry store does not move; references to its path are valid.
DATA_PLANE_OK = re.compile(r"telemetry/orchestration-learning")

# Live surface roots. Roots that do not exist yet (pre-rename) are skipped silently.
ROOTS = [
    REPO,
    HOME / ".claude/skills/delegate-triage",
    HOME / ".claude/skills/delegation-triage",  # transition alias stub (stub-ness asserted below)
    HOME / ".codex/skills",
    HOME / ".claude/agents",
    HOME / ".claude/hooks",
    HOME / ".claude/CLAUDE.md",
    HOME / ".claude/delegation.md",
    HOME / ".claude/projects/-Users-rookslog-Development-delegate-ops/memory",
    HOME / "Development/delegate-ops/delegateops/docs",
    HOME / "Projects/delegate-runtime",
    HOME / "Projects/delegation-runtime",  # pre-rename location, until mv
]

# Historical / append-only surfaces where the old names are recorded facts, plus intentional
# carriers (alias stubs, the rename map itself, this checker). Substring match on posix path.
ALLOW = [
    "/.planning/",                   # scratch outputs and dated working packets, session-historical
    "/probes/",                      # records, fixtures, INDEX (mapping note at top)
    "/ROUTE-HISTORY.md",
    "/LINEAGE.md",
    "/WARRANTS.md",                  # warrant bodies are historical; KNOWN-REPOS asserted below
    "/docs/reviews/",
    "/docs/research/",               # dated external research reports + provenance, historical
    "/docs/handoffs/",
    "/docs/superpowers/",
    "/docs/proposals/",              # dated decision docs; README.md asserted clean below
    "/dist/",                        # recorded builds, regenerate-not-edit
    "/check_rename.py",
    "/adapters/cowork-plugin/README.md",  # build lineage notes (version continuity for Cowork UI)
    "/.claude/skills/delegation-triage/SKILL.md",   # transition alias stub
    "/.codex/skills/delegation-triage/SKILL.md",    # transition alias stub
    "/.codex/skills/orchestration-learning/SKILL.md",  # transition alias stub
    "/.codex/skills/delegate-learn/references/",    # v1-frozen schema docs describe the data plane
    "/.codex/skills/orchestration-learning/references/",  # same, pre-rename location
    "/.codex/telemetry/",            # data plane
]

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}
SKIP_SUFFIXES = {".pyc", ".plugin", ".zip", ".png", ".pdf"}


def iter_files(root: Path):
    if root.is_file():
        yield root
        return
    if not root.is_dir():
        return
    for p in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.is_file() and p.suffix not in SKIP_SUFFIXES and not p.is_symlink():
            yield p


def allowed(path: Path) -> bool:
    s = path.as_posix()
    return any(a in s for a in ALLOW)


def main() -> int:
    failures: list[str] = []
    seen: set[Path] = set()

    for root in ROOTS:
        for f in iter_files(root):
            if f in seen or allowed(f):
                continue
            seen.add(f)
            try:
                text = f.read_text(errors="ignore")
            except OSError:
                continue
            for i, line in enumerate(text.splitlines(), 1):
                for m in OLD_NAMES.finditer(line):
                    span = line[max(0, m.start() - 30):m.end() + 30]
                    if DATA_PLANE_OK.search(line[max(0, m.start() - 10):m.end()]):
                        continue
                    failures.append(f"{f}:{i}: …{span.strip()}…")

    # Positive assertions -------------------------------------------------
    asserts: list[str] = []

    readme = REPO / "docs/proposals/README.md"
    if readme.exists() and OLD_NAMES.search(readme.read_text(errors="ignore")):
        asserts.append(f"{readme}: proposals README must carry the new names (allowlisted dir, asserted separately)")

    warrants = REPO / "WARRANTS.md"
    if warrants.exists() and "delegate-policy" not in warrants.read_text(errors="ignore"):
        asserts.append(f"{warrants}: KNOWN-REPOS must name delegate-policy")

    for stub in (
        HOME / ".claude/skills/delegation-triage/SKILL.md",
        HOME / ".codex/skills/delegation-triage/SKILL.md",
        HOME / ".codex/skills/orchestration-learning/SKILL.md",
    ):
        if stub.exists():
            body = stub.read_text(errors="ignore")
            if len(body.splitlines()) > 25 or "delegate-" not in body:
                asserts.append(f"{stub}: alias stub must be a short pointer to the new name")

    pointer = HOME / ".codex/telemetry/orchestration-learning/POINTER.md"
    if (HOME / ".codex/skills/delegate-learn").exists() and not pointer.exists():
        asserts.append(f"{pointer}: missing data-plane pointer file")

    # Report ---------------------------------------------------------------
    if failures:
        print(f"STALE REFERENCES ({len(failures)}):")
        for line in failures:
            print("  " + line)
    if asserts:
        print(f"FAILED ASSERTIONS ({len(asserts)}):")
        for line in asserts:
            print("  " + line)
    if failures or asserts:
        return 1
    print("check_rename: clean — zero stale references, all assertions hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
