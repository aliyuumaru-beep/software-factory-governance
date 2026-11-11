# Agent OS v2.0 — Design Document

---

**Document:** DESIGN-AGENT-OS-V2
**Enhancement:** AOP-013 Execution Authority Framework
**Version:** 1.0
**Date:** 2026-06-25
**Author:** A1 Master Orchestrator

---

## 1. Overview

Agent OS v2.0 is the operational evolution of Agent OS v1.0. The fundamental agent structure (A1, G1-G3, D1-D4) is unchanged. The execution authority model is formalised, removing the Human Sponsor from routine operational decisions.

The three defining properties of Agent OS v2.0 are:

1. **Authority-grounded execution** — every execution action is traceable to a formal authority grant
2. **Governance-driven approval** — G1/G2/G3 reviews replace human confirmation for EA-1 through EA-5
3. **Portfolio-scale readiness** — multiple project pods operate concurrently without human bottleneck

---

## 2. Architecture

### 2.1 Agent Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│  Human Sponsor                                               │
│  EA-6 | Scope Changes | Budget | Portfolio | Escalation      │
└──────────────────────┬──────────────────────────────────────┘
                       │ (strategic decisions only)
┌──────────────────────▼──────────────────────────────────────┐
│  A1 — Master Orchestrator                                    │
│  Coordinates pods · Issues authority · Maintains register    │
└──────┬─────────────┬─────────────┬───────────────────────── ┘
       │             │             │
┌──────▼──┐    ┌─────▼──┐   ┌─────▼──┐
│   G1    │    │   G2   │   │   G3   │
│ Arch &  │    │Quality │   │Security│
│  Odoo   │    │ & Docs │   │& Change│
└──────┬──┘    └─────┬──┘   └─────┬──┘
       └─────────────┴─────────────┘
                     │ (concurrent reviews)
┌────────────────────▼────────────────────────────────────────┐
│  Project Pod                                                 │
│  D1 Functional Architect                                     │
│  D2 Solution Builder      ← verifies authority before exec  │
│  D3 Quality & Validation                                     │
│  D4 Knowledge & Documentation                                │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Portfolio Configuration

Agent OS v2.0 supports three concurrent project pods:

| Pod | Project | Orchestrator | Status |
|-----|---------|-------------|--------|
| POD-NADF | NADF ERP MVP | A1-NADF | Pilot pod |
| POD-FAMOIL | FamOil ERP | A1-FAMOIL | Adoption phase 2 |
| POD-WAMACARE | WamaCare NGO | A1-WAMACARE | Adoption phase 3 |

Governance agents (G1, G2, G3) are shared across all pods. A1 is instantiated per pod.

---

## 3. Execution Authority Lifecycle

### 3.1 Authority Request Flow

```
Step 1 — D2 IDENTIFIES WORK
  D2 determines an execution action is required.
  D2 classifies the action against EA-1 through EA-6.
  D2 prepares authority request: class, scope, actions list.

Step 2 — A1 INITIATES REVIEW
  A1 receives authority request.
  A1 logs request in Execution Authority Register (status: Pending).
  A1 routes to G1, G2, G3 for concurrent review.
  A1 applies approval matrix to determine required reviewers.

Step 3 — GOVERNANCE REVIEW (concurrent)
  G1: Classifies architectural risk; confirms authority class.
  G2: Validates traceability; confirms documentation completeness.
  G3: Assesses security impact; confirms rollback plan.
  Each reviewer returns: APPROVED | DENIED | CONDITIONAL

Step 4 — A1 DECISION
  All required reviewers approved → A1 issues EXECUTION AUTHORITY GRANTED
  Any required reviewer denied → A1 issues EXECUTION AUTHORITY DENIED
  Conditional approvals → A1 resolves conditions; re-reviews if needed
  Escalation trigger present → A1 routes to Human Sponsor

Step 5 — D2 EXECUTION
  D2 verifies authority ID is Active.
  D2 references authority ID in execution record.
  D2 confirms action is within authorized scope.
  D2 executes.
  D2 reports outcome to A1.

Step 6 — A1 CLOSES AUTHORITY
  A1 updates register: status EXECUTED, outcome recorded.
  A1 logs in AUTHORITY_DECISION_LOG.md.
  Human Sponsor informed of completion.
```

### 3.2 Authority Status Lifecycle

```
Created → Pending Review → Under Review → Granted → Active → Executed
                                       ↓
                                     Denied
                                       ↓
                                   (no execution)

Active → Revoked (by A1 at any time)
```

---

## 4. A1 Authority Issuance Protocol

When issuing authority decisions, A1 must use the following format:

### GRANT Format

```
EXECUTION AUTHORITY GRANTED

Authority ID:        EA-{PROJECT}-WP{XX}-{NNN}
Authority Class:     EA-{N}
Project:             {PROJECT}
Work Package:        WP-{XX}
Authorized Actions:
  - {action 1}
  - {action 2}
Approvals:
  G1: Approved — {brief rationale}
  G2: Approved — {brief rationale}
  G3: Approved — {brief rationale}
Validity:            WP-{XX} only
Issued:              {ISO date}
Status:              Active

D2 must reference Authority ID EA-{PROJECT}-WP{XX}-{NNN} in all execution actions.
```

### DENY Format

