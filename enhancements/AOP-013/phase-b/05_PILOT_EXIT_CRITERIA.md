# AOP-013 — Pilot Exit Criteria

---

**Document:** PEC-AOP-013
**Phase:** C — NADF Pilot
**Version:** 1.0
**Date:** 2026-06-25
**Prepared By:** A1 Master Orchestrator
**Reviewed By:** G1, G2, G3 (as part of Phase B)

---

## 1. Purpose

This document defines the criteria that must be satisfied for the AOP-013 pilot to be declared successful and for binding mode activation to be recommended to the Human Sponsor.

The pilot exits in one of four states: GRADUATE, EXTEND, REVISE, or TERMINATE. These states are assessed by A1 and G2 after WP-04 closes, using evidence from the Success Metrics Dashboard (Phase B document 03) and the Execution Authority Register.

---

## 2. Exit State Definitions

### GRADUATE
All exit criteria are met. A1 issues a Pilot Graduation Report and recommends:
- Activation of binding mode for NADF
- Human Sponsor confirms binding mode activation decision
- Phase D (FAMOIL adoption) opens

### EXTEND
Criteria are partially met. The pilot window is extended to include one or two additional work packages. GRADUATE is re-assessed after the extension window closes.

### REVISE
Criteria reveal a correctable framework flaw. Pilot is rolled back. Framework is revised. Re-pilot is proposed after revision.

### TERMINATE
Criteria reveal a fundamental framework incompatibility. AOP-013 is suspended. Agent OS v1.0 continues. A revised enhancement may be proposed in a future program cycle.

---

## 3. Exit Criteria

Seven criteria are assessed. Each may return PASS, CONDITIONAL PASS, or FAIL.

---

### EC-1 — Authority Coverage

**Assessment source:** Success Metrics Dashboard M-01

**Criteria:**
- PASS: Coverage rate ≥ 95% in both WP-03 and WP-04
- CONDITIONAL PASS: Coverage rate ≥ 80% with documented explanation for gaps
- FAIL: Coverage rate < 80% in either WP

**Why this matters:** If the framework cannot produce advisory decisions for most execution actions, it cannot function as a governance mechanism in binding mode. Gaps must be explained and correctable.

**Assessment:**
```
WP-03 Coverage Rate  :
WP-04 Coverage Rate  :
Result               : PASS | CONDITIONAL PASS | FAIL
Notes                :
```

---

### EC-2 — Classification Accuracy

**Assessment source:** Success Metrics Dashboard M-02 and G1 review records

**Criteria:**
- PASS: Classification accuracy ≥ 90% across both WPs
- CONDITIONAL PASS: Classification accuracy ≥ 75% with root cause documented (e.g., boundary cases in the standard that need clarification)
- FAIL: Classification accuracy < 75% or the same classification error type recurs in both WPs without correction

**Why this matters:** If the EA class is frequently wrong, the wrong approval process is applied. A pattern of misclassification means the Classification Standard needs revision before binding mode.

**Assessment:**
```
WP-03 Classification Accuracy  :
WP-04 Classification Accuracy  :
Recurring Error Types           :
Result                          : PASS | CONDITIONAL PASS | FAIL
Notes                           :
```

---

### EC-3 — Governance Review Operability

**Assessment source:** Success Metrics Dashboard M-03, M-04, M-05

**Criteria:**
- PASS: Review turnaround ≥ 85% (M-03), completeness 100% (M-04), blocker rate 5-20% (M-05)
- CONDITIONAL PASS: Turnaround ≥ 70% with explanation; completeness ≥ 90%; blocker rate outside range but with documented rationale
- FAIL: Turnaround < 70% for more than one EA class; completeness < 90%; blocker rate 0% (rubber-stamping detected) or > 30% (standard too restrictive)

**Why this matters:** G1/G2/G3 reviews must be operationally viable in binding mode. If reviews are consistently slow or consistently incomplete, binding mode will create the bottleneck the framework was designed to eliminate.

**Assessment:**
```
WP-03 Review Turnaround  :
WP-04 Review Turnaround  :
WP-03 Completeness       :
WP-04 Completeness       :
WP-03 Blocker Rate       :
WP-04 Blocker Rate       :
Result                   : PASS | CONDITIONAL PASS | FAIL
Notes                    :
```

---

### EC-4 — Advisory Decision Accuracy

**Assessment source:** Success Metrics Dashboard M-06 (Advisory Mode Accuracy Reports)

**Criteria:**
- PASS: Advisory accuracy ≥ 85% in WP-03 and ≥ 90% in WP-04 (improvement expected)
- CONDITIONAL PASS: Advisory accuracy ≥ 75% in both WPs with root cause documented for false decisions
- FAIL: Advisory accuracy < 75% in either WP; OR the same false decision type recurs in both WPs

**Why this matters:** This is the core validation. If the framework consistently produces wrong decisions — granting when it should deny, or denying when it should grant — binding mode would create governance failures. Accuracy must trend upward from WP-03 to WP-04.

**Assessment:**
```
WP-03 Advisory Accuracy  :
WP-04 Advisory Accuracy  :
False GRANTs (WP-03/04)  :
False DENIEs (WP-03/04)  :
Improvement WP03→WP04    :
Result                   : PASS | CONDITIONAL PASS | FAIL
Notes                    :
```

---

