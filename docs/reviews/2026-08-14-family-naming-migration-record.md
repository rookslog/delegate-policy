# Family-naming migration — execution record (P2–P4)

**Started 2026-08-14, same session as ratification** (operator discharged the fresh-session
staging condition in-chat: a manual compaction "instead of starting a new session, basically
equivalent, you can keep going / continue"). Plan of record: the
[family-naming proposal](../proposals/2026-08-14-family-naming.md) §3–§4 and the LANES
Family-naming row (leg routing, commit `94440d5`). This file is the execution evidence; the
proposal stays the decision doc.

## Ratified rename boundary (driver-first deliverable)

The names rename; the word "delegation" in prose does not. Data planes and append-only
history do not move or get rewritten.

### Renames

| # | surface | old | new | phase |
|---|---|---|---|---|
| 1 | GitHub repo (public) | `rookslog/delegation-triage` | `rookslog/delegate-policy` | P2 |
| 2 | local dir | `~/Projects/delegation-triage` | `~/Projects/delegate-policy` | P2 |
| 3 | GitHub repo + local dir | `rookslog/delegation-runtime` + `~/Projects/delegation-runtime` | `rookslog/delegate-runtime` + `~/Projects/delegate-runtime` | P2 |
| 4 | in-repo self-references, live surfaces only | `delegation-triage` etc. | new names | P2 |
| 5 | deployed Claude skill | `~/.claude/skills/delegation-triage/` | `~/.claude/skills/delegate-triage/` + transition alias stub at the old name | P3 |
| 6 | deployed Codex skill | `~/.codex/skills/delegation-triage/` | `~/.codex/skills/delegate-triage/` + alias stub | P3 |
| 7 | Codex learning skill | `~/.codex/skills/orchestration-learning/` | `~/.codex/skills/delegate-learn/` + alias stub | P3 |
| 8 | agent pins | `~/.claude/agents/*.md` references | updated in place, MANIFEST re-stamped | P3 |
| 9 | hook | `~/.claude/hooks/spawn-triage-guard.py` path + strings | new skill dir name (old dir accepted during alias window) | P3 |
| 10 | global rule files | `~/.claude/CLAUDE.md` trigger, `~/.claude/delegation.md` | `delegate-triage` skill / `delegate-policy` repo | P3 |
| 11 | Cowork plugin adapter | `adapters/cowork-plugin/` source + regenerated dist | naming updated at source; **Cowork-UI install remains an operator step** (Housekeeping, already owed for the stale ROUTES snapshot) | P3 |
| 12 | memory files | delegate-ops memory dir path references | `delegate-policy` paths (quoted history kept verbatim) | P3 |
| 13 | delegate-ops repo docs | `OPEN_ITEMS.md` OI-2 cross-repo paths + any sweep hits | new paths | P3 |

### Does NOT rename / is NOT rewritten

- **Telemetry data plane:** `~/.codex/telemetry/orchestration-learning/` and `events.jsonl`
  (schema frozen at v1). A `POINTER.md` marks the code-plane rename. References **to** this
  path legitimately keep the old name — the checker exempts the `telemetry/orchestration-learning`
  pattern.
- **Append-only history:** `probes/records/*`, probe fixtures, `ROUTE-HISTORY.md`, prior
  `LINEAGE.md` entries, `WARRANTS.md` warrant bodies, `docs/reviews/*`, `docs/handoffs/*`,
  dated proposals, `dist/` recorded builds. Old names there are historical facts. The mapping
  note lives at the top of `probes/INDEX.md` and in the new LINEAGE entry rather than being
  stamped into every record (the proposal said "a top-of-file note maps old names" without
  fixing its home; editing dozens of append-only records to add it would cut against the
  culture the constraint protects — one note at the index all records are reached through,
  plus LINEAGE, delivers the same resolution).
- **`signal-layer`** (N-3 sovereign), **npm/pnpm names in `delegateops`** (untouched by
  design), **`delegate-to-antigravity` / `delegate-to-claude`** (already conformant stems),
  **git history**, session transcripts, `~/.claude.json` usage data.

## Verification: `check_rename.py` (repo root)

Fail-loud: scans the live surface roots for the three old names, exits non-zero on any hit
outside the allowlisted historical surfaces, and additionally asserts the positive
conditions (proposals README clean; WARRANTS KNOWN-REPOS names the new repo; alias stubs are
stubs). **Exit criterion for P4 = checker exits 0.** Run before renames it doubles as the
deterministic reference inventory the flash sweep is compared against.

## Corrections to the plan of record (found by the driver-first inventory)

1. **P1 measured the wrong owner namespace.** The proposal recorded GitHub availability
   PASSED for `loganrooks/*`; the actual owner is `rookslog` (`git remote -v` on both repos).
   Re-measured 2026-08-14 pre-rename: `rookslog/{delegate-policy,delegate-learn,
   delegate-runtime,delegate-triage,delegate-ops}` all 404, and the owner's full repo list
   shows no `delegate-*` collision — P1's conclusion survives under the correct owner; the
   proposal's P1 note is corrected in the same pass.
2. **`delegation-runtime` is not local-only.** It has a public GitHub remote
   (`rookslog/delegation-runtime`, local main ahead 1). Its rename is a GitHub rename with
   auto-redirects, same mechanics as row 1 — boundary row 3 updated accordingly.

## Leg log

- P2 GitHub renames · driver · `rookslog/delegate-policy` + `rookslog/delegate-runtime` live, auto-redirects · `gh api PATCH` both 200.
- P2 local dirs + remotes · driver · both moved, origins re-pointed, 19 pending commits pushed to the renamed remote · `git push` de91ff9..71a6ad7.
- P2 in-repo self-refs (live surfaces) · driver · scripted + judgment edits per the boundary; LINEAGE rename entry; probes/INDEX name-map note; WARRANTS KNOWN-REPOS (incl. correcting the stale "no remote yet" on the runtime row).
- P3 skill dirs · driver · `delegate-triage` (×2 harnesses) + `delegate-learn` moved; fail-loud alias stubs at all three old paths; telemetry POINTER.md; act-name registered mid-session.
- P3 hooks/pins/rules · driver · spawn-triage-guard re-pointed; skill-load-reminder REQUIRED_SKILLS accepts both names for the alias window; flash pins re-hashed in the gateway register; `~/.claude/CLAUDE.md` + `delegation.md` updated.
- P3 package receipt · driver · manifest regenerated as `delegate-triage-package-manifest.json` from deployed bytes, `dirty_source: true`; `check_wids --scope deployment` 60/60, 11 EXTRA = ratified overlay (pre-existing).
- P3 flash slice (R4 probe) · flash-3.7-high via agy · runtime-repo docs (3 files): footprint exactly as assigned, zero residuals, judgment calls correct (`delegation_policy` module + `~/.delegation/v2` data plane left); two report claims re-verified against source · CONCORDANT-POSITIVE.
- P4 flash sweep leg 1 · flash-3.7-high via agy · **agy CLI timeout, no output produced** ("Error: timeout waiting for response") — infrastructure error, not graded as a model result; bounded retry issued (result in the probe record).
- P4 checker · driver · `check_rename.py` **CLEAN** — zero stale references, all assertions hold. Exit criterion met.
- Cowork plugin · NOT regenerated this pass (already owed in Housekeeping for the stale ROUTES snapshot; templates updated at source, UI install is an operator step).
- Known residue: `tests/test_package_integrity.py` rename edits ride uncommitted alongside another session's in-flight modification to the same file (deliberately not committed here to avoid capturing their WIP); the `.claude.json` `skillUsage` history and session stores keep old names as data-plane facts.

**Closing stamp:** main-pass commit `5592d02` (pushed to `rookslog/delegate-policy`); runtime
side `224da1b`; delegateops side `bc4e695`. The MANIFEST preview-class deploy row resolves its
"commit id in the migration record" pointer here.
