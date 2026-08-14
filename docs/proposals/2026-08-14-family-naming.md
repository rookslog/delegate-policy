# Family naming — one brand, role-named members, a named spine

**Status: DRAFT — awaiting operator ratification of decisions N-1..N-4. Nothing renames until
then.** Filed 2026-08-14 on operator instruction ("lets do the family renaming first, draft the
naming proposal"), following the packaging deliberation (this session; alternatives + steelmen
delivered in-chat, summarized in §5). This proposal is deliberately the **cheap, reversible
first move** from that deliberation: renaming forecloses no structural option (monorepo,
standard-first federation, micro-kernel, product/practice split all remain open) and dissolves
the identity incoherence the operator named: five artifacts, five unrelated names, no noun for
the whole, overlapping observability layers whose relationships the names actively hide.

## 1. The problem being fixed

Measured state: the family is `delegation-triage` (public repo + skill), `delegate-ops/delegateops`
(product repo, local), `delegation-runtime` (split-off implementation repo, local),
`orchestration-learning` (Codex skill + live telemetry), plus `signal-layer` (sovereign
observability neighbor). Three different stems (`delegation-`, `delegate-`, `orchestration-`)
for four artifacts that are one system's roles; the whole has no name; the record spine — the
one artifact the integration deliberation concluded is THE durable asset — has no name at all
(it is currently "the intent/outcome record crosswalk").

## 2. Decisions

### N-1 — Family brand and scheme

