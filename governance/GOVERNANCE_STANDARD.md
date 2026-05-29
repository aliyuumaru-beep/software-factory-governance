# Governance Standard

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

This document defines the binding governance standard for all software projects operating under
the Software Factory. It establishes the minimum requirements for project structure, documentation,
change control, decision management, and quality assurance across every project regardless of
technology stack, client, or industry vertical.

Compliance with this standard is not optional. Every project repository must implement these
requirements or explicitly document a governance exception in its `DECISION_LOG.md`.

---

## 2. Definitions

| Term | Definition |
|------|------------|
| **Software Factory** | The governance, methodology, and delivery organization that owns and operates all projects |
| **Platform Layer** | Shared infrastructure, base configurations, and platform-level modules |
| **Industry Template** | A vertical-specific template repository (e.g., Oil & Gas ERP template) |
| **Client Deployment** | A per-client project derived from a platform and/or industry template |
| **Repository Memory** | The collection of governance documents within a repository that record decisions, history, and state |
| **Governance Impact Analysis (GIA)** | Mandatory pre-completion review of a PR across all governance dimensions |

---

## 3. Required Repository Documents

Every Software Factory project repository must contain the following documents:

### 3.1 Mandatory Files (Root)

| File | Purpose |
|------|---------|
| `README.md` | Project overview, purpose, architecture summary, and usage |
| `CLAUDE.md` | AI agent instruction set (inherits from governance, extends for project) |
| `CHANGELOG.md` | Version history of meaningful project changes |
| `DECISION_LOG.md` | Log of all architectural, security, and governance decisions |
| `IMPLEMENTATION_HISTORY.md` | Record of milestones, phases, and significant operational changes |
| `MODULE_REGISTRY.md` | Registry of all modules, components, services, integrations, and scripts |
| `ROADMAP.md` | Current project roadmap aligned to the roadmap standard |

### 3.2 Required Directories

| Directory | Contents |
|-----------|----------|
| `.github/` | PR templates, issue templates, CI workflows |
| `docs/` | Project-specific documentation |

---

## 4. Change Control Requirements

### 4.1 All Changes Must Be Made via Pull Request

No direct commits to the main or production branch are permitted except for:
- Emergency hotfixes (must be documented in `IMPLEMENTATION_HISTORY.md` within 24 hours)
- Repository initialization (first commit only)

### 4.2 PR Requirements

Every PR must:
1. Use the standard PR template from `templates/pull_request_template.md`
2. Complete the Governance Impact Analysis checklist
3. Update affected documentation before the PR is marked complete
4. Reference the relevant `DECISION_LOG.md` entry if an architectural decision was made
5. Update `MODULE_REGISTRY.md` if a new module/component/service was added

### 4.3 Commit Message Standard

Format: `<type>(<scope>): <short description>`

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `security`, `ops`

Examples:
- `feat(purchase): add custom approval workflow for POs above threshold`
- `docs(registry): register purchase_approval_ext module`
- `security(auth): restrict portal user access to own records only`

---

## 5. Decision Logging Requirements

See `governance/DECISION_LOG_STANDARD.md` for the full standard.

Summary: A decision must be logged whenever:
- A native platform feature is rejected in favour of custom code
- An architectural or data model pattern is chosen
- A security decision is made
- An integration pattern is selected
- A governance exception is approved
- A major trade-off is accepted

---

## 6. Registry Requirements

See `governance/REGISTRY_STANDARD.md` for the full standard.

Summary: Every module, component, service, integration, automation, and script must be
registered before or at the same time as the PR that introduces it is merged.

---

## 7. Documentation Requirements

See `governance/DOCUMENTATION_STANDARD.md` for the full standard.

Summary:
- Documentation must be updated in the same PR as the code change it describes.
- Stale documentation is treated as a governance defect.
- AI agents must not declare a PR complete if documentation is out of date.

---

## 8. Security Requirements

See `governance/SECURITY_STANDARD.md` for the full standard.

Summary:
- All access control decisions must be logged.
- No secrets, credentials, or API keys may be committed to any repository.
- Security decisions must be reviewed before the PR containing them is merged.

---

## 9. Backup and Recovery Requirements

See `governance/BACKUP_RECOVERY_STANDARD.md` for the full standard.

Summary:
- Every project must define its backup scope and schedule.
- A backup is only trusted after a successful restore drill.
- Restore drills must be performed at minimum quarterly for production systems.

---

## 10. Roadmap Requirements

See `governance/ROADMAP_STANDARD.md` for the full standard.

Summary:
- Every project maintains a `ROADMAP.md` that reflects only its own layer's scope.
- Roadmap items must not cross layer boundaries without an explicit dependency declaration.
- Completed roadmap items must be marked and recorded in `IMPLEMENTATION_HISTORY.md`.

---

## 11. Governance Exceptions

A governance exception is any deliberate deviation from a requirement in this standard.

Exceptions must:
1. Be logged in the project `DECISION_LOG.md` with the entry type `GOVERNANCE_EXCEPTION`.
2. State the specific requirement being waived.
3. State the reason and the time-limited scope (if applicable).
4. Be approved by the Software Factory lead.

Exceptions are not permanent unless explicitly declared as permanent in the decision log.

---

## 12. Enforcement

Compliance is enforced by:
1. AI agent instruction sets (`CLAUDE.md`) — agents must flag non-compliance before proceeding.
2. PR templates — checklists must be completed before merge.
3. Repository audit — governance documents are reviewed for completeness at each project milestone.
4. Phase gate reviews — each phase of a project roadmap includes a governance compliance check.

---

## 13. Governance Maturity Levels

| Level | Description |
|-------|-------------|
| **Level 0 — Bootstrap** | Repository initialized, root files created |
| **Level 1 — Foundation** | All mandatory files present, PR template in use |
| **Level 2 — Active Governance** | Decision log, registry, and implementation history maintained and current |
| **Level 3 — Enforced** | CI checks enforce governance compliance, no bypassed PRs |
| **Level 4 — Mature** | Restore drills complete, roadmap current, onboarding verified, governance audited |

---

*This standard is owned by the Software Factory. Changes to this document require a PR with a decision log entry.*
