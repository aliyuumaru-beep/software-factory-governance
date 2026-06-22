# PEF_ROADMAP_TEMPLATE.md
## Software Factory — Roadmap Template

**Template ID:** PEF-TPL-002  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Section 5 (D-09)  
**Produced at:** PEG-4 — Operational Planning  
**Approved by:** Product Engineering Team

---

## INSTRUCTIONS FOR USE

The Roadmap converts the approved Product Scope into a phased delivery sequence. Every phase must have objectives, deliverables, dependencies, and exit criteria. Every Capability Area from the Product Scope must appear in at least one phase.

The minimum phase structure is defined in PEF Section 4 PEG-4. Add phases between Foundation and Integrations as required by project complexity.

Replace all `[PLACEHOLDER]` text. Delete these instructions before issuing.

---

## DOCUMENT IDENTITY

| Field | Value |
|-------|-------|
| Project name | [PROJECT_NAME] |
| Client | [CLIENT_NAME] |
| Document version | [1.0] |
| Date | [YYYY-MM-DD] |
| Authority | Approved Product Scope (PEF_PRODUCT_SCOPE_TEMPLATE.md — signed [DATE]) |

---

## PHASE SUMMARY

| Phase | Name | Status | Key focus |
|-------|------|--------|-----------|
| Phase 0 | Governance Activation | [Not Started / In Progress / Complete] | Repository, governance, platform audit |
| Phase 1 | Foundation | [Status] | Core platform/modules |
| Phase 2 | [EXTENDED_CAPABILITY_NAME] | [Status] | [Description] |
| Phase N | Integrations | [Status] | Cross-functional workflows |
| Phase N+1 | Testing and Stabilisation | [Status] | UAT, defect resolution |
| Phase N+2 | Deployment | [Status] | Production go-live |
| Phase N+3 | Template Extraction | [Status] | Registry contributions |

---

## PHASE 0 — GOVERNANCE ACTIVATION
**Status:** [Not Started / In Progress / Complete]

### Objectives
- Confirm repository is properly initialised and governed
- Confirm platform contains no prohibited modules or configurations
- Pass all five Governance Activation Gate checks
- Establish Product Memory System in repository
- Confirm backup strategy

### Deliverables
| ID | Deliverable |
|----|------------|
| D-P0.1 | Discovery Report — full repository and platform audit |
| D-P0.2 | Governance Activation Gate Report — all five gates PASS |
| D-P0.3 | `docs/BACKUP_STRATEGY.md` — backup schedule and restore procedure |
| D-P0.4 | Repository scaffold committed — all Product Memory System files present |
| D-P0.5 | Platform confirmation logged in Decision Log |
| D-P0.6 | [PROJECT_SPECIFIC_GOVERNANCE_DELIVERABLE] |

### Dependencies
- Repository access confirmed
- Platform access confirmed
- Product Transfer Package loaded by development team

### Exit Criteria
- All five Governance Gates: PASS
- Platform audit complete — no prohibited modules
- Product Memory System committed and pushed
- Backup strategy documented and last backup confirmed

---

## PHASE 1 — FOUNDATION
**Status:** [Not Started / In Progress / Complete]

### Objectives
[Describe the foundation capabilities being established in this phase]
- Install and configure core [platform] modules for [DEPARTMENTS/DOMAINS]
- Install and configure required [OCA/third-party] modules
- Establish user groups and access rights for all Phase 1 areas
- Implement approval workflows for Phase 1 areas

### Deliverables
| ID | Deliverable |
|----|------------|
| D-P1.1 | [CA-01] — [description of build deliverable] |
| D-P1.2 | [CA-02] — [description] |
| D-P1.3 | [CA-03] — [description] |
| D-P1.4 | [MODULE_NAME] installed, version-pinned, and logged |
| D-P1.5 | Access rights matrix — Phase 1 areas configured |
| *Add rows as needed* | |

### Dependencies
- Phase 0 exit criteria met
- [DEPENDENCY_1: e.g. Client confirmation of approval thresholds]
- [DEPENDENCY_2: e.g. OCA module compatibility verified]

### Exit Criteria
- All Phase 1 acceptance criteria met (reference AC IDs from Product Scope)
- All Phase 1 deliverables committed to repository
- No open critical defects
- Governance documents updated

---

## PHASE 2 — [EXTENDED_CAPABILITIES_NAME]
**Status:** [Not Started / In Progress / Complete]

*Use this phase (and add further phases if needed) for capabilities that depend on Phase 1 being complete, or that require custom module development.*

### Objectives
- [OBJECTIVE_1]
- [OBJECTIVE_2]

