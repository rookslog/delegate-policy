# Deployment-aware package integrity — Apollo deployment and cleanup record

**Execution ID:** DT-DEPLOY-2026-08-04-001

**Authority:** operator instruction on 2026-08-04 to commit, deploy, and clean up after approving
DT-PROP-2026-08-04-001 with the clean-source rule

**Canonical commits:** implementation `56d06a389fb8b66c15f43abe66d7aaf17eb05cb5`;
preserved Cowork-boundary correction and deployment source
`aaa7f733bc2971a51496252e793f032153cb9317`

**Target:** Apollo user-level Claude installation

**Result:** 60-file package materialized; 22 exact excluded files moved to recoverable quarantine;
manifest stamp recorded; final integrity checks pending at the time this record was drafted

## Pre-write gates and rollback baseline

A clean clone at deployment commit `aaa7f73` ran 25 tests with 25 passing and remained clean after
the run. The pre-deploy dry-run resolved 60 package files and reported 40 `OK`, five `BEHIND`, four
`DIVERGED`, 11 `MISSING`, and eight external-overlay `EXTRA` agents.

Before writes, the executor captured all 60 planned destinations plus the absent prior package
manifest. Forty-nine planned files existed and 11 were absent; the old manifest was absent. The
content-free baseline is retained at the env-specific local locator
`~/Library/Application Support/delegation-triage/deploy-backups/DT-DEPLOY-2026-08-04-001/before-baseline.tsv`
with SHA-256 `7cd54a823795cb48eb99c9c5556e5482f2911ac19413fdc1ef8874bf80a8950a`.
Existing bytes are copied under the adjacent `before/` tree.

Rollback is therefore exact and recoverable: restore the baseline's 49 `FILE` rows, remove only
the baseline's 11 `MISSING` destinations plus the previously missing manifest, and restore the two
quarantined subtrees below. No rollback was executed.

## Divergence adjudication

The dry-run refused silent overwrite of five deployed byte sets. Direct diffs established:

- root delegation differed only by the canonical home-locator normalization;
- canonical `CONTRACT.md` adds the ratified north-star alignment rule;
- canonical `WARRANTS.md` adds repository locators, the external-overlay register, and W-026;
- canonical probe `INDEX.md` adds the intervening probe records; and
- live `STATE.md` contained the newer operator correction for Cowork loading while the first
  implementation commit still contained the stale row.

The first four changes are additive or superseding canonical state. The fifth would have been a
regression, so deployment stopped. The existing corrected `STATE.md` bytes were committed without
editing as `aaa7f73`; state and source-integrity checks passed, and a new clean clone was used for
deployment. No live-only content was silently discarded.

## Materialization and external stamp

The clean source installed the declared 60 files and wrote
`delegation-triage-package-manifest.json` with SHA-256
`a17d83ec50c30f495d23eb1f5495283a727ef440536a636ebf020ecad3308494` and source commit
`aaa7f733bc2971a51496252e793f032153cb9317`.

The exact external stamp is recorded in canonical `agents/MANIFEST.md`:

```text
<!-- claude-package-manifest:v1 sha256=a17d83ec50c30f495d23eb1f5495283a727ef440536a636ebf020ecad3308494 source_commit=aaa7f733bc2971a51496252e793f032153cb9317 -->
```

## Exact recoverable cleanup

Immediately before cleanup, all 22 live candidates were regular non-symlink files whose sizes and
SHA-256 values exactly matched the corresponding excluded source artifact. The content-free
baseline is retained beside the rollback copy as `cleanup-baseline.tsv`, SHA-256
`0204a9932d0030643fc234b1027c61052bb28827029ec2e236ff601db9b8439f`.

The executor moved the exact fixture and runtime subtrees to the env-specific recoverable locator
`~/Library/Application Support/delegation-triage/deploy-backups/DT-DEPLOY-2026-08-04-001/cleanup-quarantine/`.
It did not recursively delete them. After the move, zero files remained under the live package's
excluded fixture/runtime paths. The canonical untracked source artifacts were not changed.

