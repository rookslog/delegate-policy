CONCUR_WITH_CHANGES

## Basis

I read the frozen proposal (SHA-256 confirmed `0fe02735…e7493` — Corroborated, `shasum -a 256`), `install.py`, `check_wids.py`, `check_state.py`, `adapters/claude-code/INSTALL.md`, `agents/MANIFEST.md`, `.github/workflows/ci.yml`, and the A1 receipt at `~/Development/personal-work-ecosystem/evidence/2026-08-04-harness-parity-review-readiness-receipt.md`.

I did not accept the proposal's evidence on report. I re-derived the installed package from `install.py`'s own `claude_code_plan()` and re-ran the checker's link logic against that simulated layout, read-only, without installing anything. The root-cause claim survives: **exactly 12 broken relative edges**, matching the receipt's count (Corroborated). I then measured the Alternative B closure the proposal declined to measure, and it refutes B on B's own stated reopening condition.

The direction is right and the evidence discipline in the document is unusually good. Two findings are contract-bearing and one of them is a live, undisclosed deployed state, so the text is not yet decision-grade as written.

---

## Findings

### F-01 · BLOCKER · Deployment scope validates 123 of 131 manifest entries; the 8 it omits are the highest-consequence files

**Primary source.** `install.py:62-72` (`claude_code_plan`) writes to three destination trees: `root/skills/delegation-triage/**` (123 files), `root/agents/*.md` (7 roster pins), and `root/delegation.md` (1). Proposal §2 and §4 invoke deployment scope with a single `PACKAGE_ROOT`:

> `python3 check_wids.py --scope deployment --manifest MANIFEST TEMP_ROOT/skills/delegation-triage`

**Consequence.** Requirement §2.2 — "require the actual installed declared file set and digests to equal the manifest" — cannot reach the 7 roster pins or `delegation.md`. Those are exactly the files whose corruption matters most: the pins carry `model:`/effort frontmatter that decides every spawn, and `install.py:68-70` states in its own comment that `~/.claude/delegation.md` is "@-imported by the user's global CLAUDE.md (highest-precedence config surface)". `install.py --check` does inspect them, but it compares against *canonical source*, not against the manifest, and it exits non-zero **only** on `DIVERGED` (`install.py:154`). A deployment carrying a *superseded but once-canonical* pin classifies as `BEHIND` and exits 0. That is not hypothetical: `agents/MANIFEST.md:17` records precisely this failure — `explorer.md` stayed `model: opus` in canonical after the sonnet ruling, so "`install.py claude-code` would have silently reverted the ruling in the live roster." Manifest-equality is the only check that catches it, and the specified invocation cannot see the file.

**Smallest correction.** Specify deployment scope as taking the *installation root* plus the manifest, validating every manifest entry across all destination trees, with an explicit rule that unlisted files in `root/agents/` are reported (the existing `EXTRA` class, per `install.py:105-112`) and not treated as manifest violations — otherwise the ratified external `sol-*` overlay (`agents/MANIFEST.md:36`) makes equality unsatisfiable on any live host.

---

### F-02 · BLOCKER · The installer already ships three named excluded classes, and 41 such files are live in Apollo's deployment right now

**Primary source.** `install.py:50-51`: `probe_files()` is an unbounded `rglob("*")` over `probes/`. Corroborated by direct measurement of the plan and of the live deployment:

- Plan today: 115 probe files, of which **70 are `probes/fixtures/**`**, **1 is `probes/runtime/…/prompt.md`**, and **19 are a nested `.git/` tree** (`HEAD`, `config`, `index.lock`, hooks) inside `probes/fixtures/P-20260720-claude-profile-activation/`.
- Live `~/.claude/skills/delegation-triage`: 67 files, of which **21 fixtures, 19 nested `.git/` files, and 1 runtime prompt** are present now.

The proposal's Constraints declare "fixtures, filesystem metadata… runtime prompts, generated outputs, nested VCS state" outside the portable package, and §1 says selection "must not recurse through arbitrary runtime, fixture, prompt, metadata, or VCS trees."

**Consequence.** The Trigger and evidence section reports only the link-integrity mismatch. It does not tell the decision owner that the same installer is currently placing nested VCS state and a runtime prompt on a live host. This changes the decision: §"Proposed write set" excludes package contents, and the proposal's own rule says "Discovery of a need to change package contents… requires a visible amendment before implementation continues." That amendment is already required, before authorization, not after. Rollback ("no runtime state changes") also leaves the deployed excluded content in place with no remediation obligation.

