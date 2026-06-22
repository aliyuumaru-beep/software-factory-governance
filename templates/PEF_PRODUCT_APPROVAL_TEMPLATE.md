# PEF_PRODUCT_APPROVAL_TEMPLATE.md
## Software Factory — Product Approval Template

**Template ID:** PEF-TPL-006  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Section 5 (D-15) and Section 12  
**Produced at:** PEG-6 — Development Authorisation  
**Approved by:** Product Owner AND Governance Team (both signatures required)

---

## INSTRUCTIONS FOR USE

This document is the formal authorisation for development to begin. It is the hardest gate in the PEF. Both the Product Owner and the Governance Team must sign before the development team executes a single line of implementation code.

This document is also used at PEG-3 (Section A only — scope approval) to authorise operational planning.

**Completion sequence:**
1. Section A — complete and sign at end of PEG-3 (scope approval)
2. Sections B through E — complete at PEG-6 (development authorisation)
3. Section F — complete at PEG-7 (deployment authorisation)

Replace all `[PLACEHOLDER]` text. Delete these instructions before issuing.

---

## DOCUMENT IDENTITY

| Field | Value |
|-------|-------|
| Project name | [PROJECT_NAME] |
| Client | [CLIENT_NAME] |
| Document reference | [PA-YYYY-MM-DD-001] |
| Version | [1.0] |
| Date | [YYYY-MM-DD] |

---

## SECTION A — PRODUCT SCOPE APPROVAL (Gate 1 — PEG-3)

*Authorises operational planning to begin. Does NOT authorise development.*

### A.1 Scope Declaration

The undersigned confirms that:

1. The Product Scope document ([PRODUCT_SCOPE_DOCUMENT_REF], version [X], dated [DATE]) correctly represents the agreed product
2. All [N] Capability Areas and their Acceptance Criteria are understood and agreed
3. The Out of Scope section correctly describes the engagement boundary
4. The Asset Classification correctly identifies Generic Reusable, Sector Reusable, and Client Specific assets
5. Operational planning (PEG-4: Roadmap, Backlog, Work Packages) may proceed on the basis of this scope

### A.2 Scope Summary

| Item | Count |
|------|-------|
| Total Capability Areas | [N] |
| Total sub-capabilities | [N] |
| Custom modules required | [N] |
| Solution type | [ERP / Web App / Mobile App / AI / Workflow / Other] |
| Platform | [PLATFORM_AND_VERSION] |

### A.3 Gate 1 Signature — Product Owner

| Field | Value |
|-------|-------|
| Name | [PRODUCT_OWNER_NAME] |
| Role | [ROLE] |
| Organisation | [CLIENT_ORGANISATION] |
| Date | [YYYY-MM-DD] |
| Signature | [Signature / Digital confirmation reference] |

**By signing, the Product Owner authorises operational planning to proceed and confirms the scope is correct as stated.**

---

## SECTION B — PRE-AUTHORISATION CHECKLIST (PEG-6)

*Completed by the Product Engineering Team before presenting for signature.*

### B.1 PEF Lifecycle Checklist

| Stage | Exit Criteria Met? | Evidence |
|-------|-------------------|---------|
| PEG-1 Requirements Consolidation | ✅ / ❌ | [Document reference] |
| PEG-2 Capability Mapping | ✅ / ❌ | [Document reference] |
| PEG-3 Product Scope — approved (Section A above) | ✅ / ❌ | [Date of signature] |
| PEG-4 Operational Planning — Roadmap, Backlog, WPs complete | ✅ / ❌ | [Document references and versions] |
| PEG-5 Coverage Validation — score ≥ 95% | ✅ / ❌ | [Score: [N]%; Report: [REPORT_REF]] |
| PEG-5R Remediation (if required) — re-score ≥ 95% | ✅ / ❌ / N/A | [Post-remediation score if applicable] |

### B.2 Coverage Score Summary

| Field | Value |
|-------|-------|
| Final Coverage Score | [SCORE]% |
| Coverage Tier | [Exemplary / Acceptable / —] |
| Omissions resolved | [N resolved / 0 outstanding] |
| Scope reductions: accepted or resolved | [N accepted by Product Owner / N resolved] |
| Validated by | [NAME], [DATE] |

### B.3 Governance Activation Gate Summary

| Gate | Result | Notes |
|------|--------|-------|
| Gate A — Repository | PASS / FAIL | |
| Gate B — CI/CD | PASS / FAIL | |
| Gate C — Governance Documents | PASS / FAIL | |
| Gate D — Backup | PASS / FAIL | |
| Gate E — Product Readiness | PASS / FAIL | |
| **Overall** | **PASS / FAIL** | [N]/[TOTAL] checks passing |

Gate Report reference: [REPORT_DOCUMENT_REF]

### B.4 Product Transfer Package Checklist

| Item | Present? |
|------|---------|
| Product Transfer Document | ✅ / ❌ |
| NEXT_ACTION.md | ✅ / ❌ |
| Product Scope (signed) | ✅ / ❌ |
| Roadmap | ✅ / ❌ |
| Backlog | ✅ / ❌ |
| Work Packages | ✅ / ❌ |
| Coverage Validation Report (score ≥ 95%) | ✅ / ❌ |
| Governance Gate Report (all PASS) | ✅ / ❌ |
| Repository Scaffold | ✅ / ❌ |

All items must be ✅ before Gate 3 signatures are requested.

---

## SECTION C — DEVELOPMENT SCOPE DECLARATION

*A concise restatement of what is authorised for development.*