### Deliverables
| ID | Deliverable |
|----|------------|
| D-P2.1 | [DELIVERABLE_1] |
| D-P2.2 | [DELIVERABLE_2] |
| D-P2.3 | [CUSTOM_MODULE] — design spec approved |
| D-P2.4 | [CUSTOM_MODULE] — developed, tested, deployed to staging |
| *Add rows as needed* | |

### Dependencies
- Phase 1 exit criteria met
- [TO-BE specification for [DEPARTMENT] delivered — if applicable]
- [Custom module spec approved before development item — mandatory]

### Exit Criteria
- All Phase 2 acceptance criteria met
- All custom module specs approved before development begins
- All Phase 2 deliverables committed
- Governance documents updated

---

## PHASE [N] — INTEGRATIONS
**Status:** [Not Started / In Progress / Complete]

### Objectives
- Implement and test all cross-functional workflows
- Configure cross-department notifications and escalations
- Configure document routing workflows
- Verify end-to-end process chains function correctly across capability boundaries

### Deliverables
| ID | Deliverable |
|----|------------|
| D-PI.1 | [INTEGRATION_1] end-to-end chain tested and verified |
| D-PI.2 | [INTEGRATION_2] end-to-end chain tested and verified |
| D-PI.3 | Cross-department notification matrix configured and tested |
| D-PI.4 | Document routing workflows configured and tested |
| D-PI.5 | Integration test report committed |
| *Add rows as needed* | |

### Dependencies
- All capability area builds complete (all prior phases)

### Exit Criteria
- All integration acceptance criteria met (AC-XX Cross-functional)
- Integration test report produced and committed
- No open critical defects

---

## PHASE [N+1] — TESTING AND STABILISATION
**Status:** [Not Started / In Progress / Complete]

### Objectives
- Execute full User Acceptance Testing cycle
- Resolve all defects
- Stabilise system for production
- Produce training and handover documentation

### Deliverables
| ID | Deliverable |
|----|------------|
| D-PT.1 | UAT test plan and test cases |
| D-PT.2 | UAT execution results |
| D-PT.3 | UAT defect register — all resolved |
| D-PT.4 | UAT sign-off from Product Owner |
| D-PT.5 | [USER_TRAINING_DOCUMENTATION] |
| D-PT.6 | System administrator guide |
| *Add rows as needed* | |

### Dependencies
- Integration phase exit criteria met
- Client UAT team available and briefed
- Staging environment stable

### Exit Criteria
- UAT sign-off obtained from Product Owner
- Zero open critical defects
- Zero open high defects (or formally deferred with Product Owner agreement)
- Training documentation complete

---

## PHASE [N+2] — DEPLOYMENT
**Status:** [Not Started / In Progress / Complete]

### Objectives
- Deploy to production
- Execute data migration
- Confirm system health post-cutover
- Hand over to client operations

### Deliverables
| ID | Deliverable |
|----|------------|
| D-PD.1 | Cutover plan — approved |
| D-PD.2 | Master data migration executed and verified |
| D-PD.3 | Production deployment complete |
| D-PD.4 | Post-deployment smoke test — all critical workflows verified |
| D-PD.5 | Go-live confirmation signed by Product Owner |
| D-PD.6 | Hypercare plan — [N] days post-go-live support |
| D-PD.7 | Repository tagged `v1.0-go-live` |
| *Add rows as needed* | |

### Dependencies
- Testing phase exit criteria met (UAT sign-off)
- Production environment accessible
- Client operations team briefed

### Exit Criteria
- Production system live and stable
- Go-live confirmation signed
- Governance documents final and committed
- Hypercare period begun

---

## PHASE [N+3] — TEMPLATE EXTRACTION
**Status:** [Not Started / In Progress / Complete]

### Objectives
- Extract all Generic Reusable and Sector Reusable assets from the delivered product
- Contribute to Software Factory Template Registry
- Document each contribution

### Deliverables
| ID | Deliverable |
|----|------------|
| D-PTE.1 | Template extraction report against Asset Classification Register |
| D-PTE.2 | [GENERIC_REUSABLE_ASSET_1] — stripped, parameterised, documented |
| D-PTE.3 | [SECTOR_REUSABLE_ASSET_1] — stripped, parameterised, documented |
| D-PTE.4 | Registry contribution entries committed |
| D-PTE.5 | Registry index updated |
| *Add rows as needed* | |

### Dependencies
- Deployment phase exit criteria met
- Legal clearance for template contribution (if required by engagement contract)

### Exit Criteria
- All Generic Reusable assets contributed
- All Sector Reusable assets contributed
- Each contribution documented and independently testable
- Registry index updated

---

*PEF_ROADMAP_TEMPLATE.md v1.0 — Software Factory governance standard*
