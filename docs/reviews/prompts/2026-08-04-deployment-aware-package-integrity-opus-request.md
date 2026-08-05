# Opus review request: deployment-aware Claude package integrity

**Review ID:** DT-REV-2026-08-04-001
**Review type:** independent contract and failure-mode review
**Artifact under review:** `docs/proposals/2026-08-04-deployment-aware-package-integrity.md`
**Frozen proposal SHA-256:** `0fe02735cbf170f6856aecf71f8970ef73aa223b786eac07c83162e50e8e7493`
**Authority:** operator request in the active Codex session, 2026-08-04
**Output contract:** one verdict and severity-ranked findings; no implementation

## Required sources

Read completely:

- the proposal under review;
- `install.py`;
- `check_wids.py`;
- `check_state.py`;
- `adapters/claude-code/INSTALL.md`;
- `agents/MANIFEST.md`;
- `.github/workflows/ci.yml`; and
- the failed A1 execution receipt at the typed locator
  `personal-work-ecosystem:evidence/2026-08-04-harness-parity-review-readiness-receipt.md`.

You may inspect directly relevant repository sources to test a claim. Do not broaden into a
general architecture review.

## Review questions

1. Does primary evidence support the stated installer/checker contract mismatch, including the
   boring alternative that the package should simply include more documentation?
2. Does the proposed source/deployment split remain fail-closed, or can the manifest or
   `SOURCE_ONLY` mechanism launder missing or stale evidence?
3. Is one package specification plus one materialized manifest the smallest coherent contract?
4. Are compatibility, dirty-source, migration, privacy, and audit boundaries explicit enough?
5. Could the proposed tests pass while a real installed package is unusable or non-reproducible?
6. Which open decisions must be resolved before implementation authority is meaningful?

## Output format

Start with exactly one verdict: `CONCUR`, `CONCUR_WITH_CHANGES`, or `REVISE`.

Then provide:

- a short basis;
- findings with stable IDs, severity (`BLOCKER`, `MAJOR`, `MINOR`, or `NOTE`), primary source,
  consequence, and smallest concrete correction;
- a direct comparison of Alternatives A and B;
- explicit answers to the six review questions;
- remaining uncertainty and the evidence that would reduce it; and
- a final implementation-authorization recommendation: `READY_FOR_OWNER_DECISION` or
  `NOT_READY_FOR_OWNER_DECISION`.

Do not reveal hidden chain-of-thought. Provide conclusions, cited evidence, concise rationale,
and uncertainty. Do not write or edit files, deploy, commit, push, call other models, or spawn
descendants. Return the full report in stdout for verbatim materialization by the root
orchestrator.

## Route and authority record

- Planned: Apollo-local Claude Code, canonical `reviewer` profile, Opus, High, fresh print-mode
  session, read/grep/glob/bash/skill tools only, no descendants, no writes, normal/no-fast
  posture, one paid call.
- Nearest alternative: Sonnet/High deep-read or Codex Sol/xhigh design review. Not selected
  because the operator explicitly required Opus and the canonical R1 profile pins Opus/High.
- Falsifier: missing required source access, write attempt, descendant call, nonzero exit,
  empty/truncated report, or observed model/profile mismatch makes the review non-decision-grade.
- Recovery: preserve partial output and stop; no automatic retry or resume.
