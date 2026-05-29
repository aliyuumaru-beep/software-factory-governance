# Software Factory Adoption Strategy

**Version:** 1.0.0  
**Date:** 2026-05-29  
**Status:** APPROVED — Phase 2 Planning  
**Pilot Project:** FamOil ERP  
**Applies to:** All Software Factory project onboardings

---

## 1. Purpose

This document defines the strategy for adopting the Software Factory governance scaffold
into an existing project. It covers which governance artifacts go where, how to sequence
adoption to minimise disruption, and how to estimate effort and risk.

The FamOil ERP project is used throughout as the concrete pilot. The methodology is
generalizable to WamaCare, NADF ERP, and all future project onboardings.

---

## 2. Artifact Classification

Every file in `software-factory-governance` falls into one of four categories relative
to a governed project.

---

### Category A — Must Exist in Every Project Repository

These are project-specific living documents. They cannot live in the governance repo because
they record state that is unique to the project. They are created from templates and then
maintained continuously in the project repository.

| Artifact | Created From | Notes |
|----------|-------------|-------|
| `README.md` | `templates/project_readme_template.md` | Replace or upgrade existing README |
| `CLAUDE.md` | Governance `CLAUDE.md` + project context | Inherits then extends governance cockpit |
| `CHANGELOG.md` | Adapted to governance semantic versioning | Migrate existing if present |
| `DECISION_LOG.md` | `templates/decision_log_template.md` | Migrate prior decisions if project has history |
| `IMPLEMENTATION_HISTORY.md` | `templates/implementation_history_template.md` | Back-log completed phases at project start |
| `MODULE_REGISTRY.md` | `templates/module_registry_template.md` | Must capture ALL existing custom code |
| `ROADMAP.md` | `templates/roadmap_template.md` | Reflects client deployment layer scope only |
| `.gitignore` | Governance `.gitignore` adapted | Critical if project has no git repo yet |
| `.github/PULL_REQUEST_TEMPLATE.md` | `templates/pull_request_template.md` (verbatim) | Enables GitHub auto-load |

**Rule:** If any of these files exist in the project in a non-standard format, they must
be migrated to the governance format — not deleted and restarted. Existing decisions,
modules, and history are valuable; their format is what changes.

---

### Category B — Remain Only in the Governance Repository

These are normative standards. Copying them into project repositories would create
divergent versions that drift over time. Projects reference these — they do not own them.

**governance/ (all 9 files):**
All binding standards (GOVERNANCE_STANDARD, PR_GOVERNANCE_STANDARD, DECISION_LOG_STANDARD,
IMPLEMENTATION_HISTORY_STANDARD, REGISTRY_STANDARD, ROADMAP_STANDARD, DOCUMENTATION_STANDARD,
SECURITY_STANDARD, BACKUP_RECOVERY_STANDARD) remain authoritative in the governance repo.

**principles/ (all 3 files):**
ARCHITECTURAL_PRINCIPLES, REPOSITORY_MEMORY_PRINCIPLES, OVERENGINEERING_GUARDRAILS are
binding for all projects but are not copied. The project `CLAUDE.md` links to them.

**docs/ (all 3 files):**
GOVERNANCE_IMPACT_ANALYSIS, PROJECT_LAYERING_MODEL, SOFTWARE_FACTORY_STRUCTURE remain
in the governance repo. The project `CLAUDE.md` references `docs/GOVERNANCE_IMPACT_ANALYSIS.md`.

**onboarding/ standards (2 of 3 files):**
AI_ONBOARDING_STANDARD and DEVELOPER_ONBOARDING_STANDARD stay in the governance repo.
The third file (`PROJECT_CONTINUITY_BRIEFING_TEMPLATE.md`) is a template — see Category C.

**operations/ (all 4 files):**
BACKUP_AND_RECOVERY_STANDARD, RESTORE_DRILL_STANDARD, RELEASE_TAGGING_STANDARD,
CHANGE_MANAGEMENT_STANDARD remain in the governance repo. Projects follow these
procedures but do not copy them. Project-specific backup runbooks (if needed) are
created as `docs/BACKUP_RUNBOOK.md` in the project and reference the governance standard.

