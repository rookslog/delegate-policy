# P-20260814-family-rename-flash-legs — flash 3.7 HIGH via agy: rename sweep + first R4 implementation slice

**Context.** The family-naming migration (docs/reviews/2026-08-14-family-naming-migration-record.md)
ran its two delegated legs on the probationary flash-3.7-high route (STATE
`exploration-route-flash`), per the LANES leg-routing: driver wrote the fail-loud checker and
ratified the boundary first, so every flash output graded against a deterministic oracle
(`check_rename.py` + driver grep baseline). Effort explicitly pinned per leg:
`agy --model gemini-3.7-flash-high`.

**Passive-signal alternative considered:** none available — the migration itself generated the
work; the legs double as the probation instruments the ruling already requires.

## Leg A — implementation slice (R4 CANDIDATE, first implementation evidence)

Task: fully-specified 3-file rename slice in `delegate-runtime` (README.md,
intent-writer/SPEC.md, intent-writer/README.md), judgment rule and data-plane exceptions
stated in the prompt (fixture `slice-prompt.txt`).

- **Footprint (measured, `git diff`):** exactly the 3 assigned files; the other modified files
  in that worktree pre-dated the leg (another session's, byte-untouched by flash — their diffs
  contain zero rename tokens).
- **Correctness (measured):** zero old-name residuals in the 3 files; no paragraph reflow; two
  report claims re-checked against source and exact (README line 6 `delegation_policy` module
  name left as non-artifact; SPEC lines 31–32 `~/.delegation/v2` + `DELEGATION_V2_HOME` left as
  data plane) — both leave-decisions were the CORRECT judgment, unprompted specifics.
- **Report fidelity:** per-file line-number change lists spot-verified accurate; deliberate
  leave-unchanged items declared with reasons. Prefix noise: six filler "waiting for tests"
  lines preceded the report (cosmetic; no tests were requested or claimed as evidence).
- **Grade: CONCORDANT-POSITIVE (implementation class, R4).** First R4 flash implementation
  result on the agy surface; scope discipline consistent with the 3.6 pilot's 8/8, now on 3.7
  × the cli surface.

## Leg B — reference-inventory sweep (R6, exploration class)

- **Attempt 1: agy CLI timeout** ("Error: timeout waiting for response", exit 1, zero bytes)
  on a home-wide scope. Infrastructure error, NOT graded as a model result
  [per: claims-discipline#failure-claims — the failure mode is named from the CLI's own error,
  and the empty file distinguishes it from not-done-yet]. Lesson: bound agy sweep scopes; the
  home-wide framing is the plausible driver (unconfirmed — no retry at the wide scope was run).
- **Attempt 2 (bounded scope): CONCORDANT-POSITIVE.** Step 0: process exit confirmed via
  harness task notification before grading. Findings (fixture `sweep-out2.md`): 11 hits —
  codex `config.toml` project-trust keys ×2, `vendor-facts.md` sentinel rows ×6, bridgewright
  skill-overlay ×2 (including flagging the overlay FILENAME itself), one dated handoff review
  correctly classified historical. **Driver re-derivation: independent grep over the same scope
  found the identical set — same files, same lines, same classifications, zero misses either
  direction.** Blind-spots declaration honest and specific (named the sqlite stores, worktrees,
  and alternative shell rc files it did not sweep). All 10 live-config hits fixed by the driver
  same pass.

## Qualitative fidelity note (probation regime item 3)

Across both delivered legs: no fabricated completeness, no overstated coverage, no miscounts —
the 3.6-lineage reporting weaknesses (W-026) did NOT reproduce on either 3.7-high leg. The two
judgment surfaces (module-name vs artifact-name; data-plane vs code-plane) were handled
correctly WITHOUT enumerated per-case instructions. Failure surface observed so far is
infrastructural (CLI timeout on wide scopes), not epistemic. Limits still unprobed: adversarial
verification, high-coupling code change, long-horizon multi-file design.

## Tally effect

Exploration probation: 1/3 → **2/3 concordant** (s4-crosswalk leg + this sweep).
Implementation (R4): **1/1 concordant** — first entry; R4 stays CANDIDATE until its own floor.
Probation clears at 3/class or the 2026-09-13 operator review.
