# Restore Drill Standard

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Core Principle

> **A backup is only trusted after a successful restore.**

A restore drill is the only evidence that a backup is functional. Without a drill,
a backup is an assumption. The restore drill is non-negotiable.

---

## 2. Drill Frequency Requirements

| Environment | Minimum Frequency | Notes |
|-------------|-------------------|-------|
| Production | Quarterly (every 3 months) | May be performed on a staging copy of production data |
| Staging | Bi-annually (every 6 months) | |
| Pre-upgrade | Before every major upgrade | Required, not optional |
| Pre-migration | Before any data migration | Required, not optional |

---

## 3. Drill Scope

A restore drill must verify the full recovery path:

1. **Backup Retrieval** — confirm the backup file is accessible from its storage location.
2. **Integrity Verification** — confirm the backup file is readable and non-corrupted.
3. **Database Restore** — restore the database dump to a clean database instance.
4. **Filestore Restore** — restore the filestore archive to the correct location.
5. **Application Startup** — start Odoo against the restored database and verify it starts.
6. **Data Verification** — run the data verification checklist (section 4).
7. **Functionality Verification** — perform the functionality checklist (section 5).

All seven steps must pass for the drill to be recorded as successful.

---

## 4. Data Verification Checklist

After restore, verify the following data is present and correct:

### 4.1 Master Data
- [ ] Chart of accounts is present and correct.
- [ ] Product catalogue is present (spot-check 5 products).
- [ ] Partner/customer list is present (spot-check 5 partners).
- [ ] User accounts are present and roles are correct.

### 4.2 Transactional Data
- [ ] Most recent invoices are present and match expected totals.
- [ ] Most recent inventory moves are present.
- [ ] Most recent purchase orders are present.
- [ ] Most recent sales orders are present.

### 4.3 Attachments and Files
- [ ] At least 5 attachments are accessible (not returning 404/missing).
- [ ] Company logo is displayed correctly.

### 4.4 Configuration
- [ ] Company configuration is correct (name, logo, address, currency).
- [ ] Active users can log in.
- [ ] Installed modules list matches the expected list.

---

## 5. Functionality Verification Checklist

After data verification, perform a basic functionality smoke test:

- [ ] Log in as an administrative user.
- [ ] Navigate to at least 3 different modules without errors.
- [ ] Create a test record in at least one key module (e.g., a draft invoice).
- [ ] Confirm scheduled actions are not running against restored data unexpectedly.
- [ ] Confirm email sending is disabled or redirected for the drill environment.

---

## 6. Drill Environment Requirements

### 6.1 Isolation
The drill environment must be isolated from production. A restore drill must not:
- Overwrite production data.
- Send emails or notifications to real users.
- Trigger integrations with external systems.

### 6.2 Cleanup
After a successful drill, the restore environment must be cleaned up:
- Drop the restored database.
- Remove the restored filestore.
- Confirm no orphaned processes remain.

---

## 7. Recording the Drill Result

Every restore drill result — pass or fail — must be recorded in `IMPLEMENTATION_HISTORY.md`
with type `RESTORE_EVENT`.

Required fields:
- Date and time of drill.
- Backup used (date, type, filename).
- Drill environment (staging server, local, etc.).
- Steps completed and any failures.
- Data verification result (pass / partial / fail).
- Functionality verification result (pass / partial / fail).
- Overall result: **PASS** or **FAIL**.
- If FAIL: root cause and corrective action taken.

### Example Record

```
## IMP-NNN — Restore Drill: FamOil Production (Q2 2026)

**Date:** 2026-05-29
**Type:** RESTORE_EVENT
**Status:** COMPLETE

**Backup Used:** famoil_20260528_020000_full.dump + filestore archive
**Environment:** Staging server (isolated)

**Steps:**
- [x] Backup retrieval — OK
- [x] Integrity verification — OK
- [x] Database restore — OK (12 minutes)
- [x] Filestore restore — OK (4 minutes)
- [x] Application startup — OK
- [x] Data verification — PASS
- [x] Functionality verification — PASS

**Overall Result: PASS**
**Total Time to Restore:** 22 minutes
**RTO Target:** 60 minutes — WITHIN TARGET
```

---

## 8. Failed Drill Response

If a drill fails:

1. Do not delete or modify the backup until the cause of failure is understood.
2. Diagnose the root cause — is it the backup, the procedure, or the environment?
3. Fix the root cause.
4. Perform a new drill immediately after the fix.
5. Record both the failed and successful drills in `IMPLEMENTATION_HISTORY.md`.
6. If the backup itself is corrupted: review the backup procedure immediately and
   log a `OPERATIONAL` decision in `DECISION_LOG.md` about the corrective action.

---

## 9. Pre-Upgrade Drill Protocol

Before any Odoo version upgrade, major module installation, or data migration:

1. Perform a restore drill using the most recent backup.
2. Confirm the drill passes completely.
3. Record the result in `IMPLEMENTATION_HISTORY.md`.
4. Proceed with the upgrade only after a passing drill is recorded.
5. If the drill fails, do not proceed with the upgrade.

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