**roadmaps/SOFTWARE_FACTORY_ROADMAP.md:**
This is the factory-level roadmap. Never copied to projects.

---

### Category C — Generated from Templates into the Project

These templates in `templates/` are used exactly once per project to create project
documents. After creation, the project document is maintained independently of the template.

| Template (governance repo) | Generated Artifact (project repo) |
|---------------------------|----------------------------------|
| `templates/project_readme_template.md` | `README.md` |
| `templates/decision_log_template.md` | `DECISION_LOG.md` |
| `templates/implementation_history_template.md` | `IMPLEMENTATION_HISTORY.md` |
| `templates/module_registry_template.md` | `MODULE_REGISTRY.md` |
| `templates/roadmap_template.md` | `ROADMAP.md` |
| `templates/onboarding_template.md` | `ONBOARDING_CHECKLIST.md` (one per onboarding event) |
| `templates/pull_request_template.md` | `.github/PULL_REQUEST_TEMPLATE.md` |
| `onboarding/PROJECT_CONTINUITY_BRIEFING_TEMPLATE.md` | `PROJECT_CONTINUITY_BRIEFING.md` (one per handover) |

**Rule:** Templates are never edited in the project. If a template needs improving, update
it in the governance repo and manually propagate to affected projects via a governed PR.

---

### Category D — Referenced Only (Hyperlinks, Not Copies)

The project `CLAUDE.md` and `README.md` link to these by URL or relative path convention.
No file is created or copied in the project repository.

- All governance standards (`governance/` files)
- All principles files
- All docs files
- `onboarding/AI_ONBOARDING_STANDARD.md`
- `onboarding/DEVELOPER_ONBOARDING_STANDARD.md`
- All operations standards
- `roadmaps/SOFTWARE_FACTORY_ROADMAP.md`

**Reference convention in project documents:**
```
Governed by: Software Factory Governance Standard
Standards: https://github.com/aliyuumaru-beep/software-factory-governance
```

---

## 3. Artifact Map Summary

```
software-factory-governance/
│
├── README.md                          ← Category B (governance-only)
├── CLAUDE.md                          ← Category B (source); project extends it → Category A
├── CHANGELOG.md                       ← Category B (governance-only)
├── DECISION_LOG.md                    ← Category B (governance-only)
├── IMPLEMENTATION_HISTORY.md          ← Category B (governance-only)
├── ROADMAP.md                         ← Category B (governance-only)
├── .gitignore                         ← Category C (adapt into each project)
│
├── governance/          ← Category B (all — reference only, never copy)
├── principles/          ← Category B (all — reference only, never copy)
├── docs/                ← Category B (all — reference only, never copy)
├── roadmaps/            ← Category B (factory roadmap — never copy)
├── onboarding/
│   ├── AI_ONBOARDING_STANDARD.md           ← Category B
│   ├── DEVELOPER_ONBOARDING_STANDARD.md    ← Category B
│   └── PROJECT_CONTINUITY_BRIEFING_TEMPLATE.md ← Category C (generate per project)
│
└── templates/           ← Category C (all — generate per project, then maintain in project)
    ├── pull_request_template.md        → .github/PULL_REQUEST_TEMPLATE.md
    ├── decision_log_template.md        → DECISION_LOG.md
    ├── implementation_history_template.md → IMPLEMENTATION_HISTORY.md
    ├── module_registry_template.md     → MODULE_REGISTRY.md
    ├── roadmap_template.md             → ROADMAP.md
    ├── onboarding_template.md          → ONBOARDING_CHECKLIST.md
    └── project_readme_template.md      → README.md
```

---

## 4. Phase 2 Adoption Plan — FamOil as Pilot

### 4.1 FamOil Pre-Adoption State Assessment

