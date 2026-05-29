# Implementation History — Software Factory Governance

This file records every significant delivery, operational event, and milestone for the
Software Factory governance repository. It follows the standard defined in
`governance/IMPLEMENTATION_HISTORY_STANDARD.md`.

Entries are listed in reverse chronological order (newest first).

---

## IMP-006

**Date:** 2026-05-29
**Type:** `GOVERNANCE_UPDATE`
**Status:** COMPLETE
**Delivered By:** Software Factory lead / Claude Sonnet 4.6
**PR Reference:** This commit

### Title
GitHub Ruleset Baseline documented — live audit of `software-factory-governance` captured; recommended baseline defined for all governed repositories.

### Description
A live GitHub API audit of `aliyuumaru-beep/software-factory-governance` was performed
to capture the exact repository protection settings currently in place. The findings were
used to produce `governance/GITHUB_RULESET_BASELINE.md`, which documents both the current
state and the recommended baseline configuration for all Software Factory repositories.

### Scope
- `governance/GITHUB_RULESET_BASELINE.md` — new document; audited current state, gap analysis,
  recommended baseline, configuration instructions, conditions for change, compliance checklist

### Key Audit Findings (Current State)
The governance repository is NOT compliant with the recommended baseline it defines:

| Gap | Severity |
|-----|----------|
| `main` branch is unprotected — direct push permitted | Critical |
| No PR required before merging to `main` | Critical |
| Force push to `main` is unrestricted | High |
| All three merge strategies enabled (merge commit, squash, rebase) | High |
| Delete branch on merge is disabled | Medium |
| Wiki is enabled (docs live in repo; wiki is redundant) | Low |
| Dependabot security updates disabled | Medium |

Security controls that are correctly in place:
- Secret scanning: **Enabled** ✓
- Secret scanning push protection: **Enabled** ✓
- PR template: **Active** ✓

### Configuration Notes
The recommended baseline is documented but NOT yet applied. Applying it requires
deliberate action by the repository owner via GitHub UI or CLI (commands provided in
Section 5 of the baseline document). Each change should be recorded as an
`INFRASTRUCTURE_CHANGE` entry in this file.

### Outstanding Issues
The governance repo non-compliance with its own GitHub ruleset baseline is explicitly
documented in Section 8 of `GITHUB_RULESET_BASELINE.md`. These settings should be
applied before FamOil and WamaCare are set up, so that those repositories inherit
the correct configuration from inception.

### Post-Delivery Verification
- Live API audit confirmed via `gh api` commands
- All settings captured with exact values from the GitHub API response
- Gap analysis completed — 5 significant gaps identified
- Recommended baseline complete with rationale, CLI commands, and conditions for change

### References
DEC-009 (FamOil pilot), IMP-005 (FamOil readiness assessment)

---

## IMP-005

**Date:** 2026-05-29
**Type:** `GOVERNANCE_UPDATE`
**Status:** COMPLETE
**Delivered By:** Software Factory lead / Claude Sonnet 4.6
**PR Reference:** This commit

### Title
FamOil ERP pre-adoption readiness assessment completed — governance maturity gap fully characterised.

### Description
A structured readiness assessment of FamOil ERP was performed as the prerequisite step
before executing the four-wave governance adoption plan. The assessment used the project
memory records and filesystem state to establish a complete before-picture, identifying
every governance gap and every pre-existing artefact that requires migration rather than
creation from scratch.

### Scope — FamOil Governance Gap Analysis

**Project identity:**
- Platform: Odoo 17.0.1.3 Community Edition
- Database: `Famoil` (PostgreSQL 16.11)
- Local path: `/Users/mac/odoo17`
- Filestore: `/Users/mac/Library/Application Support/Odoo/filestore/Famoil/`
- Commercialisation readiness: 8.5/10 (Phase 3 complete as of 2026-05-24)

**Mandatory governance file status at assessment:**

| File | Status | Action Required |
|------|--------|----------------|
| `README.md` | Absent at root | Create from `templates/project_readme_template.md` |
| `CLAUDE.md` | Absent | Create, inheriting from governance `CLAUDE.md` |
| `CHANGELOG.md` | Exists — non-standard format (`FamOil-Template-v1.0.0`) | Migrate to governance semantic versioning |
| `DECISION_LOG.md` | Exists in `docs/famoil_erp_template/` — 10 entries, non-standard format | Migrate DEC-001→DEC-010 to governance format at project root |
| `MODULE_REGISTRY.md` | Absent | Create; register 2 modules + 4 scripts |
| `IMPLEMENTATION_HISTORY.md` | Absent (partial coverage in `IMPLEMENTATION_PLAYBOOK.md`) | Create; back-log Phases 1–3 |
| `ROADMAP.md` | Absent | Create; mark Phases 1–3 complete, define Phase 4 scope |
| `.gitignore` | Absent | Create with Odoo-specific exclusions before `git init` |
| `.github/PULL_REQUEST_TEMPLATE.md` | Absent | Deploy after git repo established |
| Git repository | **None** — Known Issue #7 open | Initialize at `/Users/mac/odoo17` |

