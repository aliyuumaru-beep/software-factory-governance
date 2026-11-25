# Security QA Checklist

**Status:** REGISTERED — to be expanded from SECURITY_CHECKLIST.md during Phase 2
**Decision:** DEC-013

Use this checklist for any feature that touches access control, record visibility, or external APIs.

## Access rights

- [ ] ACL entries exist for all new models (`ir.model.access.csv`)
- [ ] Minimal required permissions granted (no over-permissioning)
- [ ] Groups are inherited correctly from base groups

## Record rules

- [ ] Multi-company record rules applied where required
- [ ] Portal-visible records scoped by rule (not by ACL alone)
- [ ] Record rules tested with users outside the intended group

## API and portal

- [ ] Portal users cannot access internal-only routes
- [ ] Authentication type (`auth`) set appropriately on all routes
- [ ] No `sudo()` in portal-facing code without documented justification in DECISION_LOG.md

## Data

- [ ] No secrets, credentials, or API keys in source code
- [ ] Sensitive fields not exposed in portal or API responses

---

*Expand from official documentation and security standard during Phase 2.*