**Smallest correction.** Add one paragraph to Trigger and evidence stating the measured current inclusion and the live counts, and move "narrow the `probes/` selection rule" from an implicit §1 consequence into the explicit write set, with a named disposition for the already-deployed content (remediate on next deploy, or a separate authorized cleanup).

---

### F-03 · MAJOR · The deployed checker validates its own digest — no independent trust anchor

**Primary source.** `install.py:34-35` puts `check_wids.py` and `check_state.py` in `SKILL_FILES`; proposal §2.2 requires the installed declared file set and digests to equal the manifest, and §4's green gate runs the *deployed* checker against the *deployed* package.

**Consequence.** A modified deployed checker attests to its own integrity. The gate is fail-closed against accident and open against any edit that touches the checker. Combined with F-04, the manifest and its verifier both live inside the artifact they certify.

**Smallest correction.** State that deployment-scope validation is executed by the **source-tree** checker against the installed root, and that the deployed checker copy is a convenience artifact whose digest is authoritative only when checked from source.

---

### F-04 · MAJOR · The manifest is unanchored, so regeneration launders any change

**Primary source.** §1: "Each installation derives an immutable manifest"; Open decision 4 asks whether it lives inside the installed skill, beside the receipt, or both.

**Consequence.** "Immutable" is asserted, not mechanized. If the manifest sits inside the package root, re-running the installer or editing both file and manifest yields a passing package with no external referent. The receipt records `source commit` and a package-level `dirty-source classification`, but nothing binds a given installed tree to a manifest a reviewer trusts.

**Smallest correction.** Require a single manifest digest recorded outside the installed tree — the `agents/MANIFEST.md` deployment stamp is the existing mechanism — and make deployment scope refuse a manifest whose digest is not the stamped one.

---

### F-05 · MAJOR · `SOURCE_ONLY` over-declaration is not a failure, so the edge list can be pre-loaded

**Primary source.** §2.5 requires printing "each declared absent edge as `SOURCE_ONLY`". §2.6 fails "every missing edge not declared exactly." Nothing fails a declared edge whose target *is* present, or whose declaration is stale.

**Consequence.** The list is append-friendly and never shrinks under pressure. A future edge can be declared before it goes missing, and a declaration that stopped applying survives silently. §3's prohibition on auto-generation is a policy sentence with no enforcing mechanism; over-declaration is the same laundering by a slower route.

**Smallest correction.** Add a seventh deployment-scope rule: fail on a declared source-only edge whose target is present in the package, and fail in **source** scope on a declared edge whose target does not resolve in the source tree. Both make the list self-pruning and cross-checked.

---

### F-06 · MAJOR · A link target that escapes the package root counts as "present"

**Primary source.** §2.1 refuses traversal in *manifest entries*. §2.4 passes a link "when its target is present and regular" with no containment rule. 10 of the 12 real edges use `../../` (measured).

**Consequence.** `probes/records/X.md → ../../docs/reviews/Y.md` resolves, from the skill home, to `~/.claude/skills/docs/reviews/Y.md`. If any such path exists on a host for any reason, the edge grades as present and the package validates on that host and fails on a clean one. That is non-reproducibility introduced by the very check meant to establish it.

**Smallest correction.** Require every link target to resolve to a path *inside* the package root and to appear in the manifest; otherwise it is missing, declared or not.

---

### F-07 · MAJOR · The `--check` constraint pair is unsatisfiable, because the existing classifier mislabels nested-VCS content

**Primary source.** Constraint: "`install.py --check` keeps its existing drift semantics; lag and unclassifiable dirty-source state must not be mislabeled as divergence." Corroborated by execution:

```
source_dirty('probes/fixtures/P-20260720-claude-profile-activation/README.md') → False
git status --porcelain -uall -- <that path> → (empty)
```

Files inside the nested `.git/`-bearing fixture are invisible to `git status`, so `source_dirty` returns False and `in_history` returns False. Any lag on those files classifies as **`DIVERGED`** and exits 1 — the false accusation that the `DRIFT?` state was created to prevent (`install.py:91-102`).

