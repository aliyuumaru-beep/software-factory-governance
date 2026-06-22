# PEF_WORK_PACKAGE_TEMPLATE.md
## Software Factory — Work Package Template

**Template ID:** PEF-TPL-004  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Section 5 (D-11)  
**Produced at:** PEG-4 — Operational Planning  
**Approved by:** Product Engineering Team

---

## INSTRUCTIONS FOR USE

A Work Package is the executable unit of implementation. Each work package has a single clear objective, explicit scope, and verifiable acceptance criteria. Work packages are what the development team (human or AI) executes.

**ID format:** `WP-[AREA]-[NN]`  
Examples: `WP-GOV-01`, `WP-FIN-01`, `WP-SPEC-01`, `WP-DEV-01`, `WP-INT-01`

**Complexity:**
- **Small:** 1–2 actions; low risk; single concern
- **Medium:** 3–6 actions; moderate risk; multiple steps
- **Large:** 7–12 actions; multiple interacting components; requires design decisions
- **Very Large:** Custom module development or major integration; requires approved spec; significant testing; plan sub-tasks before starting

**The spec-before-dev rule is absolute:** No WP-DEV item may begin execution until its corresponding WP-SPEC item has been completed and its deliverable approved. This must be enforced by the development team and cannot be overridden.

Replace all `[PLACEHOLDER]` text. Delete these instructions before issuing.

---

## DOCUMENT IDENTITY

| Field | Value |
|-------|-------|
| Project name | [PROJECT_NAME] |
| Client | [CLIENT_NAME] |
| Document version | [1.0] |
| Date | [YYYY-MM-DD] |
| Authority | Approved Backlog (PEF_BACKLOG_TEMPLATE.md — [DATE]) |
| Update rule | Mark WP status In Progress when started; Done only when AC verified with evidence |

---

## PHASE 0 — GOVERNANCE ACTIVATION

---

### WP-GOV-01 — Platform and Repository Discovery
**Backlog items:** BL-GOV-01, BL-GOV-02  
**Phase:** 0  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Produce a complete, accurate Discovery Report covering the current state of the repository and platform before any implementation work begins.

**Scope:**
- Confirm repository path, Git status, current branch, and recent commit history
- Confirm remote configuration and branch protection status
- Confirm platform version and edition (critical — must match Product Scope platform declaration)
- Run prohibited module audit: verify no blocked modules are installed
- Identify any existing custom modules
- Confirm database / data store name and accessibility
- Confirm backup directory and last backup timestamp
- Confirm CI workflow status

**Dependencies:** Repository access; platform access

**Deliverables:**
- Discovery Report (structured per Section 9.2 of PEF)

**Acceptance Criteria:**
- Discovery Report covers all fields
- Platform edition confirmed and matches Product Scope
- Prohibited module audit result on file (pass or documented findings)
- Discovery Report reviewed before WP-GOV-02 begins

**Governance Reviews Required:** Product Engineering Team reviews Discovery Report before proceeding

---

### WP-GOV-02 — Governance Activation Gate
**Backlog items:** BL-GOV-03, BL-GOV-04, BL-GOV-05, BL-GOV-06, BL-GOV-07, BL-GOV-08  
**Phase:** 0  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Run all five Governance Activation Gate checks; fix all FAILs; commit the Product Memory System scaffold; certify programme is ready for implementation.

**Scope:**
- Run Gate A (Repository): version control, remote, main branch, feature branch workflow
- Run Gate B (CI/CD): pipeline, lint, build verification
- Run Gate C (Governance Documents): all mandatory Product Memory System files present
- Run Gate D (Backup): strategy documented, restore procedure present, last backup confirmed
- Run Gate E (Product Readiness): Capability Map present, platform confirmed, prohibited modules absent, Coverage Score on file
- Fix each FAIL before re-running
- Extract and commit repository scaffold to main branch
- Add session start/end rules to `docs/PRODUCT_STATE_INDEX.md`
- Produce `docs/GOVERNANCE_GATE_REPORT.md`

**Dependencies:** WP-GOV-01 complete and Discovery Report reviewed

**Deliverables:**
- `docs/GOVERNANCE_GATE_REPORT.md` — all five gates PASS
- `docs/BACKUP_STRATEGY.md`
- CI workflow file(s) active
- All Product Memory System files committed and pushed
- Session start/end rules in `docs/PRODUCT_STATE_INDEX.md`

**Acceptance Criteria:**
- All five gates: PASS
- Gate Report committed to repository
- `git push` confirmed

**Governance Reviews Required:** Governance Team confirms Gate Report before Phase 1 begins

---

## PHASE 1 — FOUNDATION

*The following is a standard pattern. Repeat for each Capability Area build in Phase 1.*

---

### WP-[CODE]-01 — [CA_NAME] Core Configuration
**Backlog items:** [BL-ITEM-01, BL-ITEM-02, BL-ITEM-03, ...]  
**Phase:** 1  
**Complexity:** [Small / Medium / Large]  
**Status:** Not Started

