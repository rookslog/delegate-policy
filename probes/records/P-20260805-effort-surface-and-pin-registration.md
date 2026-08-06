# PROBE — 2026-08-05 effort delivery surfaces + pin registration timing

- probe_id: P-20260805-effort-surface-and-pin-registration
- task class / ROUTES row: routing-table §3 (effort-inheritance hazard / effort delivery). Surface probe — compares no models; moves no counter.
- configs compared (model × effort × surface × harness): n/a — the subject is the surfaces themselves, on Claude Code native (stylewright session 5e1e8107, 2026-08-05, non-gateway).
- harness/contract hash (if pinned): not pinned — single-session observation, scope-bound to this build.
- blinded?: n/a
- frozen tree?: n/a
- adjudicator: author (driver) — findings are mechanical (schema text, tool error, file contents), not judgment calls.
- evaluator lineage: single-leg, Claude (fable driver reading its own harness surfaces). No cross-lineage leg — the claims are about tool schemas, not model capability.
- router: fable × session effort × main loop (operator directed the recording).
- **attestation:** stylewright session transcript 5e1e8107-8b3e-4cd5-b719-7055f47e6925 (Agent-tool error verbatim below); workflow agent meta at `~/.claude/projects/-Users-rookslog-Development-stylewright/5e1e8107-8b3e-4cd5-b719-7055f47e6925/subagents/workflows/wf_2e20b484-637/agent-a135b1f12ebf8a7d8.meta.json`
- fault attribution: n/a — no failure under test; the probe re-verifies a doctrine.
- detection timing: at-the-time — the operator challenged the driver's "only surface" claim mid-session; the probe ran within the hour.
- passive-signal alternative considered: findings 1–3 WERE passive (they surfaced during a real max-effort review spawn, not a constructed probe). Only the noop spawn (finding 2) was active, run because its cost was one failed tool call — below any reasonable passive-wait threshold. Exempt in spirit: it tests a falsifier of a standing doctrine.
- verdict: doctrine HOLDS, plus one new attestation gap. Detail:
  1. **MEASURED — Agent tool has no per-call effort.** The session's Agent tool schema carries `model` (sonnet/opus/haiku/fable) and no effort parameter. Per-call effort delivery on the generic surface: still absent, 2026-08-05.
  2. **MEASURED — mid-session pin deploy does not register.** Deployed `dt-probe-noop.md` (haiku × low) to `~/.claude/agents/`, then spawned `subagent_type: dt-probe-noop` in the same session. Result: `Agent type 'dt-probe-noop' not found`, and the error's available-agents list matches the session-start roster. "Pins register at session START" (MANIFEST doctrine, ADR-0022 A5 note) re-verified on the current build. Throwaway pin removed after the probe.
  3. **MEASURED — Workflow spawns lack a served-effort receipt.** `Workflow.agent()` accepts per-call `{model, effort}` including `'max'` (the only surface documenting `max`). But the spawned agent's `meta.json` records `{"agentType":"workflow-subagent","spawnDepth":1,"model":"opus"}` — model attested, effort absent. Until a receipt surface exists, any effort claim for a Workflow spawn is **requested, not served** — the same class of gap as the 2026-08-04 codex model-verification incident, where the rollout log's turn_context was the receipt. No native-Anthropic equivalent of the gateway wire logs (FP-0d rider) is known.
  4. **OPEN — `effort: max` in pin frontmatter unvalidated.** `reviewer-max.md` (opus × max) is minted and deployed this date; whether the harness accepts `max` from frontmatter, and at what served tier, is checkable only after next session start, and only if an attestation surface turns up.
- unique catches (per leg): the error message itself enumerates the live roster — a free roster-snapshot receipt for future registration probes.
- tokens / cost (if observable): one failed tool call (the spawn never ran), one file write/delete.
- **tally:** moves no counter. Feeds routing-table §3 as a dated re-verification; feeds the CONTRACT delivery-surface note (per-call effort → Workflow only, mid-session).
- deviations from clean protocol (named): single build, single session type (interactive desktop app); registration behavior on headless/cron sessions untested. Author-adjudicated (mechanical findings).
- record locator(s) + minimal verbatim excerpt(s): Agent tool error: "Agent type 'dt-probe-noop' not found. Available agents: general-purpose, statusline-setup, claude, …" (full list in session transcript). Reviewer-max canonical sha256 8785a6f2ccd2c4c79a75137fc0711d5e43dad624a4c2368c964896d4e0093865.