FamOil enters Phase 2 adoption with the following profile:

| Dimension | Current State | Governance Gap |
|-----------|--------------|----------------|
| Git repository | **None** — no git repo at `/Users/mac/odoo17` | Critical. Git is prerequisite for all PR governance |
| README | None at project root | Must be created |
| CLAUDE.md | None | Must be created |
| DECISION_LOG.md | Exists in `docs/famoil_erp_template/` — 10 entries, non-standard format | Must be migrated to governance format |
| MODULE_REGISTRY.md | None | 2 custom modules + 4 scripts must be registered |
| IMPLEMENTATION_HISTORY.md | Partial — `IMPLEMENTATION_PLAYBOOK.md` and `CHANGELOG.md` exist | Must be created in governance format; prior milestones back-logged |
| ROADMAP.md | None | Must be created; Phases 1–3 already complete |
| CHANGELOG.md | Exists — `FamOil-Template-v1.0.0` format | Must be reconciled with governance semantic versioning |
| .gitignore | None | Must be created before first commit |
| .github/PULL_REQUEST_TEMPLATE.md | None | Must be created after git repo established |
| Backup | Exists at `/Users/mac/odoo_backups/famoil_20260522_1133/` | No restore drill on record; backup is **untrusted** |
| Known issues | 4 open issues tracked in `KNOWN_ISSUES.md` | Must be referenced from IMPLEMENTATION_HISTORY.md |

**Governance Maturity Level at adoption entry: Level 0 (sub-standard — existing docs outside governance structure)**

---

### 4.2 Adoption Waves

Adoption is structured into four waves of increasing governance depth. Each wave is a
self-contained delivery unit that leaves the project in a better state than it entered.
Waves are not time-boxed to sprints — they are completed before moving on.

---

#### Wave 1 — Git Foundation and AI Cockpit

**Objective:** Establish the minimum infrastructure required for governance to function.
Nothing else can proceed without this wave.

**Prerequisite:** None.

**Deliverables:**

1. **Initialize git repository** at `/Users/mac/odoo17`
   - A carefully crafted `.gitignore` that excludes: venv (`odoo/venv/`), compiled Python
     (`__pycache__/`, `*.pyc`), database config with passwords (`odoo.conf`), filestore
     (not version-controlled — backed up separately), OS files, and secrets.
   - Only `custom_addons/`, `docs/`, `scripts/`, `CHANGELOG.md`, and governance root files
     are committed. The Odoo core source (`odoo/odoo/`) should NOT be in the project git
     repo — it is installed infrastructure, not project code.
   - First commit: governance files only, clearly labelled as "governance bootstrap."

2. **Create `CLAUDE.md`**
   - Declares inheritance from governance `CLAUDE.md`.
   - States the project (FamOil ERP), platform (Odoo 17), current phase (Phase 4 — post-commercialisation prep).
   - Lists the 4 open known issues as areas requiring caution.
   - Names the 2 custom modules and 4 scripts as existing custom code.
   - Notes that demo data (`CHIC1`, `YourCompany` warehouse) has not yet been cleaned.
   - Notes that the soybean product categorisation and raw materials cost method are open issues.

3. **Deploy `.github/PULL_REQUEST_TEMPLATE.md`**
   - Verbatim copy from governance template.

4. **Create `.gitignore`**
   - Governance `.gitignore` extended with Odoo-specific exclusions.

**Exit criteria:** `git status` is clean. `CLAUDE.md` accurately describes the project state. An AI agent reading only the project repo can orient itself correctly.

**Governance maturity gained:** Sub-Level 0 → Level 0 (Bootstrap)

---

#### Wave 2 — Repository Memory Documents

**Objective:** Create the four core memory documents that make the project legible to
future AI agents and developers. This is the highest-value wave.

**Prerequisite:** Wave 1 complete.

**Deliverables:**

