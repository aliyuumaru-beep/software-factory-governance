# Odoo 17 — Security Checklist

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

This checklist is for use before delivering any Software Factory project feature that touches access control, data visibility, or external APIs.

## Pre-delivery checklist (placeholder)

*To be populated from official documentation and Software Factory security standard during Phase 2.*

- [ ] All new models have ACL entries (`ir.model.access.csv`)
- [ ] Record rules are defined for multi-company models where required
- [ ] Portal-visible records are explicitly scoped by record rule
- [ ] No `sudo()` used in portal-facing code without documented justification
- [ ] API endpoints have appropriate `auth` type
- [ ] No secrets in source code
- [ ] Security decision logged in DECISION_LOG.md

---

*Expand and verify this checklist against official Odoo security documentation during Phase 2.*