### C.1 Authorised Platform

| Field | Value |
|-------|-------|
| Platform | [PLATFORM] |
| Version | [VERSION] |
| Edition | [e.g. Community Edition / Enterprise Edition / Open Source] |
| Prohibited features | [LIST any features/modules explicitly excluded, e.g. "Enterprise Approvals module — not available"] |

### C.2 Authorised Build Scope

| # | Capability Area | Must Have items | Should Have items | Custom modules |
|---|----------------|-----------------|------------------|----------------|
| 1 | CA-01: [NAME] | [N] | [N] | [None / module names] |
| 2 | CA-02: [NAME] | [N] | [N] | [None / module names] |
| *etc.* | | | | |
| | **TOTALS** | **[N] MH items** | **[N] SH items** | **[N] custom modules** |

### C.3 Development Boundaries

Development is authorised to proceed **within the following boundaries only:**

1. Platform: [PLATFORM_AND_VERSION] — no other platform or version may be used
2. Scope: All Must Have items in the approved Backlog ([BACKLOG_REF])
3. Custom modules: [LIST] only — no additional custom modules without Product Owner approval
4. Changes to scope require a new Section D amendment signed by the Product Owner
5. The development team may not alter the Product Scope, Roadmap, or Backlog without Product Owner approval

---

## SECTION D — SCOPE CHANGE REGISTER

*Any scope change after Gate 3 signature must be recorded here with Product Owner approval.*

| Change ID | Date | Description | Impact | Approved by | New AC? |
|-----------|------|-------------|--------|------------|---------|
| SCR-001 | [DATE] | [CHANGE_DESCRIPTION] | [Impact on cost/timeline/scope] | [PRODUCT_OWNER_NAME, DATE] | [YES/NO] |
| *Add rows as needed* | | | | | |

*No change is authorised unless this table is updated and a new Product Owner signature is obtained in the margin or as an addendum.*

---

## SECTION E — GATE 3 SIGNATURES — DEVELOPMENT AUTHORISATION (PEG-6)

### E.1 Product Owner Authorisation

*By signing below, the Product Owner authorises the Software Development Team to begin implementation against the approved Product Transfer Package.*

| Field | Value |
|-------|-------|
| Name | [PRODUCT_OWNER_NAME] |
| Role | [ROLE] |
| Organisation | [CLIENT_ORGANISATION] |
| Date | [YYYY-MM-DD] |
| Signature | [Signature / Digital confirmation reference] |

**Conditions of authorisation (if any):**
[None / List any conditions]

---

### E.2 Governance Team Confirmation

*By signing below, the Governance Team confirms that all PEF lifecycle requirements have been met and the Governance Activation Gate has passed.*

| Field | Value |
|-------|-------|
| Name | [GOVERNANCE_TEAM_REPRESENTATIVE] |
| Role | Software Factory Governance Team |
| Date | [YYYY-MM-DD] |
| Signature | [Signature / Digital confirmation reference] |
| Gate result | PASS — [N]/[TOTAL] checks passing |

---

### E.3 Product Engineering Team Confirmation

*By signing below, the Product Engineering Team confirms the Transfer Package is complete and accurate.*

| Field | Value |
|-------|-------|
| Name | [PET_LEAD_NAME] |
| Role | Product Engineering Team Lead |
| Date | [YYYY-MM-DD] |
| Signature | [Signature / Digital confirmation reference] |

---

## SECTION F — GATE 4 — DEPLOYMENT AUTHORISATION (PEG-7)

*Completed after UAT sign-off. Authorises production deployment.*

### F.1 UAT Summary

| Field | Value |
|-------|-------|
| UAT completion date | [DATE] |
| Total test cases executed | [N] |
| Total defects logged | [N] |
| Critical defects open | [N] — must be zero |
| High defects open | [N] — must be zero, or formally deferred with acceptance below |
| Deferred defects accepted | [List if any — Product Owner must sign against each] |

### F.2 Deployment Confirmation

| Field | Value |
|-------|-------|
| Target production environment | [ENVIRONMENT_DESCRIPTION] |
| Cutover date | [YYYY-MM-DD] |
| Cutover plan reference | [DOCUMENT_REF] |
| Data migration plan reference | [DOCUMENT_REF] |
| Rollback plan reference | [DOCUMENT_REF] |

### F.3 Gate 4 Signatures — Deployment Authorisation

**Product Owner:**

| Field | Value |
|-------|-------|
| Name | [PRODUCT_OWNER_NAME] |
| Date | [YYYY-MM-DD] |
| Signature | [Signature] |
| UAT sign-off reference | [UAT_DOCUMENT_REF] |

**QA Team:**

| Field | Value |
|-------|-------|
| Name | [QA_LEAD_NAME] |
| Date | [YYYY-MM-DD] |
| Signature | [Signature] |
| Defect certification | All Critical defects resolved; all High defects resolved or accepted above |

---

## SECTION G — POST-DEPLOYMENT RECORD

*Completed after production go-live.*

| Field | Value |
|-------|-------|
| Go-live date | [YYYY-MM-DD] |
| Go-live status | [Successful / Partial / Failed — describe] |
| Critical issues at go-live | [None / Describe] |
| Hypercare period | [START_DATE] to [END_DATE] |
| Repository tag | `v1.0-go-live` confirmed committed: [YES / NO] |
| Template extraction initiated | [YES / NO — date] |

---

*PEF_PRODUCT_APPROVAL_TEMPLATE.md v1.0 — Software Factory governance standard*  
*This document must be retained permanently as part of the engagement record.*
