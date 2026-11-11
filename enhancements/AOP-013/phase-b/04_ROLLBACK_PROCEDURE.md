# AOP-013 — Pilot Rollback Procedure

---

**Document:** RBK-AOP-013
**Phase:** C — NADF Pilot
**Version:** 1.0
**Date:** 2026-06-25
**Prepared By:** G3 Security & Change Governance

---

## 1. Purpose

This document defines the conditions under which the AOP-013 pilot is rolled back, the step-by-step rollback procedure, the post-rollback assessment protocol, and the conditions under which the pilot may be re-attempted.

Because the pilot operates in advisory mode with no Agent OS core modifications and no NADF delivery modifications (Sponsor Conditions 1 and 2), the rollback impact is minimal. The pilot artifacts are two new files at the NADF project root. No existing files are modified. Rollback is therefore low-risk and fast.

---

## 2. Rollback Triggers

Rollback is required immediately if any of the following conditions are met during the pilot:

### Trigger T-01 — Critical Governance Violation

A1 issues an authority decision that violates a non-negotiable rule:
- A1 issues EXECUTION AUTHORITY GRANTED for an EA-6 action
- A1 issues authority without required governance reviews
- Any single reviewer's DENIED decision is overridden or ignored

**Severity:** Critical — immediate rollback required, Human Sponsor notification required.

---

### Trigger T-02 — Advisory Mode Breach

D2 acts on an advisory authority grant as if it were binding:
- D2 references advisory authority ID as the execution gate (bypassing v1.0 Human Sponsor flow)
- D2 executes an action solely on the basis of an advisory grant without Human Sponsor approval

**Severity:** High — stop pilot immediately, assess impact, notify Human Sponsor.

---

### Trigger T-03 — Register Integrity Failure

The Execution Authority Register becomes corrupted, incomplete, or inconsistent to a degree that the audit trail is no longer reliable:
- More than 20% of entries missing required fields at WP closure
- Entries modified retroactively without a logged reason
- Status transitions that violate the lifecycle (e.g., Active → Created)

**Severity:** High — pause pilot, assess register, attempt recovery before rollback.

---

### Trigger T-04 — Pilot Exit Criteria Failure

After WP-04 closes, the pilot exit criteria assessment (Phase B document 05) returns FAIL (fewer than 5 of 7 criteria met).

**Severity:** Medium — structured rollback and framework revision required; delivery continues normally.

---

### Trigger T-05 — Sponsor Direction

The Human Sponsor directs rollback at any time for any reason.

**Severity:** Immediate compliance required.

---

## 3. Rollback Procedure

### Advisory Mode Rollback (Applicable to all triggers)

Because the pilot runs in advisory mode with no core modifications, rollback is primarily an administrative closure. No system configuration is reversed.

---

**Step 1 — Stop Issuing Advisory Decisions**

A1 immediately ceases issuing advisory authority decisions.

Any authority requests in progress (Pending Review status) are cancelled. Reviewers are notified. No further GRANT or DENY decisions are issued.

---

**Step 2 — Log Rollback Event**

A1 adds a rollback entry to AUTHORITY_DECISION_LOG.md:

```
Rollback Entry
Date          : [ISO date]
Event         : AOP-013 PILOT ROLLBACK
Trigger       : T-0{N} — [trigger name]
Authority     : A1-NADF
Detail        : [description of what triggered rollback]
Immediate Impact : All advisory decisions halted. Pilot paused.
Human Sponsor Notified : Yes / Pending
```

---

**Step 3 — Notify Human Sponsor**

A1 notifies the Human Sponsor with:
- Rollback trigger that was activated
- Last advisory decision issued
- Any in-progress work packages affected
- Proposed next action (see Section 4)

Sponsor notification is required before any further pilot action is taken.

---

**Step 4 — Preserve Pilot Artifacts**

The Execution Authority Register and AUTHORITY_DECISION_LOG.md are **retained**, not deleted. They are the evidence record for the post-rollback assessment.

A1 marks the Execution Authority Register header:

```
Pilot Status : ROLLED BACK
Rollback Trigger : T-0{N}
Rollback Date : [ISO date]
```

---

**Step 5 — Assess Pilot Artifacts for Evidence of Cause**

G3 conducts a post-rollback review:

- What triggered the rollback?
- Was it a framework design flaw, a process failure, or a one-time error?
- Can the cause be corrected without a full framework revision?
- Is the framework recoverable for re-pilot?

G3 produces a brief Post-Rollback Assessment (added to AUTHORITY_DECISION_LOG.md as a single entry).

---

**Step 6 — NADF Delivery Continues Unaffected**

WP-03 and WP-04 continue under v1.0. Rollback of the pilot has zero impact on delivery. Human Sponsor continues to approve execution as normal.

---

**Step 7 — Determine Next Action**

Based on G3 Post-Rollback Assessment and Sponsor direction, A1 determines one of:

| Action | Condition |
|--------|-----------|
| **Revise and Re-Pilot** | Cause is identifiable and correctable; framework is recoverable |
| **Extend Advisory Window** | Pilot data is insufficient; extend to WP-05 or WP-06 |
| **Suspend AOP-013** | Cause is fundamental; framework needs substantial revision |
| **Reject AOP-013** | Framework is not viable; v1.0 continues permanently |

---

## 4. Rollback Impact Assessment

### What Rollback Affects

| Item | Impact |
|------|--------|
| EXECUTION_AUTHORITY_REGISTER.md | Retained as evidence; marked ROLLED BACK |
| AUTHORITY_DECISION_LOG.md | Retained as evidence; rollback event added |
| Phase B dashboard (document 03) | Updated to reflect rollback; metrics preserved |
| AOP-013 enhancement package | Retained; revision planned if applicable |

### What Rollback Does Not Affect

| Item | Impact |
|------|--------|
| NADF WP-03 / WP-04 delivery | No impact — pilot is advisory overlay |
| NADF project files | No impact — no core files were modified |
| Agent OS v1.0 core | No impact — not touched during pilot |
| FAMOIL / WAMACARE | No impact — pilot scope was NADF only |
| Human Sponsor approval flow | No impact — v1.0 flow was never suspended |

---

## 5. Re-Pilot Conditions

If the rollback assessment recommends "Revise and Re-Pilot", the following conditions must be met before the pilot restarts:

1. Root cause is documented in AUTHORITY_DECISION_LOG.md
2. Framework revision (if required) is reviewed and approved by G1/G2/G3
3. Sponsor approves re-pilot
4. The re-pilot uses a fresh EXECUTION_AUTHORITY_REGISTER.md (prior register is archived, not deleted)
5. The re-pilot window is a new WP pair (not the same WPs that triggered rollback)

---

## 6. Rollback Readiness Confirmation

Before the pilot activates, the following readiness questions must be answered YES:

```
□ Has this rollback procedure been reviewed by G3?
□ Does A1 know the rollback trigger conditions?
□ Is the Human Sponsor aware rollback is possible and knows the notification process?
□ Are NADF WP-03/WP-04 unblocked regardless of pilot outcome?
□ Is the Execution Authority Register format recoverable (backup not required — file is new)?
```

---

*AOP-013 Pilot Rollback Procedure — G3 Security & Change Governance*
*Software Factory Governance Authority — 2026-06-25*
