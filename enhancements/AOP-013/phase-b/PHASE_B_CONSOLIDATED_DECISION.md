# AOP-013 Phase B — Consolidated Governance Review Decision

---

**Document:** CBD-AOP-013-B
**Phase:** B — Governance Review
**Version:** 1.0
**Date:** 2026-06-25
**Compiled By:** A1 Master Orchestrator

---

## Phase B Outcome

```
Phase B Status        : COMPLETE PASS
Pilot Activation      : CLEARED — pending Sponsor activation instruction
Blocking Conditions   : 0 (G3-CON-001 and G3-CON-002 both confirmed resolved by G3)
G3 Verification       : CONFIRMED — 2026-06-25 (see G3_VERIFICATION_DECISION.md)
Remaining Action      : Sponsor issues pilot activation instruction
```

---

## Reviewer Decisions

| Reviewer | Role | Decision | Conditions | Observations |
|----------|------|----------|-----------|-------------|
| G1 | Architecture & Odoo Governance | **APPROVED WITH NOTE** | None | 4 (G1-OBS-001 through G1-OBS-004) |
| G2 | Quality & Documentation Governance | **APPROVED WITH NOTE** | None | 4 (G2-OBS-001 through G2-OBS-004) |
| G3 | Security & Change Governance | **CONDITIONAL** | 2 (G3-CON-001, G3-CON-002) | 4 (G3-OBS-001 through G3-OBS-004) |

---

## Blocking Conditions — Resolution Required Before Pilot Activation

### G3-CON-001 — Mode Field in Register Template

**Raised by:** G3 Security & Change Governance
**Also noted by:** G1 (G1-OBS-004), G2 (G2-OBS-002) — cross-cutting finding

**Finding:**
The `Mode: Advisory | Binding` field distinguishing pilot-phase entries from post-pilot binding entries is defined in the Pilot Activation Package (Phase B document 02) but is absent from the base register template in document 07 (EAR-NADF-001 Section 8). If the NADF register is initialised from the current template, the Mode field will be missing. Retroactive correction requires a logged reason and creates unnecessary audit complexity.

**Resolution required:**
A1 updates the register template in `07_EXECUTION_AUTHORITY_REGISTER.md` Section 8 to include the Mode field before initialising the NADF pilot register.

**Resolution action (A1):**
```
Update the "Template for New Entries" block in document 07 Section 8.
Add the following line after "Validity Scope":
  Mode  : Advisory | Binding
Also update the "Register Format" block in document 07 Section 2 to include Mode.
Then initialise the NADF EXECUTION_AUTHORITY_REGISTER.md with the corrected template.
```

**Effort:** Low (single document edit, no Sponsor action required)

---

### G3-CON-002 — A1 Advisory Decision Protocol Acknowledgement

**Raised by:** G3 Security & Change Governance
**Also noted by:** G1 (G1-OBS-003, recommended mitigation)
**Addresses:** OBS-003 from Phase B document 01 Section 9

**Finding:**
Sponsor Condition 1 prohibits agent prompt updates during the pilot. A1 will issue advisory authority grants operating on the v1.0 prompt. Without the v2.0 authority issuance protocol baked into its prompt, A1 may produce abbreviated, informal, or field-incomplete GRANT/DENY entries. The entire pilot validation rests on those entries as accuracy evidence. A malformed or inconsistent entry cannot be reliably scored against the exit criteria.

**Resolution required:**
Before A1 issues its first advisory authority decision, A1 must create a formal protocol acknowledgement entry in AUTHORITY_DECISION_LOG.md that: (a) cites the GRANT/DENY/REVOKE formats from document 04 Section 4, (b) cites the G1/G2/G3 review checklists from document 04 Section 6, and (c) commits that all advisory decisions will use those formats exactly. This creates an auditable commitment without modifying the agent prompt.

G1's recommended mitigation — A1 injecting the GRANT/DENY formats as a session-level context block at each pilot session start — is endorsed by G3 as a permitted operating practice under Condition 1 (it is not a prompt modification).

**Resolution action (A1):**
```
Initialise AUTHORITY_DECISION_LOG.md with two entries:
  Entry 001: Pilot Activated (standard activation entry per Phase B-02)
  Entry 002: Protocol Acknowledgement entry — citing document 04 Section 4 formats
             and document 04 Section 6 checklists; confirming all advisory decisions
             will follow those formats exactly
This log entry must precede the first advisory authority decision.
```

**Effort:** Low (log entry creation, no Sponsor action required)