**Consequence.** Preserving "existing semantics" preserves a classifier that is blind in exactly the tree F-02 says should not ship. The two constraints cannot both hold without a change to `install.py`'s classification.

**Smallest correction.** Either resolve it by F-02 (stop shipping the nested VCS tree, which removes the blind spot) and say so, or add a third classification input — per-file tracked / untracked / inside-nested-VCS — and state that untracked-provenance files can never reach `DIVERGED`.

---

### F-08 · MAJOR · CI and a developer install do not build the same package, so the determinism test can be green while the real package differs

**Primary source.** `.github/workflows/ci.yml:28` runs `install.py claude-code --dry-run`. 22 of the plan's files are untracked (`git ls-files` comparison, Corroborated), including the whole nested-VCS fixture and `probes/runtime/…/prompt.md`. A CI checkout does not contain them.

**Consequence.** §4's "deterministic manifest order and bytes" and "accidental inclusion of fixtures, runtime output, prompts, nested VCS state" tests would pass in CI on a plan that omits precisely the files that fail locally. This is the direct affirmative answer to review question 5.

**Smallest correction.** Require the exclusion tests to assert against a fixture tree constructed in the test (so the classes are always present), not against whatever the checkout happens to contain, and state that the package specification must select only `git ls-files`-tracked paths.

---

### F-09 · MAJOR · Deployment-scope failure has no specified exit-code effect on `--check`

**Primary source.** §3: "`--check` retains its current byte-history classification and additionally runs deployment-scope integrity against the installed manifest." `install.py:154` returns non-zero only on `DIVERGED`.

**Consequence.** Whether a deployment-scope failure fails `--check` is undefined. This is exactly the class the review contract asks about — "whether any contract-bearing decision is hidden inside an implementation detail."

**Smallest correction.** One sentence: deployment-scope failure exits non-zero regardless of drift classification, and the two exit conditions are OR-combined.

---

### F-10 · MAJOR · The sole evidence locator uses an unregistered prefix

**Primary source.** The proposal cites `personal-work-ecosystem:evidence/…`. `WARRANTS.md:17-33` (KNOWN-REPOS locator key) lists 13 prefixes; `personal-work-ecosystem:` is not among them. A repo-wide grep returns only the proposal and its own review prompt (Corroborated).

**Consequence.** The document's only primary evidence is cited in a form the package's own convention cannot resolve, and `check_wids.py` does not validate prefixes (it only flags absolute paths, `check_wids.py:18`). I resolved it by Spotlight, not by the register.

**Smallest correction.** Add the `personal-work-ecosystem:` row to the KNOWN-REPOS key in the same pass [per: propagation].

---

### F-11 · MINOR · `INSTALL.md` already misstates `--check` semantics

**Primary source.** `adapters/claude-code/INSTALL.md:8`: "`--check`: re-hash the deployed copies and diff against canonical (exit 1 on drift/missing)." `install.py:154` exits 1 only on `DIVERGED`; `MISSING` and `BEHIND` exit 0.

**Consequence.** The file the write set proposes to edit is the wrong baseline for "existing drift semantics."

**Smallest correction.** Correct the line as part of the write set and note the pre-existing drift.

---

### F-12 · MINOR · Ad-hoc flag parsing is the established local pattern, and it is already broken

**Primary source.** `check_state.py:29` — `args = [a for a in argv[1:] if not a.startswith("--")]`. Corroborated by execution:

```
$ python3 check_state.py --today 2026-07-12
FAIL: STATE file not found: 2026-07-12   (exit 1)
```

The invocation documented in `CLAUDE.md` §Commands does not work: the flag's *value* is consumed as the positional path.

**Consequence.** §2 adds `--scope` and `--manifest` to `check_wids.py`, whose current parsing is `Path(argv[1])`. Under the same pattern, `PACKAGE_ROOT` could be silently taken from a flag value — a truncated or wrong root receiving validation, which is the failure §2's "no automatic fallback" clause exists to prevent.

**Smallest correction.** Require `argparse` for both scripts in the write set, and fix `--today` in the same pass.

---

### F-13 · MINOR · "The current 12-edge reproduction" is ambiguous and is a moving target

**Primary source.** The receipt describes a 60-file PWE package (50 md on Dionysus, 55 on Apollo); `install.py`'s plan is 131 files, 64 md under the skill home. Both yield 12 (Corroborated for `install.py`; Reported for the PWE package). 10 of the 12 originate in `probes/records/`; 5 of 40 records currently link to `../../docs/` (measured).

