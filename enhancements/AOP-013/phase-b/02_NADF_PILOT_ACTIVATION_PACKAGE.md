# AOP-013 — NADF Pilot Activation Package

---

**Document:** PAP-NADF-AOP-013
**Phase:** C — NADF Pilot
**Version:** 1.0
**Date:** 2026-06-25
**Prepared By:** A1 Master Orchestrator

---

## 1. Purpose

This package defines everything needed to activate the AOP-013 Execution Authority Framework pilot on the NADF project pod. It incorporates all Sponsor conditions, defines the advisory mode operating protocol, specifies the artifacts to be created, and provides session-by-session operating guidance.

The pilot is a controlled experiment. Its purpose is to validate that the framework generates correct authority decisions across real work packages without disrupting delivery.

---

## 2. Pilot Parameters

| Parameter | Value |
|-----------|-------|
| Project pod | POD-NADF |
| Pilot window | WP-03 and WP-04 execution |
| Operating mode | Advisory (not binding) |
| Agent OS version | v1.0 (core unchanged) |
| Framework status | Overlay on v1.0 |
| Human Sponsor gate | Remains active for all execution (v1.0 behaviour) |
| Authority register | New file at NADF project root |
| Decision log | New file at NADF project root |
| Rollback trigger | See Phase B document 04 |
| Exit trigger | See Phase B document 05 |

---

## 3. Advisory Mode — Full Definition

### What Advisory Mode Is

Advisory mode is the operating state of the Execution Authority Framework during the NADF pilot. In advisory mode:

- A1 issues authority decisions (GRANTED / DENIED) using the standard GRANT and DENY formats
- Decisions are logged in the Execution Authority Register and AUTHORITY_DECISION_LOG.md
- D2 is **not required** to reference authority IDs before executing
- D2 executes under the v1.0 flow (Human Sponsor approval as normal)
- Authority decisions and execution outcomes are compared to assess framework accuracy

### What Advisory Mode Is Not

Advisory mode does not mean A1 skips the authority process. A1 completes the full authority lifecycle — G1/G2/G3 reviews, decision issuance, register entry — as if the decision were binding. The only difference is that D2 does not wait for the advisory decision before executing.

Advisory mode does not change:
- Human Sponsor approval requirements for execution (v1.0 behaviour preserved)
- Escalation triggers E1-E6
- EA-6 boundary (production is always Human-required)
- Governance review rigor (G1/G2/G3 complete full checklists)

### Advisory Mode Entry Format

Authority register entries during the pilot include an additional field:

```
Mode : Advisory
```

This field distinguishes pilot-phase entries from future binding-mode entries. When advisory mode ends, the field value changes to:

```
Mode : Binding
```

### Advisory Mode Accuracy Tracking

After each work package closes, A1 produces an Advisory Mode Accuracy Report:

- List all advisory decisions issued during the WP
- For each GRANTED decision: confirm D2 execution was successful (framework would have been correct)
- For each DENIED decision: confirm D2 execution was not attempted or confirmed the denial rationale
- Calculate accuracy rate: correct advisory decisions / total advisory decisions

This is the primary data source for the Success Metrics Dashboard (Phase B document 03).

---

## 4. Pilot Activation Checklist

The following steps are completed before WP-03 begins. None of these steps modify Agent OS core or NADF work packages.

### Step A — Create NADF Pilot Artifacts

**A1 creates the following new files at NADF project root (`/Users/mac/nadf_erp/`):**

```
EXECUTION_AUTHORITY_REGISTER.md
AUTHORITY_DECISION_LOG.md
```

These are new files. They do not modify any existing NADF file.

**A1 initialises AUTHORITY_DECISION_LOG.md with:**

```
Entry 001
Date   : [activation date]
Event  : AOP-013 PILOT ACTIVATED — NADF Pod
Mode   : Advisory
Window : WP-03 and WP-04
Authority : A1-NADF (instructed by Sponsor Decision AOP-013-SD-001)
Detail : Execution Authority Framework enters advisory pilot. All authority
         decisions during this window are advisory and non-binding. D2 continues
         under v1.0 execution flow. Framework accuracy is tracked for validation.
```

**A1 initialises EXECUTION_AUTHORITY_REGISTER.md** using the template in `enhancements/AOP-013/07_EXECUTION_AUTHORITY_REGISTER.md` with the Mode field added to the entry format.

### Step B — WP-03 Pre-Work Authority Assessment

Before WP-03 execution begins, D1 (Functional Architect) provides A1 with the WP-03 action list. A1 pre-classifies each action against the Authority Classification Standard and drafts the expected authority request.