1. **`MODULE_REGISTRY.md`**
   Register all known custom artifacts. For FamOil this is:
   - `MOD-001`: `stock_crude_oil_tank_restriction` v17.0.1.1.0 — blocks non-Crude-Soya-Oil into Crude Oil Tanks
   - `MOD-002`: `mrp_component_availability_check` — blocks MO completion if components not fully reserved
   - `SCR-001`: `backup_famoil.sh` — database backup script
   - `SCR-002`: `inspect_famoil_config.sh` — configuration inspection script
   - `SCR-003`: `process_refined_oil_mo.py` — creates and completes Refined Soya Oil MOs via shell
   - `SCR-004`: `fix_locations_and_routing.py` — stock corrections and putaway rules (run 2026-05-24; one-off)
   
   Also identify and note: the 4 scripts in `scripts/` directory.

2. **`DECISION_LOG.md`**
   Migrate the 10 existing decisions from `docs/famoil_erp_template/DECISION_LOG.md`
   (DEC-001 to DEC-010) into the governance format. This is not deletion — it is
   migration. Existing decisions are preserved verbatim in content; only format changes.
   
   Key known decisions to ensure are captured:
   - Per-component source location limitation in Odoo 17 (parent location + `child_of` workaround)
   - SoapStock removal from BOM 10 (2026-05-23)
   - Tank restriction module (no hardcoded IDs)
   - 3-stage manufacturing pipeline design
   - Byproduct cost allocation percentages
   - Any security/access decisions from the original deployment

3. **`IMPLEMENTATION_HISTORY.md`**
   Back-log the project's completed phases:
   - `IMP-001`: Phase 1 — Inspection and Backup (complete; backup at `odoo_backups/famoil_20260522_1133/`)
   - `IMP-002`: Phase 2 — Configuration Validation (complete; 3-stage pipeline validated)
   - `IMP-003`: Phase 3 — Commercialisation Framework (complete; readiness 8.5/10)
   - `IMP-004`: Governance adoption — Wave 1 complete
   Record each with known issues at phase close and current status.

4. **`ROADMAP.md`**
   Create FamOil's roadmap at the Client Deployment layer (Layer 4):
   - Phases 1–3 marked `[COMPLETE]` with dates.
   - Phase 4 (current): Demo data cleanup, spare parts pricing, Nigeria compliance (VAT, WHT).
   - Phase 5 (next): First paying client deployment — groundnut oil mill pilot.
   - Backlog: FIRS TaxPro Max VAT report mapping, per-component source location module.

**Exit criteria:** An AI agent starting a new session can read these four documents and
know: what custom code exists, what decisions have been made and why, what has been built
and what is still open, what the current phase scope is.

**Governance maturity gained:** Level 0 → Level 1 (Foundation)

---

#### Wave 3 — Operational Alignment

**Objective:** Align FamOil's operational practices with the governance operations standards.

**Prerequisite:** Wave 2 complete.

**Deliverables:**

1. **Backup verification and restore drill**
   - The backup at `odoo_backups/famoil_20260522_1133/` (47 MB) has never had a documented restore drill.
   - Per `governance/BACKUP_RECOVERY_STANDARD.md`: it is currently **untrusted**.
   - Perform a restore drill to a staging database (e.g., `Famoil_drill`).
   - Run data verification checklist from `operations/RESTORE_DRILL_STANDARD.md`.
   - Record result in `IMPLEMENTATION_HISTORY.md` as `IMP-005` (type: `RESTORE_EVENT`).
   - Log RPO and RTO in `DECISION_LOG.md` (type: `OPERATIONAL`).

2. **Release tag for current state**
   - Apply `v1.0.0` annotated tag to the first stable commit following Wave 1.
   - Tag message: "FamOil ERP v1.0.0 — Phase 3 complete, commercialisation framework ready."

3. **`README.md`**
   - Create from `templates/project_readme_template.md`.
   - Technology stack: Odoo 17.0.1.3 Community, PostgreSQL 16.11, macOS (dev).
   - Architecture summary: 3-stage manufacturing pipeline (Extraction → Refining → Packaging).
   - Backup section: location, last backup, last verified restore (post-drill).
   - Known issues section: 4 open issues with severity.

