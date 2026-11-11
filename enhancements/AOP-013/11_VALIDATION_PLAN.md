# AOP-013 — Validation Plan

> **SUPERSESSION NOTICE — D4 / 2026-06-25**
> References to WP-02 as the pilot work package throughout this document are superseded by
> Sponsor Decision AOP-013-SD-001 Condition 4. The operative pilot window is **WP-03
> and WP-04**, not WP-02. Additionally, **VC-3 advisory mode handling**: Validation criterion
> VC-3 (D2 Executes Under Authority) cannot be satisfied in advisory mode by design. M-06
> (Advisory Decision Accuracy Rate) in the Success Metrics Dashboard is the operative
> advisory-mode proxy for VC-3 during the pilot. Full VC-3 compliance is deferred to
> binding mode activation. See `AUTHORITY_DECISION_LOG.md` Entry 002 for the full handling
> record. Operative pilot plan: `enhancements/AOP-013/phase-b/02_NADF_PILOT_ACTIVATION_PACKAGE.md`

---

**Document:** VAL-AOP-013
**Enhancement:** AOP-013 Execution Authority Framework
**Version:** 1.0 (superseded for pilot scope and VC-3 handling — see notice above)
**Date:** 2026-06-25
**Author:** G2 Quality & Documentation Governance

---

## 1. Purpose

This document defines the validation requirements for Agent OS v2.0. Validation confirms that the Execution Authority Framework operates as designed before it is adopted across all project pods.

---

## 2. Validation Scope

Validation covers:
- The NADF pilot (primary validation source)
- Framework document completeness
- Governance agent compliance
- Delivery agent compliance
- Escalation routing correctness
- Human Sponsor impact

Validation does NOT cover:
- Claude Code runtime permissions (out of scope of AOP-013)
- Odoo platform behaviour
- Project work package delivery outcomes

---

## 3. Validation Criteria

Seven criteria must be demonstrated for validation to pass.

---

### VC-1 — Governance Reviews Generate Authority

**What is validated:** G1, G2, and G3 complete authority reviews and return formal decisions. Authority grants result from governance review, not from human approval.

**Evidence required:**
- At least two authority requests reviewed by governance during WP-02 pilot
- G1/G2/G3 review entries recorded in EXECUTION_AUTHORITY_REGISTER.md
- Each entry shows reviewer name, decision, date, and rationale
- No entry shows "Human Sponsor approved" as the approval mechanism for EA-1 through EA-5

**Pass condition:** All authority grants in WP-02 are backed by governance reviews in the register.

---

### VC-2 — A1 Issues Authority in Correct Format

**What is validated:** A1 uses the standardised GRANT, DENY, and REVOKE formats. Authority IDs follow the naming convention. Decisions are explicit and documented.

**Evidence required:**
- AUTHORITY_DECISION_LOG.md contains at least one GRANT entry
- GRANT entry uses the format defined in `04_AGENT_OS_V2_DESIGN.md` Section 4
- Authority ID follows the pattern EA-{PROJECT}-WP{XX}-{NNN}
- Decision includes rationale statement
- Log is timestamped and append-only

**Pass condition:** AUTHORITY_DECISION_LOG.md format is compliant and complete.

---

### VC-3 — D2 Executes Under Authority

**What is validated:** Every D2 execution action references a valid authority ID. No actions are taken without an authority reference.

**Evidence required:**
- D2 execution records from WP-02 session transcripts
- Each execution action includes a statement referencing the authority ID
- EXECUTION_AUTHORITY_REGISTER.md shows corresponding entries with status Executed

**Pass condition:** Zero D2 execution actions without an authority ID reference.

---

### VC-4 — Audit Trail Exists

**What is validated:** The end-to-end audit trail from authority request to execution outcome is complete and traceable.

**Evidence required:**
- For each executed authority: request → G1/G2/G3 reviews → A1 decision → D2 execution → outcome
- Every step is recorded in the EXECUTION_AUTHORITY_REGISTER.md or AUTHORITY_DECISION_LOG.md
- Outcome field is populated for all Executed entries

