# P-20260815 — sol × xhigh review gates: 12-run evidence line (Tasks 8b/8c)

**Class:** code + protocol-text review gates (adversarial, delta-scoped rounds).
**Surface:** `codex exec -m gpt-5.6-sol -c model_reasoning_effort="xhigh" -s read-only -C <repo> --output-last-message <file> -` (prompt via stdin). Harness label in v2 records: `codex-exec-read-only-prompt-sha`.
**Runs:** 12 (measured: 12 prompt/verdict/run-log triples in the archive). Task 8b gate: 8 runs — round 1 split into spec + correctness lenses, then rounds 2–7. Task 8c gate: 4 runs — rounds 1–4. v2 intent/outcome records: ordinals 4–15, run-ids `G-20260814-8b-gate-{r1-spec,r1-correctness,r2,r3,r4,r5,r6}`, `G-20260815-8b-gate-r7`, `G-20260815-8c-gate{,-r2,-r3,-r4}`; all outcomes closed `accepted`; identity_source `transcript` (served model observed as gpt-5.6-sol).

## What was measured

- **Finding validity.** Every finding the driver accepted was independently verified before remediation (re-read, re-run, or mutation-tested); the delegateops DECISION_LOG (DL-23..DL-33, local-only repo) records each disposition. Across 11 FAIL rounds the findings were concrete, file:line-anchored, and — where the driver tested them — real defects, including subtle ones (an exit-13 unsettled-top-level-await trap; a witness-collision hazard in a spool checkpoint; a YAML `\s`-vs-tab parser divergence; a variance class that fell through a deviation-recording taxonomy).
- **Cross-round reliability.** In the 8b loop, rounds 3–7 findings were predominantly defects in the *previous remediation* — the reviewer caught freshly introduced mechanism every round rather than re-litigating cleared items. Delta-scoped prompts ("judge these dispositions, hunt fresh defects only in changed lines") were followed as scoped.
- **Verdict calibration: conservative/FAIL-heavy.** No round passed with an open finding; PASS-WITH-REMEDIATION appeared once (8b r7, closed by a mutation-verified test). One documented over-read: 8c r1 asserted a `[stop: S2]` charter stop that the row's own text did not support — driver adjudicated NO-STOP with the row as warrant (DL-30). That is the one reviewer claim the record shows adjudicated *against*; other rejected sub-claims, if any, were not tabulated (unchecked).
- **Timing.** Baseline for this surface remains ~10–15 min per run; per-run wall times were not tabulated but are recoverable from the archived run logs.

## What this warrants (and does not)

- Warrants: sol × xhigh on this codex-exec surface is a **reliable adversarial review gate** for both code diffs and protocol-text artifacts — high real-finding rate, honest delta-scoping, conservative verdicts, and it reliably catches the driver's own freshly introduced defects across rounds.
- Does **not** warrant an xhigh-vs-high comparison: no paired high-effort runs exist. Roster doctrine puts code review at sol **high**; 5 of the 8 8b runs were small code diffs run a tier above route — a cost observation, not a capability finding. The standing-vs-per-gate scope of the operator's "sol xhigh for reviews" ruling is still queued for one word (STATE row `review-surface-codex-sol`).
- Process lesson attached to the loop length (not a reviewer defect): remediations that introduce fresh unreviewed mechanism extend gates; close the design space once (differential fuzz / constraint enumeration) — signal obs-20260815T041059-e7cff1; companion lesson obs-20260815T050936-6e2dba (driver-side executability smoke before round 1 of protocol-text units).

## Raw evidence

Prompts, verdicts, and run logs (37 files): `~/Development/delegate-ops/gate-archives/2026-08-14-task8b-8c/` (local-only family workspace; not in any remote). Adjudications: delegateops `docs/architecture/DECISION_LOG.md` DL-23..DL-33 (local-only repo).
