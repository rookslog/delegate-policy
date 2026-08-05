# Opus review preflight: deployment-aware Claude package integrity

**Review ID:** DT-REV-2026-08-04-001
**Status:** superseded by successful Apollo Terminal review; initial SSH auth boundary preserved
**Date:** 2026-08-04
**Paid model calls during this preflight:** zero; one later authorized call recorded in adjudication
**Proposal reviewed:** frozen revision later reviewed successfully

## Closure state

The proposal and review packet exist and their deterministic source checks pass. The authorized
Opus review did not launch because the Apollo-local Claude Code authentication preflight reported
no active login in both non-interactive and interactive login shells.

This receipt is not review evidence and confers no implementation or deployment authority. The
later successful route and findings are recorded in the
[review adjudication](2026-08-04-deployment-aware-package-integrity-opus-adjudication.md).

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| `docs/proposals/2026-08-04-deployment-aware-package-integrity.md` | `0fe02735cbf170f6856aecf71f8970ef73aa223b786eac07c83162e50e8e7493` |
| `docs/reviews/prompts/2026-08-04-deployment-aware-package-integrity-opus-request.md` | `1d33ec8c8c5a4ebfa30c352b58d9fc876f6c88405b49f67859c5d71975df788f` |

## Delegation triage and task contract

- Task class: R1 independent review gate; contract integrity and failure-mode challenge.
- Planned route: Apollo-local Claude Code, canonical `reviewer`, Opus, High, fresh print-mode
  session, read/grep/glob/bash/skill tools only, no descendants, no writes, one paid call,
  normal/no-fast posture.
- Nearest alternative: Sonnet/High deep-read or Codex Sol/xhigh design review. Not selected
  because the operator explicitly required Opus and the canonical R1 profile pins Opus/High.
- Worker ownership: no files. Full stdout was to be mechanically materialized under
  `docs/reviews/`; only the root orchestrator could edit or disposition repository artifacts.
- Falsifier: missing source access, route mismatch, write attempt, descendant call, nonzero exit,
  empty/truncated report, or authentication failure makes the review non-decision-grade.
- Recovery: preserve primary output and stop. No automatic retry, resume, provider substitution,
  or second paid call.

## Requested versus observed route

| Field | Planned | Requested | Observed |
|---|---|---|---|
| host | Apollo | authentication preflight on Apollo | Apollo |
| harness | Claude Code | `claude auth status` | Claude Code 2.1.222 |
| profile | canonical `reviewer` | not transmitted to a model | file present; SHA-256 `03b5ca02128ec3b540c3bb6234581922744e73b0df4a1fea9bb581682f8dbcaa` |
| model | Opus | not transmitted | none |
| effort | High | not transmitted | none |
| service posture | normal/no-fast | no model invocation | unobserved; no service request occurred |
| authentication | active first-party session required | status query only | `loggedIn: false`, `authMethod: none`, provider `firstParty` |
| paid calls | maximum one | zero | zero |

The global Apollo loader and project loader were present at preflight with SHA-256
`da24780860a8bd25f73dc35767947e051ea2d6d9841154844ab4f90c4b23ad4b` and
`9062df6fff26e9efaf0caf50e091d04f678bf864852cf25e57deafdee38a2b61`, respectively.
Because no model process launched, this corroborates file presence only; it does not claim that
a Claude session loaded either instruction surface.

## Deterministic checks

Run from the canonical repository on Apollo before authentication preflight:

```text
python3 -m py_compile check_state.py check_wids.py install.py
python3 check_state.py
python3 check_wids.py
```

Results: syntax compilation passed; state check reported nine current dated entries and three
date-exempt entries; source integrity reported 159 Markdown files, 26 W-records defined and 26
cited, `OK`.

Authentication was checked in both an ordinary login shell and an interactive login shell. Both
returned the same logged-out result. Environment-presence checks reported no API key or auth-token
variable; no value was read or printed.

## Process correction

One initial remote-HEAD display interpolated `git` command substitution on Dionysus before SSH and
therefore printed the wrong repository tip. A fully remote `git log` immediately corrected the
observation: Apollo remains at `de91ff9`, matching `origin/main`. The bad display caused no write,
model call, or route decision.

## Owner boundary and resume condition

The owner subsequently authenticated Claude Code from an owner-controlled Apollo terminal. The
supported command exposed by the installed CLI was:

```text
claude auth login
```

No credential, token, callback value, or browser session material entered chat or the repository.
The SSH process continued to report logged out because it did not share the macOS Terminal
authentication context. Codex root therefore launched one guarded script in Apollo Terminal.
Its pre-spend status check passed there, and the frozen packet ran exactly once. No retry was
used. See the adjudication for observed route evidence.
