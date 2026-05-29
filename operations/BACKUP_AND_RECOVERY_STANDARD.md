# Backup and Recovery Operations Standard

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects
**Governance Reference:** `governance/BACKUP_RECOVERY_STANDARD.md`

---

## 1. Purpose

This document defines the operational procedures for backup execution and recovery
across all Software Factory projects. It translates the governance principles in
`governance/BACKUP_RECOVERY_STANDARD.md` into concrete operational steps.

---

## 2. Backup Procedure — Odoo Projects

### 2.1 Full Database Backup (PostgreSQL)

```bash
# Standard backup command — replace variables as appropriate
pg_dump -Fc -U <db_user> <database_name> > /path/to/backups/<database_name>_$(date +%Y%m%d_%H%M%S).dump

# Verify the dump file is non-empty and not corrupted
pg_restore --list /path/to/backups/<file>.dump | head -20
```

### 2.2 Filestore Backup

```bash
# Backup the Odoo filestore directory
tar -czf /path/to/backups/<database_name>_filestore_$(date +%Y%m%d_%H%M%S).tar.gz \
    /var/lib/odoo/filestore/<database_name>/
```

### 2.3 Coordinated Database + Filestore Backup

The database and filestore must be backed up together. A database backup without a
matching filestore backup (or vice versa) may result in broken attachments after restore.

Recommended approach: stop writes (put Odoo in maintenance mode) → dump database
→ archive filestore → resume writes.

For live backups: use database transaction consistency (pg_dump is transactionally
consistent) and accept that filestore files created between the dump start and the
filestore archive will be missing — document this as the accepted RPO.

### 2.4 Backup Naming Convention

```
<database_name>_<YYYYMMDD>_<HHMMSS>_<type>.dump
<database_name>_<YYYYMMDD>_<HHMMSS>_filestore.tar.gz
```

Examples:
- `famoil_20260529_020000_full.dump`
- `famoil_20260529_020000_filestore.tar.gz`

---

## 3. Automated Backup Schedule

### 3.1 Cron Job Template (Linux)

```bash
# Daily full backup at 02:00 AM
0 2 * * * /usr/local/bin/sf_backup.sh >> /var/log/sf_backup.log 2>&1
```

### 3.2 Backup Script Template

```bash
#!/bin/bash
set -euo pipefail

DB_NAME="${1:-<database_name>}"
BACKUP_DIR="/path/to/backups"
DATE=$(date +%Y%m%d_%H%M%S)
LOG_FILE="/var/log/sf_backup.log"

echo "[$(date)] Starting backup for ${DB_NAME}" >> "${LOG_FILE}"

# Database
pg_dump -Fc -U odoo "${DB_NAME}" > "${BACKUP_DIR}/${DB_NAME}_${DATE}_full.dump"

# Filestore
tar -czf "${BACKUP_DIR}/${DB_NAME}_${DATE}_filestore.tar.gz" \
    "/var/lib/odoo/filestore/${DB_NAME}/"

# Rotate old backups (keep 30 days)
find "${BACKUP_DIR}" -name "${DB_NAME}_*" -mtime +30 -delete

echo "[$(date)] Backup complete for ${DB_NAME}" >> "${LOG_FILE}"
```

---

## 4. Recovery Procedure

### 4.1 Pre-Recovery Checklist

Before beginning a restore:
- [ ] Confirm the backup file is complete and readable (`pg_restore --list` returns output).
- [ ] Confirm the filestore archive is not corrupted (`tar -tzf <file>` returns output).
- [ ] Confirm the database and filestore backup timestamps are coordinated.
- [ ] Stop Odoo service before restoring.
- [ ] Create a snapshot of the current state if restoring to the same server.

### 4.2 Database Restore

```bash
# Stop Odoo
sudo systemctl stop odoo

# Drop existing database (CAUTION: destructive)
dropdb -U postgres <database_name>

# Create fresh database
createdb -U postgres -O odoo <database_name>

# Restore from dump
pg_restore -U postgres -d <database_name> /path/to/backups/<file>.dump

echo "Database restore complete."
```

### 4.3 Filestore Restore

```bash
# Backup current filestore first (if exists)
mv /var/lib/odoo/filestore/<database_name> \
   /var/lib/odoo/filestore/<database_name>_pre_restore_$(date +%Y%m%d)

# Restore filestore
tar -xzf /path/to/backups/<filestore_archive>.tar.gz \
    -C /var/lib/odoo/filestore/

# Fix ownership
chown -R odoo:odoo /var/lib/odoo/filestore/<database_name>
```

### 4.4 Post-Recovery Verification

```bash
# Start Odoo
sudo systemctl start odoo

# Check Odoo logs for startup errors
sudo journalctl -u odoo -f --lines=50

# Verify database is accessible and user login works
# Run the data verification checklist defined in the project's restore drill standard
```

---

## 5. Off-Site Backup Transfer

After local backup is confirmed:

```bash
# Example: transfer to remote server via scp
scp /path/to/backups/<file>.dump user@backup-server:/remote/backup/path/

# Example: upload to object storage (requires configured CLI)
aws s3 cp /path/to/backups/<file>.dump s3://<bucket>/<prefix>/
# or
rclone copy /path/to/backups/<file>.dump remote:<bucket>/<prefix>/
```

---

## 6. Backup Verification

Verify every backup after creation:

```bash
# Verify database dump integrity
pg_restore --list /path/to/backups/<file>.dump > /dev/null && echo "Dump OK" || echo "Dump CORRUPTED"

# Verify filestore archive integrity
tar -tzf /path/to/backups/<filestore>.tar.gz > /dev/null && echo "Archive OK" || echo "Archive CORRUPTED"

# Record result in IMPLEMENTATION_HISTORY.md if this is a scheduled drill
```

---

## 7. Recovery Time Targets

Each project must define its RPO and RTO in `DECISION_LOG.md`.
These operational procedures must be tested to confirm they can meet those targets.

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
