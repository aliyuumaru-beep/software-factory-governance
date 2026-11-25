# Anti-Pattern — Common Mistakes in Odoo Development

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Decision:** DEC-013

**AI-GENERATED CONTENT WARNING:** When populated, claims will be labelled with epistemic status.

## Sections planned

- Using `sudo()` in portal-facing code (security risk)
- N+1 query pattern (not using `prefetch_ids`)
- Hardcoding IDs or XML IDs (breaks between databases)
- Triggering recomputation storms with poorly scoped `@api.depends`
- Missing `ondelete` on Many2one fields
- Using `search` inside a loop
- Modifying `_name` on an existing model (breaks the registry)

---

*Populate from project case studies and official documentation during Phase 2 onwards.*
