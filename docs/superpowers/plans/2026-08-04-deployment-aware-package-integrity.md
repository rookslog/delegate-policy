# Deployment-Aware Package Integrity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Claude Code package boundary explicit and reproducible while preserving strict source validation and refusing release-class deployment from a dirty source tree.

**Architecture:** `adapters/claude-code/package-spec.json` is reviewed package policy. `install.py` resolves only tracked sources from that policy and emits a deterministic manifest spanning the installation root; source-tree `check_wids.py` validates that manifest, the installed bytes, W-IDs, links, exact source-only edges, and an external manifest digest stamp in `agents/MANIFEST.md`. `check_state.py` and `check_wids.py` use explicit `argparse` contracts.

**Tech Stack:** Python 3.12+ standard library, `unittest`, JSON, Git CLI, existing deterministic repository checks.

**Execution status:** completed and corroborated in the uncommitted Apollo worktree; see
`DT-EXEC-2026-08-04-001`. Deployment, cleanup, commit, push, and parity execution remain outside
this plan.

## Global Constraints

- Source validation remains the default and remains strict.
- Release-class Claude deployment refuses any dirty canonical source tree before writes.
- `--check` and source checks remain available against dirty working state; only deployment is refused.
- Only `git ls-files`-tracked regular sources may enter a release manifest.
- Fixtures, runtime output, prompts, nested VCS state, filesystem metadata, credentials, settings, hooks, sessions, and telemetry are excluded.
- The manifest covers the skill tree, package-owned agent definitions, and root `delegation.md` from the Claude installation root.
- Extra non-package agents are reported as `EXTRA`, not deleted or treated as canonical.
- Source-only links are exact reviewed edges, never inferred from absence.
- The canonical source checker validates deployments; the deployed checker cannot attest to itself.
- Manifest integrity failure and genuine divergence are OR-combined nonzero exit conditions.
- No live-host cleanup, deployment, parity retry, commit, push, model call, or descendant agent is authorized by this implementation plan.
- Preserve the pre-existing dirty `STATE.md` and untracked probe artifacts.

---

### Task 1: Explicit checker CLI parsing

**Files:**
- Create: `tests/test_package_integrity.py`
- Modify: `check_state.py`
- Modify: `check_wids.py`

**Interfaces:**
- Consumes: existing source-check behavior and `check_state.py [STATE] --today YYYY-MM-DD` documentation.
- Produces: `check_state.parse_args(argv)` and `check_wids.parse_args(argv)` with deterministic source/deployment mode validation.

- [x] **Step 1: Write failing subprocess tests**

Add real CLI tests proving:

```python
def test_check_state_today_value_is_not_misparsed_as_state_path(self):
    completed = run_python(CHECK_STATE, "--today", "2026-07-12")
    self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)

def test_check_wids_deployment_requires_manifest(self):
    completed = run_python(CHECK_WIDS, "--scope", "deployment", self.temp_root)
    self.assertNotEqual(0, completed.returncode)
    self.assertIn("--manifest", completed.stderr)
```

The production mutation each catches is respectively consuming an option value as a positional path and silently accepting deployment mode without a manifest.

- [x] **Step 2: Run RED**

Run:

```text
python3 -m unittest -v tests.test_package_integrity.CheckerCliTests
```

Expected: `--today` fails with `STATE file not found: 2026-07-12`; deployment parsing fails for the wrong reason because `--scope` does not exist.

- [x] **Step 3: Implement minimal `argparse` parsers**

`check_state.py` accepts optional `state_path` plus `--today`. `check_wids.py` accepts optional root, `--scope {source,deployment}` defaulting to source, and requires `--manifest` only for deployment. Do not change source validation behavior.

- [x] **Step 4: Run GREEN and source regression**

```text
python3 -m unittest -v tests.test_package_integrity.CheckerCliTests
python3 check_state.py
python3 check_wids.py
```

Expected: tests pass; current source checks remain green.

### Task 2: Declarative tracked-source package plan

**Files:**
- Create: `adapters/claude-code/package-spec.json`
- Modify: `install.py`
- Modify: `tests/test_package_integrity.py`

**Interfaces:**
- Consumes: schema-versioned JSON with `exact_files`, `tracked_globs`, `forbidden_parts`, `forbidden_names`, and `source_only_links`.
- Produces: `load_package_spec(path) -> dict` and `claude_code_plan(root, spec=None) -> list[tuple[Path, Path]]`.

- [x] **Step 1: Write failing plan tests**

Construct a temporary Git repository containing tracked runtime files plus tracked and untracked files under `probes/fixtures/`, `probes/runtime/`, and nested `.git/`. Assert literal planned destination paths include the eight runtime files, four probe navigation files, tracked `probes/records/*.md`, tracked `agents/*.md` except `MANIFEST.md`, and root `delegation.md`; assert all excluded classes and untracked files are absent.

