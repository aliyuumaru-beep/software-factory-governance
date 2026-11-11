# Approval Matrix — Execution Authority Framework

---

**Document:** APM-AOP-013
**Enhancement:** AOP-013 Execution Authority Framework
**Version:** 1.0
**Date:** 2026-06-25
**Author:** A1 Master Orchestrator

---

## 1. Purpose

This document defines the approval matrix for Execution Authority classes EA-1 through EA-6. It specifies which governance agents must complete a review before A1 may issue authority, and whether Human Sponsor involvement is required.

---

## 2. Approval Matrix

| Authority Class | G1 Architecture | G2 Quality | G3 Security | A1 Decision | Human Sponsor |
|----------------|----------------|------------|-------------|-------------|--------------|
| EA-1 Documentation | Review Required | Optional | Optional | Auto-Grant | Informed |
| EA-2 Repository | Review Required | Review Required | Optional | Auto-Grant | Informed |
| EA-3 Configuration | Review Required | Review Required | Review Required | Explicit Required | Informed |
| EA-4 Module Install | Review Required | Review Required | Review Required | Explicit Required | Informed |
| EA-5 Database Mutation | Review Required | Review Required | Review Required | Explicit Required | Informed |
| EA-6 Production | Review Required | Review Required | Review Required | Routes to Human | Required |

---

## 3. Definitions

**Review Required**
The reviewer must complete their checklist and return a formal decision (APPROVED / DENIED / CONDITIONAL) before A1 may proceed. A missing review blocks the authority grant.

**Optional**
The reviewer may complete a review if relevant to the specific request. If no review is submitted, A1 may proceed without it. Optional reviews do not block grants.

**Auto-Grant**
After all required reviews are APPROVED, A1 issues the authority grant without a separate deliberation step. The grant is immediate.

**Explicit Required**
After all required reviews are APPROVED, A1 must make a deliberate decision and formally issue EXECUTION AUTHORITY GRANTED with a rationale statement. A1 may not auto-grant EA-3 through EA-5.

**Routes to Human**
A1 does not issue authority for EA-6 under any circumstances. A1 packages the governance review outputs and routes them to the Human Sponsor as a formal authority recommendation. The Human Sponsor issues or refuses the authority.

**Informed**
The Human Sponsor receives a notification of the authority grant and execution outcome. No action is required from the Human Sponsor.

---

## 4. Denial Rules

**Any required reviewer may block any authority grant.** Denial from a required reviewer is absolute. A1 cannot override a reviewer denial.

**G1 denial:** Architectural risk is unacceptable or authority class is wrong. Resolution: redesign the approach or re-classify.

**G2 denial:** Documentation is incomplete, traceability cannot be established, or acceptance criteria are insufficient. Resolution: complete documentation before re-submitting.

**G3 denial:** Security impact is unacceptable, rollback plan is missing, or risk exposure exceeds tolerance. Resolution: prepare rollback plan, reduce scope, or escalate.

**All denials must be logged in AUTHORITY_DECISION_LOG.md** with the reason and the resolution required.

---

## 5. Conditional Approval

A reviewer may return a CONDITIONAL approval when the concern is resolvable without a full re-review.

Example: G3 approves EA-4 module installation on condition that a backup is taken immediately before execution.

A1 must ensure conditions are met before granting authority. Conditions are recorded in the authority register entry.

Conditions that cannot be verified by A1 before execution must be treated as a denial until resolved.

---

## 6. Review Scope by Class

### EA-1 Documentation

**G1 Reviews:**
- Does the documentation change affect architectural decisions or constraints?
- Does the change accurately reflect the current architectural state?

**G2 Reviews (optional):**
- Is the documentation complete, accurate, and consistent with governance standards?

**G3 Reviews (optional):**
- Does the documentation expose sensitive information (credentials, access paths)?

---

### EA-2 Repository

**G1 Reviews:**
- Does the branch/PR/commit follow repository governance standards?
- Does the change affect architectural boundaries?

**G2 Reviews:**
- Is the PR description complete?
- Are acceptance criteria documented?
- Does the commit follow the commit message standard?

**G3 Reviews (optional):**
- Does the repository change expose security-sensitive information?

---

### EA-3 Configuration

**G1 Reviews:**
- Is the configuration change consistent with the platform profile?
- Does the change have unintended architectural side effects?
- Are preconditions met (e.g., dependent modules installed)?

**G2 Reviews:**
- Is the configuration change traceable to a work package acceptance criterion?
- Has the configuration been documented in IMPLEMENTATION_HISTORY.md?

**G3 Reviews:**
- Does the configuration change affect authentication, authorisation, or data access?
- Is the change reversible? What is the rollback procedure?
- Does the change meet the security standard?

---

### EA-4 Module Installation

**G1 Reviews:**
- Is the module on the approved list (OCA or MODULE_REGISTRY)?
- Is the dependency chain complete and verified?
- Is the module compatible with the current Odoo version?
- Does the module conflict with any installed module?

**G2 Reviews:**
- Is the module registration in MODULE_REGISTRY complete?
- Is the installation traceable to the work package?
- Is post-installation documentation planned?

**G3 Reviews:**
- Does the module introduce new access controls or bypass existing ones?
- Does the module create new external integrations or data flows?
- Is the rollback plan (module uninstall path) confirmed?
- Has the module been tested on a test/dev database before the authority request?

---

### EA-5 Database Mutation

**G1 Reviews:**
- Is the mutation approach architecturally sound?
- Does the mutation maintain data integrity constraints?
- Are any schema changes implied by this mutation?

**G2 Reviews:**
- Is the mutation traceable to an acceptance criterion?
- Is the expected outcome documented and verifiable?
- Is the mutation reversible?

**G3 Reviews:**
- Has a backup been taken and verified immediately before this authority request?
- Is the rollback procedure (restore from backup) documented and executable?
- Is the mutation scoped correctly (does it affect only the intended records)?
- Has the mutation been tested on a copy of the database?

---

### EA-6 Production

All three governance agents complete full reviews as above. A1 compiles the review package and routes to Human Sponsor with a formal recommendation including:

- Summary of G1/G2/G3 review outcomes
- Staged environment validation evidence
- Rollback procedure
- Change window proposal
- Risk summary

Human Sponsor decision: APPROVED | DEFERRED | REFUSED.

---

## 7. Review Turnaround Expectations

| Authority Class | Expected Review Turnaround |
|----------------|---------------------------|
| EA-1 | Same session |
| EA-2 | Same session |
| EA-3 | Same session to next session |
| EA-4 | Same session to next session |
| EA-5 | One to two sessions |
| EA-6 | Human Sponsor response time (not governed by this framework) |

---

## 8. Revision History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-06-25 | Initial release under AOP-013 |

---

*Approval Matrix — A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