**Custom code inventory (from project memory):**

| ID | Artifact | Type | Status |
|----|----------|------|--------|
| MOD-001 | `stock_crude_oil_tank_restriction` v17.0.1.1.0 | Custom module | Active |
| MOD-002 | `mrp_component_availability_check` | Custom module | Active |
| SCR-001 | `backup_famoil.sh` | Script | Active |
| SCR-002 | `inspect_famoil_config.sh` | Script | Active |
| SCR-003 | `process_refined_oil_mo.py` | Script (automation) | Active |
| SCR-004 | `fix_locations_and_routing.py` | Script (one-off, run 2026-05-24) | Complete / historical |

**Existing documentation to migrate (not discard):**

| Document | Location | Disposition |
|----------|----------|-------------|
| `DECISION_LOG.md` | `docs/famoil_erp_template/DECISION_LOG.md` | Migrate 10 entries to governance format at root |
| `KNOWN_ISSUES.md` | `docs/famoil_erp_template/KNOWN_ISSUES.md` | Absorb open issues into ROADMAP.md backlog and IMPLEMENTATION_HISTORY.md |
| `IMPLEMENTATION_PLAYBOOK.md` | `docs/famoil_erp_template/` | Preserve; summarise Phase 1–3 completions in IMPLEMENTATION_HISTORY.md |
| `COSTING_VALIDATION.md` | `docs/famoil_erp_template/` | Retain as supporting documentation |
| `CHANGELOG.md` | Project root | Migrate to governance semver format |
| `BACKUP_AND_RESTORE.md` | `docs/famoil_erp_template/Phase 1/` | Reference in IMPLEMENTATION_HISTORY.md; retain |

**Backup state:**
- Last backup: `/Users/mac/odoo_backups/famoil_20260522_1133/` (47 MB, taken 2026-05-22)
- Restore drill: **None on record** — backup is currently **UNTRUSTED** per governance standard
- Age at assessment: 7 days — a fresh backup should be taken before the restore drill

**Open known issues at assessment date:**

| Issue | Severity | Notes |
|-------|----------|-------|
| #1 SoyaBean miscategorised under "All" | Low | Configuration fix; Phase 4 scope |
| #2 Raw Materials category no cost method | Medium | Affects costing accuracy; Phase 4 scope |
| #5 Demo data not cleaned (CHIC1, WH, demo BOMs) | Medium | Must be resolved before first client deployment |
| #8 Spare parts/consumables list_price = ₦1 | Low | Data quality; Phase 4 scope |

**Governance maturity at assessment: Level 0 (sub-standard)**
Pre-existing documentation exists but is located outside the governance-required structure
and uses non-standard formats. This is better than Level 0 with no docs at all, but it
does not satisfy any governance compliance checks.

### Configuration Notes
No FamOil files were created or modified during this assessment. All findings are based
on project memory records and filesystem inspection.

### Outstanding Issues
FamOil Wave 1 adoption is now unblocked. The critical path is:
1. Design and verify the Odoo-specific `.gitignore`
2. `git init` at `/Users/mac/odoo17`
3. Create `CLAUDE.md`
4. Deploy `.github/PULL_REQUEST_TEMPLATE.md`

DEC-009 and DEC-010 log the pilot selection and git boundary decisions made during this assessment.

### Post-Delivery Verification
- Assessment findings cross-checked against project memory (`project_famoil.md`)
- All 6 custom artefacts identified and inventoried
- All 10 existing decision log entries confirmed present in `docs/famoil_erp_template/DECISION_LOG.md`
- Governance maturity level confirmed as Level 0 (sub-standard)

### References
DEC-009 (FamOil as pilot), DEC-010 (git boundary), IMP-004 (adoption strategy)

---

## IMP-004

**Date:** 2026-05-29
**Type:** `GOVERNANCE_UPDATE`
**Status:** COMPLETE
**Delivered By:** Software Factory lead / Claude Sonnet 4.6
**PR Reference:** Adoption strategy commit

### Title
Phase 2 Adoption Strategy created — FamOil as pilot, generalised playbook established.

### Description
A comprehensive Software Factory Adoption Strategy was produced defining artifact
classification (Categories A–D), a four-wave adoption plan for FamOil, effort estimates,
risk assessment, and the generalised adoption playbook for all future projects.