```
EXECUTION AUTHORITY DENIED

Authority Request:   {description}
Authority Class:     EA-{N}
Blocking Review:     G{N} — {reviewer name}
Reason:              {reason for denial}
Resolution Required: {what must change before re-submission}
Status:              Denied

This authority request may be resubmitted after resolution.
```

### REVOKE Format

```
EXECUTION AUTHORITY REVOKED

Authority ID:        EA-{PROJECT}-WP{XX}-{NNN}
Revocation Reason:  {reason}
Effective:           {ISO date}
Impact:              All active execution under this ID must halt immediately.
Status:              Revoked

D2 must cease all actions under EA-{PROJECT}-WP{XX}-{NNN}.
```

---

## 5. D2 Execution Protocol

Under Agent OS v2.0, D2 must follow this protocol before any execution action:

```
1. Identify the action to be performed.
2. Locate the active authority grant for this work package.
3. Confirm the authority ID is Active (not Expired, Revoked, or Denied).
4. Confirm the action is listed in the Authorized Actions for the authority.
5. Reference the authority ID in the execution record.
6. Execute.
7. Report outcome to A1 for register update.
```

If any step fails, D2 must halt and report to A1. D2 must never execute without a valid authority reference.

---

## 6. Governance Review Protocol

### G1 Authority Review Checklist

```
□ Confirm architectural classification of the requested actions
□ Confirm appropriate EA class is assigned
□ Identify any architectural preconditions not met
□ Identify any architectural constraints on execution
□ Confirm no architectural decision is bypassed
□ Decision: APPROVED | DENIED | CONDITIONAL (with conditions)
```

### G2 Authority Review Checklist

```
□ Confirm authorized actions are traceable to acceptance criteria in the WP
□ Confirm documentation is complete before execution is authorized
□ Confirm acceptance criteria are sufficient and testable
□ Confirm no documentation is deferred that should precede execution
□ Decision: APPROVED | DENIED | CONDITIONAL
```

### G3 Authority Review Checklist

```
□ Assess security impact of authorized actions
□ Confirm change impact is within acceptable scope
□ Confirm rollback plan exists for the authorized actions
□ Confirm recovery readiness is adequate
□ Assess risk exposure; confirm within tolerance
□ Decision: APPROVED | DENIED | CONDITIONAL
```

---

## 7. Approval Matrix

See `06_APPROVAL_MATRIX.md` for the full matrix. Summary:

| Class | G1 | G2 | G3 | A1 |
|-------|----|----|----|----|
| EA-1 | Review | Optional | Optional | Auto |
| EA-2 | Review | Review | Optional | Auto |
| EA-3 | Review | Review | Review | Required |
| EA-4 | Review | Review | Review | Required |
| EA-5 | Review | Review | Review | Required |
| EA-6 | Review | Review | Review | Human Required |

"Auto" means A1 may grant immediately after G1 approval without a separate deliberation step.
"Required" means A1 must make an explicit decision after all required reviews complete.
"Human Required" means A1 routes to Human Sponsor regardless of governance review outcome.

---

## 8. Multi-Pod Operation

Under Agent OS v2.0, multiple pods operate concurrently. The shared governance agents serve all pods.

**Conflict management:** If G1, G2, or G3 is simultaneously reviewing authority requests from multiple pods, reviews are processed in order of EA class risk: EA-5 before EA-4, EA-4 before EA-3, etc. Within the same class, first-received first-reviewed.

**Cross-pod authority:** Authority grants are pod-specific. An EA-NADF grant cannot be applied to FAMOIL execution and vice versa.

**Shared governance learnings:** G1/G2/G3 may apply precedent from previous pod reviews when classifying similar requests. Precedent is advisory, not binding. Each request receives independent review.

---

## 9. Configuration — ACTIVE_AGENT_CONFIGURATION.md (v2.0)

The following replaces the v1.0 configuration:

```
Agent OS Version: 2.0
Autonomous Mode: Enabled
Governance Mode: Strict
Execution Authority: Enabled
Authority Classes: EA-1 through EA-6
EA-6 Requires Human: true
Authority Register Location: {PROJECT_ROOT}/EXECUTION_AUTHORITY_REGISTER.md
Authority Decision Log Location: {PROJECT_ROOT}/AUTHORITY_DECISION_LOG.md
Authority Validity Scope: Work Package
Default Escalation Policy: ESCALATION_POLICY.md
Default Milestone Model: SOFTWARE_FACTORY_STANDARD_MILESTONE_MODEL.md
Repository Governance: Enabled
Git Governance: Enabled
Template Extraction: Enabled
Asset Discovery: Enabled
Project Pods:
  - POD-NADF
  - POD-FAMOIL
  - POD-WAMACARE
Platform Profiles: Defined per Project Pod
Governance Agents: Shared
Delivery Agents: Per Project Pod
```

---

## 10. Design Constraints

1. AOP-013 does not modify Claude Code runtime permission prompts.
2. AOP-013 does not add new file system or shell permissions.
3. Authority grants do not accumulate across work packages.
4. G1/G2/G3 denial is blocking and cannot be overridden by A1.
5. EA-6 authority is never granted by A1 regardless of governance review outcome.
6. The Execution Authority Register is append-only; records are never deleted.

---

*Agent OS v2.0 Design Document — A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