This pre-classification serves two purposes:
1. It seeds the G1/G2/G3 review process before WP execution begins
2. It gives the pilot a baseline against which advisory decisions can be assessed

### Step C — Inform Human Sponsor

A1 informs the Human Sponsor that the pilot is activated, the advisory mode is in effect, and the register and log are live. Human Sponsor continues to provide execution approvals as per v1.0.

---

## 5. Pilot Operating Protocol — Per Work Package

### Before Work Package Begins

1. A1 receives WP action list from D1
2. A1 drafts authority request(s) — may combine actions of the same class into one request
3. A1 routes draft authority requests to G1/G2/G3 for review
4. G1/G2/G3 complete concurrent reviews
5. A1 issues advisory authority decisions and logs them
6. A1 adds entries to the register (Status: Active, Mode: Advisory)
7. Human Sponsor is informed of advisory decisions (not asked to approve)

### During Work Package Execution

8. D2 executes under v1.0 flow (Human Sponsor approval as normal)
9. D2 does not reference advisory authority IDs (advisory — not required)
10. A1 observes execution outcomes

### After Work Package Closes

11. A1 compares advisory decisions to execution outcomes
12. A1 updates register entries (Status: Executed, Outcome recorded)
13. A1 produces Advisory Mode Accuracy Report for the WP
14. A1 updates Success Metrics Dashboard
15. G2 validates register completeness

---

## 6. Pilot Artifact Map

| Artifact | Location | Created By | Modified By | Purpose |
|----------|----------|-----------|-------------|---------|
| `EXECUTION_AUTHORITY_REGISTER.md` | `/Users/mac/nadf_erp/` | A1 | A1 after each decision | Full authority audit trail |
| `AUTHORITY_DECISION_LOG.md` | `/Users/mac/nadf_erp/` | A1 | A1 after each event | Timestamped event log |
| `phase-b/03_SUCCESS_METRICS_DASHBOARD.md` | Enhancement package | A1 | A1 each WP | Pilot metrics tracking |
| Advisory Mode Accuracy Report (WP-03) | Enhancement package | A1 | After WP-03 closes | WP-03 accuracy assessment |
| Advisory Mode Accuracy Report (WP-04) | Enhancement package | A1 | After WP-04 closes | WP-04 accuracy assessment |

---

## 7. Roles During the Pilot

### A1 — Master Orchestrator (Advisory)
- Issues advisory authority decisions following governance review
- Maintains Execution Authority Register
- Maintains AUTHORITY_DECISION_LOG
- Produces Advisory Mode Accuracy Reports
- Updates Success Metrics Dashboard
- Routes to Human Sponsor for escalations (unchanged from v1.0)

### G1, G2, G3 — Governance Agents
- Complete authority reviews as if decisions were binding
- Issue APPROVED / DENIED / CONDITIONAL decisions
- Review completeness is the same as binding mode — no shortcuts

### D2 — Solution Builder
- Executes under v1.0 flow
- Does not reference advisory authority IDs
- Reports execution outcomes to A1 for accuracy tracking
- Notes where advisory decisions aligned or diverged from actual execution

### Human Sponsor
- Continues to provide execution approvals (v1.0 behaviour)
- Receives advisory decision notifications (informed, not approving)
- Reviews Success Metrics Dashboard updates
- Retains full authority — no change

### D4 — Knowledge & Documentation
- Documents advisory decisions alongside execution records
- Ensures Advisory Mode Accuracy Reports are filed correctly

---

## 8. Scope Boundaries

### What the Pilot Instruments

- Authority decisions for every execution action in WP-03 and WP-04
- G1/G2/G3 review quality and turnaround
- Register completeness
- Decision accuracy vs execution outcomes
- Escalation routing

### What the Pilot Does Not Touch

- NADF work package scope, acceptance criteria, or sequence
- NADF project files other than the two new root artifacts
- Agent OS core documents or prompts
- FAMOIL or WAMACARE projects
- Any production environment

---

## 9. Communication Plan

| Event | Audience | Format |
|-------|----------|--------|
| Pilot activated | Human Sponsor | AUTHORITY_DECISION_LOG entry + informal note |
| WP-03 advisory decisions issued | Human Sponsor | Inline with normal WP-03 reporting |
| WP-03 accuracy report complete | Human Sponsor | Phase B document update |
| WP-04 advisory decisions issued | Human Sponsor | Inline with normal WP-04 reporting |
| WP-04 accuracy report complete | Human Sponsor | Phase B document update |
| Pilot exit criteria assessment | Human Sponsor | Formal Pilot Validation Report |

---

*AOP-013 NADF Pilot Activation Package — A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
