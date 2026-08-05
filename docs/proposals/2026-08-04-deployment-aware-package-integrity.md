# Deployment-aware Claude package integrity

**Proposal ID:** DT-PROP-2026-08-04-001
**Status:** approved; test-first implementation corroborated in the uncommitted Apollo worktree
**Date:** 2026-08-04
**Decision owner:** operator
**Prepared by:** Codex root
**Closure target:** test-first implementation of the reviewed contract; no deployment or cleanup
**Owner decision:** approved 2026-08-04 against revision SHA-256
`8dd749be915ebf0848364d15329ee23164516f98d2a27663b2c5cd76409c704d`, with the
clean-source release rule and test-first implementation authority. Cleanup, deployment, parity
retry, commit, push, and another model call remain outside this approval.

Implementation evidence is recorded separately in
[`DT-EXEC-2026-08-04-001`](../reviews/2026-08-04-deployment-aware-package-integrity-execution-record.md);
that record does not authorize deployment or cleanup.

## Approved decision

The owner authorized Alternative A as revised after independent review: preserve the current
strict source-tree integrity check while adding an explicit, fail-closed installed-package
contract and an isolated-install regression test.

The owner accepted the recommendation that release-class materialization refuse the entire dirty
source tree. No preview-class dirty-source path is part of this revision.

The decision authorized the bounded test-first code and dependent-documentation write set below.
It did not authorize a Claude deployment, cleanup, cross-host parity retry, commit, push, another
model call, or changes to the current dirty `STATE.md` and probe artifacts.

## Trigger and evidence

The immediate trigger is the failed and rolled-back PWE Alternative A1 materialization. Its
execution receipt is stored outside this repository at the typed locator
`personal-work-ecosystem:evidence/2026-08-04-harness-parity-review-readiness-receipt.md`.

Observed in that receipt and re-readable in the current source:

- `install.py` deploys a selected runtime subset to a Claude skill home.
- The deployed subset includes `check_wids.py`.
- `check_wids.py` recursively treats its argument as a complete Markdown package and fails
  every relative link whose target is absent.
- The same installed subset produced the same 12 unresolved repository-only links on Apollo
  and Dionysus, while the checker passed against the complete canonical repository.
- Exact rollback restored both hosts; no Opus call occurred during A1.

The independent Opus review then re-derived the current installer plan and found 131 selected
files across three destination trees: 123 under the skill home, seven agent definitions, and the
root `delegation.md`. It also found 22 selected files not tracked by the repository, including 70
fixture paths in the recursive probe selection, 19 nested-VCS files, and one runtime prompt. A
root corroboration pass reproduced those counts. The live Apollo deployment currently contains
21 fixture files, the 19 nested-VCS files, and the runtime prompt. Their presence is an observed
pre-existing deployment condition, not authority to delete them.

Inference, corroborated for this decision: the failure is a contract mismatch between the
installer's bounded runtime package and the checker's complete-source assumption, not a
Dionysus-only defect. The disconfirming test was cross-host reproduction plus the passing
canonical-source invocation. This does not establish that the proposed design is the best
repair.

Null alternative: the package might simply be incomplete and should carry the full
transitive documentation closure. The review must compare that possibility rather than
assuming a new checker mode is necessary.

## Constraints

- Source integrity remains strict by default. A missing source-tree target must still fail.
- Installed-package validation must not infer legitimacy from absence, path shape, basename,
  or a blanket directory exemption.
- The package boundary must be explicit, schema-versioned, deterministic, and inspectable.
- Credentials, settings, hooks, sessions, transcripts, runtime prompts, generated outputs,
  nested VCS state, fixtures, and filesystem metadata are outside the portable package.
- No checked-in ledger, history, or source document is rewritten to manufacture a pass.
- `install.py --check` keeps its existing drift semantics; lag and unclassifiable dirty-source
  state must not be mislabeled as divergence.
- Release materialization from a dirty source tree is refused before destination writes; this
  revision defines no preview-class exception.
- The existing dirty `STATE.md` correction and untracked probe material retain their current
  ownership and are not absorbed into this proposal.

## Alternatives

### A. Explicit source and deployment integrity scopes — recommended

Add a declarative Claude-package specification and make deployment validation consume the
exact materialized manifest derived from it. Keep full-source validation as the default.
Represent every intentionally source-only relative link as an exact declared edge, surface
it as `SOURCE_ONLY`, and fail on any undeclared missing edge.

This preserves a bounded runtime package without pretending it is the complete repository.

### B. Ship the complete transitive documentation closure — rejected by measurement

Compute and deploy every Markdown target reachable from shipped documents. This produces a
self-contained documentation graph and needs no source-only edge declarations, but the
closure can expand substantially and may pull research, archived, or external-provenance
material into a runtime package.

