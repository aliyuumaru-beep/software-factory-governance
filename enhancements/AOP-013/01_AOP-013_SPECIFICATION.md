# AOP-013 — Execution Authority Framework
## Enhancement Specification

---

**Enhancement ID:** AOP-013
**Title:** Execution Authority Framework
**Version:** 1.0
**Status:** Approved for Pilot
**Date:** 2026-06-25
**Author:** A1 Master Orchestrator
**Sponsor:** Software Factory Governance Authority
**Target Version:** Agent OS v2.0

---

## 1. Purpose

AOP-013 defines a formal Execution Authority Framework for Agent OS. It replaces ad-hoc human approval of routine implementation tasks with a structured, governance-driven authority grant process.

The objective is not to bypass Claude Code runtime safety controls. The objective is to formally transfer approval authority for routine, bounded, reversible implementation actions from the Human Sponsor to the Agent OS governance layer.

---

## 2. Background

Agent OS v1.0 demonstrated governance-based delivery across NADF WP-01. The operational model requires human confirmation before each execution step. This is appropriate for an initial pilot. It is not appropriate for scaled multi-project portfolio delivery.

The Human Sponsor's time should be reserved for:

- Phase gate approvals
- Scope changes
- Governance exceptions
- Budget decisions
- Production deployment approvals

Routine execution decisions — module installation, configuration, documentation, repository operations — should be handled internally by governance.

AOP-013 creates the formal mechanism to make this transition safe, auditable, and reversible.

---

## 3. Scope

### In Scope

- Definition of Authority Classes EA-1 through EA-6
- Approval matrix per authority class
- Execution Authority Register format and lifecycle
- Responsibility changes for A1, G1, G2, G3, D2
- Escalation rule modifications
- Governance artifact requirements
- Migration plan from Agent OS v1.0 to v2.0
- Pilot implementation on NADF

### Out of Scope

- Changes to Claude Code runtime permission controls
- Changes to Odoo platform security settings
- Changes to individual project work package scope
- Production deployment authority (remains with Human Sponsor)
- Budget authority

---

## 4. Problem Statement

### Current Model

```
Human Sponsor
    ↓
  Approve
    ↓
D2 Executes
```

Consequences:
- Human Sponsor becomes operational bottleneck
- Multiple concurrent projects are not scalable
- Orchestrators remain perpetually dependent
- Portfolio management is not achievable
- Project velocity is capped by sponsor availability

### Target Model

```
D2 Requests Authority
    ↓
G1 Architecture Review
    ↓
G2 Quality Review
    ↓
G3 Security & Risk Review
    ↓
A1 Decision
    ↓
Execution Authority Granted
    ↓
D2 Executes
Human Sponsor: Informed
```

Human Sponsor involvement is replaced by structured governance review for all routine decisions. Human Sponsor retains authority over EA-6 and all escalation classes.

---

## 5. Design Principles

**P1 — Bounded Authority**
Every authority grant is scoped to a specific work package. It does not carry over to future work.

**P2 — Auditability**
Every authority grant is recorded in the Execution Authority Register with full approval trail.

**P3 — Revocability**
A1 may revoke any active authority grant. Revocation is immediate and logged.

**P4 — Traceability**
Every D2 execution action must reference its authority ID. Ungrounded execution is a governance violation.

**P5 — Escalation Integrity**
No authority class eliminates escalation. EA-6 and all E-class escalation triggers remain with the Human Sponsor.

**P6 — Risk Proportionality**
Higher-risk authority classes require deeper governance review and more approvers.

**P7 — No Bypass**
AOP-013 does not reduce governance rigour. It replaces human approval with equivalent or stronger governance review.

---

## 6. Authority Classification

Six authority classes are defined. See `05_AUTHORITY_CLASSIFICATION_STANDARD.md` for full definitions.

| Class | Name | Risk |
|-------|------|------|
| EA-1 | Documentation Authority | Low |
| EA-2 | Repository Authority | Low |
| EA-3 | Configuration Authority | Medium |
| EA-4 | Module Installation Authority | Medium |
| EA-5 | Database Mutation Authority | High |
| EA-6 | Production Authority | Critical — Human Required |

---

## 7. Governance Responsibilities

### A1 — Master Orchestrator

New authority in AOP-013:

| Decision | Description |
|----------|-------------|
| EXECUTION AUTHORITY GRANTED | Formal authorization to proceed |
| EXECUTION AUTHORITY DENIED | Authorization refused with reason |
| EXECUTION AUTHORITY REVOKED | Active authority cancelled |

A1 may not self-grant authority. Authority requires completed governance review.

### G1 — Architecture & Odoo Governance

Must classify and assess:
- Architectural risk classification
- Appropriate authority class (EA-1 through EA-5)
- Architectural preconditions
- Architectural constraints on execution

### G2 — Quality & Documentation Governance

Must validate:
- Traceability to work package acceptance criteria
- Documentation completeness before authority is granted
- Acceptance criteria are testable and sufficient
- Compliance documentation requirements

### G3 — Security & Change Governance

Must validate:
- Security impact of proposed execution
- Change impact scope
- Rollback capability exists
- Recovery plan is adequate
- Risk exposure within tolerance

### D2 — Solution Builder

Before every execution action:
- Verify authority exists for the action
- Reference authority ID in execution record
- Confirm action is within authority scope
- Halt immediately if authority has expired or been revoked

---

## 8. Escalation Rules

The following always require Human Sponsor approval, regardless of governance review:

| Trigger | Reason |
|---------|--------|
| EA-6 Production Authority | Irreversible production risk |
| Scope increase | Changes programme contract |
| New module not in approved list | Unreviewed dependency |
| Budget impact | Financial authority |
| Security exception | Risk beyond governance mandate |
| Governance exception | Framework integrity |
| Portfolio reprioritisation | Cross-project impact |

A1 must not grant authority when any escalation trigger is present.

---

## 9. Success Criteria

AOP-013 is successful when:

1. A1-NADF, A1-FAMOIL, and A1-WAMACARE operate concurrently without Human Sponsor bottleneck.
2. Routine execution decisions are processed through governance within one session.
3. Every execution action is traceable to an authority grant.
4. The Execution Authority Register contains a complete audit trail.
5. Escalation triggers correctly route to the Human Sponsor.
6. No governance degradation compared to Agent OS v1.0.

---

## 10. Relationship to Active Projects

AOP-013 is a separate product stream.

- NADF: continues under Agent OS v1.0 during AOP-013 design phase; transitions to v2.0 during pilot
- FAMOIL: continues under Agent OS v1.0; transitions to v2.0 after pilot validation
- WAMACARE: continues under Agent OS v1.0; transitions to v2.0 after FAMOIL adoption

No NADF work packages are modified by AOP-013. No active delivery is altered.

---

## 11. Deliverables

| # | Document | Status |
|---|----------|--------|
| 01 | AOP-013 Specification (this document) | Complete |
| 02 | Architecture Impact Assessment | Complete |
| 03 | Governance Impact Assessment | Complete |
| 04 | Agent OS v2.0 Design | Complete |
| 05 | Authority Classification Standard | Complete |
| 06 | Approval Matrix | Complete |
| 07 | Execution Authority Register | Complete |
| 08 | Migration Plan | Complete |
| 09 | Risk Assessment | Complete |
| 10 | Pilot Plan | Complete |
| 11 | Validation Plan | Complete |
| 12 | Adoption Recommendation | Complete |

---

*AOP-013 Specification — Agent OS v2.0 Enhancement Program*
*Software Factory Governance Authority — 2026-06-25*
