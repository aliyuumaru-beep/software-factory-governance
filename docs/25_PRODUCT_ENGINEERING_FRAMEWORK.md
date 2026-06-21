# 25_PRODUCT_ENGINEERING_FRAMEWORK.md
## Software Factory — Product Engineering Framework (PEF)

**Document number:** SF-GOV-025  
**Version:** 1.1  
**Status:** Approved for adoption  
**Classification:** Software Factory Governance Standard  
**Applies to:** All Software Factory product engagements  
**Date issued:** 2026-06-21 (v1.0); 2026-06-21 (v1.1)  
**Review cycle:** Annual or after three reference implementations  
**Change record:** See `docs/PEF_V1_1_CHANGELOG.md`. v1.1 implements the P1 enhancements from validation report SF-VAL-PEF-001.

---

## DOCUMENT CONTROL

| Field | Value |
|-------|-------|
| Owner | Software Factory Governance Team |
| Approved by | Software Factory Director |
| Reference implementation | NADF ERP Programme (2026) |
| Supersedes | v1.0 (incremental upgrade — v1.0 lifecycle, gates, and templates preserved unchanged) |
| Related standards | SF-GOV-010 (Repository Governance), SF-GOV-015 (Agent Operating Protocol) |
| Validation basis | SF-VAL-PEF-001 (Framework Validation Review Report, 2026-06-21) |

---

## SECTION 1 — PURPOSE

### 1.1 Statement of Purpose

The Product Engineering Framework (PEF) defines the Software Factory's standard methodology for converting refined business process outputs into a validated, implementation-ready product definition that can be executed by a Software Development Team or an Autonomous Agent Team.

The PEF exists because business process analysis and software development are fundamentally different disciplines with different vocabularies, artefacts, and quality standards. Without a governed bridge between them, capability gaps, hidden scope reductions, and implementation ambiguities routinely appear during development — discovered too late and at too high a cost.

The PEF is that bridge.

### 1.2 Problem Statement

Without a formal product engineering methodology, the following failure modes occur consistently:

| Failure Mode | Consequence |
|-------------|------------|
| Business process documentation converted directly to development tasks | Capabilities missed; RACI and swimlane artefacts treated as build instructions |
| Scope defined only at the capability level | Sub-capabilities, approvals, automations, and integrations never backlogged |
| No coverage validation performed | Gaps discovered in UAT or after deployment |
| Reusable assets not identified | Every project rebuilds the same components |
| Development begins before product definition is approved | Rework, scope disputes, and delivery failures |
| Operational planning documents not produced | Autonomous agents lack sufficient context to execute correctly |

The PEF eliminates all of these through a structured eight-stage lifecycle with mandatory approval gates.

### 1.3 Design Principles

| Principle | Statement |
|-----------|-----------|
| P-01 | Business process artefacts (swimlanes, BPOGS outputs, RACI matrices) are **requirements inputs**, not implementation workstreams |
| P-02 | The Product Scope document is the **authoritative implementation source** for all development work |
| P-03 | **Coverage validation is mandatory** before development is authorised |
| P-04 | **No development begins** without a formally approved Product Approval document |
| P-05 | Every capability must trace to a backlog item; every backlog item must trace to a work package |
| P-06 | Reusable assets must be **identified, classified, and registered** at the point of production |
| P-07 | The Product Memory System must be **repository-resident** — never chat-resident |
| P-08 | Operational planning documents (Roadmap, Backlog, Work Packages) are **mandatory**, not optional |
| P-09 | Coverage gaps discovered during validation must be **remediated before authorisation** |
| P-10 | **Build Once, Reuse Many Times**: all Software Factory engagements extract reusable assets into the Template Registry |

---

## SECTION 2 — SCOPE

### 2.1 Applicability

This framework applies to all Software Factory engagements where business processes or organisational requirements are converted into a software product. It applies across all solution types:

| Solution Type | Applicability | Notes |
|--------------|--------------|-------|
| ERP Projects | Full | All eight PEG stages apply |
| Government Digital Transformation | Full | Additional compliance gate may be added at PEG-6 |
| NGO / CBO Solutions | Full | Scope typically smaller; stages compress but do not disappear |
| Manufacturing Solutions | Full | Process automation emphasis at PEG-3 and PEG-4 |
| Web Applications | Full | UI/UX deliverables added to PEG-3 |
| Mobile Applications | Full | Platform and device considerations added to PEG-3 |
| AI Solutions | Full | Model selection and training data considerations added to PEG-3 |
| Workflow Automation Projects | Full | Integration architecture emphasis at PEG-3 and PEG-4 |

### 2.2 What the PEF Governs

The PEF governs the Product Engineering Lifecycle: the stages between the completion of business process analysis and the commencement of software development.

It does not govern:
- Business Process Analysis methodology (governed by the BPOGS Framework)
- Software development methodology (governed by the Software Factory Development Standard)
- Infrastructure and deployment methodology (governed by the Software Factory DevOps Standard)
- Client engagement and commercial terms (governed by engagement contracts)

### 2.3 Entry Point

The PEF assumes the following inputs are available before PEG-1 begins:
- Refined business process documentation (AS-IS and TO-BE)
- ERP or platform mapping (for ERP projects)
- Stakeholder-approved process outputs
- An assigned Product Owner

---

## SECTION 3 — ROLES AND RESPONSIBILITIES

### 3.1 Role Definitions

#### Business Process Team
The team responsible for producing refined AS-IS and TO-BE business process documentation, including swimlane diagrams, RACI matrices, and BPOGS workbooks.

**Responsibilities in the PEF:**
- Deliver complete, approved TO-BE process documentation as PEG-1 input
- Respond to clarification requests from the Product Engineering Team during PEG-2
- Confirm capability scope when queried during Coverage Validation (PEG-5)
- Do not own or produce implementation documents

**Authority:** Cannot authorise development; provides requirements input only

#### BPOGS Team
The team responsible for business process optimisation and governance system outputs, including ERP mapping, process gap analysis, and platform alignment recommendations.

**Responsibilities in the PEF:**
- Deliver ERP/platform mapping as PEG-1 input
- Validate capability classifications during PEG-2 and PEG-3
- Confirm platform selection and module mapping
- Flag Enterprise-vs-Community gaps in ERP projects

**Authority:** Cannot authorise development; provides platform and mapping guidance

#### Product Engineering Team
The team responsible for executing PEG-1 through PEG-6: converting process outputs into a validated, approved product definition.

**Responsibilities:**
- Execute all PEF lifecycle stages
- Produce all mandatory deliverables
- Conduct Coverage Validation (PEG-5)
- Remediate all identified gaps before submitting for authorisation
- Maintain the Product Authority Model in the repository

**Authority:** Owns the product definition; initiates development authorisation

#### Product Owner
The senior stakeholder responsible for product decisions and authorisation.

**Responsibilities:**
- Review and approve the Product Scope document (PEG-3 gate)
- Review and approve the Coverage Validation Report (PEG-5 gate)
- Sign the Product Approval document (PEG-6 gate)
- Resolve scope disputes and escalations
- Accept the delivered product at UAT

**Authority:** Sole authority to approve development; holds product sign-off

#### Governance Team
The team responsible for enforcing PEF compliance and maintaining framework standards.

