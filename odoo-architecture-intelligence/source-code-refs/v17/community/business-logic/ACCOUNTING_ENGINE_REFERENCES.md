# Source-Code References — Accounting Engine (Odoo 17 Community)

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

## Key files

| File | Purpose |
|------|---------|
| `addons/account/models/account_move.py` | Journal entry (`account.move`) and line (`account.move.line`) |
| `addons/account/models/account_journal.py` | Journal configuration |
| `addons/account/models/account_account.py` | Chart of accounts |
| `addons/account/models/account_tax.py` | Tax computation |
| `addons/account/models/account_payment.py` | Payment registration |
| `addons/account/models/account_reconcile_model.py` | Reconciliation rules |

## Key classes

| Class | File | Brief purpose |
|-------|------|---------------|
| `AccountMove` | `account_move.py` | Journal entry — the central accounting document |
| `AccountMoveLine` | `account_move.py` | Individual debit/credit line |
| `AccountTax` | `account_tax.py` | Tax definition and computation |
| `AccountPayment` | `account_payment.py` | Customer/vendor payment |

---

*Populate with method signatures during Phase 2.*
