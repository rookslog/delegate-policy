# Proposal map

This directory contains the design lineage for turning `delegate-policy` (renamed 2026-08-14; see LINEAGE) from a Claude-family
routing package into a transparent, auditable, research-backed delegation product that can serve
multiple providers and harnesses.

The newest document is not automatically authoritative. Read status, authority, supersession, and
review records before using a proposal as an implementation contract.

## Current review entry point

Start with the
[Claude control-plane initiative handoff](../handoffs/2026-07-24-claude-control-plane-initiative-handoff.md).
It defines the current product thesis, required proposal review, unresolved decisions, and the
boundary between this documentation transfer and later Claude Code work.

The portfolio-level review is now the
[2026-07-24 Fable portfolio decomposition review](../reviews/2026-07-24-portfolio-decomposition-fable-review.md):
verdict REVISE (two products, not three artifacts), dispositions of the root session's
recommendations R-A–R-F, four operator decisions (D-1…D-4), and the ordered next-phase
decomposition. Dispositions: **D-3 decided 2026-07-24** (runtime → its own `delegate-runtime`
repository; D-6 resolved "neither") and **D-1, D-2, D-4 + the north star's §6-as-amended all
RATIFIED 2026-07-24** after the two-leg review panel — see the
[decision-panel adjudication](../reviews/2026-07-24-decision-panel-adjudication.md) for the
binding conditions (compatibility contract, immutable instrument identity, rung-table spec
gaps B-6a/c, §6 v2-migration constraints).

## Orientation documents

The [evidence-commons north star](2026-07-24-evidence-commons-north-star.md) records the
long-horizon vision: a community-scale evidence commons built in three layers (record
standard → local tooling → registry/governance), binding exactly one near-term decision —
the intent-record schema (decomposition item B-3) must be shareable by construction. Its
companion, [Worldings](2026-07-24-evidence-commons-worldings.md), holds the vision to
concrete inhabited situations and states what breaks without each design commitment. Both
are orientation, not implementation contracts; the north star's §6 constraint awaits
operator disposition alongside the portfolio review's decisions.

**Priority overlay (RATIFIED 2026-07-31):** the
[passive-first reprioritization](2026-07-31-passive-first-reprioritization.md) — panel-revised v2
([adjudication](../reviews/2026-07-31-passive-first-panel-adjudication.md), three legs unanimous
CONCUR_WITH_CHANGES) — proposes ranking ledger consumption (route-evidence rollup, enum-first) and
the average-user capture surface ahead of the remaining interchange work and of new experiments,
which become a graded contribution tier with falsifier-testing exempt. Every row below is read
under that priority order; the paired-trial channel's cadence is re-decided at the first §9
evaluation. The programme charter ([`PROGRAMME.md`](../../PROGRAMME.md) + [`LANES.md`](../../LANES.md))
carries the ratified direction and current lanes.

## Recommended read order

