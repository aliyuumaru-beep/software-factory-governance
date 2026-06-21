# PEF_BACKLOG_TEMPLATE.md
## Software Factory — Backlog Template

**Template ID:** PEF-TPL-003  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Section 5 (D-10)  
**Produced at:** PEG-4 — Operational Planning  
**Approved by:** Product Engineering Team

---

## INSTRUCTIONS FOR USE

Every Capability Area, sub-capability, approval workflow, integration, dashboard, custom module (spec and dev), and security requirement from the Product Scope must produce at least one backlog item.

**ID format:** `BL-[AREA]-[NN]`  
Examples: `BL-GOV-01`, `BL-FIN-01`, `BL-PROC-01`, `BL-CUSTOM-01`, `BL-INT-01`

**Area codes (adapt to project):**
- `GOV` — Governance and platform setup
- `OCA` / `PKG` — Package/module installation
- `[DEPT_CODE]` — One code per department or capability area (e.g. FIN, PROC, HR, ADM)
- `SPEC` — Custom module specifications
- `DEV` — Custom module development
- `INT` — Integrations
- `UAT` — Testing
- `TRN` — Training
- `DEP` — Deployment
- `TPL` — Template extraction

**Priority:** Must Have (MH) / Should Have (SH) / Could Have (CH)  
**Status:** Not Started / In Progress / Blocked / Done / Deferred

Replace all `[PLACEHOLDER]` text. Delete these instructions before issuing.

---

## DOCUMENT IDENTITY

| Field | Value |
|-------|-------|
| Project name | [PROJECT_NAME] |
| Client | [CLIENT_NAME] |
| Document version | [1.0] |
| Date | [YYYY-MM-DD] |
| Authority | Approved Product Scope — [DATE] |
| Update rule | Status updated after every session. No item marked Done without verified AC. |

---

## PRIORITY CLASSIFICATION

- **Must Have (MH):** Required for go-live; programme fails without it
- **Should Have (SH):** Important but go-live possible with workaround; must be delivered post-go-live if deferred
- **Could Have (CH):** Desirable enhancement; may be deferred beyond current programme scope

## STATUS VALUES

`Not Started` | `In Progress` | `Blocked` | `Done` | `Deferred`

---

## PHASE 0 — GOVERNANCE ACTIVATION

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-GOV-01 | Repository discovery and audit | Security | MH | 0 | Not Started | Repo access | D-P0.1 |
| BL-GOV-02 | Platform version and prohibited module audit | Security | MH | 0 | Not Started | Platform access | D-P0.5 |
| BL-GOV-03 | Governance Activation Gate — all five checks | Security | MH | 0 | Not Started | BL-GOV-01, BL-GOV-02 | D-P0.2 |
| BL-GOV-04 | Product Memory System scaffold committed to main | Security | MH | 0 | Not Started | BL-GOV-03 | D-P0.4 |
| BL-GOV-05 | Backup strategy documented and verified | Security | MH | 0 | Not Started | Platform access | D-P0.3 |
| BL-GOV-06 | Branch protection and CI workflow active | Security | MH | 0 | Not Started | Repo access | D-P0.2 |
| BL-GOV-07 | Platform confirmation logged in Decision Log | Security | MH | 0 | Not Started | BL-GOV-02 | D-P0.5 |
| BL-GOV-08 | Session start/end rules committed to PRODUCT_STATE_INDEX | Security | MH | 0 | Not Started | BL-GOV-04 | D-P0.4 |
| *Add project-specific governance items* | | | | | | | |

---

## PHASE 1 — FOUNDATION

### [CA-01: CAPABILITY_AREA_1_NAME]

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-[CODE]-01 | [SUB_CAPABILITY_1 implementation item] | CA-01 | MH | 1 | Not Started | Phase 0 complete | AC-01 |
| BL-[CODE]-02 | [SUB_CAPABILITY_2 implementation item] | CA-01 | MH | 1 | Not Started | BL-[CODE]-01 | AC-01 |
| BL-[CODE]-03 | [APPROVAL_WORKFLOW item — dedicated, not folded into above] | CA-01 | MH | 1 | Not Started | BL-[CODE]-02 | AC-01 |
| BL-[CODE]-04 | Configure [CA-01] user groups and access rights | Security | MH | 1 | Not Started | Phase 0 complete | AC-[SECURITY_ID] |
| BL-[CODE]-05 | Verify audit trail on [CA-01] records | Security | MH | 1 | Not Started | BL-[CODE]-01 | AC-[SECURITY_ID] |
| *Add items as needed* | | | | | | | |

