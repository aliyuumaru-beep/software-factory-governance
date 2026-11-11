# AOP-013 — Migration Plan
## Agent OS v1.0 → v2.0

---

**Document:** MIG-AOP-013
**Enhancement:** AOP-013 Execution Authority Framework
**Version:** 1.0
**Date:** 2026-06-25
**Author:** A1 Master Orchestrator

---

## 1. Purpose

This document defines the migration path from Agent OS v1.0 to Agent OS v2.0 across the three Software Factory project pods (NADF, FAMOIL, WAMACARE).

Migration is phased. The NADF pod is the pilot. FAMOIL and WAMACARE follow after pilot validation.

---

## 2. Migration Principles

**P1 — No disruption to active delivery.** NADF, FAMOIL, and WAMACARE continue delivery under Agent OS v1.0 during AOP-013 design. No work packages are modified.

**P2 — Pilot first.** NADF transitions to v2.0 first. Only after the pilot validation report is complete do the other pods migrate.

**P3 — Backward-compatible register.** The Execution Authority Register includes retrospective entries for any EA-class actions taken during v1.0 operation. This ensures a complete audit trail from the point of framework adoption.

**P4 — Prompt updates are atomic.** Agent prompts are updated as a single batch per pod. Partial updates (e.g., only A1 updated without D2) are not permitted.

**P5 — Configuration is explicit.** ACTIVE_AGENT_CONFIGURATION.md version is incremented only after all required changes are complete and validated.

---

## 3. Migration Phases

---

### Phase A — Design Framework

**Status:** COMPLETE
**Duration:** 2026-06-25 (single session)

**Deliverables:**
- [x] AOP-013 Specification
- [x] Architecture Impact Assessment
- [x] Governance Impact Assessment
- [x] Agent OS v2.0 Design
- [x] Authority Classification Standard
- [x] Approval Matrix
- [x] Execution Authority Register (template + NADF pilot entries)
- [x] Migration Plan (this document)
- [x] Risk Assessment
- [x] Pilot Plan
- [x] Validation Plan
- [x] Adoption Recommendation

**Gate:** All 12 deliverables complete and placed in `enhancements/AOP-013/`.

---

### Phase B — Governance Review

**Status:** Pending
**Duration:** 1-2 sessions

**Actions:**

1. G1 reviews AOP-013 Specification and Architecture Impact Assessment.
   - Confirms framework design is architecturally sound
   - Confirms Authority Classification Standard is complete
   - Approves or requests revision

2. G2 reviews Governance Impact Assessment and all governance artifact templates.
   - Confirms governance model is not degraded
   - Confirms register and log formats are sufficient
   - Approves or requests revision

3. G3 reviews Risk Assessment and security implications.
   - Confirms EA-5/EA-6 controls are adequate
   - Confirms escalation rules cover all security risks
   - Approves or requests revision

4. A1 compiles review outcomes.
   - All approved → proceed to Phase C
   - Any denial → revise and re-review

**Gate:** G1/G2/G3 all approved. A1 records GOVERNANCE REVIEW COMPLETE in AUTHORITY_DECISION_LOG.md.

---

### Phase C — Pilot on NADF

**Status:** Pending (after Phase B)
**Duration:** 2-4 sessions (first full work package under v2.0)

**Actions:**

1. Update NADF agent prompts to v2.0:
   - PROMPT_A1 — add authority issuance protocol
   - PROMPT_G1 — add authority classification checklist
   - PROMPT_G2 — add traceability validation block
   - PROMPT_G3 — add change impact / rollback validation block
   - PROMPT_D2 — add authority verification pre-condition

2. Create NADF pod governance artifacts:
   - `EXECUTION_AUTHORITY_REGISTER.md` at NADF project root
   - `AUTHORITY_DECISION_LOG.md` at NADF project root

3. Update `ACTIVE_AGENT_CONFIGURATION.md`:
   - Increment version to 2.0
   - Add execution authority settings

