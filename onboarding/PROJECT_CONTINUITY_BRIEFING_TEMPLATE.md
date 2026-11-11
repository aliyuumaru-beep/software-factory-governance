# Project Continuity Briefing

**Project:** _______________
**Briefing Date:** YYYY-MM-DD
**Prepared By:** _______________
**Briefing Recipient:** _______________
**Reason for Briefing:** <!-- Phase handover | Team change | AI session restart | Client handover | Emergency -->

---

## 1. Project Identity

**Project Name:** _______________
**Client / Stakeholder:** _______________
**Industry Vertical:** _______________
**Platform:** Odoo [version] / [other]
**Repository:** _______________
**Environment URLs:**
- Production: _______________
- Staging: _______________
- Development: _______________

---

## 2. Current State Summary

**Current Phase:** Phase [N] — [Phase Name]
**Phase Status:** [In Progress / Complete / Blocked]
**Overall Project Health:** [Green / Amber / Red]
**Last Major Delivery:** [Description] — [Date]

### What Has Been Built (Summary)
<!-- Two to five sentences describing the current working system.
     What can users do today? What modules are live? -->

### What Is In Progress
<!-- What is being actively worked on right now? -->

### What Is Next
<!-- What is the next significant deliverable? -->

---

## 3. Governance Approval Register

*Reference: `docs/governance/GOVERNANCE_APPROVAL_REGISTER.md` (AOP-015 mandatory artifact)*

The Governance Approval Register is the single executive view of all governance decisions,
exceptions, escalations, and authority decisions for this product. Read it before taking
any implementation action in this session.

| Register Field | Current Value |
|---------------|---------------|
| Document ID | [GAR-PRODUCT-NNN] |
| Total Decisions | [N] |
| Active | [N] |
| Open Escalations | [N] — [summary of blocking items] |
| Last Updated | [YYYY-MM-DD] |

Key items for this handover:
- **Open Escalations:** [List the ESC-XXX items blocking current work]
- **Deferred Decisions:** [List major deferred architectural items]
- **Active exceptions:** [Any accepted limitations in effect]

---

## 4. Critical Decisions in Effect

*These decisions from `DECISION_LOG.md` are currently active and must not be reversed without a new logged decision. The full department-grouped view is in the Governance Approval Register (§3 above).*

| ID | Decision | Why It Matters |
|----|----------|----------------|
| DEC-NNN | [Title] | [Why reversing it would be harmful] |

---

## 5. Known Issues and Risks

| Issue | Severity | Status | Owner |
|-------|----------|--------|-------|
|       | High / Medium / Low | Open / In Progress / Deferred | |

---

## 6. Active Custom Modules

*From `MODULE_REGISTRY.md` — active modules that the incoming team must be aware of:*

| ID | Module | Purpose | Known Issues |
|----|--------|---------|--------------|
| MOD-NNN | [name] | [purpose] | |

---

## 7. Infrastructure and Access

### Server / Hosting
- Provider: _______________
- Location: _______________
- Access method: _______________

### Database
- Name: _______________
- Host: _______________
- Access: [How to access — do not include passwords here]

### Backup
- Last backup: _______________
- Backup location: _______________
- Last verified restore: _______________

### Secrets and Credentials
- Location of secrets: [Secret management system — do not include actual credentials here]
- Who has access: _______________

---

## 8. Immediate Priorities

*What the incoming team / agent should focus on first:*

1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

---

## 9. What to Avoid

*Areas of the system that require extra care or should not be touched without consultation:*

- [Area / module / system]: [Reason for caution]

---

## 10. Key Contacts

| Role | Name | Contact |
|------|------|---------|
| Software Factory Lead | | |
| Client Contact | | |
| Server / Infrastructure | | |
| [Other] | | |

---

## 11. Open Questions

*Questions that remain unresolved and require attention from the incoming team:*

1. [Question]

---

## Handover Confirmation

The incoming team/agent confirms they have received and read this briefing:

**Received by:** _______________
**Date:** YYYY-MM-DD
**Confirmed:** [ ] Yes, I have read and understood this briefing.

*Record this handover in `IMPLEMENTATION_HISTORY.md` with type `ONBOARDING`.*
