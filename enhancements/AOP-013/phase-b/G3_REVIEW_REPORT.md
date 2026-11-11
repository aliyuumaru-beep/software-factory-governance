# AOP-013 — G3 Security & Change Governance Review Report

---

**Document:** G3-REV-AOP-013-B
**Phase:** B — Governance Review
**Date:** 2026-06-25
**Reviewer:** G3 Security & Change Governance
**Enhancement:** AOP-013 Execution Authority Framework
**Decision Reference:** AOP-013-SD-001 (Sponsor Decision — ADOPT WITH CONDITIONS)

---

## DECISION

**CONDITIONAL**

The AOP-013 framework is security-sound in design and advisory mode is correctly structured as a safety wrapper. G3 confirms the framework is ready to proceed to Phase C pilot subject to the conditions stated in Section 7 of this report. Two conditions must be resolved before WP-03 begins. Four observations are recorded as non-blocking notes for ongoing pilot governance.

---

## 1. Review Basis

This review was conducted against the following documents:

| Document | Version |
|----------|---------|
| `00_SPONSOR_DECISION.md` — AOP-013-SD-001 | 2026-06-25 |
| `01_AOP-013_SPECIFICATION.md` | 1.0 |
| `04_AGENT_OS_V2_DESIGN.md` | 1.0 |
| `09_RISK_ASSESSMENT.md` | 1.0 |
| `05_AUTHORITY_CLASSIFICATION_STANDARD.md` | 1.0 |
| `phase-b/01_GOVERNANCE_REVIEW_PACKAGE.md` | 1.0 |
| `phase-b/04_ROLLBACK_PROCEDURE.md` | 1.0 |
| `phase-b/05_PILOT_EXIT_CRITERIA.md` | 1.0 |
| `phase-b/02_NADF_PILOT_ACTIVATION_PACKAGE.md` | 1.0 |

Review scope is the AOP-013 enhancement design package as-staged. No Agent OS core documents or NADF work package documents are in scope (Sponsor Conditions 1 and 2).

---

## 2. EA-6 and Production Boundary

### Checklist Items

**[PASS] EA-6 (Production Authority) is permanently reserved for the Human Sponsor. No pathway exists for A1 to issue EA-6 authority under any condition.**

Rationale: Document 04 Section 7 is explicit — "Human Required" for EA-6; A1 routes to Human Sponsor regardless of governance review outcome. Document 05 Section 3 states: "A1 does not issue authority for EA-6." This is correctly stated as an architectural hard rule, not a policy default. No conditional pathway or exception clause exists that would allow A1 to issue EA-6 authority.

---

**[PASS] The EA-6 definition in document 05 Section 3 is unambiguous: ANY action on a production environment is EA-6 regardless of perceived risk.**

Rationale: The definition is broad and correctly framed: "Authority for any action on the production environment." The examples list covers deployment, upgrade, configuration, database modification, and backup/restore on production. The note at the end of the EA-6 section acknowledges that all current Software Factory environments are development/staging, which is accurate and appropriately contextualised.

---

**[PASS] Classification Rule 4 (EA-6 is non-negotiable) is correctly stated and its enforcement mechanism (G3 must flag misclassification) is defined.**

Rationale: Rule 4 in document 05 states "No classification analysis can result in a production action being classified below EA-6." Document 09 RISK-006 names G3 as responsible for flagging EA-6 masquerade attempts. The chain — Rule 4 in the standard, G3 as enforcer, RISK-006 as risk control — is coherent and complete.

---

## 3. Escalation Integrity

### Checklist Items

**[PASS] All escalation triggers are preserved and unchanged by AOP-013.**

Rationale: Document 01 Section 8 lists seven escalation triggers (EA-6 Production Authority, scope increase, new unapproved module, budget impact, security exception, governance exception, portfolio reprioritisation). Cross-referencing against the established escalation policy, AOP-013 adds no new escalation triggers and removes none. The framework is purely additive to the escalation layer.

---

**[PASS] The EA-6 authority class is additive to escalation — it does not replace E5 (Production Risk); it operates in parallel.**