**Consequence.** A test named "the current 12-edge reproduction" is pinned to a number that changes whenever a probe record cites a review or proposal — a documented, recurring editing pattern (`CLAUDE.md` §Editing discipline). The test will read as a regression when it is a normal append.

**Smallest correction.** Name the packager (`install.py claude-code`) and assert *set equality against the declared edge list*, not a count.

---

### F-14 · NOTE · Deployed `STATE.md` expiry couples the isolated-install gate to calendar time twice

`ci.yml:21` already fails on expired STATE entries by design. The §4 green gate adds `check_state.py TEMP_ROOT/…/STATE.md`, which will fail for the same reason at the same moment. Not a defect; worth one sentence so a future reader does not read the isolated-install gate as broken. (Deployed STATE currently passes: 9 dated, 3 exempt, OK — Corroborated.)

---

## Alternatives A and B, compared on measurement

The proposal defers this: B "remains viable if measurement shows the closure is small and contains no excluded class." I measured it (transitive Markdown closure from the shipped set, Corroborated).

| | Alternative A | Alternative B |
|---|---|---|
| Extra Markdown files | 0 | **53** |
| Added bytes | 0 | **823,364 (804 KiB)** vs 319,211 shipped — **+258%** |
| Excluded classes pulled in | none | `docs/research/external/**` PROVENANCE (external-provenance, explicitly exempted from link checks at `check_wids.py:40-42`), `docs/superpowers/plans/` (3), `docs/handoffs/` (3), `docs/research/` (3) |
| Maintainer-only surfaces pulled in | none | `CLAUDE.md`, `AGENTS.md`, `PROGRAMME.md`, `LANES.md`, `ROADMAP.md`, `LINEAGE.md`, `README.md`, `agents/MANIFEST.md` |
| Unratified material | none | `docs/proposals/` (13), `docs/reviews/` (22) — including two **untracked** files: the proposal under review and its own preflight record |
| Ongoing cost | declare ~1 edge per 8 new probe records (5/40 measured) | closure recomputed and re-shipped on every doc addition; grows monotonically |

**B fails its own reopening condition on both clauses.** The closure is not small, and it contains named excluded classes. It would also ship a runtime skill package containing the maintainer's governance files and unratified drafts — the second time this package would have put unratified material on a live host (the first is F-02).

A is the correct direction. Its cost — a hand-curated edge list with real churn — is the price of the boundary being explicit, and F-05's self-pruning rule is what keeps that list from becoming the laundering surface.

---

## Answers to the six review questions

**1. Does primary evidence support the contract mismatch, including the boring alternative?**
Yes, and I confirmed it independently rather than relying on the receipt. Simulating `install.py claude_code_plan()` and re-running the checker's link logic produced **exactly 12** broken edges — the same count the receipt reports for a *different* 60-file package, which strengthens rather than weakens the claim, since the 12 live in files common to both. Source scope currently passes (160 md files, 26 W-records, exit 0 — Corroborated), so the failure is purely a deployment-boundary artifact. The boring alternative is refuted by measurement, not by argument (see the table above). What the evidence does *not* establish is that the proposed repair is the best one; the proposal says so itself, correctly.

**2. Does the source/deployment split remain fail-closed?**
Not as written. Four laundering routes are open: over-declared or stale `SOURCE_ONLY` edges (F-05), targets escaping the package root (F-06), a self-validating deployed checker (F-03), and an unanchored manifest (F-04). Each has a one-clause fix. The *design intent* — explicit edges, no basename or directory exemption, no automatic fallback from source to deployment scope — is sound and materially better than Alternative D.

**3. Is one specification plus one materialized manifest the smallest coherent contract?**
Yes. The split earns itself: the specification is reviewed policy, the manifest is a per-installation receipt, and collapsing them would make the policy re-derivable from whatever was installed — the exact inversion §3 rules out. The smallness claim fails only on scope, not on count: one manifest is right, but it must cover all three destination trees (F-01).

