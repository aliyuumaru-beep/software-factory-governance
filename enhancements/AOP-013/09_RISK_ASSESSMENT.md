# AOP-013 — Risk Assessment

---

**Document:** RISK-AOP-013
**Enhancement:** AOP-013 Execution Authority Framework
**Version:** 1.0
**Date:** 2026-06-25
**Author:** G3 Security & Change Governance

---

## 1. Purpose

This document identifies, assesses, and mitigates risks associated with implementing AOP-013. Risks are evaluated by likelihood (L), impact (I), and combined risk score (L × I on a 1-5 scale).

---

## 2. Risk Classification

| Score | Classification |
|-------|--------------|
| 1-4 | Low |
| 5-9 | Medium |
| 10-16 | High |
| 17-25 | Critical |

---

## 3. Risk Register

---

### RISK-001 — Authority Scope Creep

**Category:** Governance
**Description:** D2 interprets the scope of an authority grant broadly and performs actions beyond what was explicitly authorized.
**Likelihood:** 3
**Impact:** 4
**Score:** 12 — High

**Root Cause:** Ambiguous action descriptions in authority grants.

**Mitigations:**
- Authorized Actions must be specific and enumerable (not "install budget-related modules" — must name each module)
- D2 must halt if an action is not explicitly listed and re-request authority
- A1 validates scope specificity before granting
- G2 flags vague action descriptions during review

**Residual Risk After Mitigation:** Medium (6)

---

### RISK-002 — Governance Review Bottleneck

**Category:** Performance
**Description:** G1/G2/G3 become the new bottleneck, replacing the Human Sponsor. Review turnaround is slow, blocking delivery.
**Likelihood:** 3
**Impact:** 3
**Score:** 9 — Medium

**Root Cause:** Governance agents are shared across pods; concurrent reviews may queue.

**Mitigations:**
- EA-1 and EA-2 reviews are lightweight by design (single reviewer, minimal checklist)
- Concurrent reviews: G1/G2/G3 review in parallel, not sequentially
- EA-3/4/5 reviews are expected same-session or next-session
- Review scope is bounded to the specific authority request, not the entire WP

**Residual Risk After Mitigation:** Low (4)

---

### RISK-003 — Authority Register Staleness

**Category:** Governance
**Description:** Active authority grants are not updated to Executed status after D2 completes work. Old Active entries accumulate and the register becomes unreliable.
**Likelihood:** 3
**Impact:** 3
**Score:** 9 — Medium

**Root Cause:** D2 completes execution but does not report outcome to A1; A1 does not close the entry.

**Mitigations:**
- D2 is responsible for reporting execution outcome to A1 immediately after completion
- A1 is responsible for updating register status within the same session
- G2 validates register completeness at each WP closure gate
- G2 flags unclosed Active entries as a blocking concern at WP closure

**Residual Risk After Mitigation:** Low (3)

---

### RISK-004 — Agent Prompt Non-Compliance

**Category:** Architecture
**Description:** Agent prompts are updated but agents do not consistently follow the authority verification protocol. D2 executes without checking authority; A1 issues authority in incomplete format.
**Likelihood:** 2
**Impact:** 4
**Score:** 8 — Medium

**Root Cause:** Prompt changes are insufficient or the authority verification step is too burdensome and skipped.

**Mitigations:**
- Pilot validation plan includes explicit check: "Was authority ID referenced in D2 execution record?"
- Non-reference is a governance violation — caught by G2 at WP closure
- Authority format is explicit and standardised (GRANT/DENY/REVOKE templates)
- Pilot feedback loop: if compliance is low, prompts are revised before wider adoption

**Residual Risk After Mitigation:** Low (4)

---

### RISK-005 — Incorrect Authority Classification

**Category:** Governance
**Description:** D2 misclassifies an action (e.g., submits a database migration as EA-3 instead of EA-5). Lower review rigour is applied to a higher-risk action.
**Likelihood:** 2
**Impact:** 5
**Score:** 10 — High

**Root Cause:** Classification standard is not applied correctly; boundary cases are ambiguous.

**Mitigations:**
- Classification Rule 1: always round up (use the higher class when uncertain)
- Classification Rule 5: uncertainty escalates — D2 must submit at the higher class
- G1 is required to confirm or correct the classification during review
- Classification Standard includes a Quick Reference table for common actions
- Pilot includes classification review as a validation criterion

**Residual Risk After Mitigation:** Low (2)

---

### RISK-006 — EA-6 Boundary Drift

**Category:** Security
**Description:** Over time, actions that should be EA-6 (production) are reclassified as EA-5 or EA-4. Production operations occur without Human Sponsor approval.
**Likelihood:** 2
**Impact:** 5
**Score:** 10 — High

