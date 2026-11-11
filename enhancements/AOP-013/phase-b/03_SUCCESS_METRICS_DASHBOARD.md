# AOP-013 — Success Metrics Dashboard

---

**Document:** SMD-AOP-013
**Phase:** C — NADF Pilot
**Version:** 1.1 (Updated: WP-03 advisory decisions issued — 2026-06-25)
**Date:** 2026-06-25
**Maintained By:** A1 Master Orchestrator

---

## Dashboard Status

```
Pilot Mode     : Advisory
Pilot Window   : WP-03 + WP-04
Current WP     : WP-03 — Procurement Core (advisory decisions issued 2026-06-25)
Phase B Review : COMPLETE PASS (G3 CONFIRMED 2026-06-25)
Phase C        : ACTIVE — pilot activated by Sponsor 2026-06-25
Last Updated   : 2026-06-25 (WP-03 advisory decisions issued; pre-execution)
Overall Status : IN FLIGHT (WP-03 advisory decisions complete; execution pending)
```

**Notes on WP-03 data:**
All WP-03 advisory decisions have been issued and logged. Metrics M-01 through M-05 and M-08 
reflect the advisory decision phase. Metrics M-06, M-07, and M-10 cannot be assessed until
WP-03 execution completes and the exit gate review closes. WP-04 remains PENDING (work
package definition not yet created).

---

## How to Read This Dashboard

Each metric has:
- **Target** — the value that constitutes success
- **WP-03 Actual** — filled after WP-03 closes
- **WP-04 Actual** — filled after WP-04 closes
- **Status** — GREEN (on target) / AMBER (at risk) / RED (off target) / PENDING

This document is updated in place after each work package closes. History is preserved in AUTHORITY_DECISION_LOG.md.

---

## Section 1 — Authority Coverage

*Does the framework cover all execution actions?*

### M-01 — Authority Request Coverage Rate

**Definition:** Percentage of D2 execution actions for which an advisory authority request was submitted and processed.

**Target:** 100% (every execution action has a corresponding advisory authority decision)

**Calculation:** (Number of authority decisions issued ÷ Number of D2 execution actions) × 100

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-01 Coverage Rate | 100% | **100%** ¹ | 100% | — | **GREEN** ¹ |
| Total execution actions | — | 9 action groups | — | — | |
| Authority decisions issued | — | 4 (EA-1/2/3/5) | — | — | |
| Uncovered actions | 0 | **0** | 0 | — | |

¹ Pre-execution coverage: all 9 WP-03 action groups are covered by 4 advisory authority
requests (EA-NADF-WP03-001 through 004). Final coverage confirmed at WP-03 exit gate.

**Threshold:** GREEN ≥ 95% | AMBER 80-94% | RED < 80%

---

### M-02 — Authority Class Accuracy Rate

**Definition:** Percentage of advisory authority decisions where G1 confirmed the correct EA class was submitted by A1 (or D2 in future binding mode).

**Target:** ≥ 90%

**Calculation:** (Correct classifications ÷ Total classifications reviewed by G1) × 100

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-02 Classification Accuracy | ≥ 90% | **100%** | ≥ 95% | — | **GREEN** |
| Correct first-attempt classifications | — | 4 / 4 | — | — | |
| G1 reclassifications required | — | **0** | — | — | |

G1 confirmed all four WP-03 classifications without reclassification:
EA-1 (documentation), EA-2 (repository), EA-3 (configuration), EA-5 (DB mutation).

**Threshold:** GREEN ≥ 90% | AMBER 75-89% | RED < 75%

---

## Section 2 — Governance Review Quality

*Are G1/G2/G3 reviews timely, complete, and accurate?*

### M-03 — Review Turnaround (EA-3/EA-4)

**Definition:** Percentage of EA-3 and EA-4 authority reviews completed within the same or next session.

**Target:** ≥ 85%

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-03 Review Turnaround | ≥ 85% | **100%** | ≥ 85% | — | **GREEN** |
| Same-session completions | — | 2 / 2 (EA-3, EA-5) | — | — | |
| Next-session completions | — | 0 | — | — | |
| Missed targets | — | **0** | — | — | |

