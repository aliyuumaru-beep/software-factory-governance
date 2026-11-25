# Solution Assessment Framework

**Status:** DEFINED
**Decision:** DEC-013
**Aligns with:** Architectural Principle 1 (Platform-Native First), `Autonomous-agent-Team/platform-profiles/23_PLATFORM_PROFILE_ODOO17_COMMUNITY.md`

---

## Purpose

This framework defines the standard method for assessing how a business requirement should be met in Odoo. It operationalises the platform-native-first principle and ensures that custom development is chosen only when native and OCA options have been genuinely evaluated.

---

## Assessment sequence

Every assessment must follow this sequence. Do not skip a tier without documented evidence of evaluation.

### Tier 1 — Native Odoo (configuration-first)

**Question:** Can this requirement be met entirely through Odoo configuration, without installing any additional module?

Evidence required:
- Confirm the relevant Odoo module(s) are available in Community edition.
- Identify the specific feature or setting.
- Cite SOURCE_REGISTER entry (`SRC-xxx`) for the evidence.
- If rejecting native: state exactly what the native solution cannot do, with citation.

**Decision rule:** If Tier 1 fully meets the requirement, stop here. Log the assessment. Do not proceed to Tier 2 or 3.

### Tier 2 — OCA module

**Question:** Does an OCA module with an active `17.0` branch exist that meets this requirement without custom code?

Evidence required:
- Identify the specific OCA module.
- Check maintenance activity (last commit, open issues, CI status).
- Check licence compatibility (must be LGPL-3 or compatible).
- Check dependencies — no undeclared Enterprise module dependencies.
- Identify any known limitations or security implications.
- Cite the `oca/v17/{domain}/{module_name}.md` assessment if available.

**Decision rule:** If a suitable OCA module exists and the evidence supports adoption, stop here. Log the decision in the project's DECISION_LOG.md with type `TECHNOLOGY`. Do not proceed to Tier 3.

### Tier 3 — Software Factory reusable module

**Question:** Does an existing Software Factory module already built for another pod meet this requirement?

Evidence required:
- Check the MODULE_REGISTRY.md of all relevant pods.
- Confirm the module is in a stable state (not deprecated or experimental).
- Confirm it is reusable without modification or with minimal extension.

**Decision rule:** If a reusable SF module exists, prefer it over new custom development.

### Tier 4 — Custom module

**Question:** Has no suitable native, OCA, or reusable SF solution been found?

Evidence required:
- Document why each prior tier was rejected, with evidence.
- Assess the upgrade risk of the proposed custom solution.
- Confirm the custom approach is the least complex solution that meets the requirement.
- Log the decision in `DECISION_LOG.md` with type `CUSTOM_CODE`.

**Decision rule:** Custom development is the last resort, not the default.

---

## Assessment record format

Each assessment file in `by-domain/{domain}/` must include:

```
<!--
oais:type: solution-assessment
oais:requirement: [one-line requirement description]
oais:odoo-version: 17
oais:edition: Community
oais:domain: [domain]
oais:tier-evaluated: [1 | 1-2 | 1-3 | 1-4]
oais:recommendation: [NATIVE | OCA | SF_REUSABLE | CUSTOM]
oais:evidence: [SRC-xxx list]
oais:decision-ref: [DEC-xxx if logged]
oais:date: [ISO date]
-->
```

---

## Relationship to governance

A Custom (Tier 4) recommendation requires a `CUSTOM_CODE` entry in the project's `DECISION_LOG.md`. The assessment file is the evidence supporting that decision.