| Proposal | Current role | Required disposition |
|---|---|---|
| [Consolidated multi-harness control plane](2026-07-21-consolidated-multi-harness-delegation-control-plane.md) | **Superseded on product boundary (D-1 ratified 2026-07-24: two products — doctrine repo + delegate-runtime).** Its layer analysis and learning-plane design remain source material for B-2/B-3. | Mine for the demand+binding rewrite; do not treat its three-artifact boundary as current. |
| [Cross-runtime routing and Codex-managed Claude delegation](2026-07-17-cross-runtime-routing-and-claude-delegation.md) | Accepted architectural lineage for Codex-managed Claude sessions, provenance, recovery, and bounded delegation. | Preserve its runtime invariants; identify which parts are absorbed by the consolidated product. |
| [Composable Claude capability and scope policy](2026-07-20-composable-claude-capability-and-scope-policy.md) | Approved direction for provider-neutral policy identity plus Claude-specific compilation. Its C0 core is implemented but non-activating. | Preserve the pure-policy boundary; revise later cohorts around the immediate Claude Code and Codex product horizon. |
| [Capability-based Claude execution profiles](2026-07-19-capability-based-claude-execution-profiles.md) | Historical profile and runtime-probe baseline, partially superseded by the composable policy. | Retain as evidence; do not treat its fixed profiles as the final public configuration model. |
| [Deferred provider-neutral router](2026-07-20-provider-neutral-multi-harness-delegation-router-deferred.md) | Earlier decision to preserve an extension seam without building a router. Its reopening triggers now require reassessment. | Decide what the consolidated proposal supersedes and what adapter invariants remain. |
| [Codex-managed Antigravity adapter](2026-07-20-codex-managed-antigravity-gemini-flash-adapter.md) | Implemented temporary provider slice and evidence about cross-provider reuse. | Treat as migration evidence and a later extension, not the immediate product center. |
| [Gemini 3.6 Flash pilot](2026-07-26-gemini-flash-36-pilot.md) | **v3 RATIFIED (D-FP-1/2/3, 2026-07-25, two riders) — pilot EXECUTED AND CLOSED 2026-07-31:** paired trial produced NO overlay row (acceptance tie; `probes/records/P-20260731-pst-paired-trial.md`). W-026 is its warrant; XV-1 remains the promotion discipline. | The first live consumer of the intent-writer + crosswalk; its schema-level sol findings seed C-5's interchange-hardening list. |
| [Family naming](2026-08-14-family-naming.md) | **N-1 RATIFIED + N-2 RESOLVED 2026-08-14 (rev.3):** stem `delegate-` — delegate-ops · **delegate-policy** (this repo; skill keeps the act-name delegate-triage) · delegate-learn · delegate-runtime; Capsule withdrawn, spine = the delegate record standard. P1 availability PASSED (GitHub namespace all free). | Migration P2–P4 EXECUTED 2026-08-14 (docs/reviews/2026-08-14-family-naming-migration-record.md); brand frozen at first npm publish. |
| [Three-strains record-standard deliberation](2026-08-14-three-strains-record-standard-deliberation.md) | **DRAFT DESIGN INPUT (2026-08-14, non-authorizing)** — DelegateOps × delegate-policy × delegate-learn integration: converge on a decision-episode record standard, no codebase merge. Arrived with two registrations: crosswalk [v0.2.3] S4 row, LANES probe row. | Probe EXECUTED and [v0.2.4] DISPOSED 2026-08-14 ([P-20260814](../../probes/records/P-20260814-s4-crosswalk-mapping.md)): standard stands; reservations reserved in the crosswalk. Next: Task-15 mapping re-check + the §2a enum publication. |

## Active contract proposal

The [deployment-aware Claude package integrity proposal](2026-08-04-deployment-aware-package-integrity.md)
is **approved with the clean-source release rule; its test-first implementation is corroborated
in the uncommitted Apollo worktree**.
The [adjudication](../reviews/2026-08-04-deployment-aware-package-integrity-opus-adjudication.md)
dispositions every finding and preserves the initial authentication boundary separately. The
proposal responds to a rolled-back cross-host materialization
whose bounded installed package failed the canonical full-source link checker. It proposes a
strict source scope plus an explicit, manifest-bound deployment scope. The 2026-08-04 owner
decision authorizes that scoped implementation only; deployment, cleanup, parity retry, commit,
and push remain outside it. The
[implementation execution record](../reviews/2026-08-04-deployment-aware-package-integrity-execution-record.md)
contains the RED/GREEN, mutation, cross-version, and authority-boundary evidence; it is not a
deployment receipt. The later
[Apollo deployment and cleanup record](../reviews/2026-08-04-deployment-aware-package-integrity-deployment-cleanup-record.md)
records the clean source commit, external manifest stamp, divergence adjudication, recoverable
cleanup, and remaining restart/parity boundary.

## Supporting evidence

Proposal reviews, correction records, and execution records live in [`../reviews/`](../reviews/).
Implementation plans live in [`../superpowers/plans/`](../superpowers/plans/). Probe records remain
the source of truth for empirical routing outcomes under [`../../probes/`](../../probes/).

## Interpretation rules

1. Separate observed facts, source-supported claims, inferences, recommendations, user decisions,
   and open decisions.
2. A provider model is not a route. Provider, model, harness, transport, authority profile,
   validation contract, and dated capability evidence jointly identify a runnable route.
3. A new model release creates a candidate and a review trigger. It does not automatically displace
   an incumbent route.
4. Sparse or heterogeneous traces generate hypotheses. Route promotion requires the warrant and
   probe discipline in the canonical package.
5. Installed copies are deployments, not competing authorities. Stable promotion requires a
   coherent source revision, release manifest, installation receipt, and drift check.