**Responsibilities:**
- Confirm Governance Activation Gate passage before implementation (PEG-6)
- Audit repository governance compliance
- Review and update this framework annually
- Manage the Software Factory Template Registry
- Approve template extraction contributions

**Authority:** Can block implementation if Governance Gate is not passed

#### Software Development Team (or Autonomous Agent Team)
The team responsible for implementing the approved product definition.

**Responsibilities:**
- Receive the Product Transfer Package (PEG-6 output)
- Execute repository discovery before any implementation
- Implement work packages in approved sequence
- Maintain Product Memory System throughout development
- Produce test evidence against each acceptance criterion
- Update governance documents after every milestone

**Authority:** Cannot modify product scope without Product Owner approval; executes within approved boundaries only

#### QA Team
The team responsible for validating that implemented capabilities meet their acceptance criteria.

**Responsibilities:**
- Review Coverage Validation Report at PEG-5
- Produce UAT test plan at PEG-7
- Execute UAT with client users
- Certify defect resolution
- Sign UAT completion

**Authority:** Can block deployment if UAT not passed

---

### 3.2 Product Owner Refusal Escalation Procedure

The Product Owner holds sole authority to sign Gate 1 (Scope Approval), Gate 3 (Development Authorisation), and Gate 4 (Deployment Authorisation). The framework therefore requires a defined procedure for the case where the Product Owner reviews a gate and **actively disputes or refuses to sign** — distinct from a gate that simply has not yet been reached (closes WEK-04). Without this procedure the programme stalls indefinitely and the Governance Team has no sanctioned authority to act.

This procedure applies whenever a Product Owner declines to sign **Gate 1**, **Gate 3**, or **Gate 4**.

**Step 1 — Record the refusal (Day 0).**
The Product Engineering Team records the refusal in the `docs/DECISION_LOG.md` and the relevant gate document, capturing: the gate refused, the date, the stated reason, and the specific items in dispute. A refusal without a stated reason is itself logged as "reason not provided".

**Step 2 — Classify the refusal.**

| Class | Definition | Path |
|-------|-----------|------|
| Substantive | The Product Owner identifies a specific defect, omission, or disagreement in the gate artefacts | Proceed to Step 3 (Remediation) |
| Procedural | The Product Owner objects to process, timing, or authority — not to the artefact content | Proceed to Step 4 (Escalation) |
| Unspecified | No reason given, or the Product Owner is unavailable / unresponsive | Proceed to Step 4 (Escalation) after the response window below |

**Step 3 — Remediation (Substantive refusals).**
The Product Engineering Team addresses each disputed item, updates the affected artefacts, and re-presents the gate. For Gate 3, any change to scope or coverage triggers the Scope Change Control Procedure (Section 12.3) and may require Coverage re-validation. The remediation and re-presentation cycle is time-boxed to **5 working days**; if the dispute persists after one full cycle, it escalates to Step 4.

**Step 4 — Escalation chain.**
Where a refusal is Procedural, Unspecified, or persists after remediation, escalation proceeds in order. Each level has a defined response window; if the window lapses without resolution, the matter advances to the next level automatically.

| Level | Authority | Response window | Mandate |
|-------|----------|-----------------|---------|
| E-1 | Product Owner ↔ Product Engineering Team lead | 5 working days | Direct resolution; document the agreed outcome |
| E-2 | Software Factory Governance Team | 5 working days | Arbitrate between PET and Product Owner; rule on whether the gate artefacts meet PEF standards |
| E-3 | Software Factory Director (with client sponsor) | 10 working days | Final arbitration; may authorise a conditional gate, a scope reset, or programme suspension |

**Step 5 — Holding state.**
While an escalation is open, the programme enters a **gate-hold state**: no stage past the disputed gate may proceed, no implementation begins (for Gate 3) and no deployment occurs (for Gate 4). The hold, its rationale, and its current escalation level are recorded in `docs/CONTROL_TOWER.md` so that any team member or AI agent reading the Product Memory System sees the blocker immediately.

**Step 6 — Resolution.**
Resolution is recorded as one of: *signed* (gate proceeds), *signed with conditions* (conditions logged and tracked), *reset* (return to an earlier PEG stage), or *suspended* (programme suspension — out of scope for v1.1; governed by a future procedure). The outcome and the authority that decided it are logged in `docs/DECISION_LOG.md`.

**Non-negotiable rule:** A gate is never treated as passed because a Product Owner is silent or unavailable. Absence of signature is a refusal of class *Unspecified* and follows this procedure. The Governance Team may not sign on the Product Owner's behalf at any level.

---

## SECTION 4 — PRODUCT ENGINEERING LIFECYCLE

The PEF lifecycle consists of eight stages, designated PEG-1 through PEG-8.

```
PEG-1          PEG-2          PEG-3          PEG-4
Requirements   Capability     Product        Operational
Consolidation  Mapping        Scope          Planning
     ↓              ↓              ↓              ↓
PEG-8          PEG-7          PEG-6          PEG-5
Template       Deployment     Development    Coverage
Extraction     & Handover     Authorisation  Validation
```

---

### PEG-1 — Requirements Consolidation

**Purpose:** Gather, organise, and confirm all inputs before product engineering begins. Nothing proceeds without complete inputs.

**Entry Criteria:**
- Business process analysis complete and signed off by client
- TO-BE documentation available for all in-scope processes
- Platform/ERP mapping available (for ERP projects)
- Product Owner identified and available
- Engagement scope confirmed in writing

**Inputs:**
- Refined AS-IS process documentation
- Detailed TO-BE process documentation
- ERP/platform mapping and gap analysis
- BPOGS outputs and workbooks
- Engagement scope document
- Any pending client clarifications register

**Activities:**
1. Compile complete inventory of all in-scope departments and processes
2. Confirm TO-BE coverage: identify any departments or processes without complete TO-BE documentation; log as pending items
3. Confirm platform selection and version (e.g. Odoo 17 CE, not Enterprise)
4. Confirm all Enterprise-vs-Community gaps are documented
5. Register all open client clarifications with owners and target dates
6. Confirm Product Owner availability for approval gates
7. Establish repository and apply Governance Activation Gate (see Section 12)

**Outputs:**
- PEG-1 Requirements Register (complete inventory of all processes, platforms, gaps)
- Open Items Log (pending clarifications, missing TO-BE)
- Confirmed platform profile (modules available, modules blocked)
- Governance Gate preliminary result

**Exit Criteria:**
- All in-scope processes inventoried
- Platform confirmed in writing
- All gaps and pending items logged
- Governance Gate run (FAILs documented and remediation planned)
- Product Owner confirmed

---

### PEG-2 — Capability Mapping

**Purpose:** Convert the process inventory into a structured capability map that becomes the master product structure. Every downstream deliverable traces back to this map.

**Entry Criteria:**
- PEG-1 exit criteria met
- Requirements Register available
- Platform profile confirmed

**Inputs:**
- PEG-1 Requirements Register
- Detailed TO-BE process documentation
- Platform module catalogue (what is native, OCA, custom, future)

