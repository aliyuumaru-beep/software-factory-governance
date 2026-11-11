# Authority Classification Standard

---

**Document:** ACS-001
**Enhancement:** AOP-013 Execution Authority Framework
**Version:** 1.0
**Date:** 2026-06-25
**Author:** G1 Architecture & Odoo Governance

---

## 1. Purpose

This standard defines the six execution authority classes (EA-1 through EA-6) used in Agent OS v2.0. It provides classification criteria, examples, risk assessment, and approval requirements for each class.

Every execution action performed by D2 must be classified against this standard before an authority request is submitted.

---

## 2. Classification Rules

**Rule 1 — Use the highest applicable class.** If an action could be classified as EA-2 or EA-3, classify it as EA-3. Always round up.

**Rule 2 — Classify by the riskiest action.** If a work package contains both EA-2 and EA-4 actions, the authority request is EA-4 for the entire request.

**Rule 3 — Do not split risk across requests.** Related actions that together constitute a higher-risk class must not be submitted as multiple lower-risk requests to avoid scrutiny.

**Rule 4 — EA-6 is non-negotiable.** No classification analysis can result in a production action being classified below EA-6.

**Rule 5 — Uncertainty escalates.** If D2 is uncertain which class applies, submit as the higher class. G1 will confirm the correct classification during review.

---

## 3. Authority Classes

---

### EA-1 — Documentation Authority

**Risk Level:** Low
**G1 Required:** Yes
**G2 Required:** Optional
**G3 Required:** Optional
**A1 Decision:** Auto (after G1 review)
**Human Required:** No

**Definition:**
Authority to create, modify, or delete documentation files that have no direct impact on system configuration, module installation, database state, or production environment.

**Qualifies as EA-1:**
- README.md creation or update
- CHANGELOG.md update
- IMPLEMENTATION_HISTORY.md update
- DECISION_LOG.md update
- ROADMAP.md update
- Governance reports and assessments
- Planning documents and specifications
- Work package documentation
- Phase gate reports
- MODULE_REGISTRY.md updates (documentation only — not the module installation itself)

**Does NOT qualify as EA-1:**
- Any file that, when saved, triggers an automated system action
- CLAUDE.md changes that alter agent behaviour
- Configuration files (use EA-3)
- Database seed/fixture files (use EA-5)

**Typical review time:** Same session
**Typical validity:** Current work package

---

### EA-2 — Repository Authority

**Risk Level:** Low
**G1 Required:** Yes
**G2 Required:** Yes
**G3 Required:** Optional
**A1 Decision:** Auto (after G1+G2 review)
**Human Required:** No

**Definition:**
Authority to perform git and repository operations that do not directly modify production-affecting system files.

**Qualifies as EA-2:**
- Branch creation
- Branch deletion (non-main, non-protected)
- Pull request creation
- Pull request description updates
- Commit of documentation-only changes
- Commit of non-functional repository files (.gitignore, .github templates)
- Tag creation (non-release)
- Merging approved PRs (after PR governance review)

**Does NOT qualify as EA-2:**
- Force push to any branch
- Deletion of protected branches
- Changes to `.github/workflows/` CI configuration (use EA-3)
- Release tagging (use EA-3)
- Any commit containing module code (use EA-4 or higher)

**Typical review time:** Same session
**Typical validity:** Current work package

---

### EA-3 — Configuration Authority

**Risk Level:** Medium
**G1 Required:** Yes
**G2 Required:** Yes
**G3 Required:** Yes
**A1 Decision:** Required (explicit)
**Human Required:** No

**Definition:**
Authority to modify system configuration settings, security settings, workflow settings, and CI/CD pipeline configuration. These actions change system behaviour without installing new modules or altering database schema.

**Qualifies as EA-3:**
- Odoo system parameters (`ir.config_parameter`)
- Odoo security settings (password policy, 2FA policy, session timeout)
- Odoo workflow and automation rules (non-data)
- CI/CD workflow file changes (`.github/workflows/`)
- Claude hooks configuration (`.claude/hooks/`)
- Server configuration file changes (`nadf.conf`, `famoil.conf`, `wamacare.conf`)
- Release tagging and changelog generation
- `.gitignore` changes that affect what is tracked
- CLAUDE.md changes that alter agent behaviour

**Does NOT qualify as EA-3:**
- Module installation (use EA-4)
- Data migration or bulk record updates (use EA-5)
- Production configuration changes (use EA-6)

**Typical review time:** Same session to next session
**Typical validity:** Current work package

---

### EA-4 — Module Installation Authority

**Risk Level:** Medium
**G1 Required:** Yes
**G2 Required:** Yes
**G3 Required:** Yes
**A1 Decision:** Required (explicit)
**Human Required:** No