4. Update Agent OS core docs:
   - `Autonomous-agent-Team/docs/02_AUTHORITY_MATRIX.md` — replace stub with full matrix
   - `Autonomous-agent-Team/docs/03_ESCALATION_POLICY.md` — add EA-6 clause
   - `Autonomous-agent-Team/docs/01_SOFTWARE_FACTORY_AGENT_FRAMEWORK.md` — add authority flow

5. Execute first full work package under v2.0:
   - NADF WP-02 Finance Core is the designated pilot work package
   - All execution actions must reference authority IDs
   - Register must be updated in real time

6. Complete Pilot Validation Report (see Validation Plan).

**Gate:** Pilot Validation Report confirms all 7 validation criteria met.

---

### Phase D — Apply to FAMOIL

**Status:** Planned (after Phase C validation)
**Duration:** 1-2 sessions

**Actions:**

1. Update FAMOIL agent prompts to v2.0 (same prompt changes as Phase C).
2. Create FAMOIL pod governance artifacts (Register + Decision Log).
3. Configure FAMOIL ACTIVE_AGENT_CONFIGURATION to v2.0.
4. Execute first FAMOIL work package under v2.0.
5. Confirm no deviations from NADF pilot experience.

**Gate:** FAMOIL completes first work package with full authority trail. No governance deviations.

---

### Phase E — Apply to WAMACARE

**Status:** Planned (after Phase D)
**Duration:** 1-2 sessions

**Actions:**

1. Update WAMACARE agent prompts to v2.0.
2. Create WAMACARE pod governance artifacts.
3. Configure WAMACARE ACTIVE_AGENT_CONFIGURATION to v2.0.
4. Execute first WAMACARE work package under v2.0.
5. Confirm no deviations.

**Gate:** WAMACARE completes first work package with full authority trail.

---

### Phase F — Portfolio Orchestration

**Status:** Planned (after Phase E)
**Duration:** Ongoing

**Actions:**

1. All three pods operating concurrently under v2.0.
2. A1 instances (NADF/FAMOIL/WAMACARE) operating independently.
3. Shared G1/G2/G3 serving all pods.
4. Human Sponsor receives summary governance reports rather than task-level approvals.
5. Portfolio-level dashboards reviewed by Human Sponsor at phase gates.

**Gate:** One complete phase gate cycle completed across all three pods simultaneously without Human Sponsor bottleneck.

---

## 4. Rollback Plan

If the NADF pilot (Phase C) reveals a critical flaw:

1. Revert NADF agent prompts to v1.0 versions.
2. Set `ACTIVE_AGENT_CONFIGURATION.md` back to version 1.0.
3. Archive the EXECUTION_AUTHORITY_REGISTER.md for post-incident review.
4. Document the failure in AOP-013 Risk Register (see document 09).
5. Revise the framework design and re-enter Phase A.

FAMOIL and WAMACARE are unaffected — they remain on v1.0 throughout the pilot.

---

## 5. Timeline

| Phase | Activity | Target |
|-------|----------|--------|
| A | Design Framework | 2026-06-25 COMPLETE |
| B | Governance Review | 2026-Q3 |
| C | NADF Pilot | 2026-Q3 |
| D | FAMOIL Adoption | 2026-Q3/Q4 |
| E | WAMACARE Adoption | 2026-Q4 |
| F | Portfolio Orchestration | 2027-Q1 |

---

## 6. Dependencies

| Dependency | Impact |
|------------|--------|
| NADF WP-02 must be the next work package | Pilot requires a real WP to exercise; WP-02 is ready |
| G1/G2/G3 must complete Phase B review before NADF prompts are updated | Phase C cannot begin without governance approval |
| FAMOIL governance maturity | Phase D requires FAMOIL to have CLAUDE.md and basic governance in place |
| WAMACARE governance maturity | Phase E requires WAMACARE minimum governance |

---

*AOP-013 Migration Plan — A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
