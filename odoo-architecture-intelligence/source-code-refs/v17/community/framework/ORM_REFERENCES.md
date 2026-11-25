# Source-Code References — ORM and Models (Odoo 17 Community)

**Status:** REGISTERED — not yet populated with verified references
**Odoo Version:** 17
**Edition:** Community
**Repository:** `https://github.com/odoo/odoo` branch `17.0`
**Commit pin:** To be recorded at Phase 2 acquisition
**Decision:** DEC-013

---

## Key files

| File | Purpose |
|------|---------|
| `odoo/models.py` | BaseModel — root class for all Odoo models |
| `odoo/api.py` | Environment, decorators (`@api.depends`, `@api.model`, etc.) |
| `odoo/fields.py` | Field type definitions |
| `odoo/osv/expression.py` | Domain expression parsing and normalization |
| `odoo/modules/registry.py` | Model registry |

## Key classes and methods

*To be populated with method signatures and brief descriptions during Phase 2.*

| Class | Method | File | Brief purpose |
|-------|--------|------|---------------|
| `BaseModel` | `_search()` | `odoo/models.py` | ORM search implementation |
| `BaseModel` | `read()` | `odoo/models.py` | Field value reads |
| `BaseModel` | `write()` | `odoo/models.py` | Record update |
| `BaseModel` | `create()` | `odoo/models.py` | Record creation |
| `BaseModel` | `unlink()` | `odoo/models.py` | Record deletion |
| `BaseModel` | `_compute_*` | `odoo/models.py` | Computed field pattern |
| `Environment` | `__getitem__()` | `odoo/api.py` | Model access via env |

---

*Populate this file during Phase 2 with actual method signatures from the pinned commit.*
*Do not add method implementations — record signatures and brief purpose descriptions only.*
