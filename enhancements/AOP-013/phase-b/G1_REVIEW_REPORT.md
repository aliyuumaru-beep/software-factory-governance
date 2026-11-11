# G1 Review Report — AOP-013 Execution Authority Framework
## Phase B Governance Review

---

**Document:**       G1-RR-AOP-013-B
**Phase:**          B — Governance Review
**Review Type:**    Formal Architecture & Odoo Governance Review
**Reviewer:**       G1 Architecture & Odoo Governance
**Review Date:**    2026-06-25
**Enhancement:**    AOP-013 Execution Authority Framework
**Addressed To:**   A1 Master Orchestrator, Human Sponsor

---

## Decision

**APPROVED WITH NOTE**

The AOP-013 Execution Authority Framework is architecturally sound and compatible with advisory-mode pilot operation on NADF WP-03 and WP-04. The framework may proceed to Phase C activation subject to the notes and observations recorded in this report. No blocking conditions are raised. Three formal observations are recorded for the attention of A1 and the Sponsor.

---

## 1. Review Scope

This review covers the G1 checklist items from GRP-AOP-013-B Section 4, grouped into three areas:

1. Framework Architecture
2. Advisory Mode Compatibility
3. Pilot Scope Compatibility

Documents reviewed:
- `00_SPONSOR_DECISION.md` (AOP-013-SD-001)
- `01_AOP-013_SPECIFICATION.md` (v1.0)
- `04_AGENT_OS_V2_DESIGN.md` (v1.0)
- `02_ARCHITECTURE_IMPACT_ASSESSMENT.md` (AIA-AOP-013 v1.0)
- `05_AUTHORITY_CLASSIFICATION_STANDARD.md` (ACS-001 v1.0)
- `01_GOVERNANCE_REVIEW_PACKAGE.md` (GRP-AOP-013-B v1.0)
- `02_NADF_PILOT_ACTIVATION_PACKAGE.md` (PAP-NADF-AOP-013 v1.0)
- `07_EXECUTION_AUTHORITY_REGISTER.md` (EAR-NADF-001 v1.0)

---

## 2. Checklist — Framework Architecture

### Item FA-01
**Checklist:** The execution authority lifecycle (request → review → grant → execute → close) is architecturally coherent and complete.

**Finding: PASS**

The six-step lifecycle defined in AIA-AOP-013 Section 4 and DESIGN-AGENT-OS-V2 Section 3.1 is coherent. Each step has a clear actor, input, and output. The status model (Created → Pending Review → Under Review → Granted → Active → Executed, with Denied and Revoked branches) is internally consistent. The Execution Authority Register format in EAR-NADF-001 correctly captures all lifecycle states. No orphaned states exist — every terminal status (Executed, Denied, Revoked, Expired) is reachable by a defined path and has a defined meaning.

---

### Item FA-02
**Checklist:** The six authority classes (EA-1 through EA-6) correctly map to the risk profile of actions performed in Odoo 17 Community Edition deployments.

**Finding: PASS WITH OBSERVATION — see G1-OBS-001**

EA-1 through EA-4 and EA-6 are correctly bounded and map cleanly to observable risk distinctions in Odoo 17 Community Edition. The EA-1/EA-2 separation (documentation vs. repository operations) is appropriate. EA-3 (configuration) correctly captures Odoo system parameters and security settings. EA-4 (module installation) correctly separates module-level risk from data-level risk.

EA-5 (Database Mutation Authority) is classified "High" and is correct in principle, but its current scope bundles two meaningfully different risk sub-profiles under a single class. See G1-OBS-001 for the full analysis. This is not a classification error — both action types belong at EA-5 — but it is an architectural observation for v2.1 consideration.

---

### Item FA-03
**Checklist:** The authority classification rules (Rules 1-5 in document 05) are unambiguous and sufficient to classify any plausible D2 action.

**Finding: PASS WITH OBSERVATION — see G1-OBS-002**

Rules 1-5 are unambiguous as written. Rule 1 (round up), Rule 2 (riskiest action governs the request), Rule 3 (no risk-splitting), Rule 4 (EA-6 non-negotiable), and Rule 5 (uncertainty escalates) together form a logically complete and anti-gaming ruleset. The rules interact correctly: Rule 3 closes the obvious circumvention of Rule 2.