**Activities:**
1. Define Capability Areas from the process inventory (one or more CAs per department)
2. For each Capability Area, define Sub-Capabilities at the implementation level
3. Classify each Sub-Capability: **Native** / **Configuration** / **OCA** / **Custom Module** / **Future Phase**
4. Apply the Enterprise Gap Protocol for ERP projects:
   - Identify the gap (what Enterprise feature would normally serve this)
   - Name the Community native alternative
   - Name the OCA alternative
   - Justify custom development only if neither alternative closes the gap
5. Identify all approval workflows and their implementation approach
6. Identify all integrations and cross-functional workflows
7. Identify all dashboards and reporting requirements
8. Identify all security and access control requirements
9. First-pass identification of reusable vs client-specific assets (formal classification in PEG-3)

**Outputs:**
- Capability Map (all CAs and sub-capabilities with classifications)
- Approval Framework (all approval types and implementation approaches)
- Integration Map (all cross-functional workflows)
- Custom Module Register (all modules requiring bespoke development, with justification)

**Exit Criteria:**
- Every in-scope process maps to at least one sub-capability
- Every sub-capability classified
- All approval types identified with implementation approach
- All integrations identified
- Custom modules justified (none added without justification)

**Governance rule:** No sub-capability may be left unclassified. "TBD" is not a valid classification — it is an open item to be resolved before PEG-2 exits.

---

### PEG-3 — Product Scope Definition

**Purpose:** Produce the authoritative product scope document that becomes the primary reference for all development work. This is the most critical output of the PEF.

**Entry Criteria:**
- PEG-2 exit criteria met
- Capability Map approved by Product Engineering Team
- Custom modules justified

**Inputs:**
- PEG-2 Capability Map
- PEG-2 Approval Framework
- PEG-2 Integration Map
- PEF_PRODUCT_SCOPE_TEMPLATE.md

**Activities:**
1. Write Product Vision and Objectives
2. Define all Capability Areas with full descriptions and implementation approach
3. Write Acceptance Criteria for every Capability Area (AC must be testable and unambiguous)
4. Define Out of Scope items explicitly (prevents scope creep)
5. Document all Assumptions (each assumption is a risk if incorrect)
6. Classify all deliverables using the Asset Classification Model:
   - **Generic Reusable** — applicable to any deployment of the same technology
   - **Sector Reusable** — applicable to the same sector (government, NGO, manufacturing, etc.)
   - **Client Specific** — not reusable; contains client-specific data, logic, or branding
7. Identify Template Extraction Opportunities (all Generic Reusable and Sector Reusable items)
8. Define Success Criteria
9. Review with Product Owner; iterate until approved

**Outputs:**
- Product Scope document (completed PEF_PRODUCT_SCOPE_TEMPLATE.md)
- Asset Classification Register

**Exit Criteria:**
- Product Scope reviewed and approved by Product Owner (signature on PEF_PRODUCT_APPROVAL_TEMPLATE.md Section A)
- Every Capability Area has at least one testable Acceptance Criterion
- Out of Scope section explicitly states what is not being built
- Asset Classification complete for all deliverables

**Critical lesson (NADF):** Product Scope approval alone is not sufficient to authorise development. It authorises operational planning only. Development authorisation comes at PEG-6.

---

### PEG-4 — Operational Planning

**Purpose:** Convert the approved Product Scope into an implementation-ready operational plan: a sequenced Roadmap, a prioritised Backlog, and executable Work Packages. This is the layer that translates "what we are building" into "how we will build it."

**Entry Criteria:**
- PEG-3 exit criteria met
- Product Scope approved by Product Owner

**Inputs:**
- Approved Product Scope
- PEF_ROADMAP_TEMPLATE.md
- PEF_BACKLOG_TEMPLATE.md
- PEF_WORK_PACKAGE_TEMPLATE.md

**Activities:**
1. **Roadmap:** Define delivery phases with objectives, deliverables, dependencies, and exit criteria per phase. Phases must follow this minimum structure:
   - Phase 0: Governance Activation
   - Phase 1: Foundation (core platform/modules)
   - Phase N: Extended Capabilities (additional modules, custom development)
   - Phase N+1: Integrations
   - Phase N+2: Testing and Stabilisation
   - Phase N+3: Deployment
   - Phase N+4: Template Extraction (if applicable)

2. **Backlog:** Generate all backlog items required to implement the product. Rules:
   - Every sub-capability in the Capability Map must produce at least one backlog item
   - Every approval workflow must produce a dedicated backlog item
   - Every integration must produce a dedicated backlog item
   - Every dashboard and reporting requirement must produce a dedicated backlog item
   - Every custom module must produce a specification item AND a development item (spec before dev — mandatory)
   - Every security/access requirement must produce a backlog item
   - Classify each item: Must Have / Should Have / Could Have

3. **Work Packages:** Group related backlog items into executable units. Rules:
   - Each work package has a single clear objective
   - Scope, dependencies, deliverables, and acceptance criteria are explicit
   - Complexity classified: Small / Medium / Large / Very Large
   - Governance reviews required are identified
   - Work packages follow approved spec-before-dev sequencing for custom modules

**Outputs:**
- Roadmap (completed PEF_ROADMAP_TEMPLATE.md)
- Backlog (completed PEF_BACKLOG_TEMPLATE.md)
- Work Packages (completed PEF_WORK_PACKAGE_TEMPLATE.md)

**Exit Criteria:**
- Every Capability Area from Product Scope maps to at least one backlog item
- Every backlog item maps to a work package
- Every approval workflow has a dedicated backlog item and work package scope entry
- Every integration has a dedicated backlog item
- All custom module spec items precede their development items in both backlog and roadmap
- No Must Have item is assigned to Phase N+2 or later without documented justification

---

### PEG-5 — Coverage Validation

**Purpose:** Independently verify that every requirement in the Product Scope is represented in the Roadmap, Backlog, and Work Packages. Identify all omissions and scope reductions before development is authorised.

This stage exists because omissions reliably occur during PEG-4. Coverage Validation is not optional and cannot be skipped.

**Entry Criteria:**
- PEG-4 exit criteria met
- Roadmap, Backlog, and Work Packages complete

**Inputs:**
- Approved Product Scope
- Roadmap
- Backlog
- Work Packages
- PEF_COVERAGE_VALIDATION_TEMPLATE.md

**Activities:**
1. For every Capability Area in the Product Scope, verify presence in each operational document:
   - Is it in the Roadmap (which phase)?
   - Is it in the Backlog (which item IDs)?
   - Is it in the Work Packages (which WP)?
2. For every sub-capability, repeat the check
3. For every approval workflow, verify dedicated coverage
4. For every integration, verify dedicated coverage
5. For every dashboard/report, verify dedicated coverage
6. For every custom module, verify spec item, development item, and test item
7. Score coverage using the Coverage Scoring Model (Section 7)
8. Classify all findings: Omission / Scope Reduction / Partial Coverage
9. Produce the Coverage Validation Report
10. If score < 95%: proceed to remediation (PEG-5R) before PEG-6

**PEG-5R — Coverage Remediation:**
- For each finding, implement the minimum targeted change to close the gap
- Preserve all existing IDs; add new IDs sequentially
- Do not modify Roadmap or Project State unless a new phase is required
- After remediation, re-run coverage check on all changed items
- Re-score; must reach ≥95% before proceeding

