# Changelog

All notable governance changes to the Software Factory Governance Repository are documented here.

This file follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) conventions.
Governance versions follow semantic versioning: MAJOR.MINOR.PATCH.

- **MAJOR** — breaking changes to governance standards that require project-level action
- **MINOR** — new standards, templates, or significant additions
- **PATCH** — corrections, clarifications, or minor additions

---

## [1.4.0] — 2026-05-29

### Added
- `governance/GITHUB_RULESET_BASELINE.md` — live audit of `software-factory-governance`
  GitHub settings + recommended baseline for all governed repositories. Covers: branch
  protection, merge strategy (squash-only recommended), repository features, security
  analysis, PR template, configuration instructions (UI + CLI), conditions for change,
  and a compliance checklist for new repository setup
- `IMPLEMENTATION_HISTORY.md` — IMP-006: GitHub ruleset baseline audit and documentation

### Governance Impact
- Every new Software Factory repository now has a defined setup checklist (Section 7)
- Two critical gaps identified on the governance repo itself: `main` is unprotected
  and all merge strategies are enabled — both must be fixed before FamOil setup begins
- Secret scanning and push protection confirmed active on governance repo

---

## [1.3.0] — 2026-05-29

### Added
- `DECISION_LOG.md` — DEC-009: FamOil selected as Phase 2 governance adoption pilot
  (rationale: highest commercial urgency, most complex migration case, no git repo for full
  Wave 1 exercise, WamaCare isolation rules)
- `DECISION_LOG.md` — DEC-010: FamOil git repository boundary defined (root at
  `/Users/mac/odoo17`; `custom_addons/`, `docs/`, `scripts/` committed; Odoo core source,
  venv, filestore, and `odoo.conf` excluded)
- `IMPLEMENTATION_HISTORY.md` — IMP-005: FamOil pre-adoption readiness assessment
  (complete gap analysis: 10 governance file gaps, 6 custom artefacts inventoried, backup
  confirmed untrusted, governance maturity established at Level 0 sub-standard)

### Updated
- `roadmaps/SOFTWARE_FACTORY_ROADMAP.md` — Phase 1 current section restructured: all
  completed items explicitly checked, remaining items broken into FamOil Wave 1–4 + WamaCare
  Wave 1 + phase close criteria; next action identified
- `ROADMAP.md` — root summary updated to match

### Governance Impact
- Two decisions logged that were previously implicit in the adoption strategy document
- FamOil adoption can begin Wave 1 immediately — all planning is now recorded
- Next action is clearly identified in both ROADMAP.md and SOFTWARE_FACTORY_ROADMAP.md

---

## [1.2.0] — 2026-05-29

### Added

- `docs/ADOPTION_STRATEGY.md` — Software Factory adoption strategy: artifact classification
  (Categories A–D), four-wave FamOil adoption plan, 14-step artifact introduction sequence,
  effort estimates (13–20 h for FamOil), risk matrix (8 risks), generalised playbook for
  all future project onboardings, and Phase 2 success criteria

### Updated

- `ROADMAP.md` — Phase 1 remaining items replaced with adoption wave checkboxes; adoption
  strategy item marked complete
- `IMPLEMENTATION_HISTORY.md` — IMP-004 added recording adoption strategy delivery

### Governance Impact
- Phase 2 adoption is now formally planned with a documented, sequenced approach
- FamOil adoption can begin immediately with Wave 1 (git init + CLAUDE.md + PR template)
- No project files were modified

---

## [1.1.0] — 2026-05-29

### Added

**Self-compliance fixes — mandatory root files**
- `DECISION_LOG.md` — 8 bootstrap decision entries (DEC-001 to DEC-008) covering governance repository structure, four-layer model, 10-dimension GIA, repository memory hierarchy, backup trust principle, governance/operations separation, bootstrapping exception, and ROADMAP.md placement decision
- `IMPLEMENTATION_HISTORY.md` — 3 entries: Phase 1 bootstrap (IMP-001), governance maturity review (IMP-002), self-compliance fixes (IMP-003)
- `ROADMAP.md` — root-level summary and phase status table; delegates full detail to `roadmaps/SOFTWARE_FACTORY_ROADMAP.md`
- `.gitignore` — standard exclusions for secrets, OS files, editor files, and temporary artefacts
- `.github/PULL_REQUEST_TEMPLATE.md` — deployed from `templates/pull_request_template.md`; GitHub now auto-loads the PR template on every new pull request

### Fixed

**Conflict C-01 — `governance` commit type missing from canonical list**
- `governance/GOVERNANCE_STANDARD.md` §4.3: added `governance` to the commit types list; added a fourth example commit using `governance` type