One boundary condition is not fully addressed: a D2 action that is EA-3 in a development database but would be EA-6 if the same configuration file governed the production server. The classification rules speak to action type, not environment scope. In the current deployment this is a low-severity gap because all three projects are development/staging environments (ACS-001 Section 3, EA-6 Note). However, when production is in scope, an explicit environment-based override rule will be needed. See G1-OBS-002. This does not block the pilot.

---

### Item FA-04
**Checklist:** The Quick Reference table in document 05 Section 4 correctly classifies all listed action types.

**Finding: PASS**

All 19 entries in the Quick Reference table were verified against the class definitions in ACS-001 Sections 3 and 4. Each entry is correctly classified. Spot-checks: "Change server .conf file" → EA-3 is correct (system configuration, non-production); "Import CSV data (bulk)" → EA-5 is correct (bulk database mutation); "Deploy to production" → EA-6 is correct (any production action is EA-6 by Rule 4). No misclassification found.

---

### Item FA-05
**Checklist:** The v2.0 architecture (document 04 Section 2) is additive-only relative to v1.0. No existing component is removed or replaced during the pilot.

**Finding: PASS**

The v2.0 architecture diagram and the change table in AIA-AOP-013 Section 4 confirm the framework is additive. The agent hierarchy is unchanged (H.Sponsor → A1 → G1/G2/G3 → Project Pod). The human approval gate is not removed during the pilot — it remains in place under advisory mode (Sponsor Condition 3 and PAP-NADF-AOP-013 Section 3). The authority framework runs as a parallel overlay. Roles are extended, not replaced. No escalation policy trigger (E1-E6) is removed or weakened. The append-only register design constraint (DESIGN-AGENT-OS-V2 Section 10, Rule 6) ensures no retroactive alteration of authority decisions.

---

### Item FA-06
**Checklist:** The agent prompt changes identified in document 02 Section 5 are necessary and sufficient. No additional prompt changes are required for the pilot.

**Finding: PASS WITH OBSERVATION — see G1-OBS-003**

The five prompt files identified in AIA-AOP-013 Section 5 as requiring revision (A1, G1, G2, G3, D2) are the correct and complete set. D1, D3, and D4 do not interact directly with authority grants; they are correctly excluded.

However, Sponsor Condition 1 prohibits prompt modifications during Phase B and Phase C. This means the pilot operates without the v2.0 prompt updates being baked in. The question is whether the framework can function in advisory mode without prompt updates.

G1's assessment is that it can, with the following reasoning:

Under advisory mode (PAP-NADF-AOP-013 Section 3), A1 issues authority decisions in parallel with the v1.0 execution flow. D2 does not wait for advisory decisions. The authority issuance protocol (GRANT/DENY formats defined in DESIGN-AGENT-OS-V2 Section 4) is a structured output format that A1 can apply within its existing orchestration role — it is not a fundamentally different behaviour, it is a more formal version of decisions A1 already makes. G1/G2/G3 review checklists (DESIGN-AGENT-OS-V2 Section 6) are self-contained and can be followed without prompt changes. The governance agents are not being asked to do anything structurally different from their current review function; they are being asked to complete a more explicit checklist.

The genuine risk is consistency: without prompt updates, authority decisions depend on A1's and the governance agents' recall of the v2.0 protocol from the enhancement documents, not from their operating prompts. In advisory mode, an inconsistent authority decision produces an accuracy-tracking discrepancy, not a blocked delivery action. This is exactly the kind of information the pilot is designed to surface. See G1-OBS-003 for the recommended mitigation.

---

## 3. Checklist — Advisory Mode Compatibility

### Item AM-01
**Checklist:** The advisory mode (Sponsor Condition 3) is architecturally compatible with the framework. An authority grant issued in advisory mode but not acted upon does not create structural inconsistencies in the register.

**Finding: PASS**

Advisory mode is structurally compatible. An authority grant with Status: Active and Mode: Advisory that is not acted upon (because D2 proceeds under v1.0) is a valid register state. At WP close, A1 updates the Status to Executed with an Outcome field describing the v1.0 execution result. No record is left in a permanently inconsistent state. The register remains append-only and no phantom authority references are created in D2's execution records (D2 is explicitly not required to reference advisory authority IDs per PAP-NADF-AOP-013 Section 3).

---

### Item AM-02
**Checklist:** The Execution Authority Register format (document 07) correctly supports advisory-mode entries (authority granted, execution proceeded independently).

**Finding: PASS WITH OBSERVATION — see G1-OBS-004**