**4. Are compatibility, dirty-source, migration, privacy, and audit boundaries explicit enough?**
No, in two places. The audit boundary omits the live excluded-class deployment (F-02) — the most consequential omission in the document. The dirty-source boundary states two constraints that cannot both hold against the current classifier (F-07). Compatibility is otherwise handled well: the default invocation is unchanged, there is no silent fallback, and the privacy rule on the receipt (no prompts, credentials, absolute paths, or file contents) is correctly specified. Migration is thin but adequate, since the source path is unchanged.

**5. Could the tests pass while a real installed package is unusable or non-reproducible?**
Yes, by three independent routes. CI builds a different package than a developer does, because 22 plan files are untracked (F-08). The green gate installs to a fresh temp root, where `install.py --check` is trivially all-`OK` and cannot detect anything. And `--check` on a real host exits 0 on `BEHIND`, so a superseded roster pin — the documented `explorer.md` incident at `agents/MANIFEST.md:17` — passes (F-01). Fixing F-01 and F-08 closes the first and third; the second needs the gate to assert against a deliberately perturbed tree, not a freshly installed one.

**6. Which open decisions must be resolved before implementation authority is meaningful?**
Open decision 1 (A vs B) is resolved by the measurement above — B is refuted; record it and close it. Open decision 4 (where the manifest lives) is **not** a filing question and must be resolved first: it determines whether F-04's trust anchor exists. Open decision 3 (dirty-source deployments) must be resolved because F-07 shows the current classifier cannot distinguish the cases it would need to. Open decision 2 (rendering source-only links as typed locators) can safely defer. Beyond the listed four, F-01 and F-02 must be settled in the proposal text, because both change the contract and the write set.

---

## Remaining uncertainty, and what would reduce it

- **[UNCERTAIN]** Whether the PWE A1 package's 12 edges are the *same 12* I measured for `install.py`'s plan. The receipt gives counts, not the edge list. Publishing the failing checker output from A1 would settle it. This does not change the verdict — both packages fail, and the fix is the same.
- **[Not tested]** No proposed code exists, so every claim about the new scope is a reading of the specification, not of behavior. An isolated install into a temp root would test F-01, F-06, and F-08 directly; I did not run one, because the review contract forbids writes.
- **[Underdetermined]** Whether the live Apollo deployment's nested `.git/` tree has caused any observable harm. I measured its presence, not its effect.
- **[Reported, not Corroborated]** Everything specific to Dionysus, the baselines, the rollback verification, and the signal-chain IDs. I had no access to that host and did not attempt any.

---

## What this review does not certify

I applied one lens: contract completeness and failure modes of the proposed integrity mechanism. I did **not** review routing doctrine, `ROUTES.md`/`WARRANTS.md` content or grading, the Cowork and Codex install targets, the `personal-work-ecosystem` repository's own tooling or the correctness of its rollback, the signal-layer records, cross-host parity readiness, the proposal's prose, or any security question beyond the excluded-class and traversal boundaries named above. I executed no install, wrote no file, spawned nothing, and made no second model call.

**Areas probed and found sound:** the root-cause claim and its 12-edge reproduction (re-derived independently); the decision to keep source scope strict and unchanged as the default; the refusal of an automatic source→deployment fallback (§2, closing the truncated-directory hole); the rejection of Alternative D on stated grounds; the receipt's privacy rule (no prompts, model output, credentials, absolute paths, or contents); the test list's coverage of traversal, absolute paths, duplicates, symlinks, non-regular files, and digest mismatch; the write-set forecast's explicit non-authority clause; the rollback section's refusal to rewrite A1 history; and the prohibition in §3 on generating the source-only list by scanning — the single most important sentence in the document.

---

## Implementation authorization recommendation

**NOT_READY_FOR_OWNER_DECISION** — narrowly, and on a bounded list.

The recommendation itself is correct and now has measured support that the draft lacked. But two findings are contract-bearing, and one of them (F-02) triggers the proposal's own amendment rule: implementation would immediately discover a need to change package contents. Authorizing the current text would authorize a contract whose validation scope omits the roster pins and `delegation.md`, and would leave the operator unaware that nested VCS state and a runtime prompt sit in `~/.claude` today.

Four edits make it ready, and none of them require new evidence: fold F-01 and F-02 into the contract and the write set; add the F-05 and F-06 clauses to §2; close open decision 1 with the measured closure; and resolve open decision 4 as a prerequisite rather than a follow-up. That is a text amendment, not a redesign, and it does not need another paid review pass.
