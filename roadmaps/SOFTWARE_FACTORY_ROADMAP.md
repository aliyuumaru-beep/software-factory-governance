# Software Factory Roadmap

**Layer:** Software Factory  
**Last Updated:** 2026-05-29  
**Current Phase:** Phase 1 — Governance Foundation  

---

## Summary

This roadmap tracks the evolution of the Software Factory itself — not any individual
project. Its scope is the governance standards, methodology, templates, tooling, and
processes that make the factory capable of delivering high-quality, governed software
projects reliably.

Projects governed by this factory: FamOil ERP, WamaCare, NADF ERP, Hospitality ERP,
Office ERP, Power Sector ERP, and all future SaaS, AI, web, mobile, infrastructure,
and automation projects.

---

## Current Phase

### Phase 1 — Governance Foundation
**Status:** IN PROGRESS  
**Target Completion:** 2026-Q2  

**Objective:** Establish the governance scaffold that all current and future projects
will inherit. Define standards, templates, and operational procedures.

**Deliverables:**
- [x] Repository initialized and cloned — 2026-05-29
- [x] README.md — governance overview and layering model
- [x] CLAUDE.md — AI agent operational cockpit
- [x] CHANGELOG.md — governance version history
- [x] `governance/` — all 9 governance standards
- [x] `templates/` — all 7 reusable templates
- [x] `onboarding/` — AI and developer onboarding standards and continuity briefing
- [x] `operations/` — backup, restore drill, release tagging, change management
- [x] `roadmaps/` — this roadmap
- [x] `principles/` — architectural, repository memory, and overengineering guardrails
- [x] `docs/` — structure, layering model, and governance impact analysis
- [ ] Apply governance scaffold to FamOil ERP repository
- [ ] Apply governance scaffold to WamaCare repository
- [ ] Initial PR process adoption confirmed on at least one project

---

## Phase History

*No completed phases yet — Phase 1 is in progress.*

---

## Upcoming Phases

### Phase 2 — PR and Repository Memory Enforcement
**Status:** PLANNED  
**Target Start:** 2026-Q3  

**Objective:** Ensure all governed projects are actively using the PR governance
standard and maintaining repository memory documents (decision log, registry,
implementation history).

**Planned Deliverables:**
- Governance compliance audit for FamOil, WamaCare, and any other active projects.
- Pull request templates deployed to each project's `.github/` directory.
- Decision log, module registry, and implementation history initialized in each project.
- CLAUDE.md deployed to each project repository.
- PR governance training for all active team members.

---

### Phase 3 — Project Onboarding Standards Adoption
**Status:** PLANNED  
**Target Start:** 2026-Q3 / Q4  

**Objective:** Formalize and verify the onboarding process for all project types —
AI agent sessions, new developers, and new project intake.

**Planned Deliverables:**
- AI onboarding sequence verified on FamOil and WamaCare.
- Developer onboarding standard applied to at least two active projects.
- Project continuity briefing template completed for each active project.
- Onboarding audit confirms no project has a governance maturity below Level 2.

---

### Phase 4 — CI Enforcement and Automated Governance Checks
**Status:** PLANNED  
**Target Start:** 2026-Q4  

**Objective:** Reduce reliance on manual governance compliance by introducing
automated checks in the CI pipeline.

**Planned Deliverables:**
- CI pipeline defined for at least one project (GitHub Actions or equivalent).
- Automated checks for: commit message format, PR template completeness, presence
  of mandatory files (DECISION_LOG.md, MODULE_REGISTRY.md, etc.).
- Linting and test runner integration.
- Branch protection rules enforced on main branches.

---

### Phase 5 — Multi-Project Adoption
**Status:** PLANNED  
**Target Start:** 2027-Q1  

**Objective:** Confirm that all active Software Factory projects are governed,
at minimum at Level 2 maturity, and that the governance system is actively used.

**Planned Deliverables:**
- FamOil ERP — governance maturity Level 2 confirmed.
- WamaCare — governance maturity Level 2 confirmed.
- NADF ERP — governance maturity Level 1 confirmed (or higher if project is active).
- Hospitality ERP — governance scaffold ready (template level, not necessarily deployed).
- Office ERP — governance scaffold ready.
- Power Sector ERP — governance scaffold ready.
- Cross-project governance report produced.

---

### Phase 6 — Software Factory Maturity
**Status:** PLANNED  
**Target Start:** 2027-Q2  

**Objective:** Achieve full Software Factory governance maturity across all active projects.
Introduce continuous improvement cycles and governance audits.

**Planned Deliverables:**
- All active projects at governance maturity Level 3 or above.
- Restore drill cadence established and verified for all production systems.
- Governance audit cycle established (quarterly review).
- Template library versioned and tagged.
- Software Factory governance v2.0 incorporating lessons learned.
- Evaluation of platform-layer shared module library.

---

## Backlog

Items identified but not yet assigned to a phase:

| Item | Priority | Notes |
|------|----------|-------|
| Governance dashboard (visual project health) | Medium | Could be a simple markdown report |
| Automated registry cross-reference checks | Low | Detect unregistered modules via static analysis |
| Multi-language governance template variants | Low | For future international deployments |
| Security audit standard | High | Periodic security review process |
| Performance benchmark standard | Low | Define acceptable Odoo response time baselines |

---

## Cross-Layer Dependencies

| This Roadmap Needs | From | Notes |
|--------------------|------|-------|
| Project repo access | All governed projects | To deploy governance scaffold |
| GitHub Actions support | GitHub | For Phase 4 CI enforcement |

---

*This roadmap is updated at each Software Factory governance milestone.*