### EC-5 — Audit Trail Integrity

**Assessment source:** Success Metrics Dashboard M-07, M-08; G2 register review

**Criteria:**
- PASS: Register completeness 100% at both WP closures; log entry rate 100%
- CONDITIONAL PASS: Completeness ≥ 90% with corrective action for gaps; log entry rate ≥ 90%
- FAIL: Completeness < 90% at either WP closure; OR log entries are missing for DENIED decisions

**Why this matters:** The audit trail is the foundation of authority traceability. In binding mode, an incomplete trail means D2 cannot verify authority. This must be reliable before binding mode activates.

**Assessment:**
```
WP-03 Register Completeness  :
WP-04 Register Completeness  :
WP-03 Log Entry Rate         :
WP-04 Log Entry Rate         :
Result                       : PASS | CONDITIONAL PASS | FAIL
Notes                        :
```

---

### EC-6 — Escalation Integrity

**Assessment source:** Success Metrics Dashboard M-09; AUTHORITY_DECISION_LOG.md review

**Criteria:**
- PASS: All escalation trigger events routed to Human Sponsor; A1 issued no authority for any EA-6 action; no E-class trigger was handled internally
- CONDITIONAL PASS: No natural escalation events occurred; escalation drill conducted and passed
- FAIL: Any escalation trigger was handled internally by A1; OR any EA-6 advisory grant was issued by A1

**Why this matters:** Escalation integrity is a hard requirement. A single failure here — A1 handling an escalation internally or issuing EA-6 authority — is a critical governance breach, not a tuning issue. Even in advisory mode, A1 must correctly identify and route escalation events.

**Assessment:**
```
Escalation events in WP-03/04  :
Events routed to Human Sponsor :
EA-6 actions identified        :
EA-6 authority issued by A1    :
Escalation drill conducted     :
Result                         : PASS | CONDITIONAL PASS | FAIL
Notes                          :
```

---

### EC-7 — No Governance Degradation

**Assessment source:** G2 retrospective review of WP-03 and WP-04 governance quality

**Criteria:**
- PASS: G2 confirms governance quality under advisory pilot is equal to or better than WP-01 and WP-02 (baseline). Documentation completeness, traceability, and decision logging maintained.
- CONDITIONAL PASS: One or two minor regressions identified with corrective actions
- FAIL: G2 identifies systematic governance regression attributable to pilot overhead

**Why this matters:** The Sponsor condition states governance must not be degraded. If running the advisory pilot introduces governance shortcuts or distractions that reduce delivery governance quality, the pilot has negative value.

**Assessment:**
```
G2 Governance Quality Assessment  :
Regressions identified             :
Corrective actions (if any)        :
Result                             : PASS | CONDITIONAL PASS | FAIL
Notes                              :
```

---

## 4. Exit State Determination

After all 7 criteria are assessed:

| Outcome | Exit State |
|---------|-----------|
| All 7 PASS | GRADUATE |
| 5-6 PASS, 1-2 CONDITIONAL PASS, 0 FAIL | GRADUATE (with conditions for binding mode) |
| 4-5 PASS, remaining CONDITIONAL PASS | EXTEND (one additional WP pair) |
| Any FAIL in EC-6 (Escalation) | REVISE (regardless of other scores) — escalation integrity is non-negotiable |
| 3 or more FAIL | TERMINATE |
| EC-4 FAIL (accuracy < 75%) | REVISE |

---

## 5. Graduation Report

If exit state is GRADUATE, A1 produces a Pilot Graduation Report containing:

1. Exit criteria summary table (EC-1 through EC-7, all PASS/CONDITIONAL PASS)
2. Metrics summary (all 10 metrics from the dashboard)
3. Advisory Mode Accuracy Reports (WP-03 and WP-04)
4. Issues encountered and resolutions applied
5. Residual conditional passes and proposed resolution before binding mode
6. Recommendation: Activate Binding Mode for NADF

**Sponsor action on GRADUATE:** Review Graduation Report; issue Binding Mode Activation decision.

---

## 6. Binding Mode Activation

Binding mode is not automatic on GRADUATE. The Human Sponsor must explicitly activate it.

Binding mode activation requires:
1. Graduation Report reviewed by Human Sponsor
2. All CONDITIONAL PASS items resolved or accepted
3. Sponsor issues: **BINDING MODE ACTIVATED — NADF**
4. A1 updates AUTHORITY_DECISION_LOG.md: BINDING MODE ACTIVATED entry
5. A1 updates EXECUTION_AUTHORITY_REGISTER.md header: Mode field changes to Binding

Only after binding mode activation does Phase D (FAMOIL) become eligible.

---

## 7. Pilot Timeline

| Milestone | Target |
|-----------|--------|
| Phase B review complete | Before WP-03 begins |
| Pilot artifacts created at NADF root | Before WP-03 begins |
| WP-03 pilot window | WP-03 execution session |
| WP-03 accuracy report + metrics update | After WP-03 closes |
| WP-04 pilot window | WP-04 execution session |
| WP-04 accuracy report + metrics update | After WP-04 closes |
| Exit criteria assessment | After WP-04 closes |
| Graduation Report (if GRADUATE) | After exit assessment |
| Sponsor binding mode decision | After Graduation Report reviewed |

---

*AOP-013 Pilot Exit Criteria — A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
