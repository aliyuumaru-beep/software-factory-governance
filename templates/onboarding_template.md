# Project Onboarding Checklist

**Project:** _______________
**Onboarding Date:** YYYY-MM-DD
**Onboarding Type:** <!-- AI Agent | Developer | Project Team -->
**Completed By:** _______________

---

## Part 1 — Governance Orientation

- [ ] Read `software-factory-governance/CLAUDE.md` (AI) or `onboarding/DEVELOPER_ONBOARDING_STANDARD.md` (human)
- [ ] Read the project `README.md` — understand what the project is and who it is for
- [ ] Read the project `CLAUDE.md` — understand the project-specific AI instructions
- [ ] Confirm the Software Factory layering model is understood (Factory → Platform → Template → Client)

---

## Part 2 — Project State Review

- [ ] Read `DECISION_LOG.md` — understand prior architectural and security decisions
- [ ] Read `IMPLEMENTATION_HISTORY.md` — understand what has been built and the current state
- [ ] Read `MODULE_REGISTRY.md` — understand what custom modules and integrations exist
- [ ] Read `ROADMAP.md` — understand the current phase and what is in scope
- [ ] Read `CHANGELOG.md` — understand the version history

---

## Part 3 — Environment Verification

- [ ] Confirm access to the project repository
- [ ] Confirm access to the development/staging environment
- [ ] Confirm the project builds and starts without errors
- [ ] Confirm database connection is working
- [ ] Confirm access to the backup storage location (if applicable)
- [ ] Confirm secret management access (environment variables or secret store)

---

## Part 4 — Technical Orientation

- [ ] Identify all custom modules in the codebase and verify they match `MODULE_REGISTRY.md`
- [ ] Identify the Odoo version and any version-specific constraints
- [ ] Review the deployment configuration (Nginx, systemd, Docker, etc.)
- [ ] Review the backup schedule and verify last successful backup
- [ ] Review the CI/CD pipeline if one is in place

---

## Part 5 — Governance Compliance Check

- [ ] Confirm `README.md` is current and accurate
- [ ] Confirm `DECISION_LOG.md` has entries for all known architectural decisions
- [ ] Confirm `MODULE_REGISTRY.md` matches the actual codebase
- [ ] Confirm `IMPLEMENTATION_HISTORY.md` reflects the current project state
- [ ] Confirm `ROADMAP.md` reflects the current phase and known upcoming work
- [ ] Note any governance defects found and create issues or PRs to address them

**Governance defects found:**
<!-- List any documents that are stale, missing, or incomplete. -->

---

## Part 6 — Onboarding Confirmation

- [ ] The project state is understood well enough to begin work.
- [ ] The current phase scope is understood — what is in and out of scope.
- [ ] Known sensitive areas and constraints are understood.
- [ ] The PR process and governance standards are understood.

**Open questions or concerns:**
<!-- List anything that was unclear or requires follow-up. -->

---

*This checklist was completed on YYYY-MM-DD by _______________.*
*Record its completion in `IMPLEMENTATION_HISTORY.md` with type `ONBOARDING`.*
