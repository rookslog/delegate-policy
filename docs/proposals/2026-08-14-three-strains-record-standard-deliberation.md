# Three strains, one waist — DelegateOps × delegation-triage × orchestration-learning

**Status: DRAFT DESIGN INPUT — non-authorizing.** Filed 2026-08-14 on operator instruction
("propagate the set") after an in-session deliberation in the delegate-ops working directory.
Nothing here changes a route, a schema, or a product boundary; the two coupled edits it arrives
with (crosswalk [v0.2.3] S4 registration, LANES probe row) are registrations, not mappings.
Operator has seen and approved the *filing*; the recommendation itself awaits its probe.

## 1. The question

How should DelegateOps (execution ledger / delegation-verification product,
`~/Development/delegate-ops/delegateops/` — local hint, local git only) integrate with delegation-triage
(this repo) and orchestration-learning (Codex telemetry skill,
`~/.codex/skills/orchestration-learning/`)? Should the three merge? A codex (gpt-5.6 sol high)
answer recommended a pipeline with pairwise adapters; the operator found it factually sound
(four load-bearing citations re-verified against the constitution 2026-08-14) but
under-imagined, and named three constraints: no sunk-cost preservation, a coherent
agentic-triaging system, and survivability across coordination paradigms (including
decentralized/peer agent teams).

## 2. Evidence assembled (four explorer lanes, 2026-08-14)

- **orchestration-learning is live, not dormant**: 755 valid events, 24 pseudonymous projects,
  written through 2026-08-13. Schema keeps planned/requested/observed provenance distinct,
  requires `rework_count`, carries an 18-value disposition vocabulary and one `policy_decision`
  precedent (`project-wave-gating-v1`). Zero mentions of DelegateOps; one mention of
  delegation-triage (human-gated promotion target, SKILL.md:87).
- **This repo already answered "merge?" once**: portfolio review D-1 (2026-07-24) split doctrine
  from runtime, coupled by compatibility contract
  ([README](README.md), [north star](2026-07-24-evidence-commons-north-star.md) §6).
- **The crosswalk predates DelegateOps by two weeks**: the
  [B-3 crosswalk](2026-07-24-intent-outcome-record-crosswalk.md) reconciles S1–S3;
  DelegateOps' `@delegateops/protocol` is a fourth, richer schema — now registered as S4
  (prospective) by the [v0.2.3] amendment accompanying this filing.
- **signal-layer Proposal H** (2026-08-13, DRAFT) moves signal-layer's boundary from ledger to
  registry (per-project installable instrument modules); the Proposal-F companion's required
  "Codex orchestration-head proposal" was never drafted — the record-standard work would
  effectively subsume it.
- **DelegateOps constitution** treats coordination paradigm as data: §8.1 classifies tasks by
  peer-communication need; §8.2 ranks Agent Team as recipe class 6; v0 policy is deterministic
  (line 612), telemetry stays local (line 1030), no framework enters the public protocol
  (line 1173).
- An external research packet (GPT-5.6 Sol Pro, uncommitted, at
  `~/Projects/research-packets/2026-08-14-adaptive-agentic-orchestration/`, local hint) independently
  converges: "the defensible unit of control is a decision episode," hybrid governed topology
  with peer mechanisms as policy-selectable local structure. Digest verdict: disciplined
  literature synthesis + two small reanalyses; 3/3 spot-checked citations resolved; zero
  experiments run; its topology recommendation is its own weakest-graded claim (C011, medium).

## 3. Recommendation

**Converge on a versioned decision-episode record standard (the waist); keep the three
artifacts as sovereign, individually replaceable implementations of three paradigm-invariant
roles — policy (prior), ledger (ground truth), learner (posterior update). No codebase merge.**

Sunk-cost inversion is the operative principle: rank artifacts by cost-to-regenerate. The
records (755 events, probes/, warrants, the DelegateOps ledger-to-be) are expensive-to-impossible
to regenerate; ROUTES tables, skills, and scripts are compiled outputs a session can rewrite.
Making the record canonical makes every implementation disposable — that, not early rebuilding,
is the anti-sunk-cost architecture. Paradigm survivability follows the same line: decentralized
coordination arrives as recipe classes and topology *values in the record*, not as a rewrite —
with one standing design constraint: **no field of the record standard may presuppose exactly
one decision-maker** (checked during the probe below; Unchecked today).

## 4. What happens when, and what flips it

1. **Now (done with this filing):** S4 registered in the crosswalk [v0.2.3]; probe row in
   [LANES](../../LANES.md); pointer left in DelegateOps `docs/architecture/OPEN_ITEMS.md`.
2. **Before DelegateOps Task 15 design:** the one-session probe — hand-map S3's six event types
   and S4's protocol fields onto the crosswalk spine, with value-level samples where live data
   exists; run the single-decision-maker grep. **Flip condition:** if the privacy-stripped
   projection of a content-rich S4 record loses the fields learning needs, the standard is
   premature and the looser adapter-per-pair coupling is correct. **EXECUTED same day:
   [P-20260814-s4-crosswalk-mapping](../../probes/records/P-20260814-s4-crosswalk-mapping.md) —
   flip condition NOT met; the standard stands. [v0.2.4] DISPOSED same day on operator
   authorization: candidates[], assignment{}, situation{}, and execution_surface reserved;
   §3a extended; projector rule added; peer/negotiated members reserved.**
3. **At Task 15** (run export + policy-analysis seed): implement the export projection against
   the reconciled spine. The `PolicyDecision` namespace collision (DelegateOps: experiment
   assignment; S3: human-reviewed promotion) is resolved there, not papered over.
4. **Not now:** an R&D-department project and a portfolio meta-coordinator are consumers of the
   waist; minting either before the standard exists means building against four incompatible
   schemas. The PROGRAMME/LANES pace-layer pattern is the template when one is minted.

## 5. Operator direction (2026-08-14, post-filing — binds the probe's scope, not a ratification)

Recorded verbatim-in-substance from the same session: the routing-policy **mechanism** is
expected to change radically, away from markdown tables — "the routing policy table should be
conditioned / determined by the relevant / salient aspects of a given situation": what's the
budget, what models are available, how much usage remains on the different plans, cost budget,
time budget, soft and hard constraints. It should also "potentially support different
routing-determining paradigms, and routing paradigms where research shows promise."

Consequence for the record standard (this is why the note lives here): the spine must capture
the **situation at decision time** — resource state, availability, quotas, constraint sets — as
first-class fields, not only the chosen route. A policy conditioned on situation is only
learnable and replayable if the situation was recorded. This converges with three existing
surfaces: DelegateOps' task-shape + resource/authority envelopes (constitution §8.1), the
packet's decision-episode definition ("task state × … × resource regime × time") and its
resource-regime vocabulary (SCARCE/NORMAL/ABUNDANT/CONTROLLED_BURN/…), and STATE.md's
scarcity-mode (a one-flag ancestor of the same idea). The markdown table is thereby re-read as
what it always was operationally: a hand-compiled cache of a conditional policy — the standard
should record the condition inputs so future mechanisms (learned, market, team-negotiated,
whatever research supports) can be evaluated against the same records. The pre-Task-15 probe
(§4.2) gains a fourth check: does the spine carry a situation/constraint axis at all?

Packet items worth pulling in when their surfaces are next touched: shadow-mode-first learned
routing with logged propensities and candidate sets; verifier non-independence (a second LLM
verifier shares the generator's blind spots — convergent with W-001's independence-over-depth);
resource-regime vocabulary as an enrichment of STATE scarcity-mode; the 10-action intervention
set (the allocator's action space is wider than model choice) as a long-arc framing input.