---

## Non-Blocking Observations — Tracked for Action

### Cross-Cutting: VC-3 Advisory Mode Gap (G2-OBS-003 — Priority)

**Raised by:** G2 Quality & Documentation Governance

**Finding:**
Validation criterion VC-3 (D2 Executes Under Authority) requires D2 to reference authority IDs in execution records. Phase B document 02 explicitly states D2 does not reference advisory authority IDs during the pilot. VC-3 as written cannot pass in advisory mode. If unaddressed, a Pilot Validation Report reviewer could score VC-3 as FAIL when the framework is in fact operating correctly.

**Disposition:**
A1 documents the advisory mode handling of VC-3 in AUTHORITY_DECISION_LOG.md as part of the Protocol Acknowledgement entry (G3-CON-002 resolution). The acknowledgement records that M-06 (Advisory Decision Accuracy) is the operative advisory-mode proxy for VC-3, and that full VC-3 compliance is deferred to binding mode activation.

This prevents a disputed finding at validation time without modifying the Validation Plan.

**Action:** Incorporate VC-3 handling note in the G3-CON-002 Protocol Acknowledgement log entry. No separate action required.

---

### Pilot Plan WP-02 Reference (G2-OBS-001)

**Raised by:** G2 Quality & Documentation Governance

**Finding:**
Documents 10 and 11 reference WP-02 as the pilot window throughout. Sponsor Condition 4 changes this to WP-03/WP-04. A reader consulting document 10 or 11 without Phase B context will see a stale reference.

**Disposition:**
Before WP-03 begins, D4 adds a supersession notice banner to the top of documents 10 and 11:
```
> SUPERSESSION NOTICE: The pilot work package reference in this document (WP-02)
> is superseded by Sponsor Decision AOP-013-SD-001 Condition 4. The operative pilot
> window is WP-03 and WP-04. See enhancements/AOP-013/phase-b/02_NADF_PILOT_ACTIVATION_PACKAGE.md.
```

**Action:** D4 adds supersession banner to documents 10 and 11 before WP-03.

---

### EA-5 Internal Risk Stratification (G1-OBS-001)

**Raised by:** G1 Architecture & Odoo Governance

**Finding:**
EA-5 bundles CSV import via Odoo UI (ORM-validated, lower risk) and direct Python/SQL writes (bypass ORM, higher risk) at the same authority class. Both belong at EA-5 (classification correct), but G3 review depth and preconditions are appropriately different. The current standard makes no written distinction.

**Disposition:**
Deferred to Authority Classification Standard v1.1. Not blocking for pilot. No current NADF work packages are expected to involve direct Python/SQL writes beyond the EA-5 actions already executed (retrospective entries in the register).

**Action:** Flag for inclusion in post-pilot standard revision. No pilot impact.

---

### Rule 6 — Production Environment Override (G1-OBS-002)

**Raised by:** G1 Architecture & Odoo Governance

**Finding:**
Classification Rules 1-5 do not include an explicit environment-based override. A future agent could theoretically misclassify a production .conf change as EA-3. EA-6 definition covers this, but an explicit Rule 6 would close the written ambiguity.

**Disposition:**
Deferred to Authority Classification Standard v1.1. No production environments are in scope for the pilot (NADF is development/staging). No pilot impact.

**Action:** Flag for post-pilot standard revision. No pilot impact.

---

### Rollback T-01 Gap (G3-OBS-001)

**Raised by:** G3 Security & Change Governance

**Finding:**
Rollback Trigger T-01 does not explicitly name "A1 handles E-class escalation trigger internally" as a rollback condition. EC-6 catches this at exit criteria, but it should trigger immediate rollback, not a deferred finding.

**Disposition:**
Accepted observation. Exit criterion EC-6 (Escalation Integrity) is a non-negotiable FAIL condition, which effectively makes it an immediate rollback trigger when discovered. However, G3's point is valid — explicitly naming it in T-01 closes the gap. Update Rollback Procedure before binding mode activation.

**Action:** D4 adds T-01 sub-item to document 04 before binding mode activation. Not required for pilot.

---

### Advisory-to-Binding Transition Gate (G3-OBS-002)

**Raised by:** G3 Security & Change Governance

**Finding:**
Binding mode activation (described in document 05 Exit Criteria Section 6) requires a Sponsor decision after the Graduation Report, but there is no binding-mode readiness checklist at the moment of transition to ensure all advisory-mode workarounds (prompt non-updates, Mode field handling, VC-3 proxy) have been formally resolved.

