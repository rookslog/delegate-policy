# Task-class enum — the §2a candidate assignment (crosswalk sibling)

**Status: FILED 2026-08-14, awaiting operator ratification.** Filed under DECISION_CHARTER
row 10 (filing is agent-side); ratification is a record-standard amendment and is the
operator's under charter row 6 — nothing in this document is live until ratified, and
`task_class.class` stays null in native v2 records (writers fail closed on non-null) exactly
as [crosswalk §2a](2026-07-24-intent-outcome-record-crosswalk.md) requires. This document is
the "sibling" publication home §2a names; ratifying it discharges §2a's publication
precondition. The subsequent §2a cross-reference edit and version bump in the crosswalk are
part of the ratified act, not a separate ask [per: propagation].

Produced by the first unattended run under the 2026-08-14 charter (session `5f55ceae`,
`.kickoff.json` in the programme root). Authored by the driver in-session; no delegation
legs (delegation test: no new information channel, no parallelism, no isolation need).

## 1. Census (measured 2026-08-14)

Source: the S3 data plane, `~/.codex/telemetry/orchestration-learning/events.jsonl`
(name unchanged by the family rename — data planes don't move; see its `POINTER.md`).

- 755 events total; **361 `route_planned` events carry `task_class`** (100% of
  `route_planned` — zero null/missing).
- **200 distinct values** — up from 58 at crosswalk v0.2 (2026-07-24) and the growth that
  re-urgented this deliverable (LANES S4 row). 147 of the 200 are singletons.
- Re-runnable extraction:
  `python3 -c "import json,collections; print(len(collections.Counter(e['task_class'] for e in map(json.loads, open('<events.jsonl>')) if e.get('task_class'))))"`
  — and `check_task_class_enum.py` (repo root, §6) re-derives every figure in this
  document from the live file and this table.

## 2. The candidate enum — 13 members + 1 reserved

Panel A12's constraint binds this design: the observed vocabulary is compositional along
routing-relevant axes, and the enum must preserve the **scope** axis and the
**review-generation** axis or state the loss. Both are preserved as first-class members:

| member | definition (assignment criterion) |
|---|---|
| `implementation` | Open-scope build: design judgment is inside the task (new code, adapters, prototypes, harnesses). |
| `bounded-implementation` | Fully-specified, bounded-footprint build: decisions already made, oracle stated, ≤small owned file set. **The scope axis survives as this member vs `implementation`.** |
| `fix` | Corrective change to an existing artifact: bugfixes, revisions, corrections, recoveries, diagnose-and-repair debugging. |
| `design` | Producing a design artifact — interface, architecture, schema, contract — as the deliverable (not the code implementing it). |
| `review` | First-generation adversarial/quality/conformance review of an artifact, including gate-class reviews. |
| `rereview` | Review of a reworked artifact — any review generation after the first. **The generation axis survives as this member vs `review`**; it wins ties against every other modifier (so `adversarial-rereview-gate` → `rereview`, not `review`). |
| `research` | External knowledge acquisition: web, literature, vendor docs, other people's practice. Reading *documentation* is research even when the documented thing is local. |
| `investigation` | Question-driven local evidence-seeking: probing live state, code paths, traces, storage — "what is happening / where is X" against this machine's artifacts. |
| `audit` | Standard-driven enumerative sweep of local artifacts: conformance, completeness, inventory — "does X conform / what's missing". |
| `synthesis` | Integrating already-gathered material into a new account; the inputs exist, the deliverable is the integration. |
| `evaluation` | Grading, ranking, or triaging artifacts/outputs/agents against criteria: graders, canaries, challenges, triage. |
| `advice` | Consultative recommendation without artifact ownership: advice, consultations, strategy checkpoints. |
| `orchestration` | Coordinating multi-agent waves as the task itself. |
| `other` | **Reserved, zero census members.** Recommended forward-compat member so a post-enforcement writer meeting a genuinely new kind of work need not fail or force-fit; `class_free` carries the native term, and an `other` showing up in decision-grade rollups is itself the signal to amend. Ratifying with or without this member is an explicit sub-decision (§5). |

Review at 111/361 events is the largest class by a factor of ~2.5 — a fact about how this
operation actually delegates, and the reason `review`/`rereview`/`evaluation` stay separate
rather than merging into one "assessment" class: they are the D-4 rung discriminators.

### Assignment rules (how the table in §4 was derived)

1. **Head-noun rule.** The final noun of the compositional value names the class
   (`…-review` → `review`, `…-audit` → `audit`, `…-implementation` → `implementation`).
2. **`bounded-` prefix is class-bearing only on the implementation family** (§3 states the
   loss elsewhere).
3. **`rereview` beats every other modifier**, including `-gate` (A12: generation is the
   discriminator a D-4 rung condition fires on; gate-ness is recoverable from `class_free`).
4. **Local-vs-external tiebreak** for head nouns that don't name a class (discovery,
   evidence, retrieval, probe, scout, forensics, metadata, inventory): external knowledge →
   `research`; local state → `investigation`; completeness sweep → `audit`.
