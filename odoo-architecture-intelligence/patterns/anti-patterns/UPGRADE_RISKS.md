# Anti-Pattern — Upgrade Risks

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Decision:** DEC-013

## Sections planned

- Monkey-patching core methods (breaks on upgrade)
- Overriding `_name` on a standard model
- Using private (`_`) methods from core
- Depending on undocumented or internal APIs
- Hardcoded database IDs in data files
- Customising standard view XML IDs without inheritance
- Writing directly to core module files

---

*Populate from official documentation, OCA upgrade guidelines, and project case studies.*