Also assert unsupported schema, absolute paths, traversal, duplicate destinations, missing tracked source, symlink source, and non-regular source raise `PackageSpecError`.

- [x] **Step 2: Run RED**

```text
python3 -m unittest -v tests.test_package_integrity.PackagePlanTests
```

Expected: import or symbol failure for `load_package_spec` / `PackageSpecError`.

- [x] **Step 3: Implement the minimal resolver**

Replace `probe_files().rglob("*")` and the hard-coded `SKILL_FILES` composition with the package specification. Resolve globs only against `git ls-files -z`; require regular non-symlink files; sort destinations lexically; reject duplicate source or destination paths and every forbidden path component/name.

Populate `source_only_links` with the 12 literal current edges named in DT-REV-2026-08-04-001, using canonical source paths and literal targets.

- [x] **Step 4: Run GREEN**

```text
python3 -m unittest -v tests.test_package_integrity.PackagePlanTests
python3 install.py claude-code --dry-run --root "$(mktemp -d)"
```

Expected: plan tests pass. The repository dry-run refuses release materialization while the source tree is dirty and writes nothing.

### Task 3: Deterministic manifest and clean-release refusal

**Files:**
- Modify: `install.py`
- Modify: `tests/test_package_integrity.py`

**Interfaces:**
- Produces: `build_manifest(pairs, spec, source_commit) -> dict`, `manifest_bytes(manifest) -> bytes`, `manifest_sha256(data) -> str`, and installed manifest path `INSTALL_ROOT/delegation-triage-package-manifest.json`.

- [x] **Step 1: Write failing manifest tests**

From a clean committed fixture repository, assert two builds are byte-identical and lexically ordered. Assert each entry contains destination-relative path, source-relative path, size, mode, and SHA-256; top-level fields contain schema version, package-spec digest, source commit, and `dirty_source: false`. Assert dirty tracked, dirty untracked, and staged source trees all refuse deployment before creating a destination.

- [x] **Step 2: Run RED**

```text
python3 -m unittest -v tests.test_package_integrity.ManifestTests
```

Expected: missing manifest helpers and dirty-source refusal.

- [x] **Step 3: Implement deterministic serialization and pre-write guard**

Use canonical UTF-8 JSON (`sort_keys=True`, compact separators, final newline). Run `git status --porcelain=v1 -uall` against the entire repository before a write-mode Claude install and return nonzero with a content-free refusal if any entry exists. Build the manifest fully before creating destination directories. `--dry-run` reports the same refusal without writes; `--check` does not invoke the clean-source deployment guard.

- [x] **Step 4: Run GREEN**

```text
python3 -m unittest -v tests.test_package_integrity.ManifestTests
```

Expected: all manifest and pre-write tests pass.

### Task 4: Fail-closed deployment validation

**Files:**
- Modify: `check_wids.py`
- Modify: `tests/test_package_integrity.py`
- Modify: `agents/MANIFEST.md`

**Interfaces:**
- Produces: `validate_deployment(installation_root, manifest_path, stamp_path) -> ValidationResult` and stamp form `<!-- claude-package-manifest:v1 sha256=<64 lowercase hex> source_commit=<40 lowercase hex> -->`.

- [x] **Step 1: Write failing manifest-shape and tree tests**

Create literal manifests and installed trees. Separate tests must fail for malformed JSON, unsupported schema, duplicate paths, absolute paths, traversal, symlink/non-regular entries, size/digest/mode mismatch, missing entries, extra files under the package skill tree, missing or mismatched external stamp, and modified deployed checker self-attestation.

Assert an extra agent not named in the manifest is printed as `EXTRA` and does not fail.

- [x] **Step 2: Run RED**

```text
python3 -m unittest -v tests.test_package_integrity.DeploymentManifestTests
```

Expected: deployment mode is not implemented.

- [x] **Step 3: Implement manifest/stamp/tree validation**

Validate the manifest before reading installed content. Require its byte digest in the canonical stamp file. Compare all package-owned files under the skill root and named root/agent destinations. Reject symlinks and path escape. Keep unrelated root surfaces unread and ignore them; list only extra Markdown agent definitions as `EXTRA`.

- [x] **Step 4: Write RED source-only link tests**

Use the 12 literal declared edges. Tests must prove:

- the bounded installed package reports exactly those edges as `SOURCE_ONLY` and exits 0;
- an undeclared thirteenth missing edge fails;
- a declaration with wrong source or target fails;
- a declared target that becomes present fails as stale;
- a target present outside the installation root fails;
- a target inside the root but absent from the manifest fails;
- source mode fails if a declaration's canonical target is missing or the source no longer contains the link; and
- source mode still fails an ordinary undeclared broken link.

- [x] **Step 5: Run link RED**