**Definition:**
Authority to install, upgrade, or uninstall Odoo modules and their approved dependencies. This includes OCA modules, community modules, and custom modules within the approved registry.

**Qualifies as EA-4:**
- OCA module installation (modules on the approved OCA list)
- Approved dependency module installation
- Custom module installation (modules in the project MODULE_REGISTRY)
- Module upgrade after patch update
- Module uninstallation (with documented impact assessment)
- Adding a module to the Odoo addons_path

**Does NOT qualify as EA-4:**
- Installation of modules not on the approved list (requires escalation — new approval)
- Installation of Enterprise Edition modules (prohibited — requires governance exception)
- Any module installation on the production database (use EA-6)
- Data migration triggered by module upgrade (use EA-5)

**Pre-conditions for EA-4 authority:**
- Module must be in MODULE_REGISTRY or on approved OCA list
- Dependency chain must be verified
- Rollback plan must exist (module uninstall path confirmed)
- Test database install confirmed before dev/staging execution

**Typical review time:** Same session to next session
**Typical validity:** Current work package; specific modules named in authority grant

---

### EA-5 — Database Mutation Authority

**Risk Level:** High
**G1 Required:** Yes
**G2 Required:** Yes
**G3 Required:** Yes
**A1 Decision:** Required (explicit)
**Human Required:** No (but Human is strongly recommended to be informed before execution)

**Definition:**
Authority to perform direct database mutations: data migrations, bulk record updates, schema-affecting operations, and any action that alters stored data outside of normal Odoo UI operations.

**Qualifies as EA-5:**
- CSV data import via Odoo import interface (bulk)
- Python scripts that directly modify database records (`env['model'].write(...)`)
- SQL scripts executed against the database
- Database restore from backup
- Bulk field value updates
- Account consolidation or re-mapping operations
- Employee record bulk update
- Chart of accounts import

**Does NOT qualify as EA-5:**
- Single-record manual edits via Odoo UI (no authority required — normal user operation)
- Module installation that creates new tables (use EA-4)
- Production database operations (use EA-6)

**Pre-conditions for EA-5 authority:**
- Database backup taken immediately before execution
- Backup verified (restore-drill or checksum)
- Rollback plan documented (restore from backup)
- Execution on test/staging database first
- G3 has confirmed recovery readiness

**Typical review time:** One to two sessions
**Typical validity:** Specific data migration event; expires after execution

---

### EA-6 — Production Authority

**Risk Level:** Critical
**G1 Required:** Yes
**G2 Required:** Yes
**G3 Required:** Yes
**A1 Decision:** Routes to Human Sponsor
**Human Required:** YES — mandatory

**Definition:**
Authority for any action on the production environment. This includes production deployment, production upgrade, production configuration change, production database modification, and production rollback.

**Qualifies as EA-6:**
- Deploying to production server
- Upgrading Odoo on production
- Installing modules on production database
- Modifying production configuration files
- Running data migrations on production database
- Production database backup/restore
- Production rollback
- Granting production access to new users

**A1 behaviour for EA-6:**
A1 does not issue authority for EA-6. A1 prepares the governance review package and routes it to the Human Sponsor with a formal recommendation. The Human Sponsor issues the authority directly.

**Pre-conditions for EA-6 (before Human Sponsor review):**
- G1/G2/G3 have all completed their reviews
- Staging environment execution was successful
- Full production backup exists and has been verified
- Rollback procedure is documented and tested
- Change window is agreed
- Communication plan is prepared

**Note:** In the current Software Factory deployment, all three projects (NADF, FAMOIL, WAMACARE) are development/staging environments. EA-6 is defined for completeness and future production deployments.

---

## 4. Classification Quick Reference

| Action Type | EA Class |
|-------------|----------|
| Update CHANGELOG.md | EA-1 |
| Create a planning document | EA-1 |
| Update DECISION_LOG.md | EA-1 |
| Create a feature branch | EA-2 |
| Open a pull request | EA-2 |
| Merge a PR to main | EA-2 |
| Change Odoo system parameter | EA-3 |
| Enable 2FA globally | EA-3 |
| Modify CI workflow file | EA-3 |
| Change server .conf file | EA-3 |
| Install OCA module | EA-4 |
| Install custom module | EA-4 |
| Upgrade installed module | EA-4 |
| Import CSV data (bulk) | EA-5 |
| Run Python data migration | EA-5 |
| Restore database from backup | EA-5 |
| Deploy to production | EA-6 |
| Any production database change | EA-6 |

---

## 5. Revision History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-06-25 | Initial release under AOP-013 |

---

*Authority Classification Standard — G1 Architecture & Odoo Governance*
*Software Factory Governance Authority — 2026-06-25*