The Opus review measured 53 additional Markdown files and 823,364 additional bytes, a 258%
increase over the shipped Markdown bytes. The closure includes maintainer governance,
unratified proposals and reviews, plans, handoffs, research, and external-provenance material.
This fails both of B's reopening conditions: the closure is not small and it contains named
excluded classes. Reopen B only if a later package boundary or measurement materially changes.

### C. Remove the checker from deployed packages

Run `check_wids.py` only in the canonical source tree. This avoids a misleading installed
command but gives up local corroboration of W-ID and link integrity after materialization.
Reject unless the deployed package gains another equally deterministic integrity gate.

### D. Accept missing links in deployment mode by pattern

Ignore missing links outside selected directories or allow all absent targets. Rejected:
this weakens the test without making the package boundary explicit and can hide a genuine
packaging regression.

## Approved Alternative A contract

### 1. One canonical package specification

Create one schema-versioned specification owned by the Claude adapter, provisionally
`adapters/claude-code/package-spec.json`. It declares:

- exact required runtime files and narrowly bounded inclusion rules;
- forbidden path classes and file types;
- exact source-only link edges as `(source path, target path)` pairs with a short rationale;
- required integrity commands; and
- the schema version understood by the installer and checker.

Patterns may select a homogeneous class such as Markdown records directly under one named
directory. They must not recurse through arbitrary runtime, fixture, prompt, metadata, or VCS
trees. Every selected source must be a regular path returned by `git ls-files`; untracked paths
cannot enter a release manifest. The implementation must materialize the resolved, lexically
sorted file list before writing anything. The current unbounded `probes/` recursion must be
replaced by this selection rule.

The specification is the package policy, not a deployment receipt. Each installation derives
an immutable manifest containing schema version, source commit, dirty-source classification,
destination-relative path from the installation root, byte size, mode, and SHA-256 for every
selected regular file across the skill, agent, and root-delegation destinations. The receipt
must not contain prompts, model output, credentials, user-specific absolute paths, or file
contents.

The manifest is not its own trust anchor. Its SHA-256 must be stamped outside the installed tree
in the canonical `agents/MANIFEST.md` deployment record before a deployment is accepted. A
deployment-scope check must refuse an unstamped or digest-mismatched manifest. A copy may also
ship with the installed package for local inspection, but that copy is not authoritative.

### 2. Two explicit checker scopes

Preserve the current command as strict source validation:

```text
python3 check_wids.py
```

Its current requirements remain: W-ID definitions resolve, source-tree relative links exist,
and forbidden user-specific paths fail outside existing narrow provenance exceptions.

Add an explicit deployment invocation, provisionally:

```text
python3 check_wids.py --scope deployment --manifest PACKAGE-MANIFEST.json INSTALLATION_ROOT
```

Deployment scope must:

1. refuse a missing, malformed, unsupported-version, duplicate-path, absolute-path, traversal,
   symlink, non-regular-file, or digest-mismatched manifest entry;
2. require the actual installed declared file set and digests to equal the manifest;
3. apply the same W-ID definition/use checks to shipped Markdown;
4. pass a relative link only when its target is present and regular, or when the exact
   `(source, target)` edge is declared source-only by the package specification recorded in
   the manifest;
5. print each declared absent edge as `SOURCE_ONLY` and a deterministic count, never as
   `OK`; and
6. fail every missing edge not declared exactly;
7. fail a declared source-only edge whose target is present in the package, and fail source
   scope when a declared edge's target does not resolve in the canonical source tree; and
8. require every present link target to resolve inside the package root and appear in the
   manifest; an escaping path is missing regardless of what happens to exist elsewhere on the
   host.

The deployment root is the Claude installation root, not only the skill home. Manifest equality
therefore covers the seven agent definitions and root `delegation.md` as well as the skill. Files
under `agents/` that are not package-owned remain the existing reported `EXTRA` class and are not
manifest violations; this preserves ratified external overlays without making them canonical.

There is no automatic fallback from source scope to deployment scope. A caller must name the
scope and manifest, so a truncated directory cannot silently receive weaker semantics.

### 3. Installer composition

`install.py claude-code` must derive its copy plan from the same package specification used by
the checker. It must refuse excluded shapes before writes, then emit the resolved manifest and
content-free summary. `--dry-run` emits the same plan without writes. `--check` retains its
current byte-history classification and additionally runs deployment-scope integrity against
the installed manifest. Any deployment-scope integrity failure exits nonzero regardless of drift
classification; the two failure conditions are OR-combined.

Deployment-scope validation is executed by the canonical source-tree checker against the
installed root. The deployed checker is a convenience copy and may not attest to its own digest.

The source-only edge list is reviewed data. The installer must not generate it by scanning for
whatever happens to be missing from the selected package; doing so would encode the failure as
policy.

