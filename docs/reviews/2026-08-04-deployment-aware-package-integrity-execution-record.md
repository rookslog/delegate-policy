# Deployment-aware package integrity — implementation execution record

**Execution ID:** DT-EXEC-2026-08-04-001

**Proposal:** DT-PROP-2026-08-04-001

**Authority:** owner approval on 2026-08-04 of revision
`8dd749be915ebf0848364d15329ee23164516f98d2a27663b2c5cd76409c704d`, with the
clean-source release rule and test-first implementation

**Source baseline:** `de91ff945d5bec44538990a2a9c7ccf2ba09be4a` on Apollo `main`

**Result:** implementation committed as `56d06a3`; existing Cowork correction preserved as
`aaa7f73`; Apollo deployment and exact cleanup recorded separately; not pushed or parity-tested

## Maintainer action

Use this record to review the implementation evidence. It is not the deployment receipt; the
later Apollo materialization and cleanup are recorded in
[`DT-DEPLOY-2026-08-04-001`](2026-08-04-deployment-aware-package-integrity-deployment-cleanup-record.md).

## Implemented contract

- A schema-versioned Claude package specification resolves a deterministic 60-file package from
  tracked regular files only. It excludes fixtures, runtime output, prompts, nested VCS state,
  metadata, and untracked content, and declares 12 exact source-only edges plus the three required
  integrity commands.
- Release install and dry-run refuse the entire dirty repository before destination writes.
  Observational `--check` remains available against dirty source.
- Installation emits a canonical-JSON manifest spanning the package-owned skill, agent, and root
  delegation destinations. Entries carry source and destination paths, source commit, size, Git
  mode, and SHA-256. The manifest digest must match a machine-readable external stamp in canonical
  `agents/MANIFEST.md`.
- Deployment validation rejects malformed or unsafe manifests, missing or changed declared files,
  unlisted skill files, stale or undeclared source-only edges, escaping or unmanifested link
  targets, invalid W-ID use, and stamp mismatch. Unowned agent definitions remain reported
  `EXTRA`; they are not deleted or made canonical.
- The installer preserves legacy byte-history classes and OR-combines genuine `DIVERGED` state
  with deployment-integrity failure. `BEHIND` is informational only while the stamped installed
  manifest remains intact.
- Both checkers now use explicit argument parsing, including the previously broken
  `check_state.py --today DATE` form.

## Test-first and debugging evidence

The implementation used named RED/GREEN slices. The initial parser tests reproduced
`STATE file not found: 2026-07-12` and the absent deployment-scope contract. Package resolver,
manifest, deployment validation, source-only declaration, and isolated-install tests then failed
on their missing interfaces before the corresponding production code was added. The production
package-spec test separately failed with `KeyError: 'required_integrity_commands'` before that
reviewed field was added.

The first isolated clean-install GREEN attempt refused a nominally clean fixture. A controlled
comparison observed one new path after the failing process,
`__pycache__/check_wids.cpython-314.pyc`; the same fixture with bytecode writes disabled installed
all 60 files. This corroborated-for-this-decision the causal diagnosis: the top-level validator
import ran before the clean-source gate. The intervention defers that import to observational
`--check`; the clean install then passed without weakening the entire-tree rule.

Mutation checks ran in a disposable clean clone. Each named test failed when its safeguard was
independently disabled and passed again after restoration:

| Disabled safeguard | Detecting test | Observed mutation result |
|---|---|---|
| clean-source guard | `test_dirty_source_refuses_dry_run_and_install_before_writes` | two expected failures |
| external digest/source stamp | `test_missing_or_mismatched_external_stamp_fails` | expected failure |
| link-root containment branch | `test_present_target_outside_root_or_absent_from_manifest_fails` | expected failure on missing containment classification |
| agent and root-delegation validation | `test_full_root_agent_and_delegation_mismatches_fail` | two expected failures |

## Fresh corroboration

Observed on Apollo with Python 3.14.6:

- syntax compilation exited 0;
- `python3 -m unittest discover -s tests -p 'test_*.py' -v` ran 25 tests with 25 passing;
- the state gate checked nine dated entries and three exempt entries as of 2026-08-04;
- strict source validation checked 165 Markdown files, with 26 W-records defined and cited;
- Cowork build and byte-determinism check exited 0 and produced SHA-256
  `924f14145b24560b9af5ab038c413d3ed99a60d3ca699f1d4e6cdbab7b9c92f0`;
- Codex rendering exited 0;
- the canonical dirty-tree Claude dry-run refused with exit 1 and reported 22 changes; and
- tracked and explicitly enumerated new implementation files passed whitespace checks.

A separate clean disposable clone on Dionysus with Python 3.12 ran the same 25 tests with 25
passing. Its Claude dry-run resolved 60 missing destination files, reported a deterministic
would-write manifest, exited 0, and did not create the requested destination root. This
corroborates the CI Python version and clean-source path; it is not cross-host Claude harness
parity evidence.

## Preserved and excluded state

The pre-existing modified `STATE.md` and untracked probe fixture/runtime trees remain present and
were not absorbed into package selection. The implementation added the previously authorized PWE
locator line to `WARRANTS.md`; no other route doctrine or agent definition changed.

During this implementation execution, no command targeted a live Claude installation for writes;
all materialization used temporary roots, while the default-root dry-run refused before writes.
The owner subsequently authorized commit, Apollo deployment, and cleanup; those later actions are
separated into `DT-DEPLOY-2026-08-04-001`. No authenticated action, parity retry, push, second
reviewer call, or descendant-agent call occurred in this implementation execution.

The implementation did not receive an additional code-review model call: the approved contract
explicitly kept further model calls and descendants out of scope. The earlier Apollo-local Opus
review is a design-contract review, not a claim that it reviewed these implementation bytes.

## Remaining authority boundary

The implementation and preserved-state commits now exist locally. Push, restart, and
Apollo/Dionysus parity execution remain separate actions; consult the later deployment record for
the live manifest and cleanup state.