**Pass condition:** 100% of executed authorities have a complete audit trail.

---

### VC-5 — Escalations Work Correctly

**What is validated:** Escalation triggers correctly route to the Human Sponsor. A1 does not issue authority when an escalation trigger is present.

**Evidence required:**
- One escalation scenario exercised (live or drilled — see Pilot Plan Section 7)
- AUTHORITY_DECISION_LOG.md shows the escalation event
- Human Sponsor received the governance package (or drill was documented)
- A1 did not issue EXECUTION AUTHORITY GRANTED for the escalated request

**Pass condition:** Escalation scenario correctly routed; A1 authority not issued for escalated request.

---

### VC-6 — Human Intervention Is Reduced

**What is validated:** Human Sponsor was not required to approve routine execution actions during WP-02. Human Sponsor was informed but did not approve EA-1 through EA-5 actions.

**Evidence required:**
- Count of Human Sponsor approvals for routine execution during WP-01 (baseline)
- Count of Human Sponsor approvals for routine execution during WP-02 (pilot)
- WP-02 count should be 0 for EA-1 through EA-5 actions

**Pass condition:** Human Sponsor approvals for routine execution (EA-1 through EA-5) = 0 during WP-02 pilot.

---

### VC-7 — No Governance Degradation

**What is validated:** The governance model under v2.0 provides equal or better governance quality compared to v1.0. Governance reviews are not shorter, weaker, or less complete.

**Evidence required:**
- G2 retrospective review of WP-02 governance quality
- Comparison: WP-01 governance outcomes (under v1.0) vs WP-02 (under v2.0)
- Assessment covers: traceability, documentation completeness, acceptance criteria quality, decision logging
- G2 signs off that governance quality is not degraded

**Pass condition:** G2 retrospective assessment confirms governance quality maintained or improved.

---

## 4. Validation Evidence Collection

| Evidence | Source | Collected By |
|----------|--------|-------------|
| Authority register entries | EXECUTION_AUTHORITY_REGISTER.md | A1 |
| Authority decision log entries | AUTHORITY_DECISION_LOG.md | A1 |
| D2 execution records | Session transcripts | G2 |
| Escalation event record | AUTHORITY_DECISION_LOG.md | A1 |
| Human Sponsor interaction count | Session records | A1 |
| G2 governance quality assessment | G2 retrospective | G2 |

---

## 5. Validation Report

At WP-02 completion, A1 produces a Pilot Validation Report containing:

1. Summary table: VC-1 through VC-7 — PASS / FAIL / CONDITIONAL PASS
2. Evidence citations for each criterion
3. Metrics (see Pilot Plan Section 6)
4. Issues identified during the pilot
5. Resolutions applied
6. Recommendation: Proceed to Phase D (FAMOIL) / Revise Framework / Halt

---

## 6. Validation Outcome Actions

| Outcome | Action |
|---------|--------|
| All 7 criteria PASS | Proceed to FAMOIL adoption (Phase D) |
| 5-6 criteria PASS | Document gaps; apply fixes; re-validate in next WP before Phase D |
| Fewer than 5 PASS | Halt; rollback NADF to v1.0; revise framework; re-enter Phase A |
| Any EA-6 issued by A1 | Immediate halt; critical governance breach; full review required |
| Any critical violation | Immediate halt; Human Sponsor notification; root cause analysis |

---

## 7. Ongoing Validation (Post-Pilot)

After pilot validation passes, each pod's first work package under v2.0 acts as a validation exercise. FAMOIL Phase D and WAMACARE Phase E each include:

- Register completeness check at WP closure
- D2 zero-reference check (should remain 0)
- Human Sponsor routine approval count (should remain 0)
- No governance degradation confirmation from G2

The framework is considered fully validated when all three pods have completed one full work package under v2.0 without a critical finding.

---

*AOP-013 Validation Plan — G2 Quality & Documentation Governance*
*Software Factory Governance Authority — 2026-06-25*