The already-deployed excluded files are not deleted by this proposal. After implementation, the
next separately authorized deployment must baseline their exact paths and remove only package-
owned excluded paths that still match that baseline. A standalone cleanup requires its own
authority and rollback. No recursive deletion is permitted.

### 4. Test-first acceptance contract

The authorized implementation begins with failing tests for:

- exact set equality between the installer-derived missing edges and the declared source-only
  edge list (currently 12 for the named `install.py claude-code` plan);
- an undeclared thirteenth missing edge;
- a declared edge with the wrong source or target;
- path traversal, absolute paths, duplicate paths, unsupported schema, symlinks, non-regular
  files, and digest mismatch;
- a source-tree broken link, which must continue to fail under the default invocation;
- accidental inclusion of fixtures, runtime output, prompts, nested VCS state, or metadata;
- deterministic manifest order and bytes; and
- exact composition between the install plan and deployment validation;
- a deliberately perturbed installed agent pin and root `delegation.md`;
- a declared source-only edge whose target becomes present;
- a target that resolves outside the package root; and
- a constructed fixture tree containing untracked fixtures, runtime output, prompts, and nested
  VCS state, so CI does not depend on those files being present in its checkout.

The green gate installs into a new temporary Claude root, without touching either live host,
then requires:

```text
python3 check_state.py TEMP_ROOT/skills/delegation-triage/STATE.md
python3 check_wids.py --scope deployment --manifest MANIFEST TEMP_ROOT
python3 install.py claude-code --root TEMP_ROOT --check
```

It also requires the existing source invocation, syntax checks, plugin determinism checks, and
repository CI-equivalent checks to pass. A later cross-host parity proposal may cite this gate;
it must still establish its own authority, baseline, rollback, and fresh-session loading.

Both checkers must use `argparse` or an equivalently explicit parser. The existing broken
`check_state.py --today DATE` behavior is repaired and regression-tested in the same slice.
The isolated state check intentionally duplicates the repository's calendar-expiry gate; an
expired `STATE.md` must fail both.

## Authorized implementation write set

The implementation write set includes only:

- `adapters/claude-code/package-spec.json`;
- `install.py`;
- `check_wids.py`;
- `check_state.py`;
- focused new or existing tests;
- `adapters/claude-code/INSTALL.md`;
- `agents/MANIFEST.md` for the deployment-manifest stamp contract;
- `WARRANTS.md` for the PWE repository locator;
- `.github/workflows/ci.yml` if the isolated-install gate is added there; and
- directly dependent proposal, review, status-map, and deployment-contract documentation.

This is the approved consequence set. Discovery of a need to change package contents, security
boundaries, `STATE.md`, route doctrine, agent definitions, or another repository requires a
visible amendment before implementation continues.

## Rollback and failure handling

Implementation rollback is reverting its future coherent commit before deployment. Any later
deployment requires a separate content-addressed baseline and exact-target
rollback. No implementation or deployment may rewrite the A1 receipt or baseline history.

If the isolated-install reproduction does not pass without weakening the full-source check, the
implementation stops and returns to design. If Alternative B's measured transitive closure is
small and free of excluded classes, the recommendation reopens rather than treating Alternative
A as predetermined.

## Independent review contract

One Apollo-local Claude Code session is authorized by the operator to review this proposal.
The reviewer owns no files and may not write, edit, deploy, commit, push, spawn descendants, or
make a second paid call. It must read the proposal, current installer/checker/CI/adapter sources,
and the A1 receipt, then challenge:

- whether the root-cause claim survives the null alternative;
- whether the source-only edge mechanism is explicit enough to remain fail-closed;
- whether the manifest/spec split is minimal and reproducible;
- compatibility and migration consequences;
- whether the test and rollback gates could detect a false pass; and
- whether any contract-bearing decision is hidden inside an implementation detail.

The requested route is Apollo's canonical `reviewer` profile at Opus, High, normal/no-fast
service posture, in a fresh print-mode session with read-only tools and no descendants. The
durable review receipt must distinguish planned, requested, and observed model, effort, harness,
profile digest, tool boundary, service posture, exit status, and artifact digest. A mismatch or
an unreadable required source makes the review non-decision-grade; it does not authorize retry.

## Decisions after review

1. **Closed provisionally:** Alternative A is recommended; measured Alternative B fails its
   reopening conditions.
2. **May defer:** whether source-only edges may ship as intentionally non-resolving Markdown links or require a
   future rendering step that replaces them with typed source locators.
3. **Decided 2026-08-04:** release materialization refuses the entire dirty source tree; no
   preview-class dirty-source path is authorized by this revision.
4. **Resolved in the proposed contract:** the manifest digest is anchored in canonical
   `agents/MANIFEST.md`; an installed copy is optional and non-authoritative.