### Scope
- `docs/ADOPTION_STRATEGY.md` — new document, 34 KB, covers all governed projects
- `ROADMAP.md` — Phase 1 remaining item updated
- `CHANGELOG.md` — v1.2.0 entry added

### Configuration Notes
The adoption strategy is the gate document for Phase 2. No FamOil files were modified.
Implementation of Wave 1 (FamOil) is the immediate next action.

### Outstanding Issues
None for this delivery. FamOil adoption has the following prerequisite risks logged in the strategy:
- R-01: .gitignore scope (Critical — must verify before first commit)
- R-04: Backup restore failure risk (High — drill before claiming backup is trusted)
- R-08: Compliance fatigue (High — first PR quality sets the standard)

### Post-Delivery Verification
- `docs/ADOPTION_STRATEGY.md` created and reviewed
- Strategy covers all 4 artifact categories, 4 adoption waves, 14-step artifact sequence, 8 risks
- No FamOil or WamaCare files modified

### References
IMP-003 (self-compliance fixes), DEC-001 (governance as standalone repo)

---

## IMP-003

**Date:** 2026-05-29
**Type:** `GOVERNANCE_UPDATE`
**Status:** COMPLETE
**Delivered By:** Software Factory lead / Claude Sonnet 4.6
**PR Reference:** Self-compliance fix commit (follows 58ceb8a)

### Title
Seven self-compliance fixes applied following the Governance Maturity Review.

### Description
A governance maturity review of all 33 files identified that the governance repository
did not comply with several of its own mandatory requirements. Seven critical fixes were
applied to bring the repository to self-compliance before Phase 2 adoption.

### Scope

| Fix | Action |
|-----|--------|
| M-01: Missing DECISION_LOG.md | Created with 8 bootstrap decision entries (DEC-001 to DEC-008) |
| M-02: Missing IMPLEMENTATION_HISTORY.md | Created with this entry and IMP-001, IMP-002 |
| M-03: Missing .github/PULL_REQUEST_TEMPLATE.md | Deployed from `templates/pull_request_template.md` |
| M-04: Missing .gitignore | Created with standard exclusions |
| M-05: Missing root ROADMAP.md | Created summary-and-delegate ROADMAP.md; DEC-008 logged |
| C-01: `governance` commit type absent | Added to GOVERNANCE_STANDARD.md §4.3 |
| C-02: Hotfix GIA resolution conflict | PR_GOVERNANCE_STANDARD.md §7 aligned with CHANGE_MANAGEMENT_STANDARD.md |

### Configuration Notes
The `.github/PULL_REQUEST_TEMPLATE.md` is now in place and will be auto-loaded by GitHub
when any PR is opened against this repository.

### Outstanding Issues
The following medium and low-priority review findings are deferred to Phase 2:
- D-01: Backup domain content overlap between governance and operations files
- D-02: Layering model described in two docs (SOFTWARE_FACTORY_STRUCTURE.md + PROJECT_LAYERING_MODEL.md)
- M-06: No Testing Standard
- M-07: No Security Audit Standard
- O-01: No lightweight GIA fast-path for trivial `docs` PRs
- O-02: Backup operations procedures are Odoo-specific

### Post-Delivery Verification
- All 7 mandatory root files now present: README.md, CLAUDE.md, CHANGELOG.md,
  DECISION_LOG.md, IMPLEMENTATION_HISTORY.md, ROADMAP.md, .gitignore
- .github/PULL_REQUEST_TEMPLATE.md deployed
- git status clean after commit
- Pushed to GitHub remote (origin/main)

### References
IMP-002 (governance maturity review), DEC-001 through DEC-008

---

## IMP-002

**Date:** 2026-05-29
**Type:** `GOVERNANCE_UPDATE`
**Status:** COMPLETE
**Delivered By:** Software Factory lead / Claude Sonnet 4.6
**PR Reference:** N/A (review session, no code change)

### Title
Governance Maturity Review of all 33 bootstrap files completed.

### Description
A full governance maturity review was performed across all 33 files created during
the Phase 1 bootstrap. The review identified duplications, conflicting standards,
overengineering risks, missing standards, merge candidates, and items to keep separate.

### Scope
All 33 files reviewed. Findings categorized by severity.

### Configuration Notes
N/A — review only, no files modified.

### Outstanding Issues
See IMP-003 for the resolution of critical findings.

Key findings from the review:
- 7 duplication patterns identified (D-01 to D-07)
- 3 conflicts identified (C-01 to C-03) — 2 critical, 1 low
- 5 overengineering risks identified (O-01 to O-05)
- 9 missing standards identified (M-01 to M-09) — 2 critical, 2 high, 4 medium, 1 low
- 3 merge candidates identified
- 7 "keep separate" confirmations