**Outputs:**
- Coverage Validation Report (completed PEF_COVERAGE_VALIDATION_TEMPLATE.md)
- Remediated Backlog and Work Packages (if PEG-5R required)
- Coverage Score

**Exit Criteria:**
- Coverage Score ≥ 95% across all four documents
- All Omissions resolved
- All Scope Reductions documented with Product Owner acceptance or resolved
- Coverage Validation Report signed by Product Engineering Team lead

---

### PEG-6 — Development Authorisation

**Purpose:** Formally authorise development to begin. This is the single hardest gate in the PEF. Nothing proceeds to implementation without this.

**Entry Criteria:**
- PEG-5 exit criteria met
- Coverage Score ≥ 95%
- Governance Activation Gate: all checks PASS
- Product Transfer Package assembled

**Inputs:**
- Approved Product Scope
- Validated Roadmap, Backlog, Work Packages
- Coverage Validation Report (score ≥ 95%)
- Governance Gate Report (all PASS)
- PEF_PRODUCT_APPROVAL_TEMPLATE.md

**Activities:**
1. Confirm all PEG-1 through PEG-5 exit criteria are met
2. Confirm Governance Gate: all five gates PASS (see Section 12)
3. Assemble Product Transfer Package:
   - Product Transfer Package document (complete product definition for the development team)
   - NEXT_ACTION.md (immediate first action for development team)
   - All operational documents (Scope, Roadmap, Backlog, Work Packages)
   - Coverage Validation Report
   - Governance Gate Report
4. Present for Product Owner signature
5. Present for Governance Team confirmation
6. Issue Development Authorisation

**Outputs:**
- Signed Product Approval document (PEF_PRODUCT_APPROVAL_TEMPLATE.md)
- Product Transfer Package
- NEXT_ACTION.md

**Exit Criteria:**
- Product Approval document signed by Product Owner AND Governance Team
- Governance Gate all PASS
- Product Transfer Package complete and transferred to development team
- Development team confirms receipt and understanding

**Non-negotiable rule:** If the Governance Gate has any FAIL at this stage, development does not begin. The FAIL is remediated and the gate is re-run.

---

### PEG-7 — Development Execution and QA

**Purpose:** Govern the development team's execution against the authorised product definition. The PEF does not prescribe the development methodology — it prescribes the governance that must operate around it.

**Entry Criteria:**
- PEG-6 exit criteria met
- Signed Product Approval document in repository
- Product Transfer Package loaded by development team

**Inputs:**
- Signed Product Approval document
- Product Transfer Package
- All operational documents

**Activities (governance obligations on development team):**
1. Session Start Protocol: read NEXT_ACTION.md, CONTROL_TOWER.md, PRODUCT_BACKLOG, relevant Work Package before any work
2. Implement work packages in sequence per approved Roadmap
3. Produce test evidence against each work package acceptance criterion before marking Done
4. Update Product Memory System after every milestone (nine mandatory files — see Section 8)
5. No scope changes without Product Owner approval and updated Product Approval document
6. All custom modules: spec approved before development begins (enforced by Backlog sequencing)
7. UAT: QA Team produces test plan; client users execute; defects resolved; sign-off obtained
8. Session End Protocol: update all nine memory files; commit; push

**Outputs:**
- Implemented and tested product
- Test evidence for all acceptance criteria
- UAT sign-off
- Updated Product Memory System (current at all times)

**Exit Criteria:**
- All Must Have backlog items: Done
- All acceptance criteria: passed and evidenced
- UAT signed off by Product Owner
- Zero open critical defects
- Product Memory System current and committed

---

### PEG-8 — Template Extraction and Registry Contribution

**Purpose:** Extract all reusable assets from the delivered product and contribute them to the Software Factory Template Registry. This is the "Build Once, Reuse Many Times" stage that makes the Software Factory more capable with every engagement.

**Entry Criteria:**
- PEG-7 exit criteria met
- Product in production
- Asset Classification Register from PEG-3 available

**Inputs:**
- Asset Classification Register
- Delivered product (all modules, configurations, governance documents)
- Software Factory Template Registry

**Activities:**
1. For every asset classified Generic Reusable or Sector Reusable in PEG-3:
   a. Strip all client-specific data, branding, and references
   b. Parameterise hard-coded client values (thresholds, names, codes)
   c. Document the asset: purpose, prerequisites, configuration steps, limitations
   d. Test the stripped asset functions independently of the client deployment
2. Contribute to Template Registry with classification, version, source engagement, and known limitations
3. Update the Registry index
4. Notify Software Factory team of new contributions

**Outputs:**
- Extracted, stripped, parameterised reusable assets
- Registry contribution entries
- Updated Template Registry index

**Exit Criteria:**
- All Generic Reusable assets contributed to Registry
- All Sector Reusable assets contributed to Registry
- Each contribution documented and tested
- Registry index updated

---

## SECTION 5 — MANDATORY DELIVERABLES

The following deliverables are required on every PEF engagement. None may be omitted without Governance Team approval.

| ID | Deliverable | Produced at | Approved by | Template |
|----|------------|------------|------------|---------|
| D-01 | PEG-1 Requirements Register | PEG-1 | Product Engineering Team | None — free-form |
| D-02 | Open Items Log | PEG-1 | Product Engineering Team | None — free-form |
| D-03 | Capability Map | PEG-2 | Product Engineering Team | PEF_CAPABILITY_MAP_TEMPLATE.md |
| D-04 | Approval Framework | PEG-2 | Product Engineering Team | None — structured table |
| D-05 | Integration Map | PEG-2 | Product Engineering Team | None — structured table |
| D-06 | Custom Module Register | PEG-2 | Product Engineering Team | None — structured table |
| D-07 | Product Scope | PEG-3 | Product Owner | PEF_PRODUCT_SCOPE_TEMPLATE.md |
| D-08 | Asset Classification Register | PEG-3 | Product Engineering Team | Part of D-07 |
| D-09 | Roadmap | PEG-4 | Product Engineering Team | PEF_ROADMAP_TEMPLATE.md |
| D-10 | Backlog | PEG-4 | Product Engineering Team | PEF_BACKLOG_TEMPLATE.md |
| D-11 | Work Packages | PEG-4 | Product Engineering Team | PEF_WORK_PACKAGE_TEMPLATE.md |
| D-12 | Coverage Validation Report | PEG-5 | Product Engineering Team lead | PEF_COVERAGE_VALIDATION_TEMPLATE.md |
| D-13 | Remediated Backlog and Work Packages (if required) | PEG-5R | Product Engineering Team | Updates to D-10, D-11 |
| D-14 | Governance Gate Report | PEG-6 | Governance Team | Part of D-15 |
| D-15 | Product Approval document | PEG-6 | Product Owner + Governance Team | PEF_PRODUCT_APPROVAL_TEMPLATE.md |
| D-16 | Product Transfer Package | PEG-6 | Product Engineering Team | Project-specific |
| D-17 | NEXT_ACTION.md | PEG-6 | Product Engineering Team | Part of D-16 |
| D-18 | UAT Test Plan | PEG-7 | QA Team | Project-specific |
| D-19 | UAT Sign-off | PEG-7 | Product Owner | Project-specific |
| D-20 | Registry Contributions | PEG-8 | Governance Team | Per Registry standard |
| D-21 | Discovery Report | PEG-7 (pre-implementation) | Product Engineering Team | PEF_DISCOVERY_REPORT_TEMPLATE.md |

