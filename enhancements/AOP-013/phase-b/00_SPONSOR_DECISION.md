# AOP-013 — Sponsor Decision Record

---

**Decision ID:** AOP-013-SD-001
**Date:** 2026-06-25
**Decision Type:** ADOPT WITH CONDITIONS
**Issued By:** Human Sponsor / Software Factory Governance Authority
**Received By:** A1 Master Orchestrator

---

## Decision

**ADOPT WITH CONDITIONS**

AOP-013 Execution Authority Framework is approved to proceed to Phase B (Governance Review) and Phase C (NADF Pilot) subject to the following conditions.

---

## Conditions

### Condition 1 — No Agent OS Core Modification
Agent OS core documents, agent prompts, and ACTIVE_AGENT_CONFIGURATION.md must not be modified during Phase B or Phase C. All v2.0 changes are staged in the enhancement package only.

**Implication:** The authority framework operates as an overlay on v1.0 during the pilot. D2 operates on v1.0 execution flow. A1 issues authority grants in parallel but they do not gate execution.

### Condition 2 — No NADF Delivery Modification
Active NADF delivery work packages and their scope, acceptance criteria, or execution plan must not be modified to accommodate the pilot. The pilot runs alongside normal delivery.

**Implication:** WP-03 and WP-04 proceed on their defined scope. The pilot instruments the authority framework around those work packages without altering them.

### Condition 3 — Advisory Mode Only
Execution Authority decisions issued by A1 during the pilot are advisory. They are formally issued, logged, and evaluated but they do not gate or block D2 execution until pilot validation is complete and binding mode is formally activated.

**Implication:** This is the critical safety condition. The framework is exercised in parallel with normal delivery. If the framework produces wrong decisions or encounters issues, delivery is not blocked. See Phase B document 01 for the full advisory mode protocol.

### Condition 4 — Pilot Scope: WP-03 and WP-04
The NADF pilot window is WP-03 and WP-04 execution. Not WP-02 as originally proposed in the Pilot Plan. The original Pilot Plan is superseded for scope purposes; all other content remains valid.

**Implication:** WP-02 completes under v1.0. WP-03 is the first pilot WP. WP-04 provides a second cycle for validation confidence.

### Condition 5 — No Portfolio Rollout
Phase D (FAMOIL) and Phase E (WAMACARE) are suspended until pilot exit criteria are met and the Sponsor issues a separate activation decision.

**Implication:** Portfolio orchestration capability (Phase F) is not a target during this phase.

---

## Deliverables Authorised

| # | Document | Status |
|---|----------|--------|
| Phase B-01 | Phase B Governance Review Package | Required before pilot activation |
| Phase B-02 | NADF Pilot Activation Package | Required before WP-03 begins |
| Phase B-03 | Success Metrics Dashboard | Required before WP-03 begins |
| Phase B-04 | Rollback Procedure | Required before WP-03 begins |
| Phase B-05 | Pilot Exit Criteria | Required before WP-03 begins |

---

## A1 Acknowledgement

A1 acknowledges the Sponsor decision and conditions. All Phase B deliverables are produced under the constraint of Conditions 1 and 2 (no core modification, no delivery modification).

Phase B governance review will be conducted against the AOP-013 package as-designed, with conditions applied. G1/G2/G3 review packages incorporate Condition 3 (advisory mode) as a formal governance requirement for the pilot phase.

---

*AOP-013 Sponsor Decision Record — Recorded by A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