**Disposition:**
The Phase D (FAMOIL) adoption package must include a Binding Mode Activation Checklist that resolves all advisory-mode workarounds before binding mode applies to any pod. This is a Phase D deliverable, not a pilot deliverable.

**Action:** Flag for Phase D package. No pilot impact.

---

### Misclassification Tagging (G3-OBS-003)

**Raised by:** G3 Security & Change Governance

**Finding:**
Misclassifications corrected mid-pilot (e.g., G1 reclassifies an EA-3 request to EA-4) should be tagged in the register to prevent them from being read as authoritative correct precedents in future calibration exercises.

**Disposition:**
A1 adds a `Reclassified` flag to any register entry where G1 corrects the submitted classification. The original submitted class is preserved; the confirmed class is added alongside.

**Action:** A1 incorporates `Reclassified` flag handling in the Protocol Acknowledgement log entry (G3-CON-002 resolution). No separate action required.

---

### EA-5 Recovery Fast-Path (G3-OBS-004)

**Raised by:** G3 Security & Change Governance

**Finding:**
"Database restore from backup" is classified EA-5 alongside planned data mutations. Emergency recovery actions under incident conditions may warrant a faster governance path.

**Disposition:**
Deferred. Emergency recovery actions are already governed by the existing `BACKUP_RECOVERY_STANDARD.md`. The EA-5 classification ensures governance oversight exists. A fast-path variant can be designed as part of a future AOP (AOP-014 or EA-5 sub-classification). Not appropriate to resolve mid-pilot.

**Action:** Flag for post-pilot program. No pilot impact.

---

## A1 Pre-Activation Actions

Before the NADF pilot register is initialised and before the first advisory authority decision is issued, A1 must complete:

| Action | Resolves | Target Document | Deadline |
|--------|----------|----------------|----------|
| Add Mode field to document 07 register template (Section 2 and Section 8) | G3-CON-001 | `07_EXECUTION_AUTHORITY_REGISTER.md` | Before NADF register init |
| Initialise NADF `EXECUTION_AUTHORITY_REGISTER.md` with corrected template | G3-CON-001 | `/Users/mac/nadf_erp/EXECUTION_AUTHORITY_REGISTER.md` | Before WP-03 |
| Initialise NADF `AUTHORITY_DECISION_LOG.md` with Entry 001 (activation) and Entry 002 (Protocol Acknowledgement — citing formats, checklists, VC-3 proxy, misclassification tagging) | G3-CON-002 + VC-3 gap + G3-OBS-003 | `/Users/mac/nadf_erp/AUTHORITY_DECISION_LOG.md` | Before first advisory decision |
| D4 adds supersession notice to documents 10 and 11 | G2-OBS-001 | `10_PILOT_PLAN.md`, `11_VALIDATION_PLAN.md` | Before WP-03 |

Once these four actions are complete, G3 is asked to confirm conditions resolved. Upon G3 confirmation, the pilot activates.

---

## Phase B Final Status

```
G1 Decision          : APPROVED WITH NOTE
G2 Decision          : APPROVED WITH NOTE
G3 Decision          : CONDITIONAL

Phase B Status       : CONDITIONAL PASS
Pilot Activation     : SUSPENDED
Blocking Conditions  : 2 (G3-CON-001, G3-CON-002)
Resolution Owner     : A1 (no Sponsor action required)
Non-Blocking Actions : 4 (G2-OBS-001, G1-OBS-001/002, G3-OBS-001)
Deferred Actions     : 4 (post-pilot standard revisions, Phase D deliverables)

Next Step            : A1 completes 4 pre-activation actions above
                       → G3 confirms resolution
                       → Phase C activates
                       → Pilot begins at WP-03

Human Sponsor        : Informed — no action required
```

---

## Cross-Review Concordance

Three findings were independently raised by multiple reviewers — confirming they are genuine issues, not single-reviewer artefacts:

| Finding | G1 | G2 | G3 |
|---------|----|----|-----|
| Mode field absent from register template | OBS-004 | OBS-002 | CON-001 (blocking) |
| Prompt non-update risk (OBS-003) | OBS-003 (mitigated) | Aware | CON-002 (blocking) |
| VC-3 advisory mode incompatibility | (not raised) | OBS-003 (priority) | Addressed in CON-002 resolution |

The cross-reviewer concordance validates G3's decision to make these blocking rather than advisory findings.

---

*AOP-013 Phase B Consolidated Governance Review Decision — A1 Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