**Exit criteria:** Backup is trusted (restore drill recorded). Project has a release tag.
README provides accurate project orientation to a new reader.

**Governance maturity gained:** Level 1 maintained and strengthened.

---

#### Wave 4 — Active PR Governance

**Objective:** Activate the PR process. Every subsequent change to FamOil goes through
a PR with a completed GIA.

**Prerequisite:** Wave 3 complete.

**Deliverables:**

1. **First governed PR**
   - Choose a bounded, low-risk change as the first PR: e.g., fixing Known Issue #1
     (SoyaBean miscategorised under "All") or Known Issue #5 (demo data cleanup).
   - Complete the full `.github/PULL_REQUEST_TEMPLATE.md` checklist.
   - Complete all 10 GIA dimensions.
   - This PR proves the process works end-to-end.

2. **`CHANGELOG.md` reconciliation**
   - Reconcile the existing `FamOil-Template-v1.0.0` CHANGELOG with the governance
     semantic versioning format.
   - v1.0.0 = Phase 3 complete (2026-05-24); v1.1.0 = governance adoption (Wave 1-4).

3. **`PROJECT_CONTINUITY_BRIEFING.md`**
   - Complete the briefing template.
   - This document is the single-source handover brief for any future AI agent, developer,
     or team member coming onto the project.

**Exit criteria:** One complete governed PR merged. CHANGELOG current. Continuity briefing complete.

**Governance maturity gained:** Level 1 → Level 2 (Active Governance)

---

### 4.3 Adoption Sequence: Recommended Artifact Introduction Order

The order within each wave matters. This is the optimal sequence:

```
Wave 1 (Prerequisites)
  1.  .gitignore               — security baseline; must exist before first commit
  2.  git init + first commit  — prerequisite for everything
  3.  CLAUDE.md                — every subsequent AI session is governance-aware from this point
  4.  .github/PULL_REQUEST_TEMPLATE.md

Wave 2 (Memory Documents — value order)
  5.  MODULE_REGISTRY.md       — establishes what custom code exists (fastest to verify)
  6.  DECISION_LOG.md          — migrates existing decisions; most effort, highest value
  7.  IMPLEMENTATION_HISTORY.md — back-logs completed phases
  8.  ROADMAP.md               — aligns current scope

Wave 3 (Operations)
  9.  Restore drill            — unblocks "trusted backup" claim
  10. Release tag v1.0.0       — anchors the current state
  11. README.md                — orients new readers; depends on registry + history being complete

Wave 4 (Active governance)
  12. First governed PR        — proves the loop end-to-end
  13. CHANGELOG.md reconciled  — version history coherent
  14. PROJECT_CONTINUITY_BRIEFING.md — handover document complete
```

**Why this order?**

- `.gitignore` before `git init` to prevent accidental commit of secrets or venv.
- `CLAUDE.md` immediately after git init so AI sessions are governed from the first moment.
- `MODULE_REGISTRY.md` before `DECISION_LOG.md` because registering modules reveals decisions
  (e.g., "why was `mrp_component_availability_check` built instead of using a native Odoo feature?")
  that need to be logged.
- `IMPLEMENTATION_HISTORY.md` after `DECISION_LOG.md` because history entries reference decision IDs.
- `ROADMAP.md` last in Wave 2 because it needs history to know what is complete.
- `README.md` late because it synthesises information from registry, history, and roadmap.
- First governed PR last because it validates the entire structure built in Waves 1–3.

---

## 5. Effort Estimate

### 5.1 Per-Wave Effort — FamOil

