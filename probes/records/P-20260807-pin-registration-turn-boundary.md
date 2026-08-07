# PROBE — 2026-08-07 pin registration fires on the user-turn boundary

- probe_id: P-20260807-pin-registration-turn-boundary
- task class / ROUTES row: routing-table §3 (effort delivery / pin registration timing). Surface probe — compares no models; moves no counter. Supersedes the timing half of P-20260805-effort-surface-and-pin-registration.
- configs compared (model × effort × surface × harness): n/a — the subject is the harness. Claude Code 2.1.222 desktop app, interactive session `f66d5a8f-6343-4445-aaa5-4d8a6495959c`, non-gateway, driver opus × xhigh.
- harness/contract hash (if pinned): not pinned — single build, single session.
- blinded?: n/a
- frozen tree?: n/a
- adjudicator: author (driver). The findings are timestamps and an attachment type read out of the session JSONL, not judgment calls.
- evaluator lineage: single-leg, Claude. No cross-lineage leg — the claim is about harness behaviour, not model capability.
- router: opus × xhigh × main loop (operator directed the recording after the observation surfaced).
- **attestation:** session transcript `~/.claude/projects/-Users-rookslog-Development-delegate-ops/f66d5a8f-6343-4445-aaa5-4d8a6495959c.jsonl`, records 220–230; file mtime on `~/.claude/agents/implementer-high.md`.
- fault attribution: n/a — no failure under test. The probe corrects a doctrine that was already known to be too strong.
- detection timing: at-the-time — the delta attachment arrived in-session and the driver flagged it in the same turn.
- passive-signal alternative considered: **fully passive.** Nothing was constructed. The pin was minted for real work (the operator asked for an `implementer-high` roster pin mid-session), and the registration behaviour surfaced as exhaust. No probe was run.
- verdict: **"Pins register at session START" is false as an absolute; the refined claim is that registration is deferred to the next user-turn boundary.** Detail:
  1. **MEASURED — the write.** `~/.claude/agents/implementer-high.md` created at `2026-08-07T07:04:02.771Z` (tool result; file mtime `03:04:02 -0400` agrees).
  2. **MEASURED — the deferral.** The driver was interrupted at `07:04:20.951Z` and the operator sent `continue` at `07:05:14.643Z`. No spawn was attempted in the interval, so this probe does not re-test the same-turn negative; P-20260805 finding 2 supplies it (`Agent type 'dt-probe-noop' not found`, seconds after its own deploy).
  3. **MEASURED — the trigger.** The harness emitted an attachment of type `agent_listing_delta` with `addedTypes: ["implementer-high"]` at `07:05:14.647Z` — **4 ms after the user message, and parented to it**. The new type was then spawned successfully at `07:06:11.730Z`.
  4. **The named candidates from the 08-05 correction are discriminated against.** That record left the trigger unknown, listing a periodic scan or a task-completion event. Neither fits: no task completed in the 72-second interval, and a periodic scan would not deliver itself as an attachment on the user message. What is measured is that **delivery** is bound to the turn boundary. Whether the boundary also triggers **detection**, or merely flushes a scan that had already run, is Unchecked and this probe cannot separate them.
  5. **CORRECTED — MANIFEST doctrine.** "A deploy without a restart is a silent no-op" is wrong on this build. It is a delayed op, and the delay is one user turn. A restart remains the *dependable* path — n=2 observations on one build is not a contract — but an operator who deploys mid-session and then types anything can spawn the new pin.
- unique catches (per leg): `agent_listing_delta` is a named attachment type, so roster refresh is a **first-class harness feature**, not an accident of caching. That is a stronger fact than the timing itself: a feature with a message type has an intended contract, and the doctrine was written against a build that either lacked it or was never tested for it.
- tokens / cost (if observable): zero marginal — the observation is exhaust from work that was happening anyway.
- **tally:** moves no counter. Feeds routing-table §3 and STATE `platform-pin-registration` (split out of `platform-no-per-call-effort` in the same pass, because the timing claim now has different evidence and a different re-check trigger than the effort-surface claims).
- deviations from clean protocol (named): n=1 on one build, one session type (interactive desktop). Registration on headless, cron, and Cowork sessions is untested, as is the behaviour when a pin is *edited* rather than added. The same-turn negative is inherited from P-20260805 rather than re-measured here. Author-adjudicated.
- record locator(s) + minimal verbatim excerpt(s): attachment payload `{"type": "agent_listing_delta", "addedTypes": ["implementer-high"], "addedLines": ["- implementer-high: Implements against an existing spec/design/directives …"]}` at transcript record 227, `parentUuid` = the `continue` user message at record 226.
