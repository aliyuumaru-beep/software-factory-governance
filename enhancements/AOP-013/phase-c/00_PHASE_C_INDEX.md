# AOP-013 Phase C — NADF Pilot Index

---

**Phase:** C — NADF Advisory Pilot
**Status:** ACTIVE (activated 2026-06-25)
**Operating Mode:** Advisory — all decisions non-binding
**Pilot Window:** WP-03 Procurement Core + WP-04 HR Core
**Maintained By:** A1-NADF Master Orchestrator

---

## Phase C Documents

| # | Document | Status |
|---|----------|--------|
| PSR-001 | [Pilot Status Report #001](PHASE_C_PILOT_STATUS_REPORT_001.md) | Complete — pilot day 0 activation report |

---

## Live Pilot Artifacts (NADF project pod)

| Artifact | Location | Status |
|----------|---------|--------|
| Execution Authority Register | `/nadf_erp/EXECUTION_AUTHORITY_REGISTER.md` | Active — 9 entries (2 pre-pilot, 4 WP-03 advisory, 3 WP-04 pending) |
| Authority Decision Log | `/nadf_erp/AUTHORITY_DECISION_LOG.md` | Active — Entries 001–009 |

---

## Phase C Sequence

```
Phase B COMPLETE PASS ──▶ Sponsor Phase C Activation ──▶ Deploy Register
                                                        ──▶ Issue WP-03 advisory decisions
                                                        ──▶ WP-03 execution (v1.0 flow)
                                                        ──▶ WP-03 exit gate + accuracy assess
                                                        ──▶ WP-04 work package definition
                                                        ──▶ Issue WP-04 advisory decisions
                                                        ──▶ WP-04 execution (v1.0 flow)
                                                        ──▶ WP-04 exit gate + accuracy assess
                                                        ──▶ Pilot Assessment (Phase D)
```

---

## Current WP-03 Advisory Decisions

| Authority ID | Class | Decision | Mode |
|-------------|-------|---------|------|
| EA-NADF-WP03-001 | EA-1 Documentation | GRANTED | Advisory |
| EA-NADF-WP03-002 | EA-2 Repository | GRANTED | Advisory |
| EA-NADF-WP03-003 | EA-3 Configuration | GRANTED | Advisory |
| EA-NADF-WP03-004 | EA-5 DB Mutation | GRANTED (CONDITIONAL) | Advisory |

Condition on EA-NADF-WP03-004: G3-WP03-CON-001 — new backup before first shell mutation.

---

## Upcoming Milestones

| Milestone | Trigger | Action |
|-----------|---------|--------|
| WP-03 exit gate | WP-03 PR merged and reviewed | A1 assesses M-06 accuracy; updates register entries 003–006; produces PSR-002 |
| WP-04 definition | WP-03 merged | A1 creates WP-04 work package; Go/No-Go checkpoint; advisory decisions |
| WP-04 exit gate | WP-04 PR merged and reviewed | A1 assesses M-06 for WP-04; updates dashboard; pilots exit criteria |
| Phase D Assessment | Both WPs closed | A1 produces pilot assessment; exits criteria evaluated; recommendation to Sponsor |

---

*AOP-013 Phase C Index — A1-NADF Master Orchestrator — 2026-06-25*
