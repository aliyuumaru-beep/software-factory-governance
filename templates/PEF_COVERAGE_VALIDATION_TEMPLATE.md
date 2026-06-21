# PEF_COVERAGE_VALIDATION_TEMPLATE.md
## Software Factory — Coverage Validation Template

**Template ID:** PEF-TPL-005  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Sections 6 and 7  
**Produced at:** PEG-5 — Coverage Validation  
**Approved by:** Product Engineering Team lead

---

## INSTRUCTIONS FOR USE

Coverage Validation is mandatory before development is authorised. It cannot be skipped.

**Process:**
1. Complete Sections 1–3 (document identity and inputs)
2. Complete Section 4 (Coverage Matrix) for every requirement in the Product Scope
3. Calculate the Coverage Score (Section 5)
4. Document all findings (Section 6)
5. If score < 95%: complete Section 7 (Remediation) and re-score
6. Sign the validation (Section 8)
7. Include this report in the Product Transfer Package

**Scoring:**
- 1.0 = Fully Covered (in all three operational documents with traceable AC)
- 0.5 = Partially Covered (in some documents but not all)
- 0.0 = Omission (absent from one or more documents)

Apply weighting (from PEF Section 7.3):
- Capability Areas: 1.0×
- Approval Workflows: 1.5×
- Integrations: 1.5×
- Custom Module Specs: 2.0×
- Security and Access: 2.0×
- Dashboards/Reports: 0.75×
- Deferred Items: 0.5×

Replace all `[PLACEHOLDER]` text. Delete these instructions before issuing.

---

## SECTION 1 — DOCUMENT IDENTITY

| Field | Value |
|-------|-------|
| Project name | [PROJECT_NAME] |
| Client | [CLIENT_NAME] |
| Validated by | [VALIDATOR_NAME] — Product Engineering Team |
| Date of validation | [YYYY-MM-DD] |
| Version | [1.0] |
| Documents validated | Product Scope v[X], Roadmap v[X], Backlog v[X], Work Packages v[X] |

---

## SECTION 2 — VALIDATION INPUTS

| Input | Document | Date / Version | Status |
|-------|---------|----------------|--------|
| Product Scope | PEF_PRODUCT_SCOPE_TEMPLATE.md | [VERSION — APPROVED DATE] | ✅ Approved |
| Roadmap | PEF_ROADMAP_TEMPLATE.md | [VERSION] | ✅ Complete |
| Backlog | PEF_BACKLOG_TEMPLATE.md | [VERSION] | ✅ Complete |
| Work Packages | PEF_WORK_PACKAGE_TEMPLATE.md | [VERSION] | ✅ Complete |

---

## SECTION 3 — VALIDATION METHOD

All validation was performed by direct comparison of the Product Scope against each operational document. Items were verified by keyword search and structural inspection. An item was not considered covered unless it was found explicitly — coverage was not assumed.

---

## SECTION 4 — COVERAGE MATRIX

### KEY
✅ Fully Covered (score: 1.0)  
⚠️ Partially Covered (score: 0.5) — gap noted  
❌ Omission (score: 0.0) — not present

---

### 4.1 Capability Areas (Weight: 1.0×)

| Capability Area | TP/Scope Ref | In Roadmap? | In Backlog? | In Work Packages? | Score | Notes |
|----------------|-------------|-------------|-------------|------------------|-------|-------|
| CA-01: [NAME] | Section [N] | ✅ Phase [N] | ✅ [BL-IDs] | ✅ [WP-IDs] | 1.0 | |
| CA-02: [NAME] | Section [N] | ✅ | ✅ | ✅ | 1.0 | |
| CA-03: [NAME] | Section [N] | ✅ | ⚠️ Sub-capability X missing dedicated item | ✅ | 0.5 | Sub-capability X folded into CA-02 item — omission |
| CA-XX: Cross-functional | Section [N] | ✅ | ✅ | ⚠️ Document routing WP not present | 0.5 | WP-XFN-02 absent |
| CA-XX: Security | Section [N] | ✅ | ✅ | ✅ | 1.0 | |
| *Add rows for all CAs* | | | | | | |