**D-21 is a mandatory PEF deliverable.** The development team (or Autonomous Agent Team) must produce a Discovery Report before any implementation code is written (see Section 9.2). For AI agents this requirement is unconditional. The Product Engineering Team reviews and accepts the Discovery Report before implementation begins; any conflict with the Product Transfer Package assumptions is resolved first.

### 5.1 PEF Template Library

The PEF template library comprises the following nine templates. All are maintained in `templates/` and versioned with the framework.

| Template | Template ID | Deliverable | Produced at |
|----------|-------------|------------|-------------|
| PEF_PRODUCT_SCOPE_TEMPLATE.md | PEF-TPL-001 | D-07 Product Scope | PEG-3 |
| PEF_ROADMAP_TEMPLATE.md | PEF-TPL-002 | D-09 Roadmap | PEG-4 |
| PEF_BACKLOG_TEMPLATE.md | PEF-TPL-003 | D-10 Backlog | PEG-4 |
| PEF_WORK_PACKAGE_TEMPLATE.md | PEF-TPL-004 | D-11 Work Packages | PEG-4 |
| PEF_COVERAGE_VALIDATION_TEMPLATE.md | PEF-TPL-005 | D-12 Coverage Validation Report | PEG-5 |
| PEF_PRODUCT_APPROVAL_TEMPLATE.md | PEF-TPL-006 | D-15 Product Approval | PEG-6 |
| PEF_DISCOVERY_REPORT_TEMPLATE.md | PEF-TPL-007 | D-21 Discovery Report | PEG-7 (pre-implementation) |
| PEF_CAPABILITY_MAP_TEMPLATE.md | PEF-TPL-008 | D-03 Capability Map | PEG-2 |
| PEF_SCOPE_CHANGE_REQUEST_TEMPLATE.md | PEF-TPL-009 | Scope change control (Section 12.3) | Any time after Gate 3 |

*Templates PEF-TPL-007 through PEF-TPL-009 were added in v1.1 per validation report SF-VAL-PEF-001 (P1 enhancements).*

---

## SECTION 6 — COVERAGE VALIDATION STANDARD

### 6.1 Purpose

Coverage Validation is the formal process of verifying that every requirement in the Product Scope is fully and correctly represented in the Roadmap, Backlog, and Work Packages. It is the single most important quality check in the PEF.

### 6.2 Coverage Requirements

A requirement is considered **Fully Covered** when:
- It is present in the Roadmap (assigned to a phase)
- It has at least one dedicated Backlog item with a unique ID
- It is represented in the scope of at least one Work Package
- Its Acceptance Criterion in the Product Scope is traceable to an Acceptance Criterion in the Work Package

A requirement is **Partially Covered** when it appears in some but not all documents, or when coverage is at the wrong level of granularity (e.g. the capability area is present but a sub-capability is missing).

A requirement is an **Omission** when it is present in the Product Scope but absent from one or more of Roadmap, Backlog, or Work Packages.

A **Scope Reduction** occurs when the operational documents cover a requirement more narrowly than the Product Scope defines it, resulting in an implementation that would fail the Product Scope acceptance criterion.

### 6.3 Coverage Check Sequence

For every item in the Product Scope, validate in this sequence:

1. **Capability Areas** — is each CA represented in Roadmap, Backlog, and Work Packages?
2. **Sub-Capabilities** — is each sub-capability represented as a backlog item or explicit work package scope entry?
3. **Approval Workflows** — does each approval type from the Approval Framework have a dedicated backlog item and work package scope entry?
4. **Integrations** — does each integration from the Integration Map have a dedicated backlog item?
5. **Custom Modules** — does each custom module have a specification item, a development item, and a test item?
6. **Dashboards and Reports** — does each reporting requirement have a dedicated backlog item?
7. **Security and Access** — are all access control requirements backlogged?
8. **Deferred Items** — are all items classified as Future or Deferred explicitly present in the backlog with a Deferred status?
9. **Acceptance Criteria** — does each Acceptance Criterion in the Product Scope trace to at least one backlog item's acceptance criteria?

### 6.4 Coverage Validation Rules

| Rule | Description |
|------|-------------|
| CVR-01 | Every Capability Area must appear in all three operational documents |
| CVR-02 | Every sub-capability must appear as a dedicated Backlog item or as an explicit named entry in a Work Package scope |
| CVR-03 | Approval workflows must never be folded into a parent capability backlog item — they require their own item |
| CVR-04 | Integrations must never be folded into department build items — they require their own Phase 4 item (or Phase 3 if configuration, not testing) |
| CVR-05 | Custom module specification items must precede development items; this ordering must be enforced in the Roadmap and Backlog |
| CVR-06 | Deferred items must appear in the Backlog with status Deferred and a Could Have classification; they must not simply be absent |
| CVR-07 | Scope Reductions must be formally accepted by the Product Owner or resolved before PEG-6 |
| CVR-08 | Partial Coverage findings are treated as Omissions for scoring purposes unless explicitly justified |

---

## SECTION 7 — COVERAGE SCORING MODEL

### 7.1 Scoring Methodology

Coverage is scored against a checklist of all requirements. Each requirement is scored independently.

| Score | Condition |
|-------|-----------|
| 1.0 | Fully Covered — present in all three operational documents with traceable AC |
| 0.5 | Partially Covered — present in some documents but not all, or AC not traceable |
| 0.0 | Omission — absent from one or more documents |

**Overall Coverage Score** = (Sum of all requirement scores) / (Total requirements) × 100%

### 7.2 Scoring Tiers

| Score | Tier | Consequence |
|-------|------|-------------|
| 98–100% | Exemplary | Proceed to PEG-6; note any 0.5 items for monitoring |
| 95–97% | Acceptable | Proceed to PEG-6 after Product Owner accepts residual 0.5 items in writing |
| 90–94% | Remediation Required | Execute PEG-5R; re-score before PEG-6 |
| < 90% | Failed | Full remediation required; scope review meeting with Product Owner before re-scoring |

### 7.3 Weighted Categories

Not all requirements carry equal risk. Apply weighting when calculating the score for escalation decisions:

| Category | Weight |
|----------|--------|
| Capability Areas | 1.0× |
| Approval Workflows | 1.5× (approval failures are high-risk) |
| Integrations | 1.5× (integration failures are high-risk) |
| Custom Module Specs | 2.0× (missing spec = certain development failure) |
| Security and Access | 2.0× (missing access control = production security risk) |
| Dashboards and Reports | 0.75× (typically lower risk to defer) |
| Deferred Items | 0.5× (by definition not in current scope) |

### 7.4 Coverage Score Calculation Example

