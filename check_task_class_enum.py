#!/usr/bin/env python3
"""Fail-loud checker for the §2a task-class enum candidate assignment.

Single source of truth is the proposal's §4 table
(docs/proposals/2026-08-14-task-class-enum.md); this script parses that table and
validates it against the live S3 events file.

Exit non-zero when:
  - any live task_class value is UNASSIGNED (vocabulary grew past the table —
    the trigger to FILE an amendment, never to edit the table in place);
  - any value is assigned to more than one class;
  - the table's own per-class counts are internally inconsistent with its cells;
  - the table is malformed/unparseable (silent no-op would read as a pass).

Count drift against the live file (new events for already-assigned values) is
REPORTED, not failed: census counts are dated facts (2026-08-14, 755 events).

Usage: python3 check_task_class_enum.py [--events PATH]
"""

import argparse
import collections
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
DOC = REPO / "docs" / "proposals" / "2026-08-14-task-class-enum.md"
DEFAULT_EVENTS = Path.home() / ".codex" / "telemetry" / "orchestration-learning" / "events.jsonl"

# table row:  | `class` | events | values | `value` (n) · `value` (n) ... |
ROW_RE = re.compile(r"^\|\s*`([a-z-]+)`\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|(.+)\|\s*$")
CELL_RE = re.compile(r"`([A-Za-z0-9-]+)`\s*\((\d+)\)")

CENSUS_DATE = "2026-08-14"
CENSUS_TOTAL_EVENTS = 755
CENSUS_TC_EVENTS = 361
CENSUS_DISTINCT = 200


def parse_table(text: str):
    """Return (assignment {value: class}, census {value: count}, class_rows)."""
    assignment, census, class_rows = {}, {}, {}
    in_s4 = False
    errors = []
    for line in text.splitlines():
        if line.startswith("## 4."):
            in_s4 = True
            continue
        if in_s4 and line.startswith("## "):
            break
        if not in_s4:
            continue
        m = ROW_RE.match(line)
        if not m:
            continue
        cls, ev_claim, val_claim, cell = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        if cls == "class":
            continue  # header row
        pairs = CELL_RE.findall(cell)
        if not pairs:
            errors.append(f"class `{cls}`: row matched but no value cells parsed")
            continue
        ev_sum = 0
        for value, n in pairs:
            n = int(n)
            if value in assignment:
                errors.append(f"`{value}` assigned twice: `{assignment[value]}` and `{cls}`")
            assignment[value] = cls
            census[value] = n
            ev_sum += n
        class_rows[cls] = (ev_claim, val_claim)
        if ev_sum != ev_claim:
            errors.append(f"class `{cls}`: row claims {ev_claim} events, cells sum to {ev_sum}")
        if len(pairs) != val_claim:
            errors.append(f"class `{cls}`: row claims {val_claim} values, cells hold {len(pairs)}")
    return assignment, census, class_rows, errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", type=Path, default=DEFAULT_EVENTS)
    args = ap.parse_args()

    if not DOC.exists():
        print(f"FAIL: proposal doc missing: {DOC}")
        return 2
    assignment, census, class_rows, errors = parse_table(DOC.read_text())

    if not assignment:
        print("FAIL: no assignment rows parsed from the §4 table (malformed table?)")
        return 2
    for e in errors:
        print(f"FAIL: {e}")

    # doc-internal totals vs the recorded census constants
    if len(assignment) != CENSUS_DISTINCT:
        errors.append(
            f"table assigns {len(assignment)} values; census records {CENSUS_DISTINCT}"
        )
        print(f"FAIL: {errors[-1]}")
    if sum(census.values()) != CENSUS_TC_EVENTS:
        errors.append(
            f"table counts sum to {sum(census.values())}; census records {CENSUS_TC_EVENTS}"
        )
        print(f"FAIL: {errors[-1]}")

    # live coverage
    if not args.events.exists():
        print(f"FAIL: events file missing: {args.events}")
        return 2
    live = collections.Counter()
    with open(args.events) as f:
        for line in f:
            e = json.loads(line)
            if e.get("task_class"):
                live[e["task_class"]] += 1

    unassigned = sorted(set(live) - set(assignment))
    if unassigned:
        print(
            f"FAIL: {len(unassigned)} live value(s) not in the table "
            f"(vocabulary grew past the {CENSUS_DATE} census — file an amendment):"
        )
        for v in unassigned:
            print(f"  UNASSIGNED: {v} ({live[v]})")
        errors.append("unassigned live values")

    vanished = sorted(set(assignment) - set(live))
    if vanished:
        # assigned but no longer observed would mean the data plane was rewritten — loud.
        print(f"FAIL: {len(vanished)} assigned value(s) absent from live events "
              f"(append-only data plane should never lose values):")
        for v in vanished:
            print(f"  VANISHED: {v}")
        errors.append("vanished values")

    drift = {v: (census[v], live[v]) for v in census if v in live and census[v] != live[v]}
    if drift:
        print(f"note: {len(drift)} value(s) drifted from census counts (dated facts, not failures)")

    if errors:
        print(f"\nFAIL — {len(errors)} error(s).")
        return 1
    print(
        f"CLEAN — {len(assignment)} values / {len(class_rows)} classes cover all "
        f"{len(live)} live values ({sum(live.values())} task_class-bearing events; "
        f"census {CENSUS_DATE}: {CENSUS_TC_EVENTS})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
