# Governance Impact Analysis (GIA)

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

The Governance Impact Analysis (GIA) is a mandatory pre-completion review that every
Pull Request must pass before it is merged. Its purpose is to ensure that no change
is merged without the author having consciously considered — and addressed — every
dimension of impact that the change might have beyond the code itself.

The GIA is not a bureaucratic checkbox exercise. Each dimension represents a category
of real-world harm that has occurred in software projects when changes were merged
without proper consideration:

- Missing documentation leads to a system no one can maintain.
- Missing decision log entries lead to decisions being reversed unknowingly.
- Missing registry entries lead to invisible technical debt.
- Missing rollback plans lead to unrecoverable production incidents.
- Missing security review leads to data breaches.

---

## 2. When the GIA Is Required

The GIA is required for **every PR** without exception. There are no PR types exempt
from the GIA. Even a documentation-only change must complete the GIA — most dimensions
will be "not impacted" for such a change, but the review must still be performed.

---

## 3. The Ten GIA Dimensions

---

### Dimension 1 — Code Impact

**Question:** What code changed? Is it tested? What is the evidence of correctness?

**What to assess:**
- Which files and modules were modified, added, or removed?
- Are there automated tests? Do they pass?
- If no automated tests exist, what manual verification was performed?
- Is the change backward-compatible, or does it break existing behaviour?
- Are there any edge cases that were not covered by testing?

**Satisfactory answer examples:**
- "Modified `purchase_approval_ext/models/purchase_order.py`. Unit tests pass. Manual test: created a PO above threshold and confirmed the approval stage triggers."
- "Documentation-only change. No code modified."

**Unsatisfactory answer:** "Looks fine." / "Tested locally." (without specifics)

---

### Dimension 2 — Documentation Impact

**Question:** Which documentation must be updated as a result of this change? Is it included in this PR?

**What to assess:**
- Does `README.md` need to be updated to reflect this change?
- Does `CLAUDE.md` need to be updated with new project-specific context?
- Do any files in `docs/` describe the area being changed?
- Does the `CHANGELOG.md` need a new entry?
- Are there setup or configuration instructions that are now out of date?

**Rule:** Documentation must be updated in the same PR as the code change. A follow-up
PR that "will update the docs later" is not acceptable.

**Satisfactory answer examples:**
- "Updated `README.md` module table and `CHANGELOG.md` with v1.2.0 entry. No `docs/` files affected."
- "Documentation-only change — this IS the documentation update."

---

### Dimension 3 — Decision Log Impact

**Question:** Was an architectural, security, data model, integration, or governance decision made or implemented in this PR? If yes, is the `DECISION_LOG.md` entry included?

**What triggers a decision log entry:**
- Custom code was chosen over a native platform feature.
- An architectural or structural pattern was selected.
- A security or access control decision was made.
- A data model choice was made that would be costly to reverse.
- An integration pattern was selected.
- A governance exception was approved.
- A major trade-off was accepted.

**Satisfactory answer examples:**
- "Decision made: custom approval workflow chosen over native Odoo three-level approval because approval thresholds must vary by product category. Decision log entry DEC-007 included in this PR."
- "No decision meeting the criteria in DECISION_LOG_STANDARD.md was made in this PR."

---

### Dimension 4 — Roadmap Impact

**Question:** Does this PR complete, add, defer, or modify a roadmap item? Has `ROADMAP.md` been updated?

**What to assess:**
- Does this PR deliver a roadmap item? Mark it `[COMPLETE]` with the date.
- Does this PR introduce work not currently on the roadmap? Add it (or add it as a completed item if it was just discovered and is now done).
- Does this PR make a roadmap item impossible or require its deferral?

**Satisfactory answer examples:**
- "Completes roadmap item: Phase 2 — Purchase approval module. ROADMAP.md updated with completion date 2026-05-29."
- "No roadmap impact — this is a bug fix within an already-delivered feature."

---

### Dimension 5 — Registry Impact

**Question:** Are any new modules, components, services, integrations, automations, or scripts introduced in this PR? Are they registered in `MODULE_REGISTRY.md`?

**What triggers a registry entry:**
- Any new custom module.
- Any new integration with an external system.
- Any new scheduled action or automation.
- Any new script that is part of project operations.
- Any new infrastructure component.

**Rule:** The registry entry must be included in the same PR that introduces the artifact.

**Satisfactory answer examples:**
- "Introduces `purchase_approval_ext` module. Registry entry MOD-004 added to MODULE_REGISTRY.md in this PR."
- "No new modules, integrations, or scripts introduced."