**CA subtotal:** [SUM of scores] / [COUNT] × 1.0 = [WEIGHTED_SUBTOTAL]

---

### 4.2 Sub-capabilities (Weight: 1.0×)

*List sub-capabilities that require individual verification — particularly those at risk of being folded into parent CA items.*

| Sub-Capability | Parent CA | In Backlog? | In WP Scope? | Score | Notes |
|----------------|----------|-------------|-------------|-------|-------|
| [SUB_CAP_1] | CA-01 | ✅ BL-[ID] | ✅ WP-[ID] scope | 1.0 | |
| [SUB_CAP_2] | CA-01 | ⚠️ Folded into BL-[ID] — not dedicated | ✅ Named in WP scope | 0.5 | Backlog item needed |
| [SUB_CAP_3] | CA-02 | ❌ Not present | ❌ Not present | 0.0 | **OMISSION** |
| *Add rows for all sub-caps requiring individual check* | | | | | |

**Sub-capability subtotal:** [WEIGHTED_SUBTOTAL]

---

### 4.3 Approval Workflows (Weight: 1.5×)

| Approval Type | Scope Ref | Dedicated BL item? | In WP scope? | Score | Weighted | Notes |
|--------------|----------|-------------------|-------------|-------|---------|-------|
| [APPROVAL_1: e.g. Procurement requisition] | Section 4 | ✅ BL-[ID] | ✅ WP-[ID] | 1.0 | 1.5 | |
| [APPROVAL_2: e.g. Finance payment] | Section 4 | ✅ BL-[ID] | ⚠️ Not explicit in WP scope | 0.5 | 0.75 | Add to WP scope |
| [APPROVAL_3: e.g. HR appointment] | Section 4 | ❌ No dedicated item | ❌ | 0.0 | 0.0 | **OMISSION — HIGH RISK** |
| *Add all approval types* | | | | | | |

**Approval workflow subtotal (weighted):** [SUM of weighted scores] / [COUNT × 1.5] = [WEIGHTED_SUBTOTAL]

---

### 4.4 Integrations (Weight: 1.5×)

| Integration | Scope Ref | Config BL item (Ph3)? | Test BL item (Ph4)? | In WP scope? | Score | Weighted | Notes |
|------------|----------|----------------------|--------------------|-----------|----|---------|-------|
| [INT_1: e.g. Budget → Procurement → Finance] | CA-XFN | ✅ BL-[ID] | ✅ BL-[ID] | ✅ WP-INT-01 | 1.0 | 1.5 | |
| [INT_2: e.g. Cross-dept notifications] | CA-XFN | ✅ BL-[ID] | ✅ BL-[ID] | ✅ WP-XFN-01 | 1.0 | 1.5 | |
| [INT_3: e.g. Document routing] | CA-XFN | ❌ No config item | ❌ No test item | ❌ | 0.0 | 0.0 | **OMISSION** |
| *Add all integrations* | | | | | | | |

**Integration subtotal (weighted):** [WEIGHTED_SUBTOTAL]

---

### 4.5 Custom Module Specifications (Weight: 2.0×)

| Module | Scope Ref | SPEC BL item? | DEV BL item? | SPEC before DEV? | WP-SPEC? | WP-DEV? | Score | Weighted | Notes |
|--------|----------|--------------|-------------|-----------------|---------|--------|-------|---------|-------|
| `[module_1]` | Section 5 | ✅ BL-SPEC-01 | ✅ BL-DEV-01 | ✅ | ✅ WP-SPEC-01 | ✅ WP-DEV-01 | 1.0 | 2.0 | |
| `[module_2]` | Section 5 | ✅ BL-SPEC-02 | ✅ BL-DEV-02 | ✅ | ✅ WP-SPEC-02 | ❌ No WP-DEV | 0.5 | 1.0 | WP-DEV-02 missing |
| `[module_3]` | Section 5 | ❌ No SPEC | ❌ No DEV | N/A | ❌ | ❌ | 0.0 | 0.0 | **CRITICAL OMISSION** |
| *Add all custom modules* | | | | | | | | | |