```
Total requirements: 40
Custom module spec items (×2.0): 3 items × 2.0 = 6.0 weighted
Approval workflows (×1.5): 5 items × 1.5 = 7.5 weighted
Integrations (×1.5): 4 items × 1.5 = 6.0 weighted
Security items (×2.0): 4 items × 2.0 = 8.0 weighted
Dashboards (×0.75): 4 items × 0.75 = 3.0 weighted
Remaining (×1.0): 20 items × 1.0 = 20.0 weighted

Total weighted denominator: 50.5

Score if 2 integrations partially covered (0.5 each):
Deduction: 2 × 1.5 × (1.0 – 0.5) = 1.5
Score: (50.5 – 1.5) / 50.5 × 100% = 97.0% → Acceptable tier
```

---

## SECTION 8 — PRODUCT AUTHORITY HIERARCHY

### 8.1 Document Authority Chain

At any point in an engagement, the following hierarchy determines which document is authoritative for any given question:

```
Product Scope                    ← What are we building? (PEG-3)
         ↓
Roadmap                          ← In what sequence? (PEG-4)
         ↓
Backlog                          ← What are the implementation items? (PEG-4)
         ↓
Work Packages                    ← What exactly does each item involve? (PEG-4)
         ↓
Coverage Validation Report       ← Has everything been covered? (PEG-5)
         ↓
Product Approval Document        ← Is development authorised? (PEG-6)
```

### 8.2 Conflict Resolution

When documents conflict, the higher authority governs. The development team must raise the conflict with the Product Engineering Team, who resolves it and updates the lower-authority document. No conflicts are resolved silently.

### 8.3 Product Memory System

The Product Memory System is the set of repository-resident files that enable any team member, AI agent, or future session to understand current programme state without requiring access to past conversations or undocumented context.

**Mandatory files:**

| File | Authority for | Update trigger |
|------|--------------|----------------|
| `docs/NEXT_ACTION.md` | Immediate next action | Every session end |
| `docs/PRODUCT_STATE_INDEX.md` | Session initialisation sequence | On creation; update when files change |
| `docs/CONTROL_TOWER.md` | Current phase, milestone, completion | Every milestone |
| `docs/PRODUCT_BACKLOG.md` | All work item statuses | Every session |
| `docs/MILESTONE_REGISTER.md` | Milestone history | On milestone completion |
| `docs/DECISION_LOG.md` | All product decisions | When any decision is made |
| `docs/IMPLEMENTATION_HISTORY.md` | Completed milestone records | On milestone completion |
| `CHANGELOG.md` | All programme changes | Every session |
| `docs/session_logs/YYYY-MM-DD.md` | Session record | Every session end |

**The product must never live in a chat window.** It lives in the repository.

### 8.4 NEXT_ACTION.md — First File Rule

`docs/NEXT_ACTION.md` must be the first file read at the start of every development session, by every team member and every AI agent. It is a single, always-current file — maximum one page — that answers the question "What do we do next?" without requiring the reader to process any other document.

---

## SECTION 9 — DEVELOPMENT HANDOVER STANDARD

### 9.1 Product Transfer Package

The Product Transfer Package is the formal handover artefact from the Product Engineering Team to the Software Development Team. It is assembled at PEG-6 and must be complete and self-contained.

**Mandatory contents:**

| Item | Description |
|------|-------------|
| Product Transfer Document | Complete product definition: vision, scope, platform profile, department requirements, module mapping, approval framework, custom modules, capability map, template registry, backlog summary, roadmap summary, milestone plan, governance requirements, Governance Gate, discovery requirements, implementation sequence, session start rules, session end rules, boundary definitions |
| NEXT_ACTION.md | First action for the development team |
| Product Scope | Full approved product scope document |
| Roadmap | Full roadmap |
| Backlog | Full backlog with all IDs |
| Work Packages | All work packages |
| Coverage Validation Report | Including remediation record |
| Product Approval Document | Signed copy |
| Repository Scaffold | All Product Memory System files pre-populated and ready to commit |

### 9.2 Discovery-Before-Implementation Rule

**The development team must run a full discovery sequence before writing a single line of implementation code.** For AI agents, this rule is unconditional.

Discovery must verify:
- Repository path, Git status, current branch, commit history
- Remote configuration and branch protection
- CI workflow status
- Platform version and edition (e.g. Odoo 17 CE vs EE — critical)
- Database existence and name
- Any installed modules that conflict with the authorised platform profile
- Existing custom modules
- Backup status

The development team produces a Discovery Report (deliverable D-21) using **PEF_DISCOVERY_REPORT_TEMPLATE.md** before implementation begins. The Product Engineering Team reviews the Discovery Report. If the discovered state conflicts materially with the Product Transfer Package assumptions, the conflict is logged in the report's Conflicts Register and resolved before implementation proceeds.

### 9.3 Session Boundary Protocol

**Session Start:** Every development session — human or AI — begins by reading, in order:
1. `docs/NEXT_ACTION.md`
2. `docs/PRODUCT_STATE_INDEX.md`
3. `docs/CONTROL_TOWER.md`
4. Relevant `docs/PRODUCT_BACKLOG.md` section
5. Current work package
6. Git status

Only then does implementation work begin.

**Session End:** Every development session ends by updating all nine Product Memory System files and committing in a single `[SESSION-END] YYYY-MM-DD governance update` commit before the session closes.

---

## SECTION 10 — TEMPLATE EXTRACTION STANDARD

### 10.1 Software Factory Template Registry

The Software Factory Template Registry is the central repository of reusable assets accumulated across all engagements. It is the mechanism by which the Software Factory becomes more capable and more efficient with every delivery.

### 10.2 Asset Classification

Every deliverable produced on a Software Factory engagement is classified in PEG-3 and confirmed at PEG-8:

| Class | Definition | Extraction action |
|-------|-----------|------------------|
| Generic Reusable | Applicable to any deployment of the same technology, regardless of sector or client | Extract and contribute to Registry — Generic tier |
| Sector Reusable | Applicable to all clients in the same sector (government, NGO, manufacturing, etc.) | Extract and contribute to Registry — Sector tier |
| Client Specific | Contains client-specific data, logic, branding, or statutory requirements | Do not extract; remains in client engagement only |

### 10.3 Extraction Rules

| Rule | Description |
|------|-------------|
| ER-01 | No client-specific data may appear in any extracted asset |
| ER-02 | All threshold values, statutory rates, and client-specific parameters must be replaced with clearly labelled placeholder variables (e.g. `{{APPROVAL_THRESHOLD_LEVEL_1}}`) |
| ER-03 | All client names, staff names, vendor names, and organisational references must be stripped |
| ER-04 | Each extracted asset must be independently testable — it must function without the client deployment |
| ER-05 | Each Registry contribution must include: asset name, version, source engagement, classification, prerequisites, configuration steps, known limitations, and extraction date |
| ER-06 | Generic Reusable assets are contributed in the same release cycle as the client deployment |
| ER-07 | Sector Reusable assets are contributed after client sign-off on PEG-7 |

### 10.4 Build Once, Reuse Many Times

When starting a new engagement, the Product Engineering Team must:
1. Search the Software Factory Template Registry before specifying any custom development
2. If a Registry asset exists that meets the requirement: use it, configure it, contribute improvements back
3. If no Registry asset exists: build it to the Generic Reusable or Sector Reusable standard where possible
4. Never build the same thing twice without a documented justification

---

## SECTION 11 — QUALITY ASSURANCE REQUIREMENTS

### 11.1 QA Touchpoints by Stage