**Objective:** [One sentence: what is being built and why]

**Scope:**
- [SCOPE_ITEM_1 — specific, implementable action]
- [SCOPE_ITEM_2]
- [SCOPE_ITEM_3 — include approval workflow items explicitly if applicable]
- Configure user groups: [USER_GROUP_1], [USER_GROUP_2], [USER_GROUP_3]
- Configure access rights per group on [RECORD_TYPES]
- Verify audit trail active on [RECORD_TYPES]

**Dependencies:** [WP-GOV-02; WP-PKG-01 if package must be installed first; etc.]

**Deliverables:**
- [DELIVERABLE_1: e.g. Chart of accounts configured and exported as reference CSV]
- [DELIVERABLE_2]
- User groups configured
- Audit trail verified

**Acceptance Criteria:** [AC-ID] — [specific criterion, not just "per AC-01"]

**Governance Reviews Required:** [Client review of [specific item] before finalisation / None]

---

### WP-PKG-01 — External Package / Module Installation
**Backlog items:** [BL-PKG-01, BL-PKG-02, BL-PKG-03]  
**Phase:** 1  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Install, verify, and version-pin all required external packages for Phase 1.

**Scope:**
- Verify [PLATFORM] [VERSION] compatibility for each package before installation: [PACKAGE_1], [PACKAGE_2], [PACKAGE_3]
- Install each package
- Pin each package version in `requirements.txt` or equivalent
- Log each installation in `docs/DECISION_LOG.md` with package name, version, source, rationale
- Confirm packages are active

**Dependencies:** WP-GOV-02

**Deliverables:**
- [N] packages installed and active
- `requirements.txt` updated with pinned versions
- [N] Decision Log entries

**Acceptance Criteria:** All packages confirmed active; each logged in Decision Log

**Governance Reviews Required:** None

---

## PHASE 2 — CUSTOM MODULE SPECIFICATIONS

*Use this pattern for every custom module specification work package.*

---

### WP-SPEC-[NN] — `[module_name]` Specification
**Backlog items:** BL-SPEC-[NN]  
**Phase:** 2  
**Complexity:** [Medium / Large / Very Large]  
**Status:** Not Started

**Objective:** Produce an approved design specification for the `[module_name]` module before any development begins.

**Scope:**
- Document: purpose, Capability Map reference ([CA-ID]), data model ([MODELS]), business rules, state machine (if applicable), UI description, integration points with existing modules, test cases, acceptance criteria
- [MODULE_SPECIFIC_SCOPE_ITEM: e.g. "Document version control approach for contract drafts and amendments"]
- Circulate for [STAKEHOLDER] review
- Obtain Product Owner approval

**Dependencies:** [DEPENDENCY: e.g. TO-BE specification for [department] delivered; Phase 1 [CA] build complete]

**Deliverables:**
- `docs/modules/[module_name]_spec.md` — approved and committed

**Acceptance Criteria:**
- Spec contains all required sections
- [DOMAIN_SPECIFIC_CRITERION: e.g. "Statutory rates confirmed by qualified adviser"]
- Product Owner signature obtained

**Governance Reviews Required:** [STAKEHOLDER] review; Product Owner sign-off

---

## PHASE 3 — CUSTOM MODULE DEVELOPMENT

*Use this pattern for every custom module development work package. A WP-SPEC must be approved before this WP begins.*

---

### WP-DEV-[NN] — Develop `[module_name]`
**Backlog items:** BL-DEV-[NN]  
**Phase:** 3  
**Complexity:** [Large / Very Large]  
**Status:** Not Started

**Objective:** Build and test the `[module_name]` module against its approved specification.

**Scope:** Per `docs/modules/[module_name]_spec.md` approved spec. Key items:
- Create module structure with correct manifest (`__manifest__.py` / `package.json` / etc.)
- Implement data models: [MODEL_1], [MODEL_2]
- Implement business logic: [LOGIC_1], [LOGIC_2]
- Implement UI: [VIEW/SCREEN_1], [VIEW/SCREEN_2]
- Implement automated rules: [RULE_1: e.g. expiry alerting scheduled action]
- Write unit tests for [CRITICAL_LOGIC]
- Deploy to staging environment and validate

**Dependencies:** WP-SPEC-[NN] approved (mandatory — development cannot begin without approved spec)

**Deliverables:**
- `[addons/module_name/]` — committed, tested, deployed to staging
- Unit test results committed
- Staging validation evidence

**Acceptance Criteria:** [AC-ID from Product Scope]; all [CRITICAL_FUNCTION] work correctly against test data

**Governance Reviews Required:** [STAKEHOLDER] validates [specific behaviour]; test results reviewed before marking Done

---

## PHASE 3 — CROSS-FUNCTIONAL WORKFLOW CONFIGURATION

---

### WP-XFN-01 — Cross-department Notification and Escalation Matrix
**Backlog items:** BL-INT-01 (configuration item)  
**Phase:** 3  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Configure all automated notification triggers and escalation rules that operate across capability/department boundaries.

