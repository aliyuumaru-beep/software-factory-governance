# PEF_PRODUCT_SCOPE_TEMPLATE.md
## Software Factory — Product Scope Template

**Template ID:** PEF-TPL-001  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Section 5 (D-07)  
**Produced at:** PEG-3 — Product Scope Definition  
**Approved by:** Product Owner (Gate 1)

---

## INSTRUCTIONS FOR USE

Complete every section. Do not leave fields blank. Where a section does not apply, write "Not applicable — [reason]". Sections marked **[REQUIRED]** cannot be omitted.

Replace all `[PLACEHOLDER]` text with project-specific content.  
Delete these instructions before submitting for approval.

---

## DOCUMENT IDENTITY

| Field | Value |
|-------|-------|
| Project name | [PROJECT_NAME] |
| Client | [CLIENT_NAME] |
| Product type | [ERP / Web App / Mobile App / AI Solution / Workflow Automation / Other] |
| Platform | [Platform name and version — be specific, e.g. "Odoo 17 Community Edition"] |
| Product Engineering Team | [Name(s)] |
| Product Owner | [Name and role] |
| Document version | [1.0] |
| Date | [YYYY-MM-DD] |
| PEG stage | PEG-3 |
| Status | [Draft / Under Review / Approved] |

---

## SECTION 1 — EXECUTIVE SUMMARY **[REQUIRED]**

*2–4 sentences. What is being built, for whom, on what platform, and why. Do not include solution details here — this is the elevator pitch.*

[EXECUTIVE_SUMMARY]

---

## SECTION 2 — PRODUCT VISION **[REQUIRED]**

*One paragraph. The desired future state once this product is delivered. Written from the client's perspective.*

[PRODUCT_VISION]

---

## SECTION 3 — PRODUCT OBJECTIVES **[REQUIRED]**

*Numbered list of specific, measurable objectives. Each objective should correspond to one or more Capability Areas.*

| # | Objective |
|---|-----------|
| O-01 | [OBJECTIVE_1] |
| O-02 | [OBJECTIVE_2] |
| O-03 | [OBJECTIVE_3] |
| *Add rows as needed* | |

---

## SECTION 4 — MAJOR CAPABILITY AREAS **[REQUIRED]**

*List all Capability Areas. These become the master structure. Every downstream item traces back here.*

| ID | Capability Area | Departments / Domains | Status |
|----|----------------|----------------------|--------|
| CA-01 | [CAPABILITY_AREA_1] | [DEPT/DOMAIN] | In Scope |
| CA-02 | [CAPABILITY_AREA_2] | [DEPT/DOMAIN] | In Scope |
| CA-03 | [CAPABILITY_AREA_3] | [DEPT/DOMAIN] | In Scope |
| CA-XX | [CROSS_FUNCTIONAL_WORKFLOWS] | All | In Scope |
| CA-XX | [SECURITY_AND_ACCESS_CONTROL] | All | In Scope |
| *Add rows as needed* | | | |

---

## SECTION 5 — CAPABILITY DESCRIPTIONS **[REQUIRED]**

*For each Capability Area, provide: description, sub-capabilities, and implementation approach.*

---

### CA-01 — [CAPABILITY_AREA_1_NAME]

**Description:** [What this capability covers and why it is needed]

**Sub-capabilities:**
- [SUB_CAPABILITY_1] — [Classification: Native / Configuration / OCA / Custom / Future]
- [SUB_CAPABILITY_2] — [Classification]
- [SUB_CAPABILITY_3] — [Classification]

**Implementation approach:** [Modules, OCA packages, custom development — be specific]

**Platform notes:** [Any platform-specific constraints, e.g. "Native helpdesk is Enterprise-only; using OCA helpdesk_mgmt instead"]

---

### CA-02 — [CAPABILITY_AREA_2_NAME]

**Description:** [Description]

**Sub-capabilities:**
- [SUB_CAPABILITY_1] — [Classification]
- [SUB_CAPABILITY_2] — [Classification]

**Implementation approach:** [Implementation approach]

**Platform notes:** [Platform notes or "None"]

---

*[Repeat for each Capability Area]*

---

### CA-XX — Cross-functional Workflows

**Description:** Workflows and data flows that span more than one Capability Area.

**Sub-capabilities:**
- [WORKFLOW_1: e.g. Budget approval → Procurement → Finance chain]
- [WORKFLOW_2: e.g. Cross-department notifications]
- [WORKFLOW_3: e.g. Document routing between departments]

**Implementation approach:** [Approach]

---

### CA-XX — Security and Access Control

**Description:** System-wide security, role-based access control, and audit requirements.

**Sub-capabilities:**
- Role-based access rights by [department / function / seniority]
- [Authentication requirements: e.g. two-factor authentication]
- Audit trail on all business-critical records

**Implementation approach:** [Approach]

---

## SECTION 6 — ACCEPTANCE CRITERIA **[REQUIRED]**

*One or more testable acceptance criteria per Capability Area. Must meet the Quality Standard in PEF Section 11.2.*

