# Deployment-aware package integrity — Opus review adjudication

**Review ID:** DT-REV-2026-08-04-001
**Date:** 2026-08-04
**Reviewer verdict:** `CONCUR_WITH_CHANGES`
**Reviewer authorization recommendation:** `NOT_READY_FOR_OWNER_DECISION` on the frozen draft
**Root disposition:** proposal revised; owner approved clean-source test-first implementation;
no deployment, cleanup, commit, push, parity retry, or further model call
**Full report:** [verbatim external review](../research/external/2026-08-04-deployment-aware-package-integrity-opus-review/REPORT.md)

## Result

The reviewer independently reproduced the installer/checker boundary mismatch and measured the
full-documentation alternative. Alternative A remains the recommended direction, but the frozen
draft omitted two destination trees, did not disclose already-deployed excluded content, and left
several manifest and link-validation paths open.

Codex root checked the load-bearing source claims against current Apollo state before revising the
proposal. The current plan contains 131 files: 123 in the skill tree, seven agent definitions,
and root `delegation.md`; 22 are untracked. The recursive probe selection includes 70 fixture
files, 19 nested-VCS files, and one runtime prompt. The live Apollo skill contains 21 fixture
files, the 19 nested-VCS files, and the runtime prompt. The PWE locator is absent from the current
KNOWN-REPOS key; `INSTALL.md` overstates `--check` failure semantics; and the documented
`check_state.py --today DATE` invocation misparses the date as a path.

These checks corroborate the findings for proposal revision. They do not establish behavior of
code that has not been written.

## Finding dispositions

| Finding | Disposition | Proposal consequence |
|---|---|---|
| F-01 BLOCKER | accept | Deployment scope now takes the installation root and covers skill, roster, and root delegation destinations; external agents remain reported `EXTRA`. |
| F-02 BLOCKER | accept | Trigger, selection contract, write set, and separately authorized cleanup boundary now disclose and disposition excluded content. |
| F-03 MAJOR | accept | Only the canonical source-tree checker may establish installed integrity; the deployed copy cannot attest to itself. |
| F-04 MAJOR | accept | The deployment manifest digest must be stamped externally in canonical `agents/MANIFEST.md`. |
| F-05 MAJOR | accept | Present or stale `SOURCE_ONLY` declarations fail and declarations are cross-checked in source scope. |
| F-06 MAJOR | accept | Present targets must remain inside the package root and appear in the manifest. |
| F-07 MAJOR | accept | Untracked and nested-VCS paths are excluded; clean source is recommended for release builds, with an owner choice required before implementation. |
| F-08 MAJOR | accept | Tests construct excluded-class fixtures and require `git ls-files`-tracked selection. |
| F-09 MAJOR | accept | Deployment-integrity failure and divergence are OR-combined nonzero exit conditions. |
| F-10 MAJOR | accept | `personal-work-ecosystem:` is added to the KNOWN-REPOS locator key in this proposal pass. |
| F-11 MINOR | accept | Correcting the existing `INSTALL.md` semantics is explicit implementation work. |
| F-12 MINOR | accept | Both checkers require explicit argument parsing; the broken `--today` form gains a regression test. |
| F-13 MINOR | accept | Acceptance uses named packager and edge-set equality, not a stable count assumption. |
| F-14 NOTE | record | The duplicate state-expiry gate is intentional and documented. |

No finding is rejected or parked. Acceptance here means the proposal text was amended; it does
not mean the corresponding software or deployment change exists.

## Revised decision surface

The revised proposal SHA-256 is
`8dd749be915ebf0848364d15329ee23164516f98d2a27663b2c5cd76409c704d`.
The reviewer explicitly stated that the bounded text amendments do not require another paid
review pass. Root accepts that recommendation because every blocker maps to an explicit contract
clause and no implementation has begun.

The owner approved revision
`8dd749be915ebf0848364d15329ee23164516f98d2a27663b2c5cd76409c704d` on 2026-08-04,
selected the clean-source release rule, and authorized its test-first implementation. There is no
preview-class dirty-source path in this contract: write-mode install and `--dry-run` must refuse
the entire dirty repository before destination writes. `--check` remains observational and may
run against dirty source.

That decision does not authorize live-host cleanup, deployment, a parity retry, commit, push, or
another model call.

The later test-first implementation and its bounded evidence are recorded in
[`DT-EXEC-2026-08-04-001`](2026-08-04-deployment-aware-package-integrity-execution-record.md).
That execution record does not change the scope or verdict of this design review.

## Unchanged boundaries

- The dirty `STATE.md` and untracked probe artifacts remain pre-existing operator/teammate work.
- The already-deployed excluded files remain untouched.
- Apollo and Dionysus parity is not established.
- The A1 execution receipt and exact rollback history remain unchanged.
- No second reviewer call was launched.