Both EA-3 and EA-5 advisory reviews (the only review-required classes for this metric)
completed in the same pilot activation session (2026-06-25).

**Threshold:** GREEN ≥ 85% | AMBER 70-84% | RED < 70%

---

### M-04 — Review Completeness Rate

**Definition:** Percentage of governance reviews where all required checklist items were addressed.

**Target:** 100%

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-04 Completeness | 100% | **100%** | 100% | — | **GREEN** |
| Complete reviews | — | 8 / 8 | — | — | |
| Incomplete reviews | 0 | **0** | 0 | — | |

8 reviews total across 4 authority requests (G1+G2 for EA-1/EA-2; G1+G2+G3 for EA-3/EA-5).
All G1 checklist (6 items), G2 checklist (5 items), G3 checklist (5 items) fully addressed.

**Threshold:** GREEN = 100% | AMBER 90-99% | RED < 90%

---

### M-05 — Governance Review Blocker Rate

**Definition:** Percentage of authority requests where a DENIED or CONDITIONAL decision was issued by G1, G2, or G3. Measures framework sensitivity — too high means framework is too restrictive; too low means reviews may not be rigorous enough.

**Target:** 5-20% (expected range; outside this range warrants investigation)

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-05 Blocker Rate | 5-20% | **25%** | 5-20% | — | **AMBER** |
| DENIED decisions | — | 0 | — | — | |
| CONDITIONAL decisions | — | **1** (EA-NADF-WP03-004) | — | — | |
| APPROVED decisions | — | 3 | — | — | |

G3 issued CONDITIONAL on EA-NADF-WP03-004 (EA-5 database mutation): new backup required
before first shell mutation. Condition is pre-acknowledged in WP-03 Go/No-Go §3 — the
backup requirement was already a planned pre-condition, not a new governance concern.
Blocker rate = 1 CONDITIONAL / 4 decisions = 25% → AMBER (marginally above GREEN upper 
bound of 20%). To be reassessed after WP-04 to confirm this is within acceptable variance.

**Threshold:** GREEN 5-20% | AMBER 1-4% or 21-30% | RED 0% or > 30%

Note: 0% would suggest reviewers are rubber-stamping; > 30% would suggest classification standard needs refinement.

---

## Section 3 — Decision Accuracy

*Does the framework make the right calls?*

### M-06 — Advisory Decision Accuracy Rate

**Definition:** In advisory mode, percentage of GRANTED decisions that were retrospectively confirmed as correct (i.e., execution succeeded without issue), and percentage of DENIED decisions that were retrospectively confirmed as justified.

**Target:** ≥ 85% overall accuracy

**Calculation:** (Correct advisory decisions ÷ Total advisory decisions) × 100

A GRANTED decision is retrospectively correct if: execution succeeded, no governance violation occurred, and post-execution review found no issue with the action.

A DENIED decision is retrospectively correct if: the concern raised by G1/G2/G3 was valid — the action would have caused an issue if executed without the raised concern being addressed.

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-06 Overall Accuracy | ≥ 85% | — | ≥ 90% | — | PENDING |
| Correct GRANTs | — | — | — | — | PENDING |
| Correct DENIEs | — | — | — | — | PENDING |
| False GRANTs (should have denied) | — | — | — | — | PENDING |
| False DENIEs (should have granted) | — | — | — | — | PENDING |

**Threshold:** GREEN ≥ 85% | AMBER 70-84% | RED < 70%

---

## Section 4 — Audit Trail Integrity

*Is the register complete and traceable?*

### M-07 — Register Completeness Rate

**Definition:** Percentage of authority entries that have all required fields populated and in a terminal status (Executed, Denied, or Revoked) at WP closure.

**Target:** 100% at each WP close

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-07 Register Completeness | 100% | — | 100% | — | PENDING |
| Complete terminal entries | — | — | — | — | PENDING |
| Open/incomplete entries at WP close | 0 | — | 0 | — | PENDING |

**Threshold:** GREEN = 100% | AMBER 90-99% | RED < 90%

---

### M-08 — Decision Log Entry Rate

**Definition:** Percentage of authority decisions (GRANTED and DENIED) that have a corresponding entry in AUTHORITY_DECISION_LOG.md.

