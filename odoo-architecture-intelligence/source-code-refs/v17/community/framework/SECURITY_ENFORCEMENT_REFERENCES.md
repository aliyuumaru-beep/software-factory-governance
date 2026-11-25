# Source-Code References — Security Enforcement (Odoo 17 Community)

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
| `odoo/models.py` | ACL enforcement in `check_access_rights()`, `check_access_rule()` |
| `odoo/addons/base/models/res_groups.py` | Group model |
| `odoo/addons/base/models/ir_rule.py` | Record rule evaluation |
| `odoo/addons/base/models/ir_model_access.py` | ACL table |
| `odoo/http.py` | Session and authentication |

## Key enforcement points

*To be populated with method signatures during Phase 2.*

| Class | Method | File | Brief purpose |
|-------|--------|------|---------------|
| `BaseModel` | `check_access_rights()` | `odoo/models.py` | Checks group-based ACL |
| `BaseModel` | `check_access_rule()` | `odoo/models.py` | Evaluates record rules |
| `IrRule` | `_compute_domain()` | `ir_rule.py` | Record rule domain computation |
| `Http` | `_authenticate()` | `odoo/http.py` | Session authentication |

---

*Populate this file during Phase 2 with actual method signatures from the pinned commit.*
