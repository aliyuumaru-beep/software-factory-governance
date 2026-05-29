# Backup and Recovery Governance Standard

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects

---

## 1. Core Principle

> **A backup is only trusted after a successful restore.**

A backup that has never been tested is an assumption, not a guarantee. This principle
is non-negotiable across all Software Factory projects. No project may claim it has a
functioning backup system until a restore from that backup has been verified successfully.

---

## 2. What Must Be Backed Up

Every project must define its backup scope, which must include at minimum:

### 2.1 Database
The full project database, including all custom module data, configuration, and
master data. Database backups must capture a point-in-time consistent snapshot.

### 2.2 Filestore
For Odoo projects: the filestore directory (`/var/lib/odoo/filestore/<database>/`)
containing attachments, images, and binary data.
The database and filestore backups must be coordinated — a database backup without
a matching filestore backup is incomplete.

### 2.3 Configuration Files
Any configuration file that is not in version control and that would be required to
restore a functioning system:
- `odoo.conf` (with secrets redacted from version-controlled copies)
- Nginx or reverse proxy configuration
- Environment variable files (secrets excluded — use secret management)

### 2.4 Custom Code
Custom code is backed up via the version control repository. The repository itself
must be backed up to a remote (GitHub/GitLab) and that remote must be confirmed
accessible.

---

## 3. Backup Schedule Requirements

| Environment | Minimum Frequency | Retention |
|-------------|-------------------|-----------|
| Production | Daily (automated) | 30 days minimum |
| Staging | Weekly | 14 days minimum |
| Development | On significant change | 7 days minimum |

Projects handling financial data, personal data, or mission-critical operations must
document a backup schedule in their `DECISION_LOG.md` that meets or exceeds this
minimum.

---

## 4. Backup Verification

### 4.1 Restore Drills
See `operations/RESTORE_DRILL_STANDARD.md` for the full procedure.

**Minimum drill frequency:**
- Production systems: quarterly (every 3 months).
- Staging systems: bi-annually (every 6 months).

### 4.2 Verification Criteria
A backup is considered verified after a restore drill confirms:
- The database restores without errors.
- The application starts and accepts connections.
- A defined set of data verification checks pass (see restore drill standard).
- The filestore is intact and attachments are accessible.

### 4.3 Recording
Every restore drill (whether successful or not) must be recorded in
`IMPLEMENTATION_HISTORY.md` with type `RESTORE_EVENT`.

---

## 5. Backup Storage Requirements

### 5.1 Location
Backups must be stored in a location separate from the production system:
- A different physical server or cloud bucket.
- Not the same disk partition as the production data.

### 5.2 Access Control
Backup storage must be access-controlled. The backup location and credentials
must follow the secret management rules in `governance/SECURITY_STANDARD.md`.

### 5.3 Encryption
Backups containing personal data, financial data, or credentials must be encrypted
at rest. The encryption approach must be logged in `DECISION_LOG.md`.

---

## 6. Recovery Objectives

Each project must define and document:

| Metric | Definition | Required Location |
|--------|------------|-------------------|
| **RPO** (Recovery Point Objective) | Maximum acceptable data loss in time | `DECISION_LOG.md` |
| **RTO** (Recovery Time Objective) | Maximum acceptable downtime during recovery | `DECISION_LOG.md` |

These objectives must be agreed with the client or stakeholder and logged.
The backup schedule and restore drill results must be consistent with the defined objectives.

---

## 7. Backup Failure Response

If a backup fails:
1. Do not wait for the next scheduled run. Investigate immediately.
2. Determine the root cause.
3. If production data is at risk, escalate to the Software Factory lead.
4. Record the failure and resolution in `IMPLEMENTATION_HISTORY.md`.

---

## 8. Pre-Upgrade Backup Requirement

Before any of the following operations, a verified backup must exist:
- Odoo version upgrade.
- Database migration.
- Major module installation or removal.
- Infrastructure reconfiguration.

"Verified" means a restore drill has been completed within the last 30 days, or a
new restore drill is performed immediately before the operation.

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
