# Source-Code References — Automated Actions and Scheduled Jobs (Odoo 17 Community)

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

## Key files

| File | Purpose |
|------|---------|
| `odoo/addons/base/models/ir_actions.py` | Server actions and automated action model |
| `odoo/addons/base/models/ir_cron.py` | Scheduled actions (cron) |

## Key classes

| Class | File | Brief purpose |
|-------|------|---------------|
| `IrActionsServer` | `ir_actions.py` | Server action — Python code, write, create, etc. |
| `IrCron` | `ir_cron.py` | Scheduled action — time-triggered server action |

---

*Populate with method signatures during Phase 2.*
