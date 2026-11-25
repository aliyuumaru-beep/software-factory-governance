# Odoo 17 — Cross-Module Integration

**Status:** REGISTERED — content not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

**AI-GENERATED CONTENT WARNING:** Claims from AI training data only will be labelled `[UNVERIFIED — AI training data only]`.

## Purpose

This file documents how Odoo modules interact with each other — the integration points, shared models, and data flows that cross module boundaries. Understanding these is essential for architecture decisions that span multiple domains.

## Sections planned

- Sales → Inventory integration (SO confirmation triggers stock moves)
- Sales → Accounting integration (invoice creation from SO)
- Purchase → Inventory integration (PO receipt triggers incoming moves)
- Purchase → Accounting integration (vendor bill from PO)
- Manufacturing → Inventory integration (component consumption, finished product receipt)
- Manufacturing → Accounting integration (production costing)
- Intercompany transactions
- Multi-company data isolation
- Shared models: `res.partner`, `res.currency`, `uom.uom`, `product.product`
- Analytic accounting integration points

---

*Populate during Phase 2 from official documentation and source-code references.*
*This is a high-priority file for architecture decisions that span multiple domains.*
