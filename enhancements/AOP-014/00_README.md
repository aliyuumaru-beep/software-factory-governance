# AOP-014 — Development Environment Trust Profile
## Enhancement Package Index

---

**Enhancement ID:** AOP-014
**Target Scope:** All Software Factory Project Pods (NADF, FamOil, WamaCare)
**Status:** DEPLOYED — NADF ONLY (DEC-AOP014-001, 2026-06-26)
**Date:** 2026-06-25
**Deployed:** 2026-06-26
**Prepared By:** A1 Master Orchestrator
**Relationship to AOP-013:** Independent enhancement stream. AOP-013 governs what D2 is
                             authorised to execute. AOP-014 governs the approval prompt
                             behaviour of the development toolchain (Claude Code) during
                             that execution. They are complementary, not overlapping.

---

## Purpose

Reduce runtime approval interruptions for routine Software Factory development activities while
preserving protection for destructive, production-impacting, or security-sensitive actions.

This enhancement defines a recommended trust profile — a three-level command classification
with whitelist, blacklist, and "Yes, and don't ask again" guidance — for the Claude Code
development environment across all three active Software Factory pods.

**This enhancement does NOT:**
- Modify governance authority (AOP-013 is unchanged)
- Change what actions are permitted under the Execution Authority Framework
- Remove approval gates for destructive or security-sensitive commands
- Modify any repository or local machine settings (design only)

---

## Deliverable Index

| # | Document | Description |
|---|----------|-------------|
| 01 | [Development Trust Profile](01_DEVELOPMENT_TRUST_PROFILE.md) | Master document: principles, classification model, pod-specific rules |
| 02 | [Command Classification Matrix](02_COMMAND_CLASSIFICATION_MATRIX.md) | Complete Level A / B / C matrix across all command categories |
| 03 | [Whitelist Recommendation](03_WHITELIST_RECOMMENDATION.md) | Level A commands recommended for "don't ask again" configuration |
| 04 | [Blacklist Recommendation](04_BLACKLIST_RECOMMENDATION.md) | Level C commands that must never be pre-approved |
| 05 | [Risk Assessment](05_RISK_ASSESSMENT.md) | Risk analysis for the trust profile itself |
| 06 | [Adoption Guidance](06_ADOPTION_GUIDANCE.md) | How to apply this profile in Claude Code for NADF, FamOil, WamaCare |
| 07 | [Deployment Record — NADF](07_DEPLOYMENT_RECORD_NADF.md) | Deployed configuration, condition compliance, change management |

---

## Sponsor Decision — DEC-AOP014-001

**Decision:** ADOPT — NADF ONLY
**Date:** 2026-06-26
**Governance Log:** DEC-017 (software-factory-governance/DECISION_LOG.md)

**Deployed artifacts:**
- `/Users/mac/nadf_erp/.claude/settings.json` — 63 Level A allow patterns
- `/Users/mac/nadf_erp/docs/governance/AOP014_METRICS_LOG.md` — metrics tracking

**Pending:**
- FamOil adoption: awaiting NADF operational review + separate Sponsor decision
- WamaCare adoption: awaiting NADF operational review + separate Sponsor decision

---

## Sponsor Decision Options (Original)

After reviewing this package:

| Option | Description |
|--------|-------------|
| **ADOPT** | Apply the full trust profile across all three pods |
| **ADOPT — NADF ONLY** | Apply to NADF pod first; extend to others after validation |
| **ADOPT WITH MODIFICATIONS** | Apply with specific command additions or removals |
| **DEFER** | Hold until AOP-013 pilot completes |
| **REJECT** | Retain current per-command approval behaviour |

---

*AOP-014 Enhancement Package — Software Factory Governance Authority — 2026-06-25*