5. **Explicit judgment rows** where the rules mislead — marked ◆ in §4 and argued in §5.

## 3. Stated losses (A12 compliance)

Everything below collapses at the `class` level and is **recoverable from `class_free`**,
which preserves the native term verbatim in every record:

- **Gate-ness** — `review-gate` (8), `design-gate`, `adversarial-review-gate`,
  `integrity-bearing-design-review-gate` all land in `review` (or `rereview`). A consumer
  needing gate-vs-advisory review must read `class_free`.
- **`bounded-` outside the implementation family** — `bounded-code-review` → `review`,
  `bounded-bugfix` → `fix`, `bounded-research` → `research`, etc. A12's scope warning was
  about the implementation family, which is preserved; this wider loss is deliberate
  (keeping bounded-× everywhere would double the enum).
- **Adversarial / independent / read-only / stakes modifiers** — `code-review-adversarial`,
  `independent-review`, `read-only-*`, `high-stakes-*`, `consequential-*`,
  `integrity-bearing-*`, `fixed-cutoff-*` all collapse into their head-noun class.
- **Artifact type** (code vs spec vs doc vs plan review; python vs swift implementation).

## 4. The full assignment — all 200 observed values

Total: 361 events, 200 values, 13 classes; every observed value assigned exactly once;
machine-checked by `scripts/check_task_class_enum.py` (§6). Judgment rows marked ◆.

