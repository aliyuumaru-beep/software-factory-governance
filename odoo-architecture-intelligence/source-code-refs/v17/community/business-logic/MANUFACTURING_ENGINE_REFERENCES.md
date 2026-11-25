# Source-Code References — Manufacturing Engine (Odoo 17 Community)

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

## Key files

| File | Purpose |
|------|---------|
| `addons/mrp/models/mrp_production.py` | Manufacturing order |
| `addons/mrp/models/mrp_bom.py` | Bill of materials |
| `addons/mrp/models/mrp_workcenter.py` | Workcenter definition |
| `addons/mrp/models/mrp_workorder.py` | Work order (operation on a workcenter) |
| `addons/mrp_account/models/mrp_production.py` | Costing for manufacturing |

## Key classes

| Class | File | Brief purpose |
|-------|------|---------------|
| `MrpProduction` | `mrp_production.py` | Manufacturing order document |
| `MrpBom` | `mrp_bom.py` | Bill of materials definition |
| `MrpWorkcenter` | `mrp_workcenter.py` | Workcenter (machine or labour resource) |
| `MrpWorkorder` | `mrp_workorder.py` | Individual operation on a workcenter |

---

*Populate with method signatures during Phase 2.*