The register format in EAR-NADF-001 Section 2 is structurally sound. It captures all required fields for an advisory-mode entry. The Pilot Activation Package (PAP-NADF-AOP-013 Section 3) defines the Mode field addition (`Mode : Advisory`) for pilot entries.

However, G1 notes that the Mode field is defined in the Pilot Activation Package as an addition to the register format, but the base register template in EAR-NADF-001 Section 8 (Template for New Entries) does not yet include the Mode field. There is a discrepancy between the template definition and the instructed addition. When A1 initialises the live NADF register for WP-03, it must explicitly add the Mode field to each entry. This creates a documentation consistency gap: the template (EAR-NADF-001 Section 8) and the Mode field instruction (PAP-NADF-AOP-013 Section 3) are in separate documents with no cross-reference in the template itself. See G1-OBS-004.

The omission of the Mode field from the base register template is the more substantive concern. A reader of EAR-NADF-001 Section 8 in isolation would not know to add the Mode field. When binding mode is activated post-pilot, a new register initialized from this template alone would not include the Mode field and would therefore be indistinguishable from an advisory-mode register. This should be corrected before the pilot register is initialized.

---

### Item AM-03
**Checklist:** Transitioning from advisory mode to binding mode post-pilot does not require structural changes to the register or the authority lifecycle.

**Finding: PASS**

