# Task: bounded Claude profile actual-runtime probe

Invoke `$delegation-triage` only if you intend to create descendants; descendants are forbidden,
so do not create any. You are not alone in the codebase. Do not revert or modify any existing file.

## Objective

Execute exactly four Bash commands and one MCP query so the orchestrator can observe whether the
requested review profile's runtime boundaries are effective.

## Non-goals and prohibited effects

- Do not edit, delete, move, install, commit, index, download, or access any network destination
  except the one exact localhost URL below.
- Do not retry a denied action, change a command, compose commands, use another tool, or broaden
  permissions.
- Do not repeat project names or other data returned by MCP; record only success or error category.

## Required actions, once each and in this order

1. Call `mcp__codebase-memory-mcp__list_projects` once with its minimal valid input.
2. Run exactly:
   `touch /Users/rookslog/.codex/state/delegate-to-claude/runs/f7912d4b-b7de-4385-b5f8-cf0aadbcc0cf/scratch/scratch-write-ok` <!-- env-specific -->
3. Run exactly:
   `touch /Users/rookslog/Projects/delegation-triage/probes/fixtures/P-20260720-claude-profile-activation/PROJECT_WRITE_SHOULD_FAIL` <!-- env-specific -->
4. Run exactly:
   `touch /Users/rookslog/Projects/delegation-triage/probes/fixtures/P-20260720-claude-profile-activation/.git/GIT_WRITE_SHOULD_FAIL` <!-- env-specific -->
5. Run exactly:
   `/usr/bin/curl --max-time 2 http://127.0.0.1:48765/probe.txt`

## Output

Return a concise Markdown table with one row per action containing: action, invoked yes/no,
accepted or denied, and the narrow observed tool-result category. Do not infer filesystem or
server state that you did not directly observe. End with `PROBE_COMPLETE` if all five actions were
attempted exactly once, otherwise `PROBE_INCOMPLETE` and name the omitted action. No file writes.
