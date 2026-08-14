I have initiated the search for all `.claude/skill-overlays` directories under `~/Projects` and `~/Development` and will inspect the results once complete.
Checking for any other `skill-overlays` directories across `~/Projects` and `~/Development`.
### Reference Sweep Results

#### 1. `~/.codex/config.toml`, `~/.codex/AGENTS.md`, and `~/.codex/*.md`

- `/Users/rookslog/.codex/config.toml : 818 : [projects."/Users/rookslog/Projects/delegation-triage"]` — **live-config**
- `/Users/rookslog/.codex/config.toml : 866 : [projects."/Users/rookslog/Projects/delegation-runtime"]` — **live-config**
- `/Users/rookslog/.codex/AGENTS.md` — *0 hits*
- `/Users/rookslog/.codex/MIGRATION-GUIDE.md` — *0 hits*

---

#### 2. `~/.claude/settings.json` and top-level `~/.claude/*.md`
*(Skipping `CLAUDE.md` and `delegation.md` per already-covered list)*

- `/Users/rookslog/.claude/settings.json` — *0 hits*
- `/Users/rookslog/.claude/vendor-facts.md : 10 : sit in the text (e.g. a `valid_until` date the delegation-triage guard parses).` — **live-config**
- `/Users/rookslog/.claude/vendor-facts.md : 32 : treats a cell with no `YYYY-MM-DD` as exempt (same rule as delegation-triage `check_state.py`).` — **live-config**
- `/Users/rookslog/.claude/vendor-facts.md : 47 : | `~/.claude/skills/delegation-triage/STATE.md` | fable-window | sentinel |` — **live-config**
- `/Users/rookslog/.claude/vendor-facts.md : 48 : | `~/Projects/delegation-triage/STATE.md` | fable-window | sentinel |` — **live-config**
- `/Users/rookslog/.claude/vendor-facts.md : 49 : | `~/Projects/delegation-triage/ROADMAP.md` | fable-window | sentinel |` — **live-config**
- `/Users/rookslog/.claude/vendor-facts.md : 50 : | `~/Projects/delegation-triage/agents/MANIFEST.md` | fable-window | sentinel |` — **live-config**
- `/Users/rookslog/.claude/cite-your-warrant.md` — *0 hits*
- `/Users/rookslog/.claude/claims-discipline.md` — *0 hits*
- `/Users/rookslog/.claude/decision-presentation.md` — *0 hits*
- `/Users/rookslog/.claude/link-what-you-cite.md` — *0 hits*
- `/Users/rookslog/.claude/MIGRATION-GUIDE.md` — *0 hits*
- `/Users/rookslog/.claude/propagation.md` — *0 hits*
- `/Users/rookslog/.claude/RTK.md` — *0 hits*

---

#### 3. `~/.zshrc` and `~/.zprofile`

- `/Users/rookslog/.zshrc` — *0 hits*
- `/Users/rookslog/.zprofile` — *0 hits*

---

#### 4. `~/Development/delegate-ops` (all text files)
*(Skipping `delegateops/docs` per already-covered list)*

- `/Users/rookslog/Development/delegate-ops/REVIEW_delegateops_v0_handoff_2026-08-07.md : 326 : Your question was opus-medium / opus-high / Gemini Flash 3.6. [per: delegation-triage]` — **historical**

---

#### 5. `<repo>/.claude/skill-overlays/` under `~/Projects` or `~/Development`

*Discovered overlay directory:* `/Users/rookslog/Development/bridgewright/.claude/skill-overlays/`
*(Note: file itself is named `delegation-triage.md`)*

- `/Users/rookslog/Development/bridgewright/.claude/skill-overlays/delegation-triage.md : 1 : # delegation-triage — bridgewright overlay` — **live-config**
- `/Users/rookslog/Development/bridgewright/.claude/skill-overlays/delegation-triage.md : 4 : **Status:** active project pins (consumed by `~/.claude/skills/delegation-triage` step 2; overlay > profile > table)` — **live-config**

---

### (1) Count Summary per Classification

- **live-config**: 10
- **historical**: 1
- **data-plane**: 0
- **Total Hits**: 11

---

### (2) Explicit Blind-Spots Declaration

1. **Deterministic Checker Roots (Explicitly Excluded per Instructions):**
   - `~/Projects/delegate-policy`
   - `~/Projects/delegate-runtime`
   - `~/.claude/skills`
   - `~/.claude/agents`
   - `~/.claude/hooks`
   - `~/.claude/CLAUDE.md`
   - `~/.claude/delegation.md`
   - `~/.claude/projects/-Users-rookslog-Development-delegate-ops/memory`
   - `~/Development/delegate-ops/delegateops/docs`
   - `~/.codex/skills`

2. **Data Plane Exception (Intentionally Unchanged):**
   - `~/.codex/telemetry/orchestration-learning/` and telemetry log references.

3. **Out-of-Scope Repositories and Directories (Not Swept per Bounded Scope):**
   - General codebase files across all other repositories in `~/Projects/*` and `~/Development/*` (sweep bounded specifically to `<repo>/.claude/skill-overlays/` and `~/Development/delegate-ops`).
   - Deep subdirectories of `~/.codex/` and `~/.claude/` not specified in target scope (e.g. SQLite databases `state_5.sqlite`, `logs_2.sqlite`, `memories_1.sqlite`, `history.jsonl`, `~/.claude/sessions/`, `~/.claude/backups/`, `~/.claude/tasks/`).
   - Ephemeral worktrees (`.claude/worktrees/*`), build artifacts, and package stores (`node_modules`, `.pnpm-store`) within `delegate-ops`.
   - Alternative shell initialization files outside `~/.zshrc` and `~/.zprofile` (e.g. `~/.zshenv`, `~/.bashrc`, `~/.bash_profile`, `~/.profile`).
