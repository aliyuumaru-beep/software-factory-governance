# Source-Code References — Stock Movements and Valuation (Odoo 17 Community)

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

## Key files

| File | Purpose |
|------|---------|
| `addons/stock/models/stock_move.py` | Stock move — primary movement record |
| `addons/stock/models/stock_quant.py` | Current stock levels (quants) |
| `addons/stock/models/stock_picking.py` | Transfer / picking (groups moves) |
| `addons/stock/models/stock_location.py` | Location hierarchy |
| `addons/stock_account/models/stock_move.py` | Valuation on move completion |
| `addons/stock_account/models/stock_valuation_layer.py` | Valuation layers (FIFO/AVCO) |

## Key classes

| Class | File | Brief purpose |
|-------|------|---------------|
| `StockMove` | `stock_move.py` | Individual inventory movement |
| `StockQuant` | `stock_quant.py` | Current stock level per location/lot |
| `StockPicking` | `stock_picking.py` | Transfer document grouping moves |
| `StockValuationLayer` | `stock_valuation_layer.py` | Costing layer for AVCO/FIFO |

---

*Populate with method signatures during Phase 2.*