| Relative path | Bytes | SHA-256 |
|---|---:|---|
| `probes/fixtures/P-20260720-claude-profile-activation/.git/HEAD` | 23 | `f6f2b945f6c411b02ba3da9c7ace88dcf71b6af65ba2e0d89aa82900042b5a10` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/config` | 137 | `cae33efdb02cf774435c1ff9cb16bcc1014606908530c6e1dc727615fe3e8cda` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/description` | 73 | `85ab6c163d43a17ea9cf7788308bca1466f1b0a8d1cc92e26e9bf63da4062aee` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/applypatch-msg.sample` | 478 | `0223497a0b8b033aa58a3a521b8629869386cf7ab0e2f101963d328aa62193f7` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/commit-msg.sample` | 1972 | `efc1401b0e99d1ff51494d154d98b46c1e99059bcd8bf9f73cecde19fd3eb23b` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/fsmonitor-watchman.sample` | 4611 | `9159720099ad5595b8e66645cbfd47763c1e920f46e0b50ae75e642bbec57ef0` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/post-update.sample` | 189 | `81765af2daef323061dcbc5e61fc16481cb74b3bac9ad8a174b186523586f6c5` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/pre-applypatch.sample` | 424 | `e15c5b469ea3e0a695bea6f2c82bcf8e62821074939ddd85b77e0007ff165475` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/pre-commit.sample` | 1649 | `57185b7b9f05239d7ab52db045f5b89eb31348d7b2177eab214f5eb872e1971b` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/pre-merge-commit.sample` | 416 | `d3825a70337940ebbd0a5c072984e13245920cdf8898bd225c8d27a6dfc9cb53` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/pre-push.sample` | 1374 | `ecce9c7e04d3f5dd9d8ada81753dd1d549a9634b26770042b58dda00217d086a` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/pre-rebase.sample` | 4898 | `4febce867790052338076f4e66cc47efb14879d18097d1d61c8261859eaaa7b3` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/pre-receive.sample` | 544 | `a4c3d2b9c7bb3fd8d1441c31bd4ee71a595d66b44fcf49ddb310252320169989` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/prepare-commit-msg.sample` | 1492 | `e9ddcaa4189fddd25ed97fc8c789eca7b6ca16390b2392ae3276f0c8e1aa4619` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/push-to-checkout.sample` | 2783 | `a53d0741798b287c6dd7afa64aee473f305e65d3f49463bb9d7408ec3b12bf5f` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/sendemail-validate.sample` | 2308 | `44ebfc923dc5466bc009602f0ecf067b9c65459abfe8868ddc49b78e6ced7a92` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/hooks/update.sample` | 3650 | `8d5f2fa83e103cf08b57eaa67521df9194f45cbdbcb37da52ad586097a14d106` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/index.lock` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `probes/fixtures/P-20260720-claude-profile-activation/.git/info/exclude` | 240 | `6671fe83b7a07c8932ee89164d1f2793b2318058eb8b98dc5c06ee0a5a3b0ec1` |
| `probes/fixtures/P-20260720-claude-profile-activation/README.md` | 216 | `371f29f8c66fc9425ecf24793f5fe526363c26f02272211b378dd57ca79b1241` |
| `probes/fixtures/P-20260720-claude-profile-activation/probe.txt` | 34 | `9e085e252611b82451f4cf6efb7ab225e5631485cb3afc8879298e241a811666` |
| `probes/runtime/P-20260720-claude-profile-activation/prompt.md` | 1932 | `c83c2ac59ac09f2be951cf11d354288e8bfc230b1e3ba3d02aca23c55aa503fe` |

## Remaining boundary

The eight external-overlay agents were reported but not modified. No push, Dionysus deployment,
cross-host parity claim, authenticated action, or session restart is part of this execution.
Roster definitions are byte-identical to their prior values, but the adapter contract still marks
a fresh session as the activation boundary for deployed surfaces.