*Note: Add a sub-section like this for every Capability Area in Phase 1*

---

### Package / Module Installation (Phase 1)

*All external packages/modules installed in Phase 1 get their own backlog items.*

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-PKG-01 | Install and version-pin [PACKAGE_1] | [CA] | MH | 1 | Not Started | Phase 0 complete | [AC] |
| BL-PKG-02 | Install and version-pin [PACKAGE_2] | [CA] | MH | 1 | Not Started | Phase 0 complete | [AC] |
| BL-PKG-03 | Log all package installations in Decision Log | Security | MH | 1 | Not Started | BL-PKG-01 onwards | — |
| *Add items as needed* | | | | | | | |

---

## PHASE 2 — [EXTENDED_CAPABILITIES] / CUSTOM MODULE SPECIFICATIONS

*Specification items must always precede development items. This is enforced by phase and dependency.*

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-SPEC-01 | Draft and approve [MODULE_1] specification | [CA] | MH | 2 | Not Started | [DEPENDENCY — e.g. TO-BE delivered, Phase 1 complete] | D-P2.x |
| BL-SPEC-02 | Draft and approve [MODULE_2] specification | [CA] | SH | 2 | Not Started | [DEPENDENCY] | D-P2.x |
| BL-[CODE]-01 | [REMAINING_CA builds triggered by TO-BE delivery] | [CA] | MH | 2 | Not Started | [TO-BE delivered] | AC-0x |
| *Add items as needed* | | | | | | | |

---

## PHASE 3 — CUSTOM MODULE DEVELOPMENT AND REMAINING BUILDS

*Development items depend on approved specs. Never add a DEV item without a corresponding SPEC item.*

### Custom Module Development

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-DEV-01 | Develop [MODULE_1] | [CA] | MH | 3 | Not Started | BL-SPEC-01 approved | AC-0x |
| BL-DEV-02 | Develop [MODULE_2] | [CA] | SH | 3 | Not Started | BL-SPEC-02 approved | AC-0x |
| *Add items as needed* | | | | | | | |

### Remaining Capability Area Builds

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-[CODE]-01 | Configure [CA] Odoo/platform build | [CA] | MH | 3 | Not Started | [TO-BE delivered + relevant spec/dev] | AC-0x |
| BL-[CODE]-02 | Configure [CA] user groups and access rights | Security | MH | 3 | Not Started | BL-[CODE]-01 | AC-[SECURITY_ID] |
| *Add items as needed* | | | | | | | |

### Cross-functional Workflow Configuration

*These items configure workflows and notifications — separate from integration TESTING in Phase 4.*

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-INT-01 | Configure cross-department notification and escalation matrix | CA-XFN | MH | 3 | Not Started | Phase 1 builds complete | AC-XFN |
| BL-INT-02 | Implement cross-department document routing workflows | CA-XFN | SH | 3 | Not Started | All builds complete; scope confirmed from TO-BE | AC-XFN |
| *Add items as needed* | | | | | | | |

---

## PHASE 4 — INTEGRATIONS (TESTING)

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-INT-T01 | [INTEGRATION_CHAIN_1] end-to-end test | CA-XFN | MH | 4 | Not Started | Phase 3 complete | AC-XFN |
| BL-INT-T02 | [INTEGRATION_CHAIN_2] end-to-end test | CA-XFN | MH | 4 | Not Started | Phase 3 complete | AC-XFN |
| BL-INT-T03 | Notification and escalation matrix verification | CA-XFN | MH | 4 | Not Started | BL-INT-01 complete | AC-XFN |
| BL-INT-T04 | Document routing workflow verification | CA-XFN | SH | 4 | Not Started | BL-INT-02 complete | AC-XFN |
| BL-INT-T05 | Cross-capability KPI/reporting roll-up verification | CA-XFN | MH | 4 | Not Started | All builds complete | AC-XFN |
| BL-INT-T06 | Integration test report | CA-XFN | MH | 4 | Not Started | BL-INT-T01 to T05 | D-PI.5 |
| *Add project-specific integration chains* | | | | | | | |

