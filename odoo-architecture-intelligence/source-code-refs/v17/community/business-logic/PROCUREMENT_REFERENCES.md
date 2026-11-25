# Source-Code References — Procurement and Replenishment (Odoo 17 Community)

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

## Key files

| File | Purpose |
|------|---------|
| `addons/purchase/models/purchase.py` | Purchase order and line |
| `addons/purchase/models/res_partner.py` | Vendor-specific fields |
| `addons/stock/models/stock_rule.py` | Procurement rules (make-to-order, reorder) |
| `addons/stock/models/stock_warehouse.py` | Route and warehouse configuration |
| `addons/purchase_stock/models/stock_rule.py` | Purchase rule integration with stock |

## Key classes

| Class | File | Brief purpose |
|-------|------|---------------|
| `PurchaseOrder` | `purchase.py` | Purchase order document |
| `StockRule` | `stock_rule.py` | Procurement rule (triggers moves or POs) |
| `StockWarehouse` | `stock_warehouse.py` | Routes and push/pull rules |

---

*Populate with method signatures during Phase 2.*
