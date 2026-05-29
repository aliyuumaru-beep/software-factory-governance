# Changelog

All notable governance changes to the Software Factory Governance Repository are documented here.

This file follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) conventions.
Governance versions follow semantic versioning: MAJOR.MINOR.PATCH.

- **MAJOR** — breaking changes to governance standards that require project-level action
- **MINOR** — new standards, templates, or significant additions
- **PATCH** — corrections, clarifications, or minor additions

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