**Custom module spec subtotal (weighted):** [WEIGHTED_SUBTOTAL]

---

### 4.6 Dashboards and Reports (Weight: 0.75×)

| Dashboard / Report | Scope Ref | BL item? | WP scope? | Score | Weighted | Notes |
|-------------------|----------|---------|-----------|-------|---------|-------|
| [DASHBOARD_1: e.g. Executive financial KPI] | CA-01 | ✅ BL-[ID] | ✅ WP-[ID] | 1.0 | 0.75 | |
| [DASHBOARD_2: e.g. M&E indicator dashboard] | CA-11 | ⚠️ Implied in BL-ME-01 | ⚠️ Not isolated in WP | 0.5 | 0.375 | Consolidate AC needed |
| *Add all dashboards* | | | | | | |

**Dashboard subtotal (weighted):** [WEIGHTED_SUBTOTAL]

---

### 4.7 Security and Access Control (Weight: 2.0×)

| Requirement | Scope Ref | BL item? | WP scope? | Score | Weighted | Notes |
|------------|----------|---------|-----------|-------|---------|-------|
| [CA-01] user groups and access rights | CA-XX Security | ✅ BL-[CODE]-04 | ✅ WP-[CODE]-01 | 1.0 | 2.0 | |
| Two-factor authentication | CA-XX Security | ✅ BL-[ID] | ✅ WP-[ID] | 1.0 | 2.0 | |
| Audit trail on all records | CA-XX Security | ✅ BL-[IDs] | ✅ WP-[IDs] | 1.0 | 2.0 | |
| Session rules committed to repo | CA-XX Security | ✅ BL-GOV-08 | ✅ WP-GOV-02 | 1.0 | 2.0 | |
| *Add all security requirements* | | | | | | |

**Security subtotal (weighted):** [WEIGHTED_SUBTOTAL]

---

### 4.8 Deferred Items (Weight: 0.5×)

| Item | Scope Ref | In Backlog as Deferred? | Score | Weighted | Notes |
|------|----------|------------------------|-------|---------|-------|
| [DEFERRED_1: e.g. Performance management] | CA-03 | ✅ BL-HR-06 — Deferred/CH | 1.0 | 0.5 | Present with correct status |
| [DEFERRED_2] | [CA] | ❌ Absent — not marked Deferred | 0.0 | 0.0 | **Must be added as Deferred** |
| *Add all deferred items* | | | | | |

**Deferred subtotal (weighted):** [WEIGHTED_SUBTOTAL]

---

## SECTION 5 — COVERAGE SCORE CALCULATION

| Category | Raw items | Weight | Weighted denom | Sum of weighted scores | Weighted achieved |
|----------|-----------|--------|----------------|----------------------|------------------|
| Capability Areas | [N] | 1.0× | [N × 1.0] | [SUM] | [ACHIEVED] |
| Sub-capabilities | [N] | 1.0× | [N × 1.0] | [SUM] | [ACHIEVED] |
| Approval Workflows | [N] | 1.5× | [N × 1.5] | [SUM] | [ACHIEVED] |
| Integrations | [N] | 1.5× | [N × 1.5] | [SUM] | [ACHIEVED] |
| Custom Module Specs | [N] | 2.0× | [N × 2.0] | [SUM] | [ACHIEVED] |
| Dashboards/Reports | [N] | 0.75× | [N × 0.75] | [SUM] | [ACHIEVED] |
| Security/Access | [N] | 2.0× | [N × 2.0] | [SUM] | [ACHIEVED] |
| Deferred Items | [N] | 0.5× | [N × 0.5] | [SUM] | [ACHIEVED] |
| **TOTAL** | | | **[TOTAL_DENOM]** | | **[TOTAL_ACHIEVED]** |