| class | events | values | assigned values (census count) |
|---|---|---|---|
| `review` | 111 | 53 | `review` (14) · `review-gate` (8) · `architecture-review` (7) · `code-review-adversarial` (5) · `adversarial-review` (4) · `code-quality-review` (4) · `code-review-conformance` (4) · `independent-review` (4) · `spec-review` (4) · `bounded-spec-review` (3) · `frozen-plan-review` (3) · `implementation-review` (3) · `bounded-code-review` (2) · `code-review` (2) · `copied-snapshot-review` (2) · `design-heavy-read-only-review` (2) · `high-stakes-planning-review` (2) · `integration-review` (2) · `task-scoped-code-review` (2) · `adoption-delta-review` (1) · `adversarial-contract-review` (1) · `adversarial-review-gate` (1) · `authority-privacy-review` (1) · `authorization-contract-review` (1) · `bounded-document-reconciliation-review` (1) · `claim-source-review` (1) · `code-quality-security-review` (1) · `consequential-design-review` (1) · `cross-system-architecture-review` (1) · `design-gate` (1) · `design-review` (1) · `document-review` (1) · `documentation-review` (1) · `external-review` (1) · `final-code-review` (1) · `focused-code-and-doc-review` (1) · `implementation-plan-review` (1) · `independent-code-review` (1) · `independent-design-review` (1) · `integrity-bearing-design-review-gate` (1) · `integrity-bearing-specification-compliance-review` (1) · `persisted-state-lifecycle-contract-review` (1) · `persisted-state-lifecycle-review` (1) · `persisted-state-reader-review` (1) · `plan-review-adversarial` (1) · `prelaunch-design-review` (1) · `proposal-review` (1) · `prototype-review` (1) · `read-only-contract-review` (1) · `read-only-memo-review` (1) · `read-only-review` (1) · `regression-review` (1) · `spec-compliance-review` (1) |
| `research` | 45 | 24 | `web-research` (6) · `research-discovery` (4) · `source-heavy-research` (4) · `literature-research` (3) · `research-execution` (3) · `bounded-research` (2) · `bounded-research-execution` (2) · `cross-vendor-model-route-research` (2) · `open-framing-research-probe` (2) · `primary-literature-research` (2) · ◆`repository-research` (2) · `browser-research` (1) · `cross-vendor-open-framing-retrieval` (1) · `cross-work-organizing-form-research` (1) · ◆`documented-harness-surface-research` (1) · ◆`documented-local-surface-research` (1) · `external-runtime-research` (1) · `interdisciplinary-research-discovery` (1) · `interpretive-user-lifeworld-research` (1) · `open-framing-research` (1) · `primary-source-web-research` (1) · `public-agentic-practice-retrieval` (1) · ◆`telemetry-schema-research` (1) · ◆`web-research-recovery` (1) |
| `bounded-implementation` | 34 | 8 | `bounded-implementation` (26) · `bounded-python-implementation` (2) · `bounded-agentic-implementation` (1) · `bounded-documentation-implementation` (1) · `bounded-mechanical-implementation` (1) · `bounded-state-transition-implementation` (1) · ◆`privacy-bounded-adapter` (1) · ◆`test-fixture-migration` (1) |
| `investigation` | 32 | 27 | `bounded-investigation` (2) · `bounded-readonly-evidence` (2) · `broad-readonly-evidence` (2) · `design-investigation` (2) · `read-only-investigation` (2) · `bounded-codepath-investigation` (1) · `bounded-contract-evidence-scout` (1) · `bounded-local-evidence-search` (1) · `bounded-read-investigation` (1) · `bounded-repository-integration-investigation` (1) · `broad-local-discovery` (1) · `broad-read-investigation` (1) · `broad-readonly-metadata` (1) · `broad-repository-investigation` (1) · `browser-access-probe` (1) · `cross-harness-trace-investigation` (1) · `read-only-architecture-discovery` (1) · `read-only-codebase-investigation` (1) · `read-only-discovery` (1) · `read-only-evidence-discovery` (1) · `route-surface-probe` (1) · `runtime-capability-probe` (1) · `storage-forensics` (1) · `targeted-code-investigation` (1) · `targeted-code-path-investigation` (1) · `targeted-data-investigation` (1) · `targeted-repo-investigation` (1) |
| `audit` | 29 | 24 | ◆`read-mostly-opportunity-inventory` (3) · `read-only-audit` (3) · `bounded-audit` (2) · `bounded-config-audit` (1) · `bounded-integration-audit` (1) · `bounded-readonly-privacy-audit` (1) · `broad-read-only-artifact-audit` (1) · `broad-repository-status-audit` (1) · `cross-host-configuration-audit` (1) · `factual-audit` (1) · `factual-omission-audit` (1) · `fixed-cutoff-aggregate-audit` (1) · `fixed-cutoff-local-health-audit` (1) · `fixed-cutoff-schema-audit` (1) · `read-only-code-audit` (1) · `read-only-governance-audit` (1) · `read-only-history-audit` (1) · `read-only-integration-audit` (1) · `read-only-quality-audit` (1) · `read-only-workflow-audit` (1) · `repo-readiness-audit` (1) · `repository-architecture-audit` (1) · `roadmap-audit` (1) · `source-access-audit` (1) |
| `implementation` | 22 | 11 | `implementation` (11) · `test-implementation` (2) · `apple-adapter-implementation` (1) · `benchmark-harness-implementation` (1) · `code-implementation` (1) · `live-probe-implementation` (1) · `multi-agent-implementation` (1) · `opus-adapter-implementation` (1) · `persisted-state-lifecycle-implementation` (1) · `prototype-implementation` (1) · `swift-protocol-implementation` (1) |
| `design` | 22 | 5 | `read-only-interface-design` (8) · `interface-design` (6) · ◆`schema-artifact` (4) · `architecture-interface-design` (3) · `contract-oracle-design` (1) |
| `fix` | 18 | 16 | `bugfix` (3) · `R4-corrective-implementation` (1) · `bounded-bugfix` (1) · `bounded-correction-closure` (1) · `bounded-fix-round` (1) · ◆`bounded-integration-debug` (1) · `bounded-provider-correction` (1) · ◆`config-debugging` (1) · `coupled-planning-correction` (1) · `grader-fix-round` (1) · `implementation-revision` (1) · `persisted-state-lifecycle-recovery` (1) · `persisted-state-semantic-correction` (1) · ◆`prototype-review-and-fix` (1) · `semantic-test-fixture-revision` (1) · `test-infrastructure-fix` (1) |
| `evaluation` | 12 | 6 | `evaluation` (6) · ◆`source-triage` (2) · `blind-independent-challenge` (1) · ◆`candidate-triage` (1) · `independent-grader` (1) · `model-adherence-canary` (1) |
| `advice` | 11 | 9 | `architecture-consultation` (3) · `advice` (1) · `architecture-advice` (1) · `consequential-strategy-advice` (1) · `contract-design-advice` (1) · `cross-system-design-advice` (1) · `cross-system-linkage-design-advice` (1) · `decision-advice` (1) · `design-advice` (1) |
| `rereview` | 9 | 6 | `implementation-rereview` (3) · `finding-rereview` (2) · ◆`adversarial-rereview-gate` (1) · `compatibility-rereview` (1) · `integration-rereview` (1) · `regression-rereview` (1) |
| `synthesis` | 8 | 7 | `research-synthesis` (2) · `broad-read-only-synthesis` (1) · `critical-research-synthesis` (1) · `cross-artifact-synthesis` (1) · `literature-gap-synthesis` (1) · `repo-status-synthesis` (1) · `storage-synthesis` (1) |
| `orchestration` | 8 | 4 | `read-only-orchestration` (5) · `evidence-orchestration` (1) · `orchestration-meta` (1) · `research-orchestration` (1) |