---

### Dimension 6 — Onboarding Impact

**Question:** Does this change affect how the system should be understood, set up, or operated by a new developer or AI agent?

**What to assess:**
- Does the change introduce a new concept that a new team member would need to know?
- Does it change how the environment is set up?
- Does it change the sequence or pre-requisites for development setup?
- Does it add a new operational procedure?
- Should `CLAUDE.md` be updated to flag this area for AI agents?

**Satisfactory answer examples:**
- "Added environment variable `PURCHASE_APPROVAL_THRESHOLD` required for the new module. Updated `README.md` setup section and `CLAUDE.md` configuration notes."
- "No onboarding impact — change is an internal refactor with no effect on setup or understanding."

---

### Dimension 7 — Security Impact

**Question:** Does this change touch authentication, authorization, access control, user data, secrets, or external APIs? Has a security review been performed?

**What to assess:**
- Does this change affect who can see or modify records?
- Does this change expose data to a new user group?
- Does this change handle credentials, tokens, or secrets?
- Does this change create or modify an external API endpoint?
- Does this change affect audit logging or session management?

**When this dimension has an impact, state explicitly:**
- What data or access is affected.
- What access control mechanism protects it.
- Whether a security decision log entry was created.

**Satisfactory answer examples:**
- "Adds portal access for vendors to view their own POs. Record rule restricts visibility to `partner_id = request.env.user.partner_id`. Security review: confirmed domain filter is applied at ORM level, not just view level. DEC-008 logged."
- "No security impact — change is a calculation fix in a manager-only module."

---

### Dimension 8 — Backup and Recovery Impact

**Question:** Does this change affect what must be backed up, how restore works, or the integrity of the backup/restore pipeline?

**What to assess:**
- Does this change introduce new data that must be included in backups?
- Does this change the filestore structure?
- Does this change a scheduled backup job?
- Does this change add external storage or integration that needs separate backup consideration?
- Does this change a migration that would affect restore procedures?

**Satisfactory answer examples:**
- "Adds a new filestore-backed attachment type for signed PO documents. Filestore is already in scope for daily backups — no backup configuration change needed. Note added to operations docs."
- "No backup/recovery impact."

---

### Dimension 9 — Rollback Impact

**Question:** How is this PR rolled back if it causes problems in production? Is the rollback plan realistic and documented?

**What to assess:**
- For simple code changes: "Revert this PR and redeploy" is sufficient.
- For database schema changes: provide a specific migration reversal procedure.
- For data migrations: specify whether data loss occurs on rollback and how to handle it.
- For infrastructure changes: provide a step-by-step rollback procedure.
- For integrations: specify how to disable the integration cleanly.

**Satisfactory answer examples:**
- "Rollback: revert PR #42, redeploy, clear Odoo cache. No schema changes. Safe to roll back at any time."
- "Rollback: requires running `migrations/rollback_0012.py` to remove the new column before reverting. Data written after deployment will be lost on rollback. Pre-deployment backup required."

---

### Dimension 10 — Testing Evidence

**Question:** What evidence confirms that this change works correctly and does not break existing functionality?

**What to provide:**
- Automated test results (test name, pass/fail count).
- Manual test steps performed and their outcomes.
- Screenshots or logs if relevant.
- Regression confirmation: what was checked to confirm existing functionality is not broken.

**Satisfactory answer examples:**
- "Ran `python -m pytest addons/purchase_approval_ext/tests/ -v`. 12 passed, 0 failed. Manual: created PO above threshold → approval stage appeared correctly. Regression: existing PO flow without threshold unchanged — verified with 3 standard POs."
- "Documentation change only — no functional change to test. Verified rendering in GitHub markdown preview."

---

## 4. GIA Completion Standards

### Passing
A GIA passes when:
- All 10 dimensions are addressed.
- Each addressed dimension provides a substantive answer (not just a checkbox tick).
- All required documentation, decision log, registry, and roadmap updates are included in the PR.

### Failing
A GIA fails when:
- Any dimension is left blank or marked "N/A" without explanation.
- Required updates (decision log, registry, etc.) are promised "in a follow-up PR."
- A security impact is present but not substantively reviewed.
- A rollback plan is missing for a schema-changing or data-migrating PR.

### AI Agent GIA Responsibility
AI agents must complete the GIA before presenting a PR for review. If an AI agent
cannot fully assess a dimension (e.g., it lacks access to the production environment
to verify backup scope), it must flag this explicitly rather than leaving the dimension
blank.

---

*This document is maintained by the Software Factory. Changes require a PR with a decision log entry.*
