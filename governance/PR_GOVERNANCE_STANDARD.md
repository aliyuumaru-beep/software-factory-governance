# PR Governance Standard

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

This standard defines the requirements for all Pull Requests (PRs) across every Software Factory
project. Its purpose is to ensure that no change is merged without a documented, reviewed,
and governance-compliant record of what changed, why, and what was affected.

---

## 2. PR Template

All PRs must use the template defined in `templates/pull_request_template.md`.

The template is not optional. PRs that do not use the template or that leave mandatory
sections incomplete must not be merged.

---

## 3. PR Types

Every PR must declare exactly one change type:

| Type | Description |
|------|-------------|
| `feat` | New feature, module, or capability |
| `fix` | Bug fix or defect correction |
| `refactor` | Code restructuring without behaviour change |
| `docs` | Documentation-only change |
| `security` | Security fix or access control change |
| `ops` | Operational change (backup, deployment, infrastructure) |
| `chore` | Dependency update, config change, housekeeping |
| `test` | Test addition or correction |
| `governance` | Change to governance documents, standards, or templates |

---

## 4. Mandatory PR Sections

### 4.1 Change Description
A clear, human-readable description of what this PR does and why.
Do not describe what the code does — describe why the change was made.

### 4.2 Governance Impact Analysis
Every PR must include a completed Governance Impact Analysis (GIA).
See `docs/GOVERNANCE_IMPACT_ANALYSIS.md` for the full definition.

The GIA must address all 10 dimensions:
1. Code impact
2. Documentation impact
3. Decision log impact
4. Roadmap impact
5. Registry impact
6. Onboarding impact
7. Security impact
8. Backup/recovery impact
9. Rollback impact
10. Testing evidence

Marking a dimension as "Not impacted" is valid only if the reason is stated.

### 4.3 Repository Memory Review
The PR author must confirm that they have read and are consistent with:
- `DECISION_LOG.md` — not reversing a prior decision without a new log entry
- `IMPLEMENTATION_HISTORY.md` — aware of prior work in this area
- `MODULE_REGISTRY.md` — new components are registered
- `ROADMAP.md` — change is within current scope

### 4.4 New Module/Component Checklist
If the PR introduces any new module, component, service, integration, automation, or script:
- [ ] Entry added to `MODULE_REGISTRY.md`
- [ ] Decision log entry created if this was an architectural choice
- [ ] Onboarding documentation updated if this changes how the system is understood

### 4.5 Decision Log Review
If the PR makes or implements an architectural, security, data model, integration, or governance decision:
- [ ] Entry added to `DECISION_LOG.md` using `templates/decision_log_template.md`
- [ ] Decision log entry referenced in this PR

### 4.6 Rollback Plan
Every PR must state a rollback plan. For most changes this is:
- "Revert this PR and redeploy." (acceptable for simple changes)
- For database schema changes, data migrations, or infrastructure changes — a detailed rollback procedure is required.

### 4.7 Final Governance Declaration
The PR author must sign off: "I confirm that this PR satisfies the Software Factory Governance Standard."

---

## 5. PR Review Requirements

### 5.1 Who Must Review
- Minimum one review from a team member who did not author the PR.
- For security changes: an explicit security review is required.
- For schema changes: a data review is required.
- For governance document changes: review by the Software Factory lead.

### 5.2 What Reviewers Must Check
Reviewers are responsible for verifying:
- [ ] PR template is complete, not just ticked without thought.
- [ ] GIA dimensions are genuinely addressed, not rubber-stamped.
- [ ] Decision log entries are present where required.
- [ ] Registry entries are present where required.
- [ ] Documentation updates are included in the PR.
- [ ] Rollback plan is realistic.

### 5.3 AI Agent Review
When an AI agent assists with or creates a PR, the agent must:
- Complete the GIA before presenting the PR for review.
- Flag any governance dimension it could not fully assess.
- Never self-approve a PR it created.

---

## 6. Merge Requirements

A PR may only be merged when:
- [ ] All mandatory checklist items are complete.
- [ ] All required reviews are approved.
- [ ] No unresolved review comments remain.
- [ ] CI checks pass (where CI is in place).
- [ ] Documentation updates are committed and included.
- [ ] The final governance declaration is signed.

---

## 7. Emergency Hotfix Procedure

In a genuine production emergency, a hotfix may be merged with:
- One reviewer (may be the same session, documented).
- A shortened but non-empty GIA (at minimum: code impact, security impact, rollback plan).
- A commitment to complete the full GIA within 24 hours, documented in `IMPLEMENTATION_HISTORY.md`.

Emergency use of this procedure must be logged as a `GOVERNANCE_EXCEPTION` in `DECISION_LOG.md`.

---

## 8. PR Naming Convention

PR titles must follow the same format as commit messages:
`<type>(<scope>): <short description>`

Examples:
- `feat(inventory): add lot-level traceability for soybean batches`
- `security(auth): restrict vendor portal to own purchase orders only`
- `docs(registry): register tank_management_ext module`
- `governance(templates): add onboarding_template.md`

---

*This standard is owned by the Software Factory. Changes require a PR with a governance document change type.*