## 5. Judgment rows (◆) and open sub-decisions

Where a rule from §2 misled or two classes were defensible — the operator ratifies these
individually or wholesale:

- **`repository-research`, `telemetry-schema-research`, `documented-local-surface-research`,
  `documented-harness-surface-research` → `research`** by head-noun rule, though the objects
  are partly local: the work reads documents/docs, not live state. The alternative
  (`investigation`) loses the head-noun rule's auditability.
- **`web-research-recovery` → `research`**, overriding recovery→`fix`: the recovery *is*
  re-performing the research; the work performed classifies, not the reason it was redone.
- **`config-debugging`, `bounded-integration-debug` → `fix`** — read as diagnose-and-repair.
  Unchecked whether either run actually closed with a repair; diagnosis-only debugging would
  argue `investigation`.
- **`prototype-review-and-fix` → `fix`** — compound head; the last head names the
  deliverable (a fixed artifact).
- **`schema-artifact` → `design`** — head noun "artifact" is classless; producing a schema
  is design work.
- **`privacy-bounded-adapter`, `test-fixture-migration` → `bounded-implementation`** — no
  implementation head noun, but both are bounded specified build work.
- **`read-mostly-opportunity-inventory` → `audit`** — an inventory is a completeness sweep;
  `investigation` was the alternative.
- **`source-triage`, `candidate-triage` → `evaluation`** — triage = ranking against
  criteria; arguably research-support (`research`) for source-triage.
- **`adversarial-rereview-gate` → `rereview`** — rule 3 applied; the one row where two
  preserved concerns (generation, gate-ness) collide, resolved for generation per A12.
- **The `other` member** (§2) — recommended, but it is a semantics change to the closed-enum
  discipline; ratify explicitly with or without it.

**Alternative considered and not recommended:** a faceted design — `class` + closed modifier
facets (`bounded: bool`, `generation: first/re`, `read_only: bool`, `gate: bool`) — captures
the compositionality without loss, but is a materially larger crosswalk change (four new
enum-bearing fields vs the already-ratified two-level shape), and `class_free` already
preserves full fidelity for consumers that need the modifiers. If rollup practice shows
consumers repeatedly parsing `class_free` for the same modifier, that is the evidence to
file the faceted amendment.

## 6. Deterministic check

`check_task_class_enum.py` (repo root, alongside `check_rename.py`): parses THIS document's §4 table
and the live events file; exits non-zero if any live `task_class` value is unassigned
(fail-loud on vocabulary growth — the failure is the trigger to file an amendment, not to
edit this table in place), if any value is assigned twice, or if the table's per-class
event/value counts disagree with a recount at the recorded census figures. Census counts are
dated facts (2026-08-14, 755 events); live drift in counts is reported, not failed, so long
as coverage stays total.

## 7. What ratification enacts

One operator "yes" authorizes, in the same pass [per: propagation]: (a) this assignment as
the published §2a candidate table; (b) the crosswalk §2a edit pointing here + version bump;
(c) the `other`-member sub-decision as adjudicated; (d) LANES P1 row advance. Enforcement of
`task_class.class` as REQ remains a **separate, later** act — §2a publication is its
precondition, not its trigger; writers keep failing closed on non-null `class` until the
enforcement amendment (also operator's, row 6) lands.