Rationale: The AOP-013 design distinguishes authority classes (EA-1 through EA-6) from escalation classes (E-series). EA-6 is a classification rule preventing A1 from issuing production authority. E5 Production Risk is the escalation trigger that routes to the Human Sponsor when a production risk is identified. They operate at different layers of the governance model and do not conflict.

---

**[PASS] Escalation rules in document 01 Section 8 cover all security-relevant scenarios.**

Rationale: The escalation table covers security exceptions explicitly ("Security exception — Risk beyond governance mandate"). Scope increase, governance exception, and budget authority are also preserved. G3 notes one observation on the completeness of this list — see G3-OBS-002 below.

---

## 4. Advisory Mode Security

### Checklist Items

**[PASS] Advisory mode does not introduce a security risk. D2 proceeds under v1.0 controls (Human Sponsor approval) during the pilot. Advisory authority grants do not expand D2's actual execution permissions.**

Rationale: Document 02 Section 3 is precise on this point: "D2 is not required to reference authority IDs before executing" and "D2 executes under the v1.0 flow (Human Sponsor approval as normal)." Advisory grants are logically separate from execution permission. The Human Sponsor gate on execution remains fully intact.

---

**[PASS] The transition from advisory to binding mode requires an explicit Sponsor activation decision. There is no automatic transition.**

Rationale: Document 05 (Pilot Exit Criteria) Section 6 is unambiguous: "Binding mode is not automatic on GRADUATE. The Human Sponsor must explicitly activate it." The activation sequence requires Graduation Report review, resolution of any CONDITIONAL PASS items, and a formal Sponsor issuance of "BINDING MODE ACTIVATED — NADF." G3 notes one observation on the sufficiency of the security gate between advisory and binding — see G3-OBS-003 below.

---

**[CONDITIONAL — see G3-CON-001] Advisory mode grants are clearly marked as non-binding in the register to prevent future misinterpretation as binding precedents.**

Rationale: Document 02 Section 3 defines a `Mode: Advisory` field for register entries, and the Activation Package (Phase B document 02) confirms the Mode field will be added to the entry format. However, the register template in the base package (document 07, not reviewed directly by G3 but referenced throughout) must be confirmed to include this Mode field before pilot activation. Without it, advisory-phase entries will lack the field that distinguishes them from future binding-mode entries. G3-CON-001 addresses this.

---

## 5. Risk Assessment

### Checklist Items

**[PASS] The 10 risks in document 09 are comprehensive. No significant security or change risk has been omitted.**

Rationale: The register covers governance (RISK-001, 003, 005, 006, 010), performance (RISK-002), architecture (RISK-004, 007), continuity (RISK-008), and adoption (RISK-009). The risk scoring methodology (L × I, 1-5 scale) is appropriate. All High-rated pre-mitigation risks (RISK-001, 005, 006) have credible mitigations with named responsible parties. G3 identifies one unregistered risk — see G3-OBS-004 below.

---

**[PASS] RISK-006 (EA-6 Boundary Drift) mitigation is adequate.**

Rationale: The mitigation chain is sound: EA-6 definition is absolute (document 05 Rule 4), G3 is named as responsible for flagging misclassification (document 09), and A1 is instructed with a hard rule rather than a judgement call. The residual risk rating of Low (2) is appropriately conservative.

---

**[PASS] RISK-005 (Misclassification) mitigation is adequate for advisory mode.**

Rationale: G1 confirms or corrects classification during review, Rule 5 (uncertainty escalates) creates a conservative floor, and the Quick Reference table (document 05 Section 4) reduces ambiguity for common actions. In advisory mode, a misclassification does not block execution, which further limits acute harm. G3 notes a structural concern about misclassification and training data entrenchment — see G3-OBS-004.

---

**[PASS] The rollback procedure (Phase B document 04) is executable and complete.**

Rationale: The five rollback triggers (T-01 through T-05) are defined with severity levels and distinct response protocols. The rollback steps are sequential and actionable. Because the pilot is advisory-only with no core modifications, the rollback impact is correctly assessed as administrative closure rather than system reversal. The preservation-not-deletion policy for pilot artifacts is the correct evidential approach.