**Root Cause:** Gradual normalisation; EA-6 definition drift; A1 issues authority for borderline production actions.

**Mitigations:**
- EA-6 definition is absolute: ANY action on a production environment
- Rule 4: EA-6 is non-negotiable — no classification analysis can result in a production action below EA-6
- G3 is responsible for flagging EA-6 attempts masquerading as lower classes
- A1 must never issue authority for EA-6 — hard rule, not a judgement call
- Pilot review includes EA-6 boundary compliance as a criterion

**Residual Risk After Mitigation:** Low (2)

---

### RISK-007 — Cross-Pod Authority Confusion

**Category:** Architecture
**Description:** An authority grant for NADF is (accidentally or intentionally) applied to FAMOIL execution.
**Likelihood:** 1
**Impact:** 4
**Score:** 4 — Low

**Root Cause:** Authority IDs are similar; D2 references wrong ID.

**Mitigations:**
- Authority IDs are project-namespaced: EA-NADF-WP01-001 cannot be misread as FAMOIL
- D2 must verify project name in the authority entry before execution
- Registers are maintained separately per pod

**Residual Risk After Mitigation:** Low (1)

---

### RISK-008 — Governance Agent Unavailability

**Category:** Continuity
**Description:** One or more governance agents (G1/G2/G3) are unavailable for a session. Authority grants are blocked. Delivery halts.
**Likelihood:** 1
**Impact:** 3
**Score:** 3 — Low

**Root Cause:** Agent OS sessions are discrete; a session ends before a review is completed.

**Mitigations:**
- Authority requests persist in the register with status Pending Review
- Next session resumes from pending review without loss
- EA-1/EA-2 requests can proceed on G1 approval alone (G2/G3 optional)
- Escalation to Human Sponsor if review is blocked for more than two sessions

**Residual Risk After Mitigation:** Low (1)

---

### RISK-009 — Framework Complexity Overhead

**Category:** Adoption
**Description:** The authority framework adds process overhead that outweighs the benefit of reduced human approval. Agents spend more time on governance than delivery.
**Likelihood:** 2
**Impact:** 3
**Score:** 6 — Medium

**Root Cause:** Too many authority requests per work package; review process too detailed for low-risk actions.

**Mitigations:**
- EA-1 and EA-2 are designed to be lightweight (single reviewer, auto-grant after review)
- One authority grant can cover multiple related actions of the same class within a WP
- Pilot includes a measure: ratio of governance time to delivery time; flag if excessive
- Adoption Recommendation includes a simplification option if pilot shows overhead

**Residual Risk After Mitigation:** Low (3)

---

### RISK-010 — Human Sponsor Disengagement

**Category:** Governance
**Description:** The Human Sponsor, relieved of routine approvals, disengages from governance entirely. Critical escalations are not reviewed promptly.
**Likelihood:** 2
**Impact:** 4
**Score:** 8 — Medium

**Root Cause:** Reduced human touchpoints may reduce engagement.

**Mitigations:**
- Human Sponsor receives informed notifications for all grants — stays aware without approving
- Phase gate governance reviews remain mandatory Human Sponsor events
- EA-6 and all escalation triggers require Human Sponsor — engagement is preserved for high-stakes decisions
- Pilot includes a structured debrief with Human Sponsor at WP completion

**Residual Risk After Mitigation:** Low (4)

---

## 4. Risk Summary

| Risk | Category | Pre-Mitigation | Post-Mitigation |
|------|----------|---------------|-----------------|
| RISK-001 Scope Creep | Governance | High (12) | Medium (6) |
| RISK-002 Review Bottleneck | Performance | Medium (9) | Low (4) |
| RISK-003 Register Staleness | Governance | Medium (9) | Low (3) |
| RISK-004 Prompt Non-Compliance | Architecture | Medium (8) | Low (4) |
| RISK-005 Misclassification | Governance | High (10) | Low (2) |
| RISK-006 EA-6 Boundary Drift | Security | High (10) | Low (2) |
| RISK-007 Cross-Pod Confusion | Architecture | Low (4) | Low (1) |
| RISK-008 Agent Unavailability | Continuity | Low (3) | Low (1) |
| RISK-009 Framework Overhead | Adoption | Medium (6) | Low (3) |
| RISK-010 Sponsor Disengagement | Governance | Medium (8) | Low (4) |

**Overall Assessment:** Risk profile is acceptable. No Critical risks. High risks are reduced to Medium or Low through mitigations. The framework is safe to pilot.

---

## 5. Risk Acceptance Statement

The Software Factory Governance Authority accepts the residual risks identified above as within tolerance for the AOP-013 pilot phase. Risks will be re-assessed after the NADF pilot validation report is complete.

---

*AOP-013 Risk Assessment — G3 Security & Change Governance*
*Software Factory Governance Authority — 2026-06-25*