| Wave | Activities | Estimated Hours | Complexity Driver |
|------|-----------|-----------------|-------------------|
| **Wave 1** | Git init, .gitignore (Odoo-specific), CLAUDE.md, PR template | 2–3 h | .gitignore scope for Odoo project; CLAUDE.md project context |
| **Wave 2** | Registry (6 artifacts), Decision Log migration (10 → governance format), Implementation History (3 phases), Roadmap | 6–9 h | Decision log migration is the bottleneck; requires judgment on existing entries |
| **Wave 3** | Restore drill + recording, release tag, README | 3–5 h | Restore drill requires a clean staging environment |
| **Wave 4** | First governed PR, CHANGELOG reconciliation, continuity briefing | 2–3 h | PR governance has a learning curve on first use |
| **Total** | | **13–20 h** | |

### 5.2 Ongoing Governance Overhead (Post-Adoption)

Once governance is established, the recurring overhead per PR is:

| PR Type | GIA Effort | Notes |
|---------|-----------|-------|
| `feat` — new module/integration | 45–60 min | Registry entry + decision log + full GIA |
| `fix` — bug fix | 15–20 min | Most dimensions N/A; rollback and testing evidence required |
| `docs` — documentation only | 10–15 min | Lightweight; most dimensions not impacted |
| `governance` — standard update | 20–30 min | Decision log entry typically required |
| `ops` — backup/deployment | 30–45 min | Backup/recovery dimension requires care |

For FamOil in active development (~2–4 PRs per month), governance overhead is estimated
at 2–4 hours per month after the first month of adoption.

---

## 6. Risk Assessment

### Risk Matrix

| Risk | Likelihood | Impact | Severity | Mitigation |
|------|-----------|--------|----------|-----------|
| **R-01: .gitignore scope error** — accidental commit of venv, secrets, or database | HIGH | HIGH | **Critical** | Verify `git status` output before first commit; review every file in staging area |
| **R-02: Decision log migration loss** — existing DEC-001 to DEC-010 nuance lost in format migration | MEDIUM | HIGH | **High** | Read every existing entry before migrating; flag ambiguous entries for human review |
| **R-03: Undiscovered custom code** — modules or scripts not in memory that need registration | MEDIUM | MEDIUM | **Medium** | Run `find /Users/mac/odoo17/custom_addons -name "*.py"` audit before creating registry |
| **R-04: Backup restore failure** — drill fails because backup is 7 days old or corrupted | MEDIUM | HIGH | **High** | Perform drill early; if backup is invalid, take a fresh backup and drill immediately |
| **R-05: Scope creep during adoption** — team wants to fix open issues #1, 2, 5, 8 during governance work | HIGH | MEDIUM | **Medium** | Governance adoption PRs do not fix functional issues; log them in roadmap backlog only |
| **R-06: CHANGELOG format conflict** — existing `FamOil-Template-v1.0.0` scheme incompatible with governance semver | LOW | LOW | **Low** | Treat existing version as governance v1.0.0; continue from there |
| **R-07: Git repo boundary confusion** — should `/Users/mac/odoo17` or only `custom_addons/` be the git root | HIGH | MEDIUM | **Medium** | Decision: git root = `/Users/mac/odoo17`; .gitignore excludes Odoo core, venv, and filestore |
| **R-08: Compliance fatigue** — team rubber-stamps GIA rather than genuinely completing it | MEDIUM | HIGH | **High** | First PR is reviewed by Software Factory lead; set quality standard early |

### Highest-Risk Activity: Wave 1 — Git Initialization

Git initialization of `/Users/mac/odoo17` is the single highest-risk activity because:

1. The Odoo venv (`odoo/venv/`) is ~500 MB. A missed `.gitignore` entry would stage it.
2. `odoo.conf` may contain database passwords. Must be excluded from commits.
3. The filestore (`~/Library/Application Support/Odoo/filestore/Famoil/`) must never be
   committed — it is binary data backed up separately.
4. The Odoo core source (`odoo/odoo/`) should not be under project git — it is a dependency,
   not project code. Use a clear boundary.