**Coverage Score = [TOTAL_ACHIEVED] / [TOTAL_DENOM] × 100 = [SCORE]%**

**Tier:** [Exemplary (98–100%) / Acceptable (95–97%) / Remediation Required (90–94%) / Failed (<90%)]

**Proceed to PEG-6?** [YES — score ≥ 95% / NO — remediation required]

---

## SECTION 6 — FINDINGS

### 6.1 Omissions
*Items present in Product Scope but absent from one or more operational documents.*

| # | Item | Category | Missing from | Risk | Recommended action |
|---|------|---------|------------|------|-------------------|
| O-01 | [OMISSION_DESCRIPTION] | [Category] | [Backlog / WP / Roadmap] | [High / Medium / Low] | [Specific action to close] |
| O-02 | | | | | |
| *Add rows as needed* | | | | | |

### 6.2 Scope Reductions
*Items where operational documents cover a requirement more narrowly than the Product Scope defines it.*

| # | Item | Scope says | Documents show | Risk | Resolution |
|---|------|-----------|---------------|------|-----------|
| SR-01 | [SCOPE_REDUCTION_DESCRIPTION] | [What scope defines] | [What documents show] | [Risk] | [Resolution — Product Owner accept or close gap] |
| *Add rows as needed* | | | | | |

### 6.3 Partial Coverage Observations
*Items scored 0.5 — present but not fully covered.*

| # | Item | Partial coverage description | Action required |
|---|------|---------------------------|----------------|
| PC-01 | [DESCRIPTION] | [Where coverage is partial and why] | [Action to achieve 1.0] |
| *Add rows as needed* | | | |

---

## SECTION 7 — REMEDIATION (if score < 95%)

### 7.1 Remediation Actions

| Finding ID | Action | Assigned to | Target date | Status |
|-----------|--------|------------|------------|--------|
| O-01 | [SPECIFIC_ACTION: e.g. Add BL-HR-06 to Backlog as Deferred/CH] | [NAME] | [DATE] | [Not Started / Complete] |
| SR-01 | [ACTION] | | | |
| *Add rows as needed* | | | | |

### 7.2 Remediation Principles
- Preserve all existing IDs; assign new IDs sequentially
- Do not modify Roadmap or Project State unless a new phase is genuinely required
- After remediation, re-run coverage check on all changed items only
- Do not re-validate unchanged items

### 7.3 Re-score (after remediation)

*Complete this table after all remediation actions are done.*

| Category | Pre-remediation score | Post-remediation score | Change |
|----------|-----------------------|----------------------|--------|
| Capability Areas | [%] | [%] | [+/-] |
| Approval Workflows | [%] | [%] | [+/-] |
| *etc.* | | | |
| **OVERALL** | **[PRE_%]** | **[POST_%]** | |

**Post-remediation Coverage Score: [SCORE]%**  
**Tier: [TIER]**  
**Proceed to PEG-6? [YES / NO]**

---

## SECTION 8 — VALIDATION SIGN-OFF

| Field | Value |
|-------|-------|
| Coverage Score | [FINAL_SCORE]% |
| Tier | [TIER] |
| Pre-remediation score (if applicable) | [PRE_SCORE]% |
| All omissions resolved? | [YES / NO — list outstanding] |
| All scope reductions: accepted or resolved? | [YES / NO — list outstanding] |
| Remediation performed? | [YES / NO] |
| Validated by | [NAME], Product Engineering Team |
| Signature / confirmation | [Signature / Digital confirmation] |
| Date | [YYYY-MM-DD] |

**Recommendation:** [PROCEED to PEG-6 / REMEDIATION REQUIRED before PEG-6]

---

*PEF_COVERAGE_VALIDATION_TEMPLATE.md v1.0 — Software Factory governance standard*