| Stage | QA Activity | QA Deliverable |
|-------|------------|----------------|
| PEG-2 | Review Capability Map for completeness | Signed capability map review |
| PEG-3 | Review Acceptance Criteria for testability | AC review notes |
| PEG-5 | Independent coverage check review | Concurrence on Coverage Score |
| PEG-6 | Confirm UAT plan is present in transfer package | UAT readiness confirmation |
| PEG-7 | Produce UAT test plan; execute UAT; certify defect resolution | UAT Sign-off |

### 11.2 Acceptance Criteria Quality Standard

All Acceptance Criteria must meet these standards:

| Standard | Description |
|----------|-------------|
| Testable | Can be verified by a person or automated test without interpretation |
| Unambiguous | Has exactly one reading — no "should" or "might" |
| Boundary-defined | States the specific condition (e.g. "above ₦500,000 threshold" not "above threshold") |
| Evidence-specified | States what evidence confirms the criterion is met |
| Independent | Can be tested without reference to another criterion |

**Anti-patterns to reject at QA:**
- "Works correctly" — not testable
- "Is fast" — no boundary defined
- "Matches the TO-BE" — requires interpretation; the AC must restate the requirement
- "TBD" — not acceptable at PEG-5 or later

### 11.3 Test Evidence Standard

The development team must produce test evidence for every acceptance criterion before the item is marked Done in the Backlog. Acceptable evidence formats:

| Format | Acceptable for |
|--------|---------------|
| Screenshot with timestamp | UI behaviour, state transitions, approval flows |
| Database query result | Data integrity, record creation, status values |
| Log extract | Automated actions, scheduled actions, notifications |
| Automated test result | Any criterion amenable to automated testing |
| Written test record (tester, date, result, observation) | Where automated test or screenshot is not applicable |

Assertions without evidence are not accepted.

### 11.4 Defect Severity Classification

PEG-7 exit criteria, Gate 4, and Section 13 (SC-10) all require "zero open critical defects". The framework therefore defines what makes a defect Critical, High, Medium, or Low, using objective criteria so that two teams classify the same defect identically (closes OMI-04). Severity is assigned by the QA Team and confirmed by the Product Owner at Gate 4. Where a defect satisfies criteria for two levels, the **higher** severity applies.

| Severity | Objective criteria (any one qualifies) | Gate 4 effect |
|----------|----------------------------------------|---------------|
| **Critical** | Core business function unusable with no workaround; **or** data loss / data corruption; **or** security breach exposing data or access control; **or** a Must Have acceptance criterion cannot be met; **or** the system is down for all users. | **Blocks Gate 4.** Deployment cannot proceed while any Critical defect is open. |
| **High** | A primary capability fails but a manual or partial workaround exists; **or** a Should Have acceptance criterion fails; **or** incorrect output in a non-financial, non-statutory field; **or** an approval workflow misroutes but is recoverable. | Must be resolved or have a Product-Owner-accepted, time-boxed remediation plan before Gate 4. |
| **Medium** | A secondary or convenience feature is impaired; **or** a Could Have item fails; **or** a cosmetic-but-confusing UI fault that risks user error; **or** a reporting/dashboard discrepancy that does not affect transactional data. | Does not block Gate 4 if logged with an owner and target fix date. |
| **Low** | Cosmetic issue with no functional impact; **or** wording, formatting, or layout; **or** an enhancement request disguised as a defect. | Does not block any gate; tracked in the backlog. |

**Classification rules:**

| Rule | Description |
|------|-------------|
| DSR-01 | Severity is a function of impact and workaround availability — not of how hard the defect is to fix. |
| DSR-02 | "Zero open critical defects" (PEG-7 exit, Gate 4, SC-10) means zero defects classified Critical by these criteria. |
| DSR-03 | A data-loss, data-corruption, or security-exposure defect is always Critical regardless of frequency. |
| DSR-04 | A defect that breaks a Must Have acceptance criterion is at minimum High, and Critical if no workaround exists. |
| DSR-05 | Severity may be re-classified only with a logged reason; the original classification and the reason are retained. |
| DSR-06 | Disputed severity follows the Product Owner Refusal / dispute path only if it blocks a gate; otherwise the QA Team's classification stands. |

Defects are recorded in the project defect register with: ID, summary, severity (per this section), affected acceptance criterion, status, and evidence of resolution.

---

## SECTION 12 — APPROVAL GATES

### 12.1 Gate Structure

The PEF has four formal approval gates. No stage may proceed past its gate without the gate passing.

| Gate | At | Checked by | Required outcome |
|------|----|-----------|-----------------|
| Gate 1 — Scope Approval | End of PEG-3 | Product Owner | Product Scope signed |
| Gate 2 — Coverage Approval | End of PEG-5 | Product Engineering Team lead | Coverage Score ≥ 95% |
| Gate 3 — Development Authorisation | End of PEG-6 | Product Owner + Governance Team | Product Approval signed; Governance Gate all PASS |
| Gate 4 — Deployment Authorisation | End of PEG-7 | Product Owner + QA Team | UAT sign-off; zero critical defects |

### 12.2 Governance Activation Gate

The Governance Activation Gate is a pre-implementation checklist run at PEG-6 (and recommended at PEG-1). All checks must PASS before development is authorised.

**Gate A — Repository**

| Check | Pass Criterion |
|-------|---------------|
| Version control initialised | Repository exists and is accessible |
| Remote configured | Remote URL confirmed |
| Main branch protected | Direct push to main blocked |
| Feature branch workflow | Feature branches used; PR required for merge |

**Gate B — CI/CD**

| Check | Pass Criterion |
|-------|---------------|
| CI pipeline configured | At least one workflow executes on PR |
| Lint or static analysis | Configured and passing |
| Build verification | Build completes without error |

**Gate C — Governance Documents**

| Check | Pass Criterion |
|-------|---------------|
| NEXT_ACTION.md | Present and current |
| CONTROL_TOWER.md | Present and populated |
| PRODUCT_BACKLOG | Present and populated |
| MILESTONE_REGISTER | Present and populated |
| DECISION_LOG | Present and populated |
| CHANGELOG | Present and populated |
| PRODUCT_STATE_INDEX | Present |

**Gate D — Backup and Recovery**

| Check | Pass Criterion |
|-------|---------------|
| Backup strategy documented | `docs/BACKUP_STRATEGY.md` exists |
| Restore procedure documented | Restore steps present in backup strategy |
| Last backup confirmed | Backup file timestamp within 24 hours |

**Gate E — Product Readiness**

| Check | Pass Criterion |
|-------|---------------|
| Capability Map present | In repository or transfer package |
| Platform confirmed | Decision Log entry confirming platform and version |
| No prohibited modules | Platform audit confirms no prohibited modules installed |
| Coverage Score on file | Coverage Validation Report with score ≥ 95% |

**Gate result format:**
```
GOVERNANCE ACTIVATION GATE REPORT
===================================
Project: [Name]
Date: YYYY-MM-DD

Gate A — Repository:         PASS / FAIL ([n]/4)
Gate B — CI/CD:              PASS / FAIL ([n]/3)
Gate C — Governance Docs:    PASS / FAIL ([n]/7)
Gate D — Backup:             PASS / FAIL ([n]/3)
Gate E — Product Readiness:  PASS / FAIL ([n]/4)

OVERALL: PASS / FAIL ([n]/21 checks)

BLOCKERS:
  [Each FAIL with required action and owner]
```