### Post-Delivery Verification
Review report produced and reviewed. Critical findings escalated to IMP-003.

### References
IMP-001 (Phase 1 bootstrap), IMP-003 (self-compliance fixes)

---

## IMP-001

**Date:** 2026-05-29
**Type:** `PHASE_COMPLETE`
**Status:** COMPLETE
**Delivered By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Commit 58ceb8a (root commit — governance exception DEC-007 applies)

### Title
Phase 1 — Governance Foundation: Software Factory governance scaffold created and pushed to GitHub.

### Description
The `software-factory-governance` repository was created from scratch and populated with
the full governance scaffold. This is the authoritative governance, standards, continuity,
onboarding, and implementation methodology repository for all current and future Software
Factory projects.

The repository was cloned from the empty GitHub repository `aliyuumaru-beep/software-factory-governance`
and initialized with 33 files across 7 directories in a single bootstrap commit.

### Scope

**Root files (3):**
- `README.md` — governance overview, layering model, usage guide
- `CLAUDE.md` — AI agent operational cockpit
- `CHANGELOG.md` — governance version history (v1.0.0)

**Governance standards — `governance/` (9 files):**
- `GOVERNANCE_STANDARD.md` — master standard with maturity levels
- `PR_GOVERNANCE_STANDARD.md` — PR rules and enforcement
- `DECISION_LOG_STANDARD.md` — decision logging requirements
- `IMPLEMENTATION_HISTORY_STANDARD.md` — milestone and event recording
- `REGISTRY_STANDARD.md` — module and component registration
- `ROADMAP_STANDARD.md` — four-layer roadmap separation
- `DOCUMENTATION_STANDARD.md` — documentation requirements
- `SECURITY_STANDARD.md` — security and access control requirements
- `BACKUP_RECOVERY_STANDARD.md` — backup governance and restore trust principle

**Templates — `templates/` (7 files):**
- `pull_request_template.md` — full PR checklist with GIA
- `decision_log_template.md` — decision log entry form
- `implementation_history_template.md` — implementation history entry form
- `module_registry_template.md` — module registry entry form
- `roadmap_template.md` — roadmap form for all layers
- `onboarding_template.md` — project onboarding checklist
- `project_readme_template.md` — project README template

**Onboarding — `onboarding/` (3 files):**
- `AI_ONBOARDING_STANDARD.md` — mandatory 7-step AI session onboarding
- `DEVELOPER_ONBOARDING_STANDARD.md` — developer onboarding requirements
- `PROJECT_CONTINUITY_BRIEFING_TEMPLATE.md` — handover briefing template

**Operations — `operations/` (4 files):**
- `BACKUP_AND_RECOVERY_STANDARD.md` — pg_dump procedures and recovery steps
- `RESTORE_DRILL_STANDARD.md` — restore drill procedure and checklists
- `RELEASE_TAGGING_STANDARD.md` — tag naming and annotation requirements
- `CHANGE_MANAGEMENT_STANDARD.md` — Type 1–4 change classification and approval gates

**Roadmaps — `roadmaps/` (1 file):**
- `SOFTWARE_FACTORY_ROADMAP.md` — 6-phase factory roadmap

**Principles — `principles/` (3 files):**
- `ARCHITECTURAL_PRINCIPLES.md` — 10 binding architectural principles
- `REPOSITORY_MEMORY_PRINCIPLES.md` — authority hierarchy for information sources
- `OVERENGINEERING_GUARDRAILS.md` — 8 rules against premature abstraction

**Documentation — `docs/` (3 files):**
- `GOVERNANCE_IMPACT_ANALYSIS.md` — 10-dimension GIA with pass/fail criteria
- `PROJECT_LAYERING_MODEL.md` — four-layer model with boundary rules
- `SOFTWARE_FACTORY_STRUCTURE.md` — repository inventory and naming conventions

### Configuration Notes
- Repository: `https://github.com/aliyuumaru-beep/software-factory-governance`
- Default branch: `main`
- Local path: `/Users/mac/software-factory-governance`
- Bootstrap commit: `58ceb8a`
- Note: Bootstrap commit was a direct commit to main (governance exception DEC-007)

### Outstanding Issues
Self-compliance gaps identified in IMP-002 and resolved in IMP-003.

### Post-Delivery Verification
- `git status` confirmed clean after push
- Repository confirmed accessible on GitHub
- All 33 files verified present via `find` command
- Commit `58ceb8a` pushed to `origin/main` successfully

### References
DEC-001 (standalone governance repo decision), DEC-002 (four-layer model),
DEC-003 (10-dimension GIA), DEC-004 (repository memory hierarchy),
DEC-005 (backup trust principle), DEC-006 (governance/operations split)
