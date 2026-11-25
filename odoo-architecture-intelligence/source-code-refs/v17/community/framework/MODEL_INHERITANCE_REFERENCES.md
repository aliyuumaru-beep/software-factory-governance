# Source-Code References — Model Inheritance (Odoo 17 Community)

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

## Inheritance types in Odoo

| Type | `_inherit` / `_name` pattern | Effect |
|------|------------------------------|--------|
| Classical (extension) | `_inherit = 'existing.model'`; no `_name` | Extends existing model in-place |
| Prototype (copy) | `_inherit = 'existing.model'`; `_name = 'new.model'` | Creates new model from existing |
| Delegation | `_inherits = {'parent.model': 'field_id'}` | Column delegation via FK |

## Key files

| File | Purpose |
|------|---------|
| `odoo/models.py` | `MetaModel.__new__()` — class building; `ModelBase._setup_base()` — inheritance resolution |
| `odoo/modules/registry.py` | Stores model classes per database |

---

*Populate with method signatures during Phase 2.*