---

## 6. Change Impact

### Checklist Items

**[PASS] AOP-013 is contained within the enhancement package. Change impact is Low.**

Rationale: Sponsor Conditions 1 and 2 enforce a hard containment boundary: no Agent OS core modification, no NADF work package modification. The only net-new files during the pilot are two files at the NADF project root (EXECUTION_AUTHORITY_REGISTER.md and AUTHORITY_DECISION_LOG.md). No existing file is modified. This is the minimum possible change footprint for a governance pilot of this scope.

---

**[PASS] The pilot registers and decision logs created at NADF project root are new files; they do not overwrite or modify existing files.**

Rationale: Confirmed by Phase B document 02 Section 4 Step A, which explicitly states "These are new files. They do not modify any existing NADF file." The file paths are specified (`/Users/mac/nadf_erp/`). No ambiguity.

---

## 7. G3 Conditions (Blocking — Must Be Resolved Before Pilot Activates)

### G3-CON-001 — Mode Field Confirmation in Register Template

**Condition:** Before WP-03 begins, A1 must confirm that the Execution Authority Register template (document 07) has been updated to include the `Mode: Advisory | Binding` field, or that the Pilot Activation Package's instruction to add the Mode field will be applied to every register entry from the first entry onward.

**Basis:** Checklist item "Advisory mode grants are clearly marked as non-binding" cannot be fully verified without confirming the register template includes this field. If the first register entries are created without the Mode field, retroactive addition would constitute a modification requiring a logged reason — unnecessary complexity that is avoided by confirming the field exists before activation.

**Resolution:** A1 confirms in writing (AUTHORITY_DECISION_LOG.md) before pilot activation that the Mode field is included in the register entry format. This can be done as part of the PILOT ACTIVATED log entry — no separate document revision is required.

---

### G3-CON-002 — A1 Advisory Decision Protocol Acknowledgement (OBS-003)

**Condition:** Before WP-03 begins, A1 must produce a brief written acknowledgement confirming its understanding of the advisory protocol constraints under Sponsor Condition 1 (no prompt updates). Specifically, A1 must confirm:

1. It will use the GRANT/DENY/REVOKE formats defined in document 04 Section 4 in full, without abbreviation, even though prompts are not updated.
2. It will maintain the register in the format specified in the Activation Package for every advisory decision, not a summarised or informal substitute.
3. It understands that format drift in advisory-mode decisions is a data quality risk for the accuracy assessment — malformed GRANT entries cannot be reliably compared to execution outcomes.

**Basis:** This addresses OBS-003 from the Governance Review Package Section 9. Sponsor Condition 1 means A1 is operating the v2.0 authority process using the v1.0 prompt structure. This creates a process compliance risk: without prompt updates, A1 may issue advisory decisions in an informal, partial, or inconsistent format. In advisory mode, the grants do not gate execution — but they are the primary validation dataset. A grant entry that is missing fields, uses a non-standard format, or omits an approvals section cannot be scored for accuracy. The entire pilot validation rests on the quality and consistency of A1's advisory decisions. This is not a theoretical risk; it is a data integrity prerequisite.

**Resolution:** A1 records the acknowledgement in AUTHORITY_DECISION_LOG.md as a pre-activation entry (before Entry 001 of the pilot proper). No framework document revision is required.

---

## 8. G3 Observations (Non-Blocking)

### G3-OBS-001 — Rollback Trigger T-01 Definition Gap

**Classification:** Observation — Non-blocking

**Finding:** Rollback Trigger T-01 (Critical Governance Violation) names three specific violations: A1 issuing EA-6 authority, A1 issuing authority without required reviews, and a reviewer's DENIED decision being overridden. These three are correctly identified. However, T-01 does not name a fourth critical governance violation that the framework itself defines: an escalation trigger being handled internally by A1 rather than being routed to the Human Sponsor (as required by document 01 Section 8 and Exit Criterion EC-6).

