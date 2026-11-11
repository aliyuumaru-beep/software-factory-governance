# AOP-013 — Pilot Plan
## NADF Work Package 02 Pilot

> **SUPERSESSION NOTICE — D4 / 2026-06-25**
> The pilot work package reference throughout this document (WP-02) is superseded by
> Sponsor Decision AOP-013-SD-001 Condition 4. The operative pilot window is **WP-03
> and WP-04**, not WP-02. All other content in this document remains valid.
> Operative pilot plan: `enhancements/AOP-013/phase-b/02_NADF_PILOT_ACTIVATION_PACKAGE.md`

---

**Document:** PILOT-AOP-013
**Enhancement:** AOP-013 Execution Authority Framework
**Version:** 1.0 (superseded for pilot scope — see notice above)
**Date:** 2026-06-25
**Author:** A1 Master Orchestrator

---

## 1. Purpose

This document defines the plan for piloting Agent OS v2.0 on the NADF project pod using Work Package 02 (Finance Core) as the first live exercise of the Execution Authority Framework.

---

## 2. Pilot Objectives

1. Demonstrate that governance reviews generate execution authority in a real work package.
2. Demonstrate that A1 issues authority using the defined format.
3. Demonstrate that D2 executes under authority, referencing authority IDs.
4. Verify that the Execution Authority Register is maintained in real time.
5. Verify that the AUTHORITY_DECISION_LOG.md captures all decisions.
6. Verify that escalation triggers correctly route to the Human Sponsor.
7. Measure the governance overhead and confirm it is proportionate.

---

## 3. Pilot Scope

**Project Pod:** POD-NADF
**Work Package:** WP-02 — Finance Core (next scheduled WP after WP-01 closes)
**Environment:** NADF ERP development instance (localhost:8071, DB=NADF)
**Duration:** Full WP-02 execution under v2.0 (estimated 2-4 sessions)

The pilot does not affect:
- NADF work packages beyond WP-02
- FAMOIL project
- WAMACARE project
- Any production environment

---

## 4. Pilot Prerequisites

Before the pilot begins:

| Prerequisite | Responsible | Status |
|-------------|-------------|--------|
| AOP-013 Phase A deliverables complete | A1 | Complete |
| AOP-013 Phase B governance review complete | G1/G2/G3 | Pending |
| NADF agent prompts updated to v2.0 | A1 + D4 | Pending |
| EXECUTION_AUTHORITY_REGISTER.md created at nadf_erp root | A1 | Pending |
| AUTHORITY_DECISION_LOG.md created at nadf_erp root | A1 | Pending |
| ACTIVE_AGENT_CONFIGURATION.md incremented to v2.0 | A1 | Pending |
| WP-01 formally closed (PR #5 merged) | A1 | Pending |
| Human Sponsor informed of pilot intent | A1 | Pending |

---

## 5. Pilot Execution Steps

### Step 1 — Initialize v2.0 Artifacts

A1 creates the following files at NADF project root:
- `EXECUTION_AUTHORITY_REGISTER.md`
- `AUTHORITY_DECISION_LOG.md`

A1 updates `ACTIVE_AGENT_CONFIGURATION.md` to version 2.0.

A1 records in AUTHORITY_DECISION_LOG.md:
```
Entry 001
Date: [date]
Event: AGENT OS v2.0 ACTIVATED — NADF Pod
Authority: A1-NADF
Detail: AOP-013 pilot begins. WP-02 Finance Core is the pilot work package.
```

### Step 2 — WP-02 Authority Request

D2 reviews WP-02 scope and identifies all execution actions required.

D2 submits authority request to A1 with:
- Action list (specific, enumerable)
- Proposed authority class (per Classification Standard)
- Reference to WP-02 acceptance criteria

### Step 3 — Governance Review

A1 initiates concurrent G1/G2/G3 reviews.

G1 completes Architecture Review against EA-4 checklist (if module installation involved).
G2 completes Quality Review against traceability checklist.
G3 completes Security & Change Review against rollback checklist.

Each reviewer returns APPROVED / DENIED / CONDITIONAL.

### Step 4 — Authority Decision

A1 collects all reviews.

If all required reviews approved: A1 issues EXECUTION AUTHORITY GRANTED using the standard GRANT format.

A1 updates EXECUTION_AUTHORITY_REGISTER.md: status Active.
A1 updates AUTHORITY_DECISION_LOG.md: entry logged.

### Step 5 — D2 Execution

D2 verifies authority ID is Active.
D2 references authority ID in execution record.
D2 executes authorized actions within scope.
D2 reports outcome to A1.

### Step 6 — Close Authority

A1 updates EXECUTION_AUTHORITY_REGISTER.md: status Executed, outcome recorded.
A1 updates AUTHORITY_DECISION_LOG.md: execution completion logged.
Human Sponsor receives informed notification.

### Step 7 — WP-02 Closure

At WP-02 closure:
- G2 validates EXECUTION_AUTHORITY_REGISTER.md is complete and reconciled
- All executed actions are traceable to authority grants
- No actions were taken without authority reference
- All authority entries are in a terminal state (Executed / Denied / Revoked)

---

## 6. Pilot Monitoring

During the pilot, A1 tracks:

| Metric | Target |
|--------|--------|
| Authority requests submitted | All execution actions covered |
| Authority grants issued | Equal to requests (or fewer if actions combined) |
| Authority denials | Documented with reason and resolution |
| D2 actions without authority reference | 0 |
| Review turnaround (EA-4) | Same session or next session |
| Register completeness at WP close | 100% |
| Human Sponsor interactions | EA-6 and escalation triggers only |

---

## 7. Escalation Test

During the pilot, A1 will deliberately test one escalation scenario:

**Test:** WP-02 requires a configuration change (EA-3). During G3 review, G3 identifies a security concern that meets the E3 (Security Risk) escalation trigger.

**Expected behaviour:**
- G3 returns DENIED with escalation flag
- A1 routes to Human Sponsor with EA classification package
- Human Sponsor reviews and decides
- Authority is issued or refused based on Human Sponsor decision

**Pass criterion:** Escalation routes correctly; Human Sponsor receives the governance package; no authority is issued by A1.

If no natural escalation trigger arises during WP-02, this test is simulated in a documented drill, recorded in AUTHORITY_DECISION_LOG.md.

---

## 8. Pilot Validation

Pilot is validated against the criteria in `11_VALIDATION_PLAN.md`.

A Pilot Validation Report is produced at WP-02 completion and presented to the Human Sponsor.

The report includes:
- Authority register audit
- Metrics against targets
- Escalation test result
- Governance overhead assessment
- Issues identified and resolved
- Recommendation for Phase D (FAMOIL adoption)

---

## 9. Pilot Success / Failure Criteria

**Pilot PASSES if:**
- All 7 validation criteria in `11_VALIDATION_PLAN.md` are met
- D2 zero-referenced actions = 0
- Register is complete at WP-02 closure
- No authority was issued for EA-6 actions by A1

**Pilot CONDITIONALLY PASSES if:**
- 5-6 of 7 validation criteria met
- Known gaps are documented with remediation plan

**Pilot FAILS if:**
- Fewer than 5 validation criteria met
- OR any EA-6 action was authorized by A1
- OR any critical governance violation occurred

**On FAIL:** Rollback to v1.0, revise framework, re-enter Phase A.

---

*AOP-013 Pilot Plan — A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