| option | scheme | buys | costs |
|---|---|---|---|
| **A (recommended)** | stem **`delegate-`**, umbrella brand **DelegateOps**, npm scope `@delegateops` unchanged | Minimal delta: the product dir is ALREADY `delegate-ops`; OI-1 already measured `delegateops`/`@delegateops`/`delegateops.dev` free; constitution's namespace constant untouched; renames are one-word edits (`delegation-triage`→`delegate-triage`, `delegation-runtime`→`delegate-runtime`, `orchestration-learning`→`delegate-learning`) | "Ops" flavor reads product-ish for the practice/lab member; umbrella = product name, which soft-commits toward the monorepo/umbrella structural option rhetorically (not technically) |
| B | fresh coined brand (strongest candidates surfaced: **remit** — "the scope of delegated authority", near-perfect semantic fit; **legate/legation** — delegated authority + its house) | A real identity, chosen not inherited; works equally as a future standard's name | Availability **Unchecked** for every candidate (npm `remit` believed taken — Conjecture); re-stamps npm scope, namespace constant (one-line by design, constitution §OI-1), and every doc; taste iteration delays the win |
| C | two brands now: product keeps `delegateops`, practice family gets its own name | Honestly encodes the product-vs-practice boundary (packaging option 4) before structure | Decides the structural question by naming — the operator explicitly deferred structure; two identity decisions instead of one |
| D | defer | zero cost | the mess persists; every week adds references that the eventual rename must sweep |
| **E (recommended, rev.2)** | **brand the invariant: family = Capsule** (the spine); members role-named against the spine; **`DelegateOps` persists as the MEMBER name for the v0 supervisor-runtime**, where delegation is literally true | Paradigm-neutral at the family level — the name that survives is the asset that survives (records outlive paradigms, the architecture's own thesis); a future peer/market runtime arrives as a sibling member, no rename, no lie; merges naturally with the standard-first structural option | bare `capsule` is a common word — collisions likely, availability **Unchecked** (P1 decides; qualified or coined variant is the fallback); family brand and the measured-free `@delegateops` npm scope diverge until the structural decision |

**Recommendation: E (rev.2, 2026-08-14 same day).** Rev.1 recommended A on the load-bearing
assumption that the operator's objection was incoherence, not the word "delegate" — the
operator's follow-up ("should we be using delegate if we are potentially opening up to other
paradigms?") falsified that assumption, firing rev.1's own flip condition. "Delegate" names one
coordination paradigm (principal→agent); the family-level invariant across paradigms is the
*recorded commitment of work* — the capsule — so the family brands the invariant and
paradigm-committed names live at the member level where they are true. Rev.2's load-bearing
assumption: a workable Capsule-family name clears the P1 availability measurement (bare,
qualified, or coined variant). Flip: if no variant clears, fall back to A with the paradigm
caveat recorded, or a coined neutral (B) chosen on the same brand-the-invariant criterion.

### N-2 — The spine's name

The record standard (intent/outcome records, crosswalk §§1–3, v0.2.4 reserved fields) becomes
**Capsule** — "a delegate capsule" is one decision-episode record; "the Capsule standard" is the
schema. Provenance: in-house vocabulary, not coined — the v0 plan already names Task 15 Step 2
"versioned **Run Capsule** export" (plan line 1787). Alternatives: stay descriptive ("the
record standard") — free but nameless, which is the §1 disease; coin fresh — no candidate beats
the incumbent's continuity. The crosswalk doc retitles at its next amendment ("Capsule
crosswalk (v0.2.x)"); field names, `v` values, and schema content DO NOT change.

### N-3 — signal-layer

**Stays sovereign and unrenamed.** It is general observability, wider than delegation; its
Proposal H registry is the designed seam a `delegate-*` instrument plugs into. Affiliation is
recorded by cross-reference, not by name. (Renaming it into the family would decide the
micro-kernel structural question by naming — same error as N-1 option C.)

### N-4 — Peripheral directories

`~/Projects/routing-evidence`, `~/Projects/agent-provenance`, `~/Projects/AgenticOpsResearch`
and similar are **out of scope** — each gets an absorb-or-archive disposition when next
touched, recorded in its own one-line note. Listed here so the sweep is bounded, not implied.

## 3. The rename map (under N-1 option A)

| today | becomes | mechanics |
|---|---|---|
| `delegation-triage` (GitHub `loganrooks/delegation-triage`, public) | **`delegate-triage`** | GitHub rename (automatic redirects); local dir; skill + pin + plugin names get transition aliases (§4 P3) |
| `delegateops` repo at `Development/delegate-ops` | unchanged | already conformant; umbrella brand holder |
| `delegation-runtime` | **`delegate-runtime`** | local-only, no remote — one `mv` + reference sweep |
| `orchestration-learning` (Codex skill + telemetry dir) | **`delegate-learning`** | skill dir rename + alias; **telemetry data dir does NOT move** (the store outlives the code plane; a pointer file marks the new name) — schema stays frozen at v1 per the integration deliberation |
| the record standard (unnamed) | **Capsule** | doc retitle at next amendment; no schema change |
| `signal-layer` | unchanged | sovereign (N-3) |

## 4. Migration phases (each ≤1 session; reversible through P2)

- **P1 — ratify.** Operator decides N-1..N-4. Precondition before P2, OI-1-style: measure
  availability of the chosen names where they are public-facing (GitHub `delegate-triage`
  collision check; npm only matters at first publish). All availability claims in this doc are
  **Unchecked** until this measurement runs.
- **P2 — canonical renames.** GitHub + local dirs + in-repo self-references (README, LINEAGE,
  PROGRAMME). LINEAGE.md records the rename with date and reason — identity changes are
  provenance events here, not cosmetics.
- **P3 — deployed surfaces.** Skills, pins, the delegation-roster plugin, `~/.claude` CLAUDE.md
  triggers, hooks (`spawn-triage-guard` parses surface names — check its regexes), Codex skill
  dir. Every rename ships a **transition alias** for one review cycle so running sessions and
  muscle memory don't break; MANIFEST stamps each deploy as usual.
- **P4 — reference sweep.** Grep-driven, fail-loud: memory files, crosswalk/OI-2 cross-repo
  paths, KNOWN-REPOS in WARRANTS, probe records (historical records are NOT rewritten — a
  top-of-file note maps old names, append-only culture holds). A checker script asserting zero
  stale references is the exit criterion.

**Freeze trigger:** at first npm publish the brand is FROZEN (OI-1: post-publish renames are
cheap for 72 hours, then constrained). Any N-1 revisit must happen before v0 ships.

## 5. What this does NOT decide

Monorepo vs polyrepo vs federation vs micro-kernel (the structural question — discriminating
evidence named in the packaging deliberation: external adoption, cadence friction inside one
repo, the Proposal H pilot); product-vs-practice split; whether Capsule is later published as a
standalone standard. Renaming is upstream of all of these and forecloses none.
