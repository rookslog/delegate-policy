# P-20260814 — S4 crosswalk mapping (the pre-Task-15 probe)

- **date:** 2026-08-14
- **authorization:** operator, in-session ("run the pre-task-15 mapping probe"); scope = the
  LANES S4-seam row + the operator direction recorded in the
  [three-strains deliberation §5](../../docs/proposals/2026-08-14-three-strains-record-standard-deliberation.md)
  (situation-conditioned routing; plural routing paradigms).
- **attestation:** mixed, per finding — `script-measured` (stdlib python over the live S3 store,
  755 events, this session), `first-hand read` (S4 protocol sources exported at delegateops HEAD
  `ac1635e` via `git archive` — the working tree was dirty with another session's Task-8b edits,
  so HEAD is the stable referent), `cross-vendor leg` (gemini-3.7-flash-high via `agy -p`,
  first exercise of the 2026-08-14 exploration ruling; adjudicated in F7).
- **tally:** none — design probe; feeds the LANES S4-seam lane and delegateops OI-2, not a
  route-flip counter.

## Verdict

**The flip condition is NOT met: a privacy-stripped projection of an S4 decision/outcome record
retains every learning-load-bearing field. The record-standard direction stands.** The
content-bearing S4 fields (`rationale`, `ConsultationRecord.question`,
`CounterfactualDisposition.wouldHaveDecided`, evidence locators, `vendorExtensions`) all drop
under the §5 allowlist, and none is needed for routing-policy learning; the learning core —
`candidates[]`, `choice`, `reasonCodes` (closed 19-member enum), `policyVersion`, the
`PolicyDecision` propensity pair, envelope grant numerics, quota/auth enums, dispositions,
verification kinds — is CODE-typed throughout (decision.ts:76–124, execution.ts:68–131,
provider-state.ts:11–33, first-hand). Verification *evidence* exports only as kind + hash, so a
cross-project consumer sees that verification ran and its outcome, not its content — the same
information surface S3's `validator_outcome` practice already provides.

## Findings