An internal escalation handling failure is distinct from an EA-6 grant. It would occur if A1 received a scope change request or a security exception and issued an authority grant rather than routing to the Sponsor. Under the current T-01 definition, this would not trigger immediate rollback — it would only surface at exit criteria assessment (EC-6 FAIL), which could be after WP-04 closes.

**Recommendation:** Consider adding a fourth bullet to T-01: "A1 handles an E-class escalation trigger internally rather than routing to Human Sponsor." G3 does not make this a condition because the EC-6 criterion would still catch the failure before GRADUATE is declared, and pilot artifact retention would preserve the evidence. However, earlier detection is preferable for a critical governance class of error.

---

### G3-OBS-002 — Binding Mode Transition Security Gate

**Classification:** Observation — Non-blocking

**Finding:** Document 05 Section 6 correctly requires explicit Sponsor activation before binding mode engages. The gate is: Graduation Report reviewed by Sponsor, CONDITIONAL PASS items resolved or accepted, Sponsor issues formal activation. This is structurally sound.

However, the gate between advisory and binding mode is exclusively a human decision based on a framework-generated report. There is no independent technical or governance checkpoint that verifies the A1 instance that will operate in binding mode is the same A1 that operated in advisory mode — that is, that no prompt configuration changes, context drift, or session-boundary issues have occurred between the last advisory session and the first binding session.

For advisory mode, this gap is immaterial. For binding mode, where A1 decisions gate D2 execution, the absence of a "binding mode readiness check" at transition time is a latent risk. The Sponsor decision activates a mode change, but no one verifies the agent is ready to operate in that mode at activation time.

**Recommendation:** Before Phase D (FAMOIL adoption), G3 recommends adding a binding mode readiness check step to the activation sequence: a test authority request that exercises the full GRANT/DENY cycle under binding conditions, reviewed by G1/G2/G3, before live delivery execution is authorized. This is outside the NADF pilot scope and is not a Phase C condition.

---

### G3-OBS-003 — RISK-005 Misclassification and Training Data Entrenchment

**Classification:** Observation — Non-blocking

**Finding:** RISK-005 (Incorrect Authority Classification) is assessed as High pre-mitigation, reduced to Low (2) post-mitigation. The mitigations are appropriate for preventing individual misclassifications from causing harm. However, there is a structural concern that the risk register does not address: if the advisory pilot is used as classification training data for future framework tuning — which is the intended use (see document 05 EC-2, Classification Accuracy criterion) — then a systematic misclassification pattern in WP-03 that is corrected only in WP-04 may still influence future boundary decisions if WP-03 data is weighted equally to WP-04 data.

The EC-2 criterion correctly flags "recurring error type in both WPs" as a FAIL condition. But a recurring error type in WP-03 only (corrected in WP-04) would qualify as CONDITIONAL PASS — and the WP-03 misclassified entries remain in the register as historical data. If future maintainers treat the register as authoritative classification precedent without distinguishing corrected-in-WP-04 entries, wrong patterns could be entrenched.

**Recommendation:** The Advisory Mode Accuracy Reports (produced after each WP) should explicitly tag corrected misclassifications in the register with a `Classification Corrected: [date] [rationale]` marker, so historical entries are not treated as validated precedents. This is a low-cost data hygiene step that prevents a future data quality problem.

---

### G3-OBS-004 — EA-5 Recovery Action Classification

**Classification:** Observation — Non-blocking

**Finding:** The EA-5 definition in document 05 Section 3 includes "Database restore from backup" in the list of qualifying actions. The Quick Reference table also maps "Restore database from backup" to EA-5. This is architecturally consistent — a database restore does alter stored data and cannot be undone without another restore.

However, database restore is typically a recovery action, not a mutation action. The governance overhead of EA-5 (G1/G2/G3 review, one-to-two session turnaround, backup verification precondition) is appropriate when the restore is planned as part of a rollback from a failed data migration. It is potentially excessive when the restore is an emergency recovery from data corruption or accidental deletion, where speed of recovery is the primary concern.

In the current Software Factory context (development and staging environments only), this distinction is low-stakes. In a future production-adjacent context, requiring full EA-5 governance for an emergency restore could delay recovery in a time-critical situation. EA-6 already covers production database restores.