| ID | Capability | Acceptance Criterion |
|----|-----------|---------------------|
| AC-01 | CA-01 | [TESTABLE_CRITERION_1] |
| AC-02 | CA-02 | [TESTABLE_CRITERION_2] |
| AC-03 | CA-03 | [TESTABLE_CRITERION_3] |
| *Add rows as needed* | | |

**AC writing checklist — each criterion must be:**
- [ ] Testable without interpretation
- [ ] Unambiguous (one reading only)
- [ ] Boundary-defined (specific values, not "above threshold")
- [ ] Evidence-specified (what proves it is met)
- [ ] Independent (testable alone)

---

## SECTION 7 — ASSET CLASSIFICATION **[REQUIRED]**

*Classify every significant deliverable. This feeds PEG-8 Template Extraction.*

### Generic Reusable Assets
*Applicable to any deployment of this technology, regardless of sector or client.*

- [ASSET_1: e.g. Repository governance scaffold]
- [ASSET_2: e.g. CI workflow template]
- [ASSET_3]

### Sector Reusable Assets
*Applicable to all [sector] clients. Specify the sector.*

**Sector:** [Government / NGO / Manufacturing / Other]

- [ASSET_1: e.g. Government chart of accounts structure]
- [ASSET_2: e.g. Multi-level procurement approval workflow]
- [ASSET_3]

### Client Specific Assets
*Contain client data, branding, statutory specifics, or organisational references. Do not extract.*

- [ASSET_1: e.g. Client organisational hierarchy and staff names]
- [ASSET_2: e.g. Client vendor data]
- [ASSET_3: e.g. Client-specific statutory rates]

---

## SECTION 8 — TEMPLATE EXTRACTION OPPORTUNITIES

*List items from the Generic and Sector Reusable asset lists that will be contributed to the Software Factory Template Registry at PEG-8.*

| Component | Category | Extraction method |
|-----------|---------|------------------|
| [COMPONENT_1] | [Generic Reusable / Sector Reusable] | [Strip references; parameterise thresholds; etc.] |
| [COMPONENT_2] | | |
| *Add rows as needed* | | |

---

## SECTION 9 — OUT OF SCOPE **[REQUIRED]**

*Explicit statement of what is NOT being built. This is a change-control boundary.*

The following are explicitly out of scope for this engagement:

- [OUT_OF_SCOPE_1: e.g. Infrastructure provisioning and server configuration]
- [OUT_OF_SCOPE_2: e.g. Hardware procurement]
- [OUT_OF_SCOPE_3: e.g. End-user training delivery — documentation produced, delivery is client responsibility]
- [OUT_OF_SCOPE_4: e.g. Integration with [SYSTEM] — not identified in process documentation]
- [OUT_OF_SCOPE_5]

---

## SECTION 10 — ASSUMPTIONS **[REQUIRED]**

*Each assumption is a risk if incorrect. State them explicitly.*

| # | Assumption |
|---|-----------|
| A-01 | [ASSUMPTION_1: e.g. Platform is installed and accessible at [PATH]] |
| A-02 | [ASSUMPTION_2: e.g. Client will provide master data for migration] |
| A-03 | [ASSUMPTION_3: e.g. TO-BE specifications for remaining departments will be delivered before their builds commence] |
| A-04 | [ASSUMPTION_4: e.g. All OCA modules are version-compatible with the installed platform version] |
| *Add rows as needed* | |

---

## SECTION 11 — SUCCESS CRITERIA **[REQUIRED]**

*How will we know the product has been successfully delivered?*

| # | Criterion |
|---|-----------|
| S-01 | All four PEF approval gates passed |
| S-02 | Coverage Score ≥ 95% confirmed on file |
| S-03 | All Must Have backlog items: Done with test evidence |
| S-04 | All Acceptance Criteria passed and evidenced |
| S-05 | UAT sign-off obtained from Product Owner |
| S-06 | Product deployed to production without data loss or critical failure |
| S-07 | [PROJECT_SPECIFIC_CRITERION_1] |
| S-08 | [PROJECT_SPECIFIC_CRITERION_2] |
| *Add rows as needed* | |

---

## GATE 1 — PRODUCT OWNER APPROVAL

*This section must be completed before PEG-4 begins.*

| Field | Value |
|-------|-------|
| Approved by | [PRODUCT_OWNER_NAME] |
| Role | [ROLE] |
| Date | [YYYY-MM-DD] |
| Signature | [Signature / Digital confirmation reference] |
| Conditions (if any) | [None / List conditions] |

**By signing this document, the Product Owner confirms:**
1. The Product Scope correctly represents the agreed product
2. All Capability Areas and their Acceptance Criteria are understood and agreed
3. Out of Scope items correctly describe the engagement boundary
4. Operational planning (PEG-4) may proceed on the basis of this scope

---

*PEF_PRODUCT_SCOPE_TEMPLATE.md v1.0 — Software Factory governance standard*
