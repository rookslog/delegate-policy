# Claude Code adapter — scripted install

Deploy = `python3 install.py claude-code` (default root `~/.claude`; use `--root` to override) +
record the printed manifest stamp in canonical `agents/MANIFEST.md` + **restart**. The package
boundary is declared by `package-spec.json`; only tracked regular files selected by that spec are
copied. Fixtures, runtime output, prompts, nested VCS state, and other forbidden classes cannot
enter a release package.

Release materialization is clean-source only. Both a real install and `--dry-run` refuse before
writes when `git status --porcelain=v1 -uall` reports any tracked, staged, or untracked change in
the canonical repository. `--check` remains available against a dirty source because it observes
an existing deployment rather than creating a release.

The install writes `delegation-triage-package-manifest.json` at the Claude installation root. Its
deterministic entries cover the package-owned skill files, seven roster definitions, and root
`delegation.md`. The manifest records source and destination paths, source commit, size, mode, and
SHA-256 without file contents or user-specific absolute paths. It is not its own trust anchor: a
deployment is accepted only after the exact printed digest and source commit are stamped outside
the installed tree in canonical `agents/MANIFEST.md`.

- `--dry-run`: resolve and report the exact package and would-be manifest without writing.
- `--check`: retain the legacy byte-history classes, then validate the installed manifest, stamp,
  full package-owned tree, W-IDs, and links with the canonical source checker. `DIVERGED` or any
  integrity failure exits nonzero. `BEHIND` remains informational only while the stamped installed
  manifest is intact; `MISSING` is reported by the legacy classifier and fails through manifest
  integrity. Extra Markdown agent definitions outside the package are reported as `EXTRA`, are not
  made canonical, and are neither failed nor deleted.
- Standalone deployment validation:
  `python3 check_wids.py --scope deployment --manifest ROOT/delegation-triage-package-manifest.json ROOT`.
  Intentionally absent repository-only edges are printed exactly as declared `SOURCE_ONLY` edges;
  undeclared, stale, escaping, or unmanifested targets fail closed.
- The spawn-triage guard (`~/.claude/hooks/spawn-triage-guard.py`) reads the bold
  `**Active: <profile>**` line in deployed `STATE.md`; exactly one such line may exist across the
  skill home.
- **Restart**: restart after a roster change. A deploy is not live in the turn it lands, but it is
  a delayed op rather than a no-op — on this build the harness announces added types with an
  `agent_listing_delta` at the next user-turn boundary and they spawn from there
  (P-20260807-pin-registration-turn-boundary). Whether an *edited* definition re-registers the
  same way is untested, which is why the install contract still asks for the restart.

Rollback is a separately authorized deployment from the previous clean source commit followed by
an external manifest-stamp update and restart. The installer never removes extra agents or stale
excluded content; any cleanup needs an exact baseline, explicit authority, and its own rollback.
