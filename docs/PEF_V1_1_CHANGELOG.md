# PEF v1.1 — Change Log

**Framework:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md (SF-GOV-025)  
**Upgrade:** v1.0 → v1.1  
**Date:** 2026-06-21  
**Nature of change:** Incremental enhancement. The v1.0 eight-stage lifecycle (PEG-1–PEG-8), four-gate architecture, Coverage Validation standard, scoring model, Product Memory System, and the six original templates are **preserved unchanged**. No v1.0 content was removed or rewritten.

---

## 1. Validation Basis

This upgrade implements the **P1 (immediate) enhancements** identified in:

> **PEF Framework Validation Review Report — SF-VAL-PEF-001** (`docs/PEF_FRAMEWORK_VALIDATION_REPORT.md`), dated 2026-06-21.

The validation report assessed v1.0 at an overall readiness score of **84.45 / 100** and gave a verdict of **✅ APPROVED WITH ENHANCEMENTS**. Part 11 of the report defines five "immediate actions before first non-NADF engagement". Those five — and only those five — are implemented here. The report's P2, P3, and P4 enhancements are explicitly deferred (see Sections 4 and 5 below).

---

## 2. Changes Made

### New templates (3)

| Template | Template ID | Purpose | Validation ref |
|----------|-------------|---------|----------------|
| `templates/PEF_DISCOVERY_REPORT_TEMPLATE.md` | PEF-TPL-007 | Standard structure for the mandatory Discovery Report (Section 9.2) | WEK-03 / ENH-03 |
| `templates/PEF_CAPABILITY_MAP_TEMPLATE.md` | PEF-TPL-008 | Required structure for the D-03 Capability Map — the PEG-2 master product structure | WEK-02 / ENH-04 |
| `templates/PEF_SCOPE_CHANGE_REQUEST_TEMPLATE.md` | PEF-TPL-009 | Post-Gate 3 scope change control instrument | OMI-05 / ENH-02 |

### Framework updates (`docs/25_PRODUCT_ENGINEERING_FRAMEWORK.md`)

| Change | Location | Validation ref |
|--------|----------|----------------|
| Version bumped to 1.1; Document Control updated (Supersedes, Validation basis, Change record) | Header / Document Control | — |
| Product Owner Refusal Escalation Procedure added (records, classification, remediation, E-1/E-2/E-3 escalation chain, gate-hold state, resolution) for Gate 1, Gate 3, Gate 4 | New Section 3.2 | WEK-04 / ENH-06 |
| D-03 Capability Map now references `PEF_CAPABILITY_MAP_TEMPLATE.md` (was "None — structured table") | Section 5 deliverables table | WEK-02 / ENH-04 |
| Discovery Report added as mandatory deliverable D-21, referencing `PEF_DISCOVERY_REPORT_TEMPLATE.md` | Section 5 (D-21) | WEK-03 / ENH-03 |
| PEF Template Library subsection listing all nine templates | New Section 5.1 | ENH-03/04 |
| Section 9.2 now names the Discovery Report template and its Conflicts Register | Section 9.2 | WEK-03 |
| Defect Severity Classification (Critical/High/Medium/Low) with objective criteria and rules DSR-01–06 | New Section 11.4 | OMI-04 / ENH-01 |
| Scope Change Control Procedure (post-Gate 3): six steps, approval-authority matrix, Coverage re-validation trigger, rules SCC-01/02 | New Section 12.3 | OMI-05 / ENH-02 |
| Footer version line updated to v1.1 with changelog pointer | Document footer | — |

---

## 3. P1 Enhancements Implemented

The five immediate actions from validation report Part 11 are complete:

1. ✅ **`PEF_DISCOVERY_REPORT_TEMPLATE.md`** added to the template library (ENH-03).
2. ✅ **`PEF_CAPABILITY_MAP_TEMPLATE.md`** added to the template library and wired to D-03 (ENH-04).
3. ✅ **`PEF_SCOPE_CHANGE_REQUEST_TEMPLATE.md`** added **and** Scope Change Control Procedure added to Section 12 (Section 12.3) (ENH-02 / OMI-05).
4. ✅ **Defect severity levels** defined in Section 11 (Section 11.4) (ENH-01 / OMI-04).
5. ✅ **Product Owner refusal escalation procedure** added to Section 3 (Section 3.2) (ENH-06 / WEK-04).

---

## 4. Deferred to v1.2 (P2 enhancements)

These were **not** implemented in v1.1 and remain open:

| ID | Enhancement | Validation ref |
|----|------------|----------------|
| ENH-04 (partial) | Template for D-06 Custom Module Register as a standalone document (v1.1 captures it as a section within the Capability Map template; a dedicated `PEF_CUSTOM_MODULE_REGISTER_TEMPLATE.md` remains deferred) | Part 8 |
| ENH-05 | Partial TO-BE delivery protocol (PEG-1 / PEG-7) | OMI-02 |
| ENH-07 | Autonomous Agent vs Human Team governance differences | OMI-06 |
| ENH-08 | Data Migration Governance section | WEK-09 |
| ENH-09 | Hypercare Governance (PEG-7 exit / pre-PEG-8) | WEK-10 |
| ENH-10 | Registry lookup as a mandatory PEG-2 activity with deliverable | OMI-03 |
| — | `PEF_DEFECT_REGISTER_TEMPLATE.md`, `PEF_OPEN_ITEMS_LOG_TEMPLATE.md`, `PEF_DATA_MIGRATION_PLAN_TEMPLATE.md` | Part 8 |

---

## 5. Deferred to v2.0 (P3 / P4 enhancements)

| ID | Enhancement | Validation ref |
|----|------------|----------------|
| ENH-11 | Engagement size classification and scaling matrix | WEK-07 / OMI-07 |
| ENH-12 | AI Solution supplementary annex (model governance, bias, data lineage, inference) | WEK-08 |
| ENH-13 | Regulatory compliance gate content for government projects | OMI-08 |
| ENH-14 | Framework amendment procedure | OMI-01 |
| ENH-15 | Clarify CHANGELOG.md root location in Sections 8.3 / 9.3 | WEK-01 |
| ENH-16 | Programme suspension / reset procedure | WEK-05 |
| ENH-17 | Registry versioning and concurrent access governance | OMI-10 |
| ENH-18 | Create SF-GOV-010 and SF-GOV-015 (referenced but non-existent standards) | WEK-06 |
| — | SaaS / multi-tenant guidance; mobile-specific guidance | Part 6 |

**Restriction carried forward from v1.0 validation:** the framework must **not** be applied to AI solutions, SaaS products, or heavily regulated-industry projects until the relevant annexes (ENH-12, ENH-13) are produced.

---

## 6. Backward Compatibility

- All existing deliverable IDs (D-01 – D-20), gate numbers, PEG stage numbers, CVR rules, ER rules, and template IDs (PEF-TPL-001 – 006) are unchanged.
- New identifiers introduced: deliverable **D-21**; template IDs **PEF-TPL-007/008/009**; sections **3.2, 5.1, 11.4, 12.3**; rule sets **DSR-01–06** and **SCC-01/02**.
- Engagements already in flight under v1.0 may adopt v1.1 immediately; the new Discovery Report (D-21) applies at the next PEG-7 entry, and the Scope Change Control Procedure applies to any SCR raised after adoption.

---

*PEF v1.1 Change Log — Software Factory governance standard*  
*Implements P1 enhancements from SF-VAL-PEF-001. Next action: framework ready for first non-NADF engagement.*