**Recommendation:** Before binding mode is activated for any project, G3 recommends the Sponsor and G1 consider whether to create an exception pathway for emergency recovery restores on development/staging databases: for example, a Recovery Fast-Path classification within EA-5 that permits G3-only review (rather than G1+G2+G3) when the restore is in response to a documented failure event. This is a design discussion for the v2.1 enhancement cycle, not a Phase C issue.

---

## 9. Summary Decision Matrix

| Checklist Area | Item | Result |
|---|---|---|
| EA-6 Boundary | EA-6 reserved for Human Sponsor — no A1 pathway | PASS |
| EA-6 Boundary | EA-6 definition unambiguous (any production action) | PASS |
| EA-6 Boundary | Rule 4 enforcement mechanism defined | PASS |
| Escalation Integrity | All escalation triggers preserved unchanged | PASS |
| Escalation Integrity | EA-6 additive to E5, not replacing | PASS |
| Escalation Integrity | Escalation rules cover security-relevant scenarios | PASS |
| Advisory Mode Security | Advisory grants do not expand D2 permissions | PASS |
| Advisory Mode Security | Advisory-to-binding transition requires explicit Sponsor decision | PASS |
| Advisory Mode Security | Advisory entries distinguishable from binding entries | CONDITIONAL (G3-CON-001) |
| Risk Assessment | Risk register is comprehensive | PASS |
| Risk Assessment | RISK-006 (EA-6 Drift) mitigation adequate | PASS |
| Risk Assessment | RISK-005 (Misclassification) mitigation adequate for advisory mode | PASS |
| Risk Assessment | Rollback procedure executable and complete | PASS |
| Change Impact | AOP-013 contained within enhancement package | PASS |
| Change Impact | Pilot artifacts are net-new files only | PASS |

---

## 10. Conditions Summary

| ID | Condition | Resolution Required By |
|----|-----------|----------------------|
| G3-CON-001 | Mode field confirmation in register template | Before WP-03 begins |
| G3-CON-002 | A1 advisory decision protocol acknowledgement (addresses OBS-003) | Before WP-03 begins |

Both conditions are resolvable by A1 via a single AUTHORITY_DECISION_LOG.md pre-activation entry. No framework document revision is required. No Sponsor action is required for resolution.

---

## 11. Ongoing Pilot Monitoring — G3 Responsibilities

During the pilot, G3 will:

1. Complete G3 authority reviews (EA-3, EA-4, EA-5 requests) as if decisions were binding, per the advisory mode protocol.
2. Specifically monitor EA-6 boundary compliance — flag any advisory grant that approaches EA-6 territory, even in a development/staging context.
3. Monitor T-01 violation indicators in AUTHORITY_DECISION_LOG.md.
4. At WP-03 and WP-04 closure, assess whether the misclassification tracking recommendation in G3-OBS-003 has been applied to the Accuracy Reports.
5. Contribute to the EC-6 (Escalation Integrity) assessment at pilot exit.

---

## 12. G3 Decision

```
Decision    : CONDITIONAL
Date        : 2026-06-25
Reviewer    : G3 Security & Change Governance
Rationale   : The AOP-013 framework is security-sound. EA-6 boundary is
              correctly defined and hard-coded. Advisory mode correctly
              preserves all v1.0 Human Sponsor controls. Rollback procedure
              is adequate and low-impact. The two conditions are administrative
              prerequisites that can be resolved by A1 before pilot activation
              without framework revision or Sponsor action. Four observations
              are non-blocking and addressed to appropriate owners for
              consideration during and after the pilot.
Conditions  : G3-CON-001 (Mode field confirmation) and G3-CON-002 (A1
              advisory protocol acknowledgement) must both be recorded in
              AUTHORITY_DECISION_LOG.md before WP-03 begins. G3 will confirm
              resolution before issuing final APPROVED status.
```

---

*G3 Security & Change Governance Review Report — AOP-013 Phase B*
*Software Factory Governance Authority — 2026-06-25*