**Scope:**
- Identify all cross-boundary notification events from TO-BE specifications
- Configure automated triggers for each event (server actions on state change, scheduled actions for overdue escalations)
- Configure escalation thresholds: [THRESHOLD_1], [THRESHOLD_2]
- Test each notification fires on its trigger condition
- Test each escalation fires at its threshold

**Dependencies:** Phase 1 capability builds complete; remaining department builds complete

**Deliverables:**
- `docs/notification_matrix.md` — all events documented
- Automated triggers committed
- Test evidence for each notification and escalation

**Acceptance Criteria:** All configured notification events verified; escalation fires within correct threshold

**Governance Reviews Required:** Stakeholders confirm escalation thresholds before configuration

---

### WP-XFN-02 — Cross-department Document Routing
**Backlog items:** BL-INT-02 (configuration item)  
**Phase:** 3  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Implement document routing workflows that route records across department boundaries per the TO-BE specifications.

**Scope:**
- Confirm routing requirements from all delivered TO-BE specifications
- [ROUTING_FLOW_1: e.g. Finance payment advice → requesting department on confirmation]
- [ROUTING_FLOW_2: e.g. Legal contract → Finance on execution]
- Implement routing as automated actions or follower rules as appropriate
- Test each routing flow end-to-end

**Dependencies:** All department builds complete; TO-BE spec confirmation gate (scope may change as remaining TO-BEs are delivered)

**Deliverables:**
- Routing specification confirmed and documented
- Routing workflows committed
- Test evidence for each flow

**Acceptance Criteria:** Each routing workflow tested with a real document traversing the route without manual intervention

**Governance Reviews Required:** User review of routing specification before configuration

---

## PHASE 4 — INTEGRATIONS (TESTING)

---

### WP-INT-01 — Cross-functional Integration Testing
**Backlog items:** [BL-INT-T01 through BL-INT-T06]  
**Phase:** 4  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Verify all cross-department workflows and data flows function correctly end-to-end.

**Scope:**
- Test and verify [INTEGRATION_CHAIN_1]
- Test and verify [INTEGRATION_CHAIN_2]
- Test and verify notification and escalation matrix (from WP-XFN-01)
- Test and verify document routing workflows (from WP-XFN-02)
- Verify cross-capability KPI/reporting roll-up against source data — confirm aggregation accuracy
- Produce integration test report

**Dependencies:** All Phase 3 builds complete; WP-XFN-01 and WP-XFN-02 complete

**Deliverables:**
- Test results for each integration chain
- Notification/escalation test evidence
- Document routing test evidence
- KPI roll-up accuracy verified with source data comparison
- `docs/integration_test_report.md` committed

**Acceptance Criteria:** [AC-XFN from Product Scope]; all chains execute end-to-end without error; no data mismatch; notifications fire correctly; KPI roll-up matches source data

**Governance Reviews Required:** Product Engineering Team reviews integration test report

---

## PHASE 5 — UAT AND STABILISATION

---

### WP-UAT-01 — User Acceptance Testing
**Backlog items:** [BL-UAT-01 through BL-UAT-04]  
**Phase:** 5  
**Complexity:** Very Large  
**Status:** Not Started

**Objective:** Execute full UAT cycle with client users; resolve all defects; obtain sign-off.

**Scope:**
- Produce UAT test plan with one test case per acceptance criterion (AC-01 through AC-[LAST])
- Coordinate UAT execution with client user representatives per capability area
- Log all defects; triage (Critical / High / Medium / Low); resolve and retest
- Obtain signed UAT sign-off from Product Owner

**Dependencies:** WP-INT-01 complete

**Deliverables:**
- UAT test plan
- UAT execution results
- Defect register (all Critical and High resolved; Medium/Low resolved or formally deferred)
- Signed UAT sign-off document

**Acceptance Criteria:** Signed UAT sign-off from Product Owner; zero open Critical defects

**Governance Reviews Required:** QA Team certifies defect resolution; Product Owner signs UAT document

---

## WORK PACKAGE COMPLETENESS CHECKLIST

*Complete before submitting to PEG-5 Coverage Validation.*

| Check | Status |
|-------|--------|
| Every Backlog item maps to a named Work Package or explicit WP scope entry | [ ] |
| Every approval workflow has a dedicated scope entry (not implied within capability WP) | [ ] |
| Every integration has a configuration WP (Phase 3) AND a testing WP (Phase 4) | [ ] |
| Every custom module has WP-SPEC before WP-DEV — sequencing enforced in dependencies | [ ] |
| WP-XFN-01 (notification/escalation) and WP-XFN-02 (document routing) present | [ ] |
| WP-INT-01 explicitly covers notification, routing, and KPI roll-up verification | [ ] |
| Every WP has at least one verifiable acceptance criterion | [ ] |
| Every WP states governance reviews required | [ ] |
| No WP-DEV exists without a preceding WP-SPEC dependency | [ ] |

---

*PEF_WORK_PACKAGE_TEMPLATE.md v1.0 — Software Factory governance standard*
