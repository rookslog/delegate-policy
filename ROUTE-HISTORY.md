# ROUTE-HISTORY — provenance for ROUTES.md (load-on-demand; never needed for routing)

Everything here was moved out of the routing table 2026-07-25 (operator directive: progressive
disclosure — the table is ingested by every triage; provenance is not). Canonical repo only — not
packaged into adapters. Full detail: `probes/records/`, `WARRANTS.md`, `docs/reviews/`.

## Per-row provenance

**R1** — re-pointed fable→opus high 2026-07-24, operator ruling: *"opus 5 is now the model… you can
get away with opus high for reviews."* Record: `P-20260724-r1-reroute-opus`. Cross-vendor lens
datum: n=1 deviated known-answer (P-20260717-sol-b20 — blind catch of the hardest MAJOR with
executable repro, 0 false positives). The fable-retained-classes clarification (incl. "driving
long-horizon work") was folded 2026-07-24/25.

**R2/R3 fallbacks** — xhigh→high 2026-07-25 (batch-A ruling, `P-20260725-batch-tier-rulings`):
FrontierCode Main favors high over xhigh by 4.4 pts for opus-5; authoring-adjacent cuts concur.

**R4** — opus xhigh→medium 2026-07-24, operator ruling *"opus medium for most things"*; adopts the
O5-SC leg (FrontierCode Main: medium 53.4 > xhigh 43.6) of a vendor pair still Contested against
the release-page monotone charts [W-024(c)]. Ruling record: `P-20260724-r4-r5-reroute-opus5-effort`.
The effort-frontier probe (`P-20260724-r4-effort-frontier`) stays open, now medium-incumbent vs
xhigh-challenger; **Run 1 (2026-07-25, Cowork Workflow dual-knob): medium leg blind-ACCEPTED,
xhigh leg blind-REJECTED (1 MAJOR), narrow margin — concordant, n=1.** Second documentary reading:
W-025(a).

**R5** — opus high→low, same ruling; W-024(b): low's shape is benchmark-dependent and unmeasured on
mechanical edits. Sonnet demotion probe re-scoped to sonnet high vs opus low (cost order inverted
by opus-5 pricing), count 1/3.

**R7** — re-pointed opus→sonnet high 2026-07-17 (operator ruling: sonnet-first, harness carries the
discipline) [W-023].

**R10** — xhigh→high 2026-07-25 (batch-A): was the last live xhigh opus pin; carried the F2
`thinking:disabled`+xhigh HTTP-400 exposure; HLE delta +0.4 (inside CSV read error).

**R13** — scope-refinement CANDIDATE from W-025(b): external taxonomy scopes fable's premium to
persistent-async / dynamic-decomposition / days-scale orchestration, opus high for bounded
fan-outs (known lanes, one synthesis). Surfaced via panel, not executed — fable-row moves stay
blocked by W-024(d): no controller-isolation measurement exists (see the packet's
`local_eval/` preregistered design and missing-evidence register M-001–M-007). Fallback xhigh→high
2026-07-25 (batch-A), concordant with the W-025 bounded-fan-out tier.

**R14 (retired)** — merged into R15 2026-07-25 (batch-B): its opus-only rationale held only for the
encrypted advisor TOOL; the plaintext advisor SUBAGENT path (W-022) is the shipped pattern. Prior
row text had referenced an opus-4.8 advisor (plaintext measured on 4.8; opus-5 format Unchecked).

**R15 fallback** — xhigh→high 2026-07-25 (batch-A): O5-SC HLE gives opus xhigh only +0.4 over high;
the fable-xhigh pin itself is SUPPORTED (fable HLE 54.4→57.8, +3.4 — largest fable gain in the CSV).

## Constraints provenance

**Judgment floor at sonnet** — P-20260720 logs-verification triad (n=1, post-hoc): haiku overclaimed
and missed the one load-bearing discrepancy; both sonnet legs caught it and scoped what they could
not check.

**Subagent-spawn cap (default 4)** — adopted 2026-07-25 (batch-D) per O5-PG via W-025: Opus 5
"delegates more readily" than 4.8; deterministic caps recommended.

**Preamble Unchecked caveat** — W-016/W-017 re-graded `Unchecked for opus-5` 2026-07-24 (proposal
F3); renewal path = the open effort probes.

## Profiles

**budget-conscious** — deleted 2026-07-25 (batch-C): its deltas predated opus-5 repricing
($5/$25, half fable) and the R1/R4/R5/R7 re-routes; one delta had become cost-raising. Re-derive
from `docs/reviews/2026-07-24-post-opus5-routing-issues.md` #1–#3.

## 2026-08-14 — flash-3.7 exploration ruling (R6; R7 reading legs; R4 candidate)

Operator, in-session (delegate-ops working dir), verbatim: "for our 'routing' gemini flash 3.7
high beats sonnet every time for exploration. use that, it even might be worth utilizing for
certain implementation tasks given its speed and cost. … gemini flash through antigravity cli
(agy)." Applied as: R6 route → **flash 3.7 high via `agy`** (surface `cli`, the crosswalk
v0.2.2 axis value), sonnet pins retained as the no-agy fallback; R7 exploration/reading legs →
same; R7's judgment layer, opus escalation, and the sonnet judgment floor unchanged (the
ruling's stated scope is "exploration"). R4 gains a CANDIDATE note (speed/cost slices) —
suggestion, not ruling. Precedence basis: explicit operator declaration > table (CONTRACT §2a,
§5) — delivered and recorded, not argued. Evidence posture: all prior flash evidence is version
3.6 on the CLIProxyAPI-gateway / antigravity-adapter surfaces (W-026; P-20260731-pst acceptance
tie) — prior-version, cross-surface priors, neither support nor contradiction for this ruling.
The operator also named the meta-failure this entry exists to prevent: repeating rulings across
repos because sessions "never listen." The coupled-edit set (ROUTES + STATE + explorer pins +
MANIFEST re-hash + redeploy, one commit) is what makes the ruling load-bearing at every spawn —
the 2026-07-24 canonicality repair (explorer.md) documents what happens when the set is split.

**Addendum, same day (operator, mid-probe):** "the routing is preliminary / experimental, and so
there should be more thorough checks and monitoring around the work it does, at least temporarily
until we have a more solid understanding of its limits, potentialities, capacities, etc as
interpreted / read from the research report, the benchmarking data (beyond the simple quantified
and aggregated metrics)." Encoded as the PROBATIONARY regime in STATE `exploration-route-flash`
(per-leg re-derivation, completeness check, qualitative fidelity note, 3-attested-per-class or
operator review to clear; 30-day review date). First graded instance: P-20260814-s4-crosswalk-mapping
F7 — high fidelity on delivered content, truncated delivery with blind-spots section undelivered
and undeclared.

**Correction to the addendum, same session:** the "truncated delivery, blind spots undelivered"
grading of P-20260814 F7 was the delegator's liveness error — the output file was read at 50KB
while the leg was still writing; the finished artifact is a complete 180KB inventory with a full
blind-spots declaration, two late-section claims re-verified against source. First-instance
grade flips to concordant-positive (1/3). The regime keeps the lesson as its step 0: confirm
process exit before grading. Flash's record on this leg is clean; the flag-alias invocation trap
from attempt 1 stands as the only surface finding.