### 12.3 Scope Change Control Procedure (Post-Gate 3)

Once Gate 3 (Development Authorisation) is signed, the Product Scope, Roadmap, Backlog, and Coverage Score are baselined. Any change after this point can **silently invalidate the approved Coverage Score** and cause development to proceed against uncovered requirements (closes OMI-05). This procedure governs every scope change raised after Gate 3 and before final deployment. It applies in addition to the existing Scope Change Register in `PEF_PRODUCT_APPROVAL_TEMPLATE.md` Section D — the register is the permanent ledger; this procedure is how an entry earns its place in it.

**No scope change is implemented until this procedure completes.**

**Step 1 — Raise.** The change is captured on a **Scope Change Request** using `PEF_SCOPE_CHANGE_REQUEST_TEMPLATE.md`, with a unique `SCR-NNN` ID. Any party may raise an SCR; the Product Engineering Team owns it thereafter.

**Step 2 — Impact assessment.** The Product Engineering Team completes the impact assessment (scope, acceptance criteria, backlog, work packages, roadmap, cost, timeline, security, custom modules, asset classification). No dimension may be left blank.

**Step 3 — Coverage re-validation trigger.** The SCR determines whether PEG-5 Coverage Validation must be re-run. Re-validation is **mandatory** when the change adds or alters any Capability Area, sub-capability, approval workflow, integration, custom module, security requirement, or acceptance criterion. If re-validation is triggered, the affected items are re-scored and must reach ≥ 95% before approval.

**Step 4 — Approval authority.**

| Change characteristic | Approval required |
|----------------------|-------------------|
| No new/changed CA, AC, or coverage-bearing item (e.g. clarification, cosmetic) | Product Owner approval |
| Adds or alters coverage-bearing items (triggers Step 3) | Product Owner approval **and** Governance Team confirmation that Coverage re-validated ≥ 95% |
| Changes the engagement boundary (adds a Capability Area or removes a Must Have) | Product Owner re-signature on the Product Approval document (new Gate 3 addendum) |

**Step 5 — Record in the ledger.** The approved SCR is recorded in `PEF_PRODUCT_APPROVAL_TEMPLATE.md` Section D using the **same SCR ID**. The Backlog, Work Packages, Roadmap, and (if re-run) the Coverage Validation Report are updated to reflect the change. The two records must never diverge.

**Step 6 — Implement.** Only after Steps 1–5 are complete may the change be implemented, with test evidence produced against any new or changed acceptance criterion per Section 11.3.

**Rule SCC-01:** A scope change that triggers Coverage re-validation but is implemented without it is a governance breach. Any work built against an un-revalidated change must be re-validated before it can be marked Done.

**Rule SCC-02:** If the Product Owner refuses to approve or refuses to re-sign a boundary-changing SCR, the Product Owner Refusal Escalation Procedure (Section 3.2) applies.

---

## SECTION 13 — SUCCESS CRITERIA

A PEF engagement is considered successfully completed when all of the following are true:

| ID | Criterion |
|----|-----------|
| SC-01 | All four approval gates passed in sequence |
| SC-02 | Coverage Score ≥ 95% confirmed and on file |
| SC-03 | All Must Have backlog items: Done, with test evidence |
| SC-04 | All Acceptance Criteria passed and evidenced |
| SC-05 | UAT sign-off obtained from Product Owner |
| SC-06 | Product deployed to production without data loss or critical system failure |
| SC-07 | Product Memory System current and committed at time of deployment |
| SC-08 | All Generic Reusable and Sector Reusable assets contributed to Template Registry |
| SC-09 | Registry contribution documented and indexed |
| SC-10 | No open critical defects at point of handover |

---

## APPENDIX A — PEF STAGE SUMMARY

| Stage | Name | Key Output | Gate |
|-------|------|-----------|------|
| PEG-1 | Requirements Consolidation | Requirements Register, Platform Profile | None — entry check only |
| PEG-2 | Capability Mapping | Capability Map, Approval Framework, Integration Map | None — internal review |
| PEG-3 | Product Scope Definition | Product Scope document | Gate 1: Product Owner signature |
| PEG-4 | Operational Planning | Roadmap, Backlog, Work Packages | None — proceeds to PEG-5 |
| PEG-5 | Coverage Validation | Coverage Validation Report (≥95%) | Gate 2: PET lead signature |
| PEG-5R | Coverage Remediation | Remediated documents | Re-score gate: ≥95% |
| PEG-6 | Development Authorisation | Product Approval, Transfer Package | Gate 3: PO + Governance signature |
| PEG-7 | Development Execution and QA | Tested product, UAT sign-off | Gate 4: PO + QA sign-off |
| PEG-8 | Template Extraction | Registry contributions | Governance Team confirmation |

---

## APPENDIX B — LESSONS INCORPORATED FROM NADF REFERENCE IMPLEMENTATION

The following lessons from the NADF ERP Programme (2026) are formally incorporated into this framework:

| Lesson | Framework Response |
|--------|-------------------|
| Product Scope generation alone is insufficient | PEG-4 Operational Planning is a mandatory separate stage |
| Operational planning documents must be generated | Roadmap, Backlog, and Work Packages are all mandatory deliverables (D-09, D-10, D-11) |
| Coverage validation is mandatory | PEG-5 is a required stage; cannot be skipped |
| Coverage gaps must be remediated | PEG-5R is a defined sub-stage with its own exit criteria |
| Coverage must be revalidated after remediation | PEG-5R requires re-scoring to ≥95% before PEG-6 |
| Development cannot begin without approval | Gate 3 (PEG-6) requires signatures from both Product Owner and Governance Team |
| Swimlanes are requirements inputs, not implementation workstreams | Stated explicitly in PEG-1 (inputs) and Section 2.2 (what PEF does not govern) |
| Product Scope becomes the authoritative implementation source | Section 8.1 Product Authority Hierarchy |
| Reusable assets must be identified | PEG-3 Asset Classification; PEG-8 Template Extraction |
| Build Once, Reuse Many Times must be supported | Section 10 Template Extraction Standard; Section 10.4 Build Once rule |
| Enterprise vs Community platform assumptions cause cascading errors | PEG-1 platform confirmation activity; PEG-2 Enterprise Gap Protocol; Governance Gate E |
| Sub-capability omissions are the most common coverage failure | CVR-02 mandates sub-capability coverage; Section 6.3 coverage check sequence |
| Approval workflows are routinely under-specified | CVR-03 mandates dedicated approval workflow backlog items; 1.5× weighting in scoring |
| Session rules must be repository-resident | Section 9.3 Session Boundary Protocol; NEXT_ACTION.md First File Rule |

---

*Software Factory Product Engineering Framework v1.1*  
*This document is a Software Factory governance standard. It is not client-specific.*  
*v1.1 implements P1 enhancements from validation report SF-VAL-PEF-001 — see `docs/PEF_V1_1_CHANGELOG.md`.*  
*Next review: 2027-06-21 or after the third reference implementation, whichever comes first.*