**Conflict C-02 — Emergency hotfix GIA resolution was ambiguous**
- `governance/PR_GOVERNANCE_STANDARD.md` §7: replaced "commitment to complete the full GIA within 24 hours, documented in `IMPLEMENTATION_HISTORY.md`" with "Full GIA completed within 24 hours via a follow-up PR. The hotfix deployment and GIA commitment recorded in `IMPLEMENTATION_HISTORY.md` within 24 hours." Now aligned with `operations/CHANGE_MANAGEMENT_STANDARD.md` §2 Type 4.

### Clarified

**Root ROADMAP.md compliance for governance-layer repositories**
- `governance/GOVERNANCE_STANDARD.md` §3.1: added note clarifying that governance-layer repositories may satisfy the root `ROADMAP.md` requirement via a summary-and-delegate file; all project repositories must keep a single `ROADMAP.md` at root. See DEC-008.

### Governance Impact
- Repository now self-compliant with its own mandatory file requirements
- Governance Maturity Level: **Level 0 → Level 1 (Foundation)**
- All 7 mandatory root files now present: `README.md`, `CLAUDE.md`, `CHANGELOG.md`, `DECISION_LOG.md`, `IMPLEMENTATION_HISTORY.md`, `ROADMAP.md`, `.gitignore`
- `.github/PULL_REQUEST_TEMPLATE.md` active on GitHub

---

## [1.0.0] — 2026-05-29

### Added

**Repository Structure**
- `README.md` — governance repository overview, layering model, and usage guide
- `CLAUDE.md` — AI agent operational cockpit and instruction set
- `CHANGELOG.md` — this file

**Governance Standards (`governance/`)**
- `GOVERNANCE_STANDARD.md` — master governance standard for all Software Factory projects
- `PR_GOVERNANCE_STANDARD.md` — PR governance rules and enforcement
- `DECISION_LOG_STANDARD.md` — when and how decisions must be logged
- `IMPLEMENTATION_HISTORY_STANDARD.md` — how milestones and operational changes are recorded
- `REGISTRY_STANDARD.md` — when and how modules/components/services must be registered
- `ROADMAP_STANDARD.md` — separation between factory, platform, template, and client roadmaps
- `DOCUMENTATION_STANDARD.md` — documentation requirements and maintenance standards
- `SECURITY_STANDARD.md` — security governance and access control standards
- `BACKUP_RECOVERY_STANDARD.md` — backup governance and recovery trust standards

**Templates (`templates/`)**
- `pull_request_template.md` — reusable PR checklist with governance impact analysis
- `decision_log_template.md` — decision log entry template
- `implementation_history_template.md` — implementation history entry template
- `module_registry_template.md` — module/component registry entry template
- `roadmap_template.md` — roadmap template for all project layers
- `onboarding_template.md` — project onboarding checklist template
- `project_readme_template.md` — project README template

**Onboarding Standards (`onboarding/`)**
- `AI_ONBOARDING_STANDARD.md` — standard for onboarding AI agents to a project
- `DEVELOPER_ONBOARDING_STANDARD.md` — standard for onboarding developers to a project
- `PROJECT_CONTINUITY_BRIEFING_TEMPLATE.md` — continuity briefing template for project handover

**Operations Standards (`operations/`)**
- `BACKUP_AND_RECOVERY_STANDARD.md` — backup operations and recovery procedures
- `RESTORE_DRILL_STANDARD.md` — restore drill requirements and procedures
- `RELEASE_TAGGING_STANDARD.md` — release tagging conventions and procedures
- `CHANGE_MANAGEMENT_STANDARD.md` — change management procedures and approval gates

**Roadmaps (`roadmaps/`)**
- `SOFTWARE_FACTORY_ROADMAP.md` — initial Software Factory roadmap with 6 phases

**Principles (`principles/`)**
- `ARCHITECTURAL_PRINCIPLES.md` — binding architectural principles for all projects
- `REPOSITORY_MEMORY_PRINCIPLES.md` — principles governing repository memory priority
- `OVERENGINEERING_GUARDRAILS.md` — rules preventing unnecessary abstraction and custom code

**Documentation (`docs/`)**
- `SOFTWARE_FACTORY_STRUCTURE.md` — Software Factory structure and organization
- `PROJECT_LAYERING_MODEL.md` — four-layer model definition and boundary rules
- `GOVERNANCE_IMPACT_ANALYSIS.md` — mandatory pre-PR governance impact analysis definition

### Scope

Governance covers the following projects at initialization:
- FamOil ERP (Odoo 17, soybean oil production)
- WamaCare (Odoo 17, NGO/CBO management)
- NADF ERP (Odoo 17, agricultural development)
- Hospitality ERP (Odoo 17, hotel and hospitality)
- Office ERP (Odoo 17, office administration)
- Power Sector ERP (Odoo 17, power utility)
- Future SaaS, AI, web, mobile, infrastructure, and automation projects

---

*Unreleased changes appear above the most recent version entry.*