**F1 — S3→spine holds structurally; the free vocabularies grew faster than the events**
(script-measured, live store vs the crosswalk's 222-event-era numbers): `task_class` 200
distinct / 361 route_planned (was 58/94) — the §2a closed-enum publication precondition got
~3.4× harder and the §8 "everyone routes on `class_free`" falsifier is trending true;
dispositions 19 distinct / 338 (was 12/96) — five new compositional values need §3a rows
(`accept-with-qualification`, `accept-with-contract-exception`,
`accept-with-visible-evidence-role-qualification`, `accept-counterframe` → accepted or
accepted-after-rework per the existing pattern; `accept-after-review` → accepted);
`validator_outcome` 72 distinct (A4's free-code characterization confirmed at scale);
`observed_model` None (126) or `unknown` (70) in 196/338 dispositions — mostly on `accept`, so
live S3 massively fails the [v0.2.1] F-3 write-rule; legal, because F-3 binds *native v2
writers* and these project as `projection: projected-v1`, but the projector needs an explicit
rule (None → `unknown` binding, never null) or 58% of S3 outcomes become un-joinable.
Alias drift is live and three-way for the flash binding itself: `google:gemini-3.6-flash-high` /
`google-gemini-3-6-flash-high` / `gemini-3.6-flash-high` (25 events) — the §2 normalized-binding
rule earns its place.

**F2 — S4→spine: near-isomorphic on the decision core, and S4 EXCEEDS the spine on the two
fields the learning literature calls load-bearing.** `DecisionRecord` (decision.ts:76–96) maps
cleanly: `policyVersion` → `route_id` semantics (a policy artifact identifier; registered-id
rule applies), `reasonCodes[]` → `reason_code` (S4's 19 members are a *registered closed
vocabulary* — exactly what §6-4 demands and S3 never had), `committedAt` → `ts`,
`supervisorSessionId` → `session_id`, recipe surface/model/effort → `surface` /
`requested_model` / `requested_effort`, `configurationHash` + `capabilitySnapshotId` →
`harness_contract` partials. But the spine has NO field for the **candidate menu** and none for
**assignment propensity** — while S4 records both by construction (`candidates[]` required on
every decision; `PolicyDecision.assignmentProbability` + `arm` are *required* when
`randomized: true`, decision.ts:104–124). Off-policy evaluation of any future learned router
needs logged candidate sets and propensities (packet 02_OPERATING_POLICY_SPEC §15; the OPE
literature it cites); a spine that cannot carry them cannot host the learning loop.
**Recommendation (not executed): [v0.2.4] reserve `candidates[]`
({binding, surface, eligibility, rank}) and `assignment{policy_version, probability, arm}` on
the intent record** — same reserve-now rationale as `price_lineage` (§6.1 makes late addition
a v3).

**F3 — the situation axis (operator direction §5): S4 is the donor.** The spine's only
situation carriers today are `price_lineage`, `router_effort`, and the S3 riders. S4 carries a
full CODE-typed situation surface: `ContextPosition` {tokensUsed, contextWindowTokens, source:
harness_reported|estimated} (decision.ts:32–38), `ProviderStateSnapshot` with `AuthStatus`
(5 members) and `QuotaPressure` (plentiful/normal/constrained/nearly_exhausted/exhausted/unknown)
and `quotaSource: user_supplied|machine_observed|unknown` (provider-state.ts:11–66), and
`ResourceEnvelope` grants {dimension, amount, confidence: exact|estimated|observed|unknown,
hard/reserve split} (resources.ts:17–95). Budget, availability, remaining usage, cost/time
constraints, soft-vs-hard — the operator's list, already typed. **Recommendation (not
executed): [v0.2.4] reserve a nullable `situation{}` struct on the intent record, shaped by
projection from these S4 types.** A situation-conditioned routing mechanism (the operator's
stated direction) is only learnable and replayable if the condition inputs are in the record.

**F4 — privacy projection: see Verdict.** One boundary named honestly: `vendorExtensions` is an
open map (execution.ts:83) — born-non-exportable under §5.1, correctly.

**F5 — single-decision-maker check.** S4: authority envelopes form a strict tree
(`maxDescendants` strictly decreasing parent→child, authority.ts:161–168); `DecisionRecord` has
a singular `supervisorSessionId` and singular `choice`. That is per-DECISION singularity, not
per-SYSTEM: peer topology is already representable (`claude.agent_team` surface,
`PEER_COMMUNICATION` reason code, execution.ts), and the packet's own bounded-team controls
require a named adjudicator — so "one decider per committed decision" survives decentralization.
Spine: two fields encode a two-party hierarchy — `rework_actor` (root/delegate/none/unknown; a
peer's rework is inexpressible) and `router_model` (singular; a negotiated/market decision has
no single router). Both are additive enum extensions (`peer`; `negotiated`) when a paradigm
needs them — no structural block. The deliberation §3 constraint ("no spine field may
presuppose exactly one decision-maker") **holds today with those two extensions flagged**.

**F6 — namespace collisions, resolved by projection naming.** S4 `PolicyDecision` = experiment
assignment (with propensity) → projects as `assignment{}` (F2), never as a policy event. S3
`policy_decision` = human-gated policy promotion → stays a governance *event*, outside the
intent/outcome records (the crosswalk's scope). Second collision: both S3 (`consultation`
events, 48 live) and S4 (`ConsultationRecord`, decision.ts:49–62) record advice — the spine has
no consultation field; flagged as v3 scope, not reserved now (no learning claim currently rides
on it). Third: S4 recipe `effort` is a free string (execution.ts:76) vs the spine's closed
enum — normalization at projection, same treatment as model aliases.

**F7 — the cross-vendor leg (agy surface, first exercise of the 2026-08-14 ruling).** First
invocation returned a bare model-identity line: my flag error — `--print` and `--prompt` are
aliases of the SAME flag in agy; passing both swallowed the prompt text. Surface lesson: use
`agy -p "<prompt>"` with the prompt as the flag's argument, nothing else prompt-like on the
line. Second invocation (correct form) delivered a 50,064-byte field inventory. **Adjudication (first
graded instance of the STATE probationary regime):** every spot-checkable row matches my
first-hand reads exactly — DecisionRecord field list and optionality (decision.ts:76–96),
PolicyDecision's two branches with required propensity (decision.ts:104–124), recipe common
fields (execution.ts:74–83) — and its CODE/CONTENT classifications are sound (locator, spec,
rationale, question → CONTENT; hashes and enums → CODE). It also surfaced outcome-side
vocabularies I had not read first-hand: Adjudication `verdict`
VERIFIED/REJECTED/NEEDS_EVIDENCE/UNKNOWN with a `blind` flag (evidence.ts:72–82),
VerificationPlan `independenceRequirement` none/independent_agent/human (evidence.ts:62–70),
DeviationRecord categories including `worker_substitution` (plan.ts:60–78) — graded
cited-unchecked (line-cited, not re-read by me; nothing in the Verdict rests on them alone).
**Failure noted: the deliverable is truncated mid-table (ends inside ReplanRecord.triggers) and
the requested sections 2–5 — enum vocabularies, single-decision-maker check, situation fields,
declared blind spots — were never delivered, with no truncation notice.** Whether the cutoff is
the CLI print-timeout or the model stopping is Unchecked. This is the omission-class weakness
the roster already records for flash pins, now observed on the agy surface; it cost this probe
nothing because F2/F3/F5 were established first-hand before the leg returned, and it is the
concrete case for the probationary regime's completeness check.

**F8 — surface vocabulary.** S4's 10-member dotted enum (claude.inline / subagent / workflow /
agent_team / headless / headless_bare, antigravity.headless, codex.app_server, codex.cli,
api.deepseek — execution.ts:110–121) refines the spine's 6. Projection S4→spine is total but
lossy (headless vs headless_bare both → `cli`; subagent cannot split pin-vs-generic without
recipe detail). **Recommendation (not executed): register S4's members into the spine `surface`
vocabulary (additive)** rather than accept the loss — the delivery-surface axis is exactly what
CONTRACT §3 treats as routing-relevant. Noted with it: `antigravity.headless` requires a pinned
`model` because `agy models` serves multiple lineages from one surface (execution.ts:97–103,
measured in-source 2026-08-07) — the same reasoning the 2026-08-14 flash ruling's records
follow.

## Dispositions

1. **OI-2 (delegateops): closable** — resolution is this record; the standard stands.
2. **Recommended amendments [v0.2.4], operator/panel disposition owed, NOT executed here:**
   reserve `candidates[]` + `assignment{}` (F2), reserve `situation{}` (F3), register S4
   surface members (F8), add §3a rows for the five new S3 dispositions (F1), projector rule for
   S3 null `observed_model` (F1), `rework_actor`/`router_model` extension members named for the
   day a paradigm needs them (F5).
3. **S3 vocabulary registration workload re-estimated:** 200 task_class values (was 58) — the
   §2a candidate assignment should be produced from the live store before it grows again.

## Blind spots

Read first-hand: decision.ts (full), execution.ts:68–131, provider-state.ts / resources.ts /
authority.ts (targeted), the full crosswalk, S3 schema.md (full), live events.jsonl
(script-measured). NOT read: plan.ts, objective.ts, events.ts, evidence.ts beyond :7–39,
capability.ts, the 2,931-line JSON schema (the cross-vendor leg covers these; its claims are
graded per F7's adjudication, and nothing in the Verdict rests on them alone). S4 is mid-build
(Task 8b in flight on the same repo): field names may drift before Task 15 — the mapping is
provisional by construction, which is why the crosswalk registration says "mapping owed," not
"mapping done."