```text
python3 -m unittest -v tests.test_package_integrity.SourceOnlyLinkTests
```

Expected: current checker treats declared deployed edges as ordinary failures and does not cross-check declarations.

- [x] **Step 6: Implement exact link and W-ID semantics**

Share existing W-ID, relative-link, exemption, and forbidden-path logic between modes. In deployment mode, a present file target must be contained by the installation root and listed in the manifest; a directory target is present only when at least one manifest entry is beneath it. Declared absent edges print `SOURCE_ONLY`; all other missing edges fail. Cross-check every declaration during source mode.

- [x] **Step 7: Run GREEN**

```text
python3 -m unittest -v tests.test_package_integrity.DeploymentManifestTests tests.test_package_integrity.SourceOnlyLinkTests
python3 check_wids.py
```

Expected: focused tests and strict source check pass.

### Task 5: Installer composition and isolated-install regression

**Files:**
- Modify: `install.py`
- Modify: `tests/test_package_integrity.py`

**Interfaces:**
- Consumes: source-tree `check_wids.validate_deployment` and the installed manifest.
- Produces: `install.py claude-code --check` that OR-combines divergence and deployment-integrity failures.

- [x] **Step 1: Write failing end-to-end tests**

Copy the minimal package source into a temporary Git repository, commit it, run the real `install.py claude-code --root TEMP_ROOT`, stamp the emitted manifest digest in the fixture's canonical `agents/MANIFEST.md`, then run:

```text
python3 check_state.py TEMP_ROOT/skills/delegation-triage/STATE.md
python3 check_wids.py --scope deployment --manifest TEMP_ROOT/delegation-triage-package-manifest.json TEMP_ROOT
python3 install.py claude-code --root TEMP_ROOT --check
```

Assert all pass. Perturb a roster pin, root `delegation.md`, a skill file, and the manifest in separate tests; each must make `--check` nonzero. Assert `BEHIND` may remain informational only when deployment integrity still matches the stamped manifest.

- [x] **Step 2: Run RED**

```text
python3 -m unittest -v tests.test_package_integrity.IsolatedInstallTests
```

Expected: no emitted manifest and no deployment-integrity composition.

- [x] **Step 3: Implement minimal integration**

Write selected files and the manifest only after the clean-source guard. Keep the existing byte-history classification. Invoke source-tree deployment validation for `--check`, print its deterministic summary, and return 1 when either genuine divergence or integrity validation fails.

- [x] **Step 4: Run GREEN and mutation checks**

```text
python3 -m unittest -v tests.test_package_integrity.IsolatedInstallTests
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected: all tests pass. Temporarily disabling the full-root agent/delegation checks, stamp check, containment check, or clean-source guard must make at least one named test fail; restore immediately after each check.

### Task 6: Documentation, CI, and closure evidence

**Files:**
- Modify: `adapters/claude-code/INSTALL.md`
- Modify: `.github/workflows/ci.yml`
- Modify: `docs/proposals/2026-08-04-deployment-aware-package-integrity.md`
- Modify: `docs/reviews/2026-08-04-deployment-aware-package-integrity-opus-adjudication.md`
- Modify: `docs/proposals/README.md`
- Modify: `WARRANTS.md` only if dependent locator text changes
- Modify: `agents/MANIFEST.md`

**Interfaces:**
- Produces: current command documentation, deterministic CI gate, and an execution record separated from proposal/review chronology.

- [x] **Step 1: Update documentation after behavior is green**

Correct `INSTALL.md`: `MISSING` and `BEHIND` are informational under legacy drift classification but deployment integrity is fail-closed; document manifest location, external stamp, clean-source refusal, extra-agent behavior, and rollback. Add the unittest suite to CI before source checks. Record implementation state without claiming deployment or cleanup.

- [x] **Step 2: Run complete verification**

```text
python3 -m py_compile check_state.py check_wids.py install.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 check_state.py
python3 check_wids.py
python3 install.py cowork
python3 install.py cowork --check
python3 install.py claude-code --dry-run
python3 install.py codex > /dev/null
git diff --check
```

Expected: all deterministic tests/checks pass except the Claude dry-run must deliberately refuse the current dirty source tree before writes. Record that nonzero result as the expected clean-source gate, then repeat the dry-run from a clean temporary clone and require exit 0.

- [x] **Step 3: Inspect boundaries**

Require the exact before/after status to retain the pre-existing `STATE.md`, probe fixtures, and runtime artifacts. Confirm no path under the live Apollo Claude root changed, no cleanup occurred, and no commit or push occurred.

- [x] **Step 4: Stop at version-control authority**

Present the coherent implementation diff, test evidence, expected dirty-tree refusal, and remaining deployment/cleanup boundary. Do not stage, commit, push, deploy, or retry parity without separate owner authority.