**Target:** 100%

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-08 Log Entry Rate | 100% | **100%** | 100% | — | **GREEN** |
| Decisions with log entries | — | 4 / 4 | — | — | |
| Decisions without log entries | 0 | **0** | 0 | — | |

All 4 WP-03 advisory GRANTs (incl. 1 CONDITIONAL) are logged in AUTHORITY_DECISION_LOG.md
Entries 005–008. WP-04 prospective entries logged in Entry 009 as PENDING.

**Threshold:** GREEN = 100% | AMBER 90-99% | RED < 90%

---

## Section 5 — Escalation Performance

*Do escalation triggers route correctly?*

### M-09 — Escalation Routing Accuracy

**Definition:** Percentage of escalation trigger events that were correctly routed to the Human Sponsor (not resolved by A1).

**Target:** 100%

| Metric | WP-03 Target | WP-03 Actual | WP-04 Target | WP-04 Actual | Status |
|--------|-------------|-------------|-------------|-------------|--------|
| M-09 Escalation Accuracy | 100% | — | 100% | — | PENDING |
| Escalation events | — | — | — | — | PENDING |
| Correctly routed | — | — | — | — | PENDING |
| Incorrectly handled by A1 | 0 | — | 0 | — | PENDING |

**Threshold:** GREEN = 100% | AMBER = N/A | RED = any incorrect handling

---

## Section 6 — Human Sponsor Impact

*Is the framework reducing routine sponsor involvement as intended?*

### M-10 — Sponsor Routine Approval Count

**Definition:** Number of execution actions that required Human Sponsor approval in advisory mode. During the pilot, D2 continues under v1.0 so this should equal the total execution actions. This metric becomes meaningful post-pilot when binding mode activates.

**Baseline (v1.0, WP-01):** Record actual Human Sponsor approval count for WP-01 here for comparison.

| Metric | WP-01 Baseline | WP-03 Actual | WP-04 Actual |
|--------|----------------|-------------|-------------|
| M-10 Sponsor approvals | — (record from WP-01) | — | — |
| Advisory decisions issued | N/A | — | — |
| Delta (would-be reduction in binding mode) | N/A | — | — |

Note: During advisory pilot, D2 still requires v1.0 Human Sponsor approvals. The delta shows the projected reduction when binding mode activates.

---

## Section 7 — Overall Pilot Summary

*Assessed after WP-04 closes.*

| Metric | Target | WP-03 | WP-04 | Overall |
|--------|--------|-------|-------|---------|
| M-01 Coverage Rate | 100% | **GREEN** (100%) | PENDING | PENDING |
| M-02 Classification Accuracy | ≥ 90% | **GREEN** (100%) | PENDING | PENDING |
| M-03 Review Turnaround | ≥ 85% | **GREEN** (100%) | PENDING | PENDING |
| M-04 Review Completeness | 100% | **GREEN** (100%) | PENDING | PENDING |
| M-05 Blocker Rate | 5-20% | **AMBER** (25%) | PENDING | PENDING |
| M-06 Advisory Accuracy | ≥ 85% | PENDING ² | PENDING | PENDING |
| M-07 Register Completeness | 100% | PENDING ² | PENDING | PENDING |
| M-08 Decision Log Rate | 100% | **GREEN** (100%) | PENDING | PENDING |
| M-09 Escalation Accuracy | 100% | N/A (0 events) | PENDING | PENDING |
| M-10 Sponsor Approvals | — | PENDING ² | PENDING | PENDING |
| **Overall Status** | All GREEN | IN FLIGHT | PENDING | **IN FLIGHT** |

² Requires WP-03 execution to complete and exit gate to close before assessment.

---

## Dashboard Update Protocol

After each work package closes:

1. A1 completes the Advisory Mode Accuracy Report for that WP
2. A1 updates all metrics with actual values
3. A1 assigns GREEN / AMBER / RED to each metric
4. A1 updates Overall Status in the header block
5. A1 adds a WP-close entry to AUTHORITY_DECISION_LOG.md noting dashboard update
6. Human Sponsor receives summary notification

---

*AOP-013 Success Metrics Dashboard — A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25 (Baseline)*
