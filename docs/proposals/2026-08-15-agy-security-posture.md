# Antigravity security posture — the two operator decisions, concretely

**Status: BOTH DECIDED 2026-08-15 — operator granted in-session ("i give you permission to
do it"), recommendations applied as written below: Decision 1 = leave the global
Antigravity settings as-is (no change made; flip condition stands); Decision 2 = the
adapter-scoped allow rule ADDED to `~/.claude/settings.json` (backup
`settings-backup-20260815T*-permissions.json` beside the capture store). Registers at next
session start. Operator's standing clarification recorded the same exchange: reserved
items are ask-first, not operator-hands-only, and every ask must carry alternatives +
load-bearing assumptions (memory `ratification-delegation-ruling`).** *(Superseded status
line:)* FILED 2026-08-15, awaiting operator decision (both items are standing security
configuration — never agent-side, whatever the charter delegates). This document exists so
each queued item is one click away from the exact bytes it would change. Background evidence:
STATE `agy-adapter-invocation`, the adapter
(`~/Projects/delegate-runtime/delegate-to-antigravity/` — local hint), and the 2026-08-14 cross-harness
delegation research report (operator's Downloads).

## Decision 1 — harden the global Antigravity settings?

File: `~/.gemini/antigravity-cli/settings.json`

Measured 2026-08-14 (stream init event, session `5f55ceae`): `permission_mode:
always-proceed` from this file reaches headless runs **even under `--sandbox`**, and the file
currently sets `allowNonWorkspaceAccess: true` with the home directory itself (`/Users/rookslog` — local hint) a trusted
workspace — so any headless worker can touch anything under home, auto-approved.

**Recommendation: leave as-is for now.** The adapter no longer relies on Antigravity-side
permissions as a boundary (detached worktree + fixed argv + no
`--dangerously-skip-permissions` are the operative boundary), and hardening this file changes
your interactive Antigravity behavior too — prompts where there were none. The measured
workspace-delivery defect was fixed adapter-side (`--add-dir`, delegate-runtime `e1f24f1`),
not by this file.

If you want defense-in-depth anyway, the minimal harden that does not break headless
delegation is dropping `$HOME` from `trustedWorkspaces` (keep the specific project dirs) and
setting `allowNonWorkspaceAccess: false`. The report's fuller posture (command allowlists,
deny rules) is in its "Recommended Antigravity permission posture" section — apply only with
an allowlist generated for your actual stacks.

**What would flip the recommendation:** any evidence of a worker acting outside its worktree
*through Antigravity's own tools* despite the adapter boundary (the `permission_suspect`
counter and jobs ledger are watching for exactly this), or raw `agy` write-mode use returning
to routine practice.

## Decision 2 — scope Claude Code sessions to the adapter instead of raw `agy`?

File: `~/.claude/settings.json` (`permissions.allow`)

The fragment — this is the whole change. The `<ADAPTER>` placeholder is the adapter script's
absolute path (local hint: `~/Projects/delegate-runtime/delegate-to-antigravity/scripts/agy_delegate.py`),
spelled out fully because the allow-rule must pin the exact executable:

```json
{
  "permissions": {
    "allow": [
      "Bash(python3 <ADAPTER> *)"
    ]
  }
}
```

Effect: sessions can run the hardened adapter without a permission prompt each time; raw
`agy` invocations still prompt. **Recommendation: add it** — it removes friction from the
sanctioned path while keeping the unsanctioned one gated. The adapter refuses unknown
arguments and pins its own flags, which is what makes the blanket allow safe (the research
report's "allow one hardened broker, not arbitrary agy" principle).

**What would flip it:** if the adapter ever gains a pass-through for caller-supplied agy
flags, this allow-rule becomes a hole and should be removed in the same change.

## Related, already queued elsewhere

- Cowork 0.6.0 UI install + plugin rename: LANES "Family naming" row.
- Both 2026-08-14 ratifications: ENACTED 2026-08-15 by operator delegation — see
  [task-class enum](2026-08-14-task-class-enum.md) and
  [projector intent rules](2026-08-14-s3-projector-intent-rules.md) status lines.
