# PEF_SCOPE_CHANGE_REQUEST_TEMPLATE.md
## Software Factory — Scope Change Request Template

**Template ID:** PEF-TPL-009  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Section 12.3 (Scope Change Control Procedure)  
**Produced at:** Any time after Gate 3 (Development Authorisation, PEG-6)  
**Approved by:** Product Owner (with Governance Team confirmation where Coverage re-validation is triggered)

---

## INSTRUCTIONS FOR USE

Use one Scope Change Request (SCR) per discrete change. A scope change after Gate 3 may **silently invalidate the Coverage Score** if it is not assessed (closes OMI-05). No change is implemented until this form is completed and approved.

**Reconciliation note:** Each approved SCR must also be recorded in `PEF_PRODUCT_APPROVAL_TEMPLATE.md` **Section D — Scope Change Register**, using the **same SCR ID**. This template is the assessment instrument; the Approval document's register is the permanent ledger. Do not maintain two divergent records.

Sections marked **[REQUIRED]** cannot be omitted. Replace all `[PLACEHOLDER]` text.  
Delete these instructions before submitting for approval.

---

## SECTION A — REQUEST IDENTITY **[REQUIRED]**

| Field | Value |
|-------|-------|
| SCR ID | SCR-[NNN] |
| Project name | [PROJECT_NAME] |
| Raised by | [NAME, ROLE] |
| Date raised | [YYYY-MM-DD] |
| Current PEG stage | [e.g. PEG-7] |
| Status | [Raised / Under Assessment / Approved / Rejected / Implemented] |
| Priority | [Critical / High / Medium / Low] |

---

## SECTION B — CHANGE DESCRIPTION **[REQUIRED]**

**What is being requested:**

[Describe the change precisely. State the new or altered requirement.]

**Reason for the change:**

[Why is this needed now? e.g. late TO-BE delivery, regulatory change, defect-driven re-scope, client request.]

**Affected Capability Areas / Backlog items / Work Packages:**

| Type | ID | Title |
|------|----|----|
| [CA / Backlog / WP] | [ID] | [Title] |
| *Add rows as needed* | | |

---

## SECTION C — IMPACT ASSESSMENT **[REQUIRED]**

*Completed by the Product Engineering Team before approval. Every dimension must be answered, even if "No impact".*

| Dimension | Assessment |
|-----------|-----------|
| Scope impact | [What is added, removed, or altered] |
| New / changed Acceptance Criteria | [List new AC IDs, or "None"] |
| Backlog impact | [New items / changed items / removed items with IDs] |
| Work Package impact | [Which WPs change] |
| Roadmap / phase impact | [New phase needed? Sequencing change? Or "None"] |
| Cost impact | [Estimate or "None"] |
| Timeline impact | [Estimate or "None"] |
| Security / access impact | [Yes/No + detail] |
| Custom module impact | [New spec required? Spec-before-dev still satisfied?] |
| Asset classification impact | [Does this change Generic/Sector/Client classification?] |

---

## SECTION D — COVERAGE RE-VALIDATION TRIGGER **[REQUIRED]**

*A scope change post-Gate 3 can invalidate the approved Coverage Score (≥95%). Determine here whether PEG-5 Coverage Validation must be re-run.*

| Question | Answer |
|----------|--------|
| Does this change add a new Capability Area, sub-capability, approval workflow, integration, custom module, or security requirement? | [YES / NO] |
| Does this change alter an existing Acceptance Criterion? | [YES / NO] |
| **Coverage re-validation required?** | [YES — re-run PEG-5 for affected items / NO — justify below] |

**Justification if NO:**

[Explain why the approved Coverage Score remains valid without re-running PEG-5.]

**Re-validation outcome (if YES):**

| Field | Value |
|-------|-------|
| Affected items re-scored | [IDs] |
| New Coverage Score | [N%] |
| Score ≥ 95%? | [YES / NO — remediate before approval] |
| Re-validated by | [NAME, YYYY-MM-DD] |

---

## SECTION E — APPROVAL DECISION **[REQUIRED]**

### E.1 Product Owner Decision

| Field | Value |
|-------|-------|
| Decision | [Approved / Rejected / Deferred] |
| Name | [PRODUCT_OWNER_NAME] |
| Role | [ROLE] |
| Date | [YYYY-MM-DD] |
| Signature / confirmation reference | [Reference] |
| Conditions (if any) | [None / List] |

### E.2 Governance Team Confirmation *(required only when Section D triggered Coverage re-validation)*

| Field | Value |
|-------|-------|
| Coverage re-validation confirmed ≥ 95% | [YES / N/A] |
| Confirmed by | [NAME] |
| Date | [YYYY-MM-DD] |

---

## SECTION F — IMPLEMENTATION AND LEDGER **[REQUIRED]**

| Action | Status |
|--------|--------|
| Recorded in PEF_PRODUCT_APPROVAL_TEMPLATE.md Section D (same SCR ID) | [Done / Pending] |
| Product Approval document re-signed (if required by 12.3) | [Done / N/A] |
| Backlog / Work Packages / Roadmap updated | [Done / Pending] |
| Coverage Validation Report updated (if re-run) | [Done / N/A] |
| Change implemented and evidenced | [Done / Pending] |

---

*PEF_SCOPE_CHANGE_REQUEST_TEMPLATE.md v1.0 — Software Factory governance standard*