---

## PHASE 5 — TESTING AND STABILISATION

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-UAT-01 | UAT test plan and test cases | All | MH | 5 | Not Started | Phase 4 complete | D-PT.1 |
| BL-UAT-02 | UAT execution with client users | All | MH | 5 | Not Started | BL-UAT-01 | D-PT.2 |
| BL-UAT-03 | UAT defect resolution | All | MH | 5 | Not Started | BL-UAT-02 | D-PT.3 |
| BL-UAT-04 | UAT sign-off | All | MH | 5 | Not Started | BL-UAT-03 | D-PT.4 |
| BL-TRN-01 | [USER_TRAINING_DOCUMENTATION] | All | SH | 5 | Not Started | Phase 4 complete | D-PT.5 |
| BL-TRN-02 | System administrator guide | Security | SH | 5 | Not Started | Phase 4 complete | D-PT.6 |

---

## PHASE 6 — DEPLOYMENT

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-DEP-01 | Cutover plan produced and approved | All | MH | 6 | Not Started | BL-UAT-04 | D-PD.1 |
| BL-DEP-02 | Master data migration | All | MH | 6 | Not Started | BL-DEP-01 | D-PD.2 |
| BL-DEP-03 | Production deployment | All | MH | 6 | Not Started | BL-DEP-02 | D-PD.3 |
| BL-DEP-04 | Post-deployment smoke test | All | MH | 6 | Not Started | BL-DEP-03 | D-PD.4 |
| BL-DEP-05 | Go-live confirmation signed | All | MH | 6 | Not Started | BL-DEP-04 | D-PD.5 |
| BL-DEP-06 | Repository tagged v1.0-go-live | Security | MH | 6 | Not Started | BL-DEP-05 | D-PD.7 |

---

## PHASE 7 — TEMPLATE EXTRACTION

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-TPL-01 | Template extraction report | All | SH | 7 | Not Started | BL-DEP-05 | D-PTE.1 |
| BL-TPL-02 | [GENERIC_REUSABLE_ASSET_1] — strip, parameterise, document | All | SH | 7 | Not Started | BL-TPL-01 | D-PTE.2 |
| BL-TPL-03 | [SECTOR_REUSABLE_ASSET_1] — strip, parameterise, document | All | SH | 7 | Not Started | BL-TPL-01 | D-PTE.3 |
| BL-TPL-04 | Registry contributions submitted | All | SH | 7 | Not Started | BL-TPL-02 to 03 | D-PTE.4 |
| BL-TPL-05 | Registry index updated | All | SH | 7 | Not Started | BL-TPL-04 | D-PTE.5 |
| *Add one item per extracted asset* | | | | | | | |

---

## BACKLOG COMPLETENESS CHECKLIST

*Complete before submitting to PEG-5 Coverage Validation.*

| Check | Status |
|-------|--------|
| Every Capability Area from Product Scope has ≥1 backlog item | [ ] |
| Every sub-capability has ≥1 dedicated item or is named in a WP scope | [ ] |
| Every approval workflow has its own dedicated item (not folded into a capability item) | [ ] |
| Every integration has a configuration item (Phase 3) AND a test item (Phase 4) | [ ] |
| Every custom module has a SPEC item that precedes its DEV item | [ ] |
| Every dashboard and reporting requirement has a dedicated item | [ ] |
| Every security and access requirement has a dedicated item | [ ] |
| Deferred items are present with status Deferred (not simply absent) | [ ] |
| BL-GOV-08 (session rules committed to repo) is present | [ ] |
| All IDs are sequential within their groups | [ ] |

---

*PEF_BACKLOG_TEMPLATE.md v1.0 — Software Factory governance standard*
