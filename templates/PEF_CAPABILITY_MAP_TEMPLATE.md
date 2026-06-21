# PEF_CAPABILITY_MAP_TEMPLATE.md
## Software Factory — Capability Map Template

**Template ID:** PEF-TPL-008  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Section 5 (D-03); PEG-2 — Capability Mapping  
**Produced at:** PEG-2 — Capability Mapping  
**Approved by:** Product Engineering Team

---

## INSTRUCTIONS FOR USE

The Capability Map is the **master product structure**. Every downstream deliverable — Product Scope, Backlog, Work Packages, and the Coverage Validation check sequence — traces back to this document. Producing it in a consistent structure is therefore mandatory (PEF Section 5; closes WEK-02).

Complete every section. Sections marked **[REQUIRED]** cannot be omitted.

**Classification rule (PEG-2 governance):** Every sub-capability must be classified as exactly one of **Native / Configuration / OCA / Custom Module / Future Phase**. `TBD` is **not** a valid classification — it is an open item that must be resolved before PEG-2 exits.

Replace all `[PLACEHOLDER]` text with project-specific content.  
Delete these instructions before submitting for review.

---

## DOCUMENT IDENTITY

| Field | Value |
|-------|-------|
| Project name | [PROJECT_NAME] |
| Client | [CLIENT_NAME] |
| Platform | [Platform name and version — be specific, e.g. "Odoo 17 Community Edition"] |
| Product Engineering Team | [Name(s)] |
| Document version | [1.0] |
| Date | [YYYY-MM-DD] |
| PEG stage | PEG-2 |
| Status | [Draft / Under Review / Approved] |

---

## SECTION 1 — CAPABILITY MAP SUMMARY **[REQUIRED]**

| Metric | Count |
|--------|-------|
| Capability Areas (CA) | [N] |
| Sub-capabilities | [N] |
| Classified: Native | [N] |
| Classified: Configuration | [N] |
| Classified: OCA | [N] |
| Classified: Custom Module | [N] |
| Classified: Future Phase | [N] |
| Unclassified (must be 0 to exit PEG-2) | [N] |

---

## SECTION 2 — CAPABILITY AREA INDEX **[REQUIRED]**

*One or more Capability Areas per department/domain. These IDs are the spine of the entire programme.*

| CA ID | Capability Area | Department / Domain | Source process(es) | Status |
|-------|----------------|--------------------|--------------------|--------|
| CA-01 | [CAPABILITY_AREA_1] | [DEPT/DOMAIN] | [TO-BE process ref] | In Scope |
| CA-02 | [CAPABILITY_AREA_2] | [DEPT/DOMAIN] | [TO-BE process ref] | In Scope |
| CA-XX | Cross-functional Workflows | All | [refs] | In Scope |
| CA-XX | Security and Access Control | All | [refs] | In Scope |
| *Add rows as needed* | | | | |

---

## SECTION 3 — SUB-CAPABILITY MAP **[REQUIRED]**

*The core of the document. Decompose every Capability Area into implementation-level sub-capabilities and classify each. Every in-scope process must map to at least one sub-capability.*

### CA-01 — [CAPABILITY_AREA_1_NAME]

| Sub-cap ID | Sub-capability | Classification | Implementation approach | Notes / platform constraint |
|-----------|---------------|----------------|------------------------|----------------------------|
| SC-01.1 | [SUB_CAPABILITY] | [Native/Configuration/OCA/Custom Module/Future Phase] | [Module / OCA package / custom dev] | [e.g. "Native helpdesk is Enterprise-only; using OCA helpdesk_mgmt"] |
| SC-01.2 | [SUB_CAPABILITY] | [Classification] | [Approach] | [Notes] |
| *Add rows as needed* | | | | |

### CA-02 — [CAPABILITY_AREA_2_NAME]

| Sub-cap ID | Sub-capability | Classification | Implementation approach | Notes / platform constraint |
|-----------|---------------|----------------|------------------------|----------------------------|
| SC-02.1 | [SUB_CAPABILITY] | [Classification] | [Approach] | [Notes] |
| *Add rows as needed* | | | | |