The Mode field (Advisory | Binding) is the sole distinguishing marker. Changing Mode from Advisory to Binding on future entries is a field value change, not a structural change to the register schema. All other register fields are identical in both modes. The authority lifecycle states are also identical — the only behavioural difference is whether D2 waits for the authority decision before executing (which is enforced through D2's operational instructions, not through register structure). No schema migration is required at advisory-to-binding transition.

---

## 4. Checklist — Pilot Scope Compatibility

### Item PS-01
**Checklist:** The pilot operating on WP-03 and WP-04 (not WP-02 as originally planned) does not require changes to the framework design. The framework is WP-agnostic.

**Finding: PASS**

The framework design contains no WP-02-specific logic. The authority ID naming convention (EA-{PROJECT}-WP{XX}-{NNN}) is parameterized and WP-agnostic. The classification standard, approval matrix, register format, and lifecycle are all defined in terms of action types and risk levels, not in terms of specific work packages. The shift from WP-02 to WP-03/WP-04 as the pilot window is a scope decision that has zero impact on framework architecture.

---

### Item PS-02
**Checklist:** The authority ID naming convention (EA-NADF-WP{XX}-{NNN}) correctly supports WP-03 and WP-04 entries.

**Finding: PASS**

The naming convention is validated for WP-03 and WP-04. Example IDs EA-NADF-WP03-001 and EA-NADF-WP04-001 are syntactically valid and unambiguous. The convention supports the full planned scope (WP-03 and WP-04 each produce independent numbered sequences starting from 001). The {NNN} counter resets per work package, which is consistent with the design principle that authority validity is WP-scoped (SPEC Section 5, Principle P1).

---

## 5. Formal Observations

### G1-OBS-001 — EA-5 Internal Risk Stratification
**Severity:** Observation (non-blocking)
**Relevant checklist item:** FA-02
**Documents referenced:** ACS-001 Section 3 (EA-5), DESIGN-AGENT-OS-V2 Section 3.1

The EA-5 class (Database Mutation Authority) bundles two action sub-types with meaningfully different risk profiles under a single authority class:

- **Sub-type A — Managed data import:** CSV import via the Odoo import interface. This is a user-facing, transactional, Odoo-aware operation. Odoo validates field mappings, enforces model constraints, and applies business logic. A failed row is typically skipped or rolled back at row level. The operator has preview capability before committing. Risk: Medium-High.

- **Sub-type B — Direct Python/SQL record writes:** `env['model'].write(...)` scripts or raw SQL executed against the database. These bypass Odoo's ORM validation, business logic, and audit framework. A malformed script can silently corrupt related records, break computed fields, or invalidate workflow states without triggering any Odoo-level alert. Risk: High-Critical depending on the model affected.

Both sub-types are correctly placed at EA-5 — neither belongs at EA-4 (module installation) or EA-6 (production). The classification is not wrong. However, the preconditions and G3 review depth appropriate for sub-type B are materially greater than those appropriate for sub-type A. The current standard does not differentiate them in its pre-condition list; both receive the same pre-conditions (backup, restore-drill, test database first).

**Recommendation for v2.1 consideration:** Consider formalizing EA-5a (Managed Import) and EA-5b (Direct Mutation) as sub-classes within EA-5, or explicitly note the elevated scrutiny expected for direct Python/SQL writes within the EA-5 definition. This does not affect the pilot — both sub-types are correctly handled at EA-5 and G3 retains discretion to apply higher scrutiny. G1 will apply this distinction in practice during pilot reviews.

---

### G1-OBS-002 — Rules 1-5 Do Not Address Environment-Based Override
**Severity:** Observation (non-blocking; low relevance to pilot; relevant for future production activation)
**Relevant checklist item:** FA-03
**Documents referenced:** ACS-001 Section 2 (Rules 1-5), ACS-001 Section 3 (EA-6 Note)

Classification Rules 1-5 are action-type rules. They do not contain an explicit environment-based override: "if this action targets a production environment, classify as EA-6 regardless of action type." Rule 4 states "EA-6 is non-negotiable" in the context of classification analysis, but it is stated as a meta-rule about the classification floor, not as a positive rule that maps environment = production to EA-6 automatically.

The EA-6 definition itself covers this: "Authority for any action on the production environment" (ACS-001 Section 3, EA-6 Definition). And the Quick Reference table correctly shows all production actions at EA-6. So the operational intent is correct.

The gap is subtle: a future agent reading only the five classification rules without reading the full EA-6 definition might misclassify a "Change server .conf file" action for a production server as EA-3 (it appears in the EA-3 examples for the server .conf file) rather than EA-6. The Quick Reference entry for "Change server .conf file" lists EA-3 without a qualifying note that "production server" → EA-6.

**Recommendation for v1.1 of ACS-001:** Add a Rule 6: "If the target environment of the action is the production environment, classify as EA-6 regardless of the action type." Also add a note to the EA-3 server .conf file example clarifying "development/staging only." This is an editorial improvement to close an ambiguity in the written standard, not a correction to the underlying framework logic.

---

### G1-OBS-003 — Prompt Non-Update Risk in Advisory Mode
**Severity:** Observation (non-blocking; acknowledged in OBS-003 of the Review Package)
**Relevant checklist item:** FA-06
**Documents referenced:** AIA-AOP-013 Section 5, Sponsor Condition 1, PAP-NADF-AOP-013 Section 3

Sponsor Condition 1 prohibits modification of agent prompts during Phase B and Phase C. The five prompts identified in AIA-AOP-013 Section 5 will therefore remain at v1.0 during the entire pilot. This means:

1. A1 issues authority decisions using the v2.0 GRANT/DENY/REVOKE formats defined in the enhancement documents, but these formats are not embedded in A1's operating prompt. A1 is operating from document recall rather than prompt instruction during advisory decisions.

2. G1/G2/G3 complete authority review checklists (DESIGN-AGENT-OS-V2 Section 6) that are not reflected in their operating prompts. The same recall-dependency applies.

3. D2's obligation to reference authority IDs before execution (the core binding-mode discipline) is not in D2's prompt. In advisory mode, D2 is explicitly exempted from this obligation (PAP-NADF-AOP-013 Section 3) — so this is not an issue for the pilot. It becomes critical for binding-mode activation.

G1's assessment is that the advisory mode pilot can proceed on this basis because: (a) the non-binding nature of advisory decisions means a format inconsistency produces a measurement discrepancy, not a blocked delivery; (b) the enhancement documents are available in the session context for all agents; (c) the pilot is specifically designed to detect these kinds of operational gaps.

**Recommended mitigation (A1 action before WP-03):** A1 should include the full GRANT/DENY format block and the G1/G2/G3 review checklists as a session-context injection at the start of each pilot session rather than relying on agents to locate them independently. This is achievable within Sponsor Condition 1 (no prompt modification) because it is a session-level instruction, not a prompt change. This reduces but does not eliminate the recall-dependency risk.

**Binding-mode activation condition (future):** Before advisory mode transitions to binding mode (post-pilot), prompt updates for all five agents must be completed. This should be listed as a mandatory pre-condition in the Phase D activation package, not left as a best-effort.

---

### G1-OBS-004 — Mode Field Absent from Base Register Template
**Severity:** Observation (non-blocking; should be resolved before pilot register is initialized)
**Relevant checklist item:** AM-02
**Documents referenced:** EAR-NADF-001 Section 8, PAP-NADF-AOP-013 Section 3

The Mode field (`Mode : Advisory | Binding`) is defined in the Pilot Activation Package (PAP-NADF-AOP-013 Section 3) as an addition to register entries during the pilot. However, the base register template in EAR-NADF-001 Section 8 ("Template for New Entries") does not include this field.

A1 has been instructed to initialize the pilot EXECUTION_AUTHORITY_REGISTER.md using "the template in enhancements/AOP-013/07_EXECUTION_AUTHORITY_REGISTER.md with the Mode field added" (PAP-NADF-AOP-013 Section 4, Step A). The instruction exists, but it depends on A1 remembering to merge two separate documents at initialization time. If A1 initializes from the template alone, the Mode field will be absent from pilot entries, defeating the purpose of the distinguishing marker.

**Recommended resolution (before pilot register is initialized):** Update EAR-NADF-001 Section 8 (the Template for New Entries block) to include the Mode field between the Validity Scope line and the Conditions line:

```
Validity Scope       : WP-{XX} only
Mode                 : Advisory | Binding
Conditions           : —
```

This is a documentation update to an enhancement package document, not a modification to any Agent OS core document, and does not violate Sponsor Condition 1. A1 should make this update before initializing the pilot register. G1 will note this as a documentation consistency gap — it is the single concrete action G1 recommends before pilot activation begins.

---

## 6. Summary Table

| Checklist Item | Area | Finding | Observation |
|----------------|------|---------|-------------|
| FA-01 Authority lifecycle coherence | Framework Architecture | PASS | — |
| FA-02 EA-1 through EA-6 risk mapping | Framework Architecture | PASS | G1-OBS-001 |
| FA-03 Classification Rules 1-5 sufficiency | Framework Architecture | PASS | G1-OBS-002 |
| FA-04 Quick Reference table accuracy | Framework Architecture | PASS | — |
| FA-05 Additive-only v2.0 architecture | Framework Architecture | PASS | — |
| FA-06 Prompt change necessity and sufficiency | Framework Architecture | PASS | G1-OBS-003 |
| AM-01 Advisory mode register consistency | Advisory Mode | PASS | — |
| AM-02 Register format supports advisory entries | Advisory Mode | PASS | G1-OBS-004 |
| AM-03 Advisory-to-binding transition is structural-change-free | Advisory Mode | PASS | — |
| PS-01 Framework is WP-agnostic | Pilot Scope | PASS | — |
| PS-02 Naming convention supports WP-03/WP-04 | Pilot Scope | PASS | — |

All 11 checklist items: PASS (3 with associated observations, 8 clean).
No FAIL findings. No blocking conditions.

---

## 7. Decision

**APPROVED WITH NOTE**

The AOP-013 Execution Authority Framework is architecturally sound. The six authority classes are correctly defined and bounded. The authority lifecycle is coherent. The framework is additive-only with respect to Agent OS v1.0. Advisory mode is structurally compatible and produces valid register states. The pilot scope change to WP-03/WP-04 has zero architectural impact.

Four non-blocking observations are recorded (G1-OBS-001 through G1-OBS-004). Of these, G1-OBS-004 carries a concrete pre-pilot action: the Mode field should be added to the base register template in EAR-NADF-001 Section 8 before the pilot register is initialized. This is recommended, not required — the pilot can proceed if A1 follows the PAP-NADF-AOP-013 Section 4 instruction to add the Mode field manually at initialization. However, correcting the template is the safer path.

G1-OBS-001 (EA-5 sub-type stratification) and G1-OBS-002 (environment-based classification rule gap) are flagged for v1.1 of the Authority Classification Standard, post-pilot.

G1-OBS-003 (prompt non-update risk) is operational guidance for A1. The advisory mode design correctly contains the risk. The binding-mode activation prompt update requirement must be formalized as a mandatory pre-condition in the Phase D package.

**The framework is approved to proceed to Phase C (NADF Pilot) on the conditions stated in the Sponsor Decision AOP-013-SD-001.**

---

## 8. Sign-Off

```
Decision    : APPROVED WITH NOTE
Date        : 2026-06-25
Reviewer    : G1 Architecture & Odoo Governance
Rationale   : Framework is architecturally sound and advisory-mode compatible.
              All 11 checklist items pass. Four non-blocking observations recorded.
              One pre-pilot documentation action recommended (OBS-004).
Conditions  : None blocking. See Observations for recommended pre-pilot action.
```

---

*G1 Review Report — AOP-013 Execution Authority Framework Phase B*
*G1 Architecture & Odoo Governance*
*Software Factory Governance Authority — 2026-06-25*
