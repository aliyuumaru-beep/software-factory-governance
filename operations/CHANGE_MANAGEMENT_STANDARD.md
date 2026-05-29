# Change Management Standard

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects

---

## 1. Purpose

Change management ensures that modifications to production systems are controlled,
reversible, and communicated. Uncontrolled changes to production are the most common
source of unplanned downtime and data integrity issues.

This standard applies to all changes — code, configuration, infrastructure, and data.

---

## 2. Change Types

### Type 1 — Standard Change
A routine, low-risk change that follows an established procedure.

*Examples:* routine module update, configuration file adjustment, user account creation,
scheduled maintenance.

**Requirements:**
- PR merged to main.
- Release tag created.
- Deployment recorded in `IMPLEMENTATION_HISTORY.md`.
- No additional approval gate required beyond the standard PR review.

### Type 2 — Significant Change
A change with meaningful risk or complexity — new functionality, data migrations,
integration changes, or infrastructure modifications.

*Examples:* new module deployment, database migration, new external integration,
Nginx reconfiguration.

**Requirements:**
- PR merged to main with complete GIA.
- Verified backup taken before deployment.
- Rollback plan documented.
- Release tag created.
- Post-deployment verification checklist run.
- Deployment recorded in `IMPLEMENTATION_HISTORY.md`.

### Type 3 — Major Change
A change with high risk or broad system impact — version upgrades, major schema changes,
security architecture changes, infrastructure migrations.

*Examples:* Odoo version upgrade, database restructuring, server migration, moving from
HTTP to HTTPS.

**Requirements:**
- PR merged to main with complete GIA and security review.
- Restore drill completed within 30 days of deployment.
- Pre-upgrade snapshot tag created.
- Change window communicated to stakeholders.
- Staged deployment (staging first, production after staging verification).
- Post-deployment verification checklist run.
- Decision log entry for the change.
- Deployment recorded in `IMPLEMENTATION_HISTORY.md`.

### Type 4 — Emergency Change (Hotfix)
A change required immediately to resolve a production incident.

*Examples:* critical bug fix, security patch, data corruption recovery.

**Requirements:**
- Minimum one-person review (even if expedited).
- Shortened GIA (code, security, rollback dimensions at minimum).
- Deployment recorded in `IMPLEMENTATION_HISTORY.md` within 24 hours.
- Full GIA completed within 24 hours via a follow-up PR.
- Governance exception logged in `DECISION_LOG.md`.

---

## 3. Deployment Approval Gates

| Change Type | Approval Required |
|-------------|------------------|
| Type 1 (Standard) | Standard PR review (1 reviewer) |
| Type 2 (Significant) | Standard PR review + verified backup confirmation |
| Type 3 (Major) | PR review + restore drill record + staging verification |
| Type 4 (Emergency) | Minimum 1 reviewer (post-deployment full review required) |

---

## 4. Production Deployment Checklist

Before every production deployment:

- [ ] PR is merged to main.
- [ ] Release tag is created.
- [ ] Backup taken and verified (required for Type 2+).
- [ ] Rollback plan is documented.
- [ ] Deployment window is appropriate (avoid peak business hours for Type 2+).
- [ ] Stakeholders notified if downtime is expected.

During deployment:

- [ ] Odoo service stopped.
- [ ] Changes applied.
- [ ] Odoo service restarted.
- [ ] Application starts without errors (check logs).

After deployment:

- [ ] Post-deployment verification checklist run.
- [ ] Stakeholders notified of completion.
- [ ] Deployment recorded in `IMPLEMENTATION_HISTORY.md`.
- [ ] Monitoring reviewed for anomalies (if monitoring is in place).

---

## 5. Rollback Decision Criteria

A rollback should be initiated when:
- The application fails to start after deployment.
- Critical functionality is broken and cannot be quickly hotfixed.
- Data integrity issues are detected.
- Error rate spikes significantly above baseline.

Rollback procedure:
1. Stop Odoo service.
2. Check out the prior release tag.
3. Restore from the pre-deployment backup if schema changes were applied.
4. Restart Odoo service.
5. Verify application starts and basic functionality works.
6. Record the rollback in `IMPLEMENTATION_HISTORY.md`.
7. Perform root cause analysis.

---

## 6. Communication Requirements

### 6.1 Planned Maintenance
For planned downtime (Type 3 changes): notify stakeholders at least 48 hours in advance.

### 6.2 Emergency Changes
For emergency changes: notify stakeholders as soon as the issue is confirmed and
provide a status update within 1 hour.

### 6.3 Post-Incident Report
For Type 4 emergency changes, a post-incident report must be written and stored in
`IMPLEMENTATION_HISTORY.md` within 72 hours. It must include:
- Timeline of the incident.
- Root cause.
- Actions taken.
- Preventive measures.

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
