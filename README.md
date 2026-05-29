# Software Factory Governance Repository

## Purpose

This repository is the **authoritative governance source of truth** for all software projects
designed, built, deployed, or maintained under the Software Factory.

It is **not** a client project. It is **not** an ERP template. It is the shared governance
infrastructure that every project inherits from — whether that project is an Odoo ERP deployment,
a SaaS product, a mobile application, an AI system, or an infrastructure automation.

---

## What This Repository Contains

| Directory | Contents |
|-----------|----------|
| `governance/` | Binding standards for PRs, decisions, registries, roadmaps, documentation, security, and backup |
| `templates/` | Reusable templates for PRs, decision logs, registries, roadmaps, and onboarding |
| `onboarding/` | Standards and briefings for onboarding AI agents, developers, and project teams |
| `operations/` | Standards for backup/recovery, restore drills, release tagging, and change management |
| `roadmaps/` | The Software Factory-level roadmap |
| `principles/` | Architectural principles, repository memory principles, and overengineering guardrails |
| `docs/` | Structure documentation, layering model, and governance impact analysis definition |

---

## Who This Governs

All current and future Software Factory projects are governed by these standards:

- **FamOil ERP** — Soybean oil production and distribution (Odoo 17)
- **WamaCare** — NGO/CBO management platform (Odoo 17)
- **NADF ERP** — Agricultural development ERP (Odoo 17)
- **Hospitality ERP** — Hotel and hospitality management (Odoo 17)
- **Office ERP** — Office administration and operations (Odoo 17)
- **Power Sector ERP** — Power utility and infrastructure ERP (Odoo 17)
- Future SaaS, AI, web, mobile, infrastructure, and automation projects

---

## The Software Factory Layering Model

```
┌─────────────────────────────────────────┐
│          Software Factory Layer          │  ← This repository governs this layer
│  Governance · Standards · Methodology    │
├─────────────────────────────────────────┤
│            Platform Layer                │  ← Shared platform modules, base configs
│     Odoo 17 · Shared Infrastructure      │
├─────────────────────────────────────────┤
│        Industry Template Layer           │  ← Vertical-specific templates
│  Oil & Gas · NGO · Hospitality · Power   │
├─────────────────────────────────────────┤
│        Client Deployment Layer           │  ← Per-client customization and data
│   FamOil · WamaCare · NADF · Others      │
└─────────────────────────────────────────┘
```

See `docs/PROJECT_LAYERING_MODEL.md` for the full model definition.

---

## How to Use This Repository

### For AI Agents
Read `CLAUDE.md` first. It is your operational cockpit. Do not proceed without it.

### For Developers
Read `onboarding/DEVELOPER_ONBOARDING_STANDARD.md` before touching any project.

### For New Projects
1. Copy applicable templates from `templates/` into the new project repository.
2. Adapt `templates/project_readme_template.md` as the project `README.md`.
3. Complete `onboarding/PROJECT_CONTINUITY_BRIEFING_TEMPLATE.md` at project start.
4. Register all modules/components using `templates/module_registry_template.md`.
5. Initialize the project `DECISION_LOG.md` using `templates/decision_log_template.md`.

### For PRs
All PRs across all projects must use the checklist in `templates/pull_request_template.md`
and pass the Governance Impact Analysis defined in `docs/GOVERNANCE_IMPACT_ANALYSIS.md`.

---

## Governance Principles (Summary)

1. **Repository memory outranks AI memory.** What is written in a repository supersedes anything an AI agent recalls from prior context.
2. **No undocumented decisions.** Every architectural, security, data model, or custom-code decision must be logged.
3. **No unregistered components.** Every module, service, integration, script, or automation must appear in the registry.
4. **A backup is only trusted after a successful restore.** See `operations/RESTORE_DRILL_STANDARD.md`.
5. **Governance before completion.** No PR is complete until the Governance Impact Analysis is satisfied.
6. **Avoid overengineering.** See `principles/OVERENGINEERING_GUARDRAILS.md`.

---

## Versioning

This repository follows semantic versioning for governance releases.
See `CHANGELOG.md` for the version history.

---

## Maintained By

Software Factory — Internal Governance  
Repository initialized: 2026-05-29  
Governed projects: FamOil, WamaCare, NADF ERP, Hospitality ERP, Office ERP, Power Sector ERP, and future projects