**Recommended repository boundary:**
```
/Users/mac/odoo17/         ← git root
├── .gitignore             ← must exclude everything below except custom_addons, docs, scripts
├── CLAUDE.md              ← committed
├── README.md              ← committed
├── [other governance files] ← committed
├── custom_addons/         ← committed (project code)
│   ├── stock_crude_oil_tank_restriction/
│   └── mrp_component_availability_check/
├── docs/                  ← committed (project documentation)
│   └── famoil_erp_template/
├── scripts/               ← committed (operational scripts)
│   ├── backup_famoil.sh
│   ├── inspect_famoil_config.sh
│   └── [others]
├── odoo/                  ← EXCLUDED by .gitignore (Odoo core + venv)
└── odoo.conf              ← EXCLUDED by .gitignore (contains passwords)
```

---

## 7. Generalisation: Adoption Playbook for All Future Projects

The FamOil adoption defines the repeatable playbook for all subsequent projects.

### New Project (No Prior History)

Effort: 6–10 hours. Waves 1–4 simplified because there is no migration work.

Sequence: git init → .gitignore → CLAUDE.md → PR template → empty governance files →
first PR that populates them in a single governed PR → release tag → first feature PR.

### Existing Project with Documentation (like FamOil)

Effort: 13–20 hours. Waves 1–4 as documented above. Migration is the bottleneck.

Key difference: existing decisions and history must be migrated, not lost.

### Existing Project with No Documentation

Effort: 8–14 hours. No migration work, but the MODULE_REGISTRY requires code archaeology —
reading the codebase to discover what custom modules and integrations exist.

This is the highest governance risk scenario: unknown custom code means unknown technical debt.

### Target Governance Maturity Per Project by End of Phase 2

| Project | Entry Level | Target by Phase 2 End |
|---------|------------|----------------------|
| FamOil ERP | Level 0 (sub-standard) | **Level 2 (Active Governance)** |
| WamaCare | Level 0 (assumed) | **Level 1 (Foundation)** |
| NADF ERP | Not started | Level 0 (Bootstrap) |
| Hospitality ERP | Not started | N/A (Phase 2 scope is FamOil + WamaCare) |

---

## 8. Phase 2 Success Criteria

Phase 2 is complete when:

- [ ] FamOil: All 4 adoption waves complete. Governance maturity Level 2 verified.
- [ ] FamOil: At least 3 PRs merged using the full governance PR template.
- [ ] FamOil: Restore drill completed and recorded.
- [ ] FamOil: `MODULE_REGISTRY.md` matches the actual codebase (verified by code audit).
- [ ] FamOil: `DECISION_LOG.md` contains the migrated decisions from prior docs.
- [ ] WamaCare: Wave 1 complete. `CLAUDE.md` and `.github/PULL_REQUEST_TEMPLATE.md` in place.
- [ ] Governance repo: Phase 2 roadmap items marked `[COMPLETE]` in `ROADMAP.md`.
- [ ] Governance repo: `IMPLEMENTATION_HISTORY.md` updated with Phase 2 delivery entry.
- [ ] No FamOil or WamaCare PR merged without a PR template after the adoption date.

---

## 9. What Not to Do During Adoption

These anti-patterns are common during governance adoption and must be avoided:

| Anti-pattern | Why it fails |
|-------------|--------------|
| Fix functional bugs during governance waves | Scope creep; governance adoption becomes a feature sprint and never finishes |
| Create perfect documents on first pass | The registry, decision log, and history will be imperfect at first; get them to 80% and iterate |
| Migrate decisions verbatim without understanding them | Format migration is not the same as understanding; read each decision before migrating |
| Skip the restore drill because "there's already a backup" | This is precisely the situation the restore drill standard exists to prevent |
| Require full GIA on the first PR | The first PR is a learning exercise; coach quality, do not block on perfection |
| Commit the Odoo venv or core source | Will bloat the repository to gigabytes; irreversible without `git filter-branch` |

---

*This strategy is owned by the Software Factory. Changes require a governed PR.*  
*Implementation of Wave 1 begins after this document is reviewed and approved.*
