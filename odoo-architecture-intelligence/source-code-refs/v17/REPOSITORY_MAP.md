# Odoo 17 Source Repository Map

**Status:** REGISTERED — commit pins to be recorded at acquisition time
**Decision:** DEC-013
**Last updated:** 2026-11-25

---

## Community repositories

| Repository | URL | Branch | Purpose |
|------------|-----|--------|---------|
| Odoo Community | `https://github.com/odoo/odoo` | `17.0` | Core framework and standard modules |
| Odoo Community (design-themes) | `https://github.com/odoo/design-themes` | `17.0` | Website themes |

**Pinned commit:** To be recorded at Phase 2 acquisition.

## Enterprise repositories

| Repository | Notes |
|------------|-------|
| `https://github.com/odoo/enterprise` | Requires Odoo Enterprise licence. Not publicly accessible. Source-code references for Enterprise features cannot be independently verified. Mark any Enterprise-derived references as `[ENTERPRISE — cannot independently verify source]`. |

## OCA repositories

| Domain | Repository | Branch |
|--------|-----------|--------|
| Accounting | `https://github.com/OCA/account-financial-tools` | `17.0` |
| Accounting payment | `https://github.com/OCA/account-payment` | `17.0` |
| Inventory | `https://github.com/OCA/stock-logistics-warehouse` | `17.0` |
| Manufacturing | `https://github.com/OCA/manufacture` | `17.0` |
| HR | `https://github.com/OCA/hr` | `17.0` |
| Project | `https://github.com/OCA/project` | `17.0` |

---

## Key file paths — Odoo Community 17

*To be populated during Phase 2 acquisition. Record format:*
*`{relative_path} — {class_or_module} — {brief purpose}`*

| Area | File path | Key class / function | Purpose |
|------|-----------|---------------------|---------|
| ORM base | `odoo/models.py` | `BaseModel` | Root class for all Odoo models |
| ORM API | `odoo/api.py` | `Environment`, `@api.model`, `@api.depends` | Environment and decorator definitions |
| Security | `odoo/models.py` | `BaseModel.check_access_rights()` | ACL enforcement entry point |
| HTTP | `odoo/http.py` | `Controller`, `route()` | HTTP routing and controller base |
| Module loader | `odoo/modules/loading.py` | `load_modules()` | Module loading and dependency resolution |
| Accounting | `addons/account/models/account_move.py` | `AccountMove` | Journal entry model |
| Stock | `addons/stock/models/stock_move.py` | `StockMove` | Inventory movement model |
| Manufacturing | `addons/mrp/models/mrp_production.py` | `MrpProduction` | Manufacturing order model |
| Procurement | `addons/purchase/models/purchase.py` | `PurchaseOrder` | Purchase order model |
| Sales | `addons/sale/models/sale_order.py` | `SaleOrder` | Sales order model |

*All paths are relative to the `odoo/odoo` repository root. Commit SHA to be pinned at Phase 2.*
