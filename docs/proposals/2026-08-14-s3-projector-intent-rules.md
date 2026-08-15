# S3→v2 projector — intent-side rules (crosswalk amendment ask)

**Status: RATIFIED 2026-08-15 — operator-authorized by delegation (same drop-in as the
task-class enum; recorded DECISION_LOG delegate-ops). Enacted same pass: crosswalk v0.2.5
(§2 surface-row qualifier, readings 2–4 confirmed, `human` identity-source member) +
seed-alias extension (delegate-runtime `f2b3e9a`; gemini spellings included, bare
version-ambiguous names still unresolved by design).** *(Superseded status line follows for
the record:)* FILED 2026-08-14, awaiting operator ratification (charter row 6). Filed by the
same unattended run that filed the task-class enum; row 10 covers the filing. Implemented
DARK in delegate-runtime `e5226ed` — safe pre-ratification because the rollup's attestation
floor withholds ALL projected/self-reported evidence from decision grade, so no unratified
rule reaches a decision surface.

## The gap

Crosswalk v0.2.4 ratified the OUTCOME-side projector rules (F1: S3 None→literal `unknown`
binding, identity_source omitted). The intent side has one unspecified REQ field and two
implemented readings to confirm:

1. **`surface` (the amendment ask):** REQ ✓ in §2, S3 column ∅, no projector rule. Proposed
   rule: **projected-v1 intents omit `surface`** (consumers read it as `unrecorded`) —
   claiming any closed-enum member would be an inference stated as fact; S3 spawns span
   cli/teammate/generic surfaces and the ledger never recorded which. Amend the §2 surface
   row's REQ qualifier to "✓ (native; projected records may omit — unrecorded)".
2. **`harness_contract` (reading to confirm):** §2 already marks it "✓ (v2-only)" — the
   validator now enforces REQ for natives only. Confirming this reading is part of the
   ratification, not a new rule.
3. **Effort/model coercions (loss-stated, confirm):** `inherited`/`root-inherited` →
   `session-inherited`; out-of-enum efforts (`ultra` 4, `standard` 2) → `unknown`;
   alias-unresolvable models → null requested_model. All counted in the projector's emitted
   loss report. Companion (agent-side once ratified): extend `SEED_MODEL_ALIASES` with the
   measured drift (`gpt-5.6-sol` 77, `gpt-5.6-luna` 72, `fable`, versioned claude ids,
   gemini spellings) — version-ambiguous bare names (`opus`, `sonnet`, `claude-opus`) stay
   unresolved.
4. **One-terminal-per-run (confirm):** where S3 recorded two terminal dispositions for one
   run (7 live runs), the LAST terminal wins and earlier ones are dropped as a stated loss —
   §3a's terminal bindings forbid demotion.

## Ratification enacts

(a) the §2 surface-row qualifier edit + version bump; (b) confirmation of readings 2–4;
(c) the seed-alias extension. Live receipts: projector run over the 755-event ledger →
360 intents, losses all enumerated (report in the delegate-runtime commit message and
re-runnable: `s3_projector.py --source <events.jsonl> --out <dir>`).