*[Repeat one table per Capability Area, including Cross-functional Workflows and Security and Access Control.]*

---

## SECTION 4 — APPROVAL WORKFLOWS **[REQUIRED]**

*Feeds the Approval Framework (D-04). Each approval workflow must later receive its own dedicated backlog item (CVR-03) — never folded into a parent capability.*

| Approval ID | Approval workflow | Related CA | Trigger / boundary | Implementation approach |
|-------------|-------------------|-----------|--------------------|-----------------------| 
| AP-01 | [e.g. Procurement approval above ₦500,000] | [CA-xx] | [Specific threshold/condition] | [Native workflow / OCA / custom] |
| *Add rows as needed* | | | | |

---

## SECTION 5 — INTEGRATIONS AND CROSS-FUNCTIONAL FLOWS **[REQUIRED]**

*Feeds the Integration Map (D-05). Each integration must later receive its own dedicated backlog item (CVR-04).*

| Integration ID | Integration / cross-functional flow | From → To | Implementation approach |
|----------------|-------------------------------------|-----------|------------------------|
| INT-01 | [e.g. Budget approval → Procurement → Finance] | [CA-xx → CA-yy] | [Approach] |
| *Add rows as needed* | | | |

---

## SECTION 6 — CUSTOM MODULE REGISTER **[REQUIRED]**

*Feeds D-06. A custom module may be proposed only when neither a Native, Configuration, nor OCA option closes the gap. Each custom module must be justified — none may be added without justification (PEG-2 exit criterion).*

| Module ID | Proposed module | Related sub-cap(s) | Enterprise Gap Protocol justification | Spec required? |
|-----------|-----------------|--------------------|--------------------------------------|----------------|
| CM-01 | [module_technical_name] | [SC-xx.y] | [Enterprise feature normally serving this → Community native alt → OCA alt → why custom is required] | Yes |
| *Add rows as needed* | | | | |

---

## SECTION 7 — DASHBOARDS AND REPORTING **[REQUIRED]**

*Each reporting requirement must later receive its own dedicated backlog item.*

| Report ID | Dashboard / report | Related CA | Audience | Implementation approach |
|-----------|--------------------|-----------|----------|------------------------|
| RP-01 | [REPORT_NAME] | [CA-xx] | [Role] | [Native reporting / OCA / custom] |
| *Add rows as needed* | | | | |

---

## SECTION 8 — SECURITY AND ACCESS CONTROL **[REQUIRED]**

| Sec ID | Requirement | Related CA | Implementation approach |
|--------|------------|-----------|------------------------|
| SEC-01 | [e.g. Role-based access by department and seniority] | All | [Approach] |
| SEC-02 | [e.g. Audit trail on business-critical records] | All | [Approach] |
| *Add rows as needed* | | | |

---

## SECTION 9 — ENTERPRISE GAP PROTOCOL LOG (ERP projects) **[REQUIRED for ERP]**

*Record every point where an Enterprise feature would normally serve a requirement, the Community/OCA alternative chosen, and the decision. For non-ERP projects, write "Not applicable — non-ERP engagement".*

| Gap ID | Enterprise feature | Community native alternative | OCA alternative | Decision |
|--------|--------------------|------------------------------|-----------------|----------|
| EG-01 | [FEATURE] | [Native alt or "none"] | [OCA module or "none"] | [Use native / Use OCA / Custom (justified in §6)] |
| *Add rows as needed* | | | | |

---

## SECTION 10 — PEG-2 EXIT CHECKLIST **[REQUIRED]**

- [ ] Every in-scope process maps to at least one sub-capability
- [ ] Every sub-capability classified (zero unclassified / zero TBD)
- [ ] All approval workflows identified with implementation approach
- [ ] All integrations identified
- [ ] All custom modules justified via the Enterprise Gap Protocol
- [ ] Dashboards and reporting requirements captured
- [ ] Security and access control requirements captured

| Field | Value |
|-------|-------|
| Capability Map approved by (PET) | [NAME] |
| Date | [YYYY-MM-DD] |

---

*PEF_CAPABILITY_MAP_TEMPLATE.md v1.0 — Software Factory governance standard*
