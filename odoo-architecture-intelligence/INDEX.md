# OAIS — Master Index

**Status:** STUB — table structure defined; file paths will be populated as content is added.
**Decision:** DEC-013
**Last updated:** 2026-11-25

Read this file first. Identify the domain and version, then follow the path to the relevant file.

---

## How to read this index

Each row maps a topic to its file location within `odoo-architecture-intelligence/`.
The Status column shows whether content has been acquired:

| Status | Meaning |
|--------|---------|
| `REGISTERED` | File exists; content not yet acquired |
| `RETRIEVED` | Official source obtained and filed |
| `SOURCE_VERIFIED` | Content verified against official source or source code |
| `LAB_VERIFIED` | Behaviour verified in isolated environment |
| `INDEPENDENTLY_REVIEWED` | Reviewed by independent technical reviewer |

---

## Domain 1 — ORM and Model Architecture

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| ORM overview and query API | `intelligence/v17/architecture/ORM_AND_MODELS.md` | REGISTERED | — | — |
| Model inheritance (classical, delegation, prototype) | `intelligence/v17/architecture/ORM_AND_MODELS.md` | REGISTERED | — | — |
| Computed and related fields | `intelligence/v17/architecture/ORM_AND_MODELS.md` | REGISTERED | — | — |
| Onchange and constraints | `intelligence/v17/architecture/ORM_AND_MODELS.md` | REGISTERED | — | — |
| Source-code reference | `source-code-refs/v17/framework/ORM_REFERENCES.md` | REGISTERED | — | — |
| Official documentation | `official-docs/v17/README.md` | REGISTERED | — | — |

## Domain 2 — Security and Access Rights

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Access rights model (groups, ACL) | `security/ACCESS_RIGHTS_MODEL.md` | REGISTERED | — | — |
| Record rules | `security/RECORD_RULES.md` | REGISTERED | — | — |
| Portal and API security | `security/PORTAL_AND_API_SECURITY.md` | REGISTERED | — | — |
| Security enforcement in source | `source-code-refs/v17/framework/SECURITY_ENFORCEMENT_REFERENCES.md` | REGISTERED | — | — |
| Security checklist | `security/SECURITY_CHECKLIST.md` | REGISTERED | — | — |

## Domain 3 — Views and Web Client

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| View types and structure | `intelligence/v17/architecture/VIEWS_AND_UI.md` | REGISTERED | — | — |
| QWeb templates | `intelligence/v17/architecture/VIEWS_AND_UI.md` | REGISTERED | — | — |
| OWL components (v17+) | `intelligence/v17/architecture/VIEWS_AND_UI.md` | REGISTERED | — | — |
| Web client source reference | `source-code-refs/v17/business-logic/WEB_CLIENT_REFERENCES.md` | REGISTERED | — | — |

## Domain 4 — Controllers and HTTP

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| HTTP controllers and routes | `intelligence/v17/architecture/CONTROLLERS_AND_HTTP.md` | REGISTERED | — | — |
| JSON-RPC and REST patterns | `intelligence/v17/architecture/CONTROLLERS_AND_HTTP.md` | REGISTERED | — | — |
| Source-code reference | `source-code-refs/v17/business-logic/WEB_CLIENT_REFERENCES.md` | REGISTERED | — | — |

## Domain 5 — Business Workflows

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Automated actions | `intelligence/v17/architecture/WORKFLOW_AND_AUTOMATION.md` | REGISTERED | — | — |
| Scheduled actions (cron) | `intelligence/v17/architecture/WORKFLOW_AND_AUTOMATION.md` | REGISTERED | — | — |
| Server actions | `intelligence/v17/architecture/WORKFLOW_AND_AUTOMATION.md` | REGISTERED | — | — |
| Source-code reference | `source-code-refs/v17/business-logic/AUTOMATION_SCHEDULED_JOBS_REFERENCES.md` | REGISTERED | — | — |

## Domain 6 — Accounting

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Chart of accounts and journal entries | `intelligence/v17/functional/ACCOUNTING.md` | REGISTERED | — | — |
| Tax engine | `intelligence/v17/functional/ACCOUNTING.md` | REGISTERED | — | — |
| Reconciliation | `intelligence/v17/functional/ACCOUNTING.md` | REGISTERED | — | — |
| Multi-currency | `intelligence/v17/functional/ACCOUNTING.md` | REGISTERED | — | — |
| Community vs Enterprise differences | `intelligence/v17/functional/ACCOUNTING.md` | REGISTERED | — | — |
| Accounting engine source reference | `source-code-refs/v17/business-logic/ACCOUNTING_ENGINE_REFERENCES.md` | REGISTERED | — | — |

## Domain 7 — Inventory

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Stock movements and quants | `intelligence/v17/functional/INVENTORY.md` | REGISTERED | — | — |
| Valuation methods (FIFO, AVCO, standard) | `intelligence/v17/functional/INVENTORY.md` | REGISTERED | — | — |
| Lot and serial number tracking | `intelligence/v17/functional/INVENTORY.md` | REGISTERED | — | — |
| Multi-warehouse and routes | `intelligence/v17/functional/INVENTORY.md` | REGISTERED | — | — |
| Stock source reference | `source-code-refs/v17/business-logic/STOCK_MOVEMENTS_REFERENCES.md` | REGISTERED | — | — |

## Domain 8 — Manufacturing

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Bill of materials and routing | `intelligence/v17/functional/MANUFACTURING.md` | REGISTERED | — | — |
| Work orders and workcenter | `intelligence/v17/functional/MANUFACTURING.md` | REGISTERED | — | — |
| By-products and scrap | `intelligence/v17/functional/MANUFACTURING.md` | REGISTERED | — | — |
| Manufacturing engine source reference | `source-code-refs/v17/business-logic/MANUFACTURING_ENGINE_REFERENCES.md` | REGISTERED | — | — |

## Domain 9 — Procurement

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Purchase orders and approval | `intelligence/v17/functional/PROCUREMENT.md` | REGISTERED | — | — |
| Replenishment rules (make-to-order, reorder) | `intelligence/v17/functional/PROCUREMENT.md` | REGISTERED | — | — |
| Vendor management | `intelligence/v17/functional/PROCUREMENT.md` | REGISTERED | — | — |
| Procurement source reference | `source-code-refs/v17/business-logic/PROCUREMENT_REFERENCES.md` | REGISTERED | — | — |

## Domain 10 — Sales

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Sales order lifecycle | `intelligence/v17/functional/SALES.md` | REGISTERED | — | — |
| Pricelist and discount | `intelligence/v17/functional/SALES.md` | REGISTERED | — | — |
| Sales–purchase–inventory integration | `intelligence/v17/functional/CROSS_MODULE_INTEGRATION.md` | REGISTERED | — | — |
| Sales and purchase source reference | `source-code-refs/v17/business-logic/SALES_PURCHASE_REFERENCES.md` | REGISTERED | — | — |

## Domain 11 — Website and Portal

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Portal access and visibility | `intelligence/v17/architecture/WEBSITE_AND_PORTAL.md` | REGISTERED | — | — |
| Website builder | `intelligence/v17/architecture/WEBSITE_AND_PORTAL.md` | REGISTERED | — | — |
| eCommerce (Enterprise) | `intelligence/v17/architecture/WEBSITE_AND_PORTAL.md` | REGISTERED | — | — |

## Domain 12 — Testing

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Unit testing framework | `testing-and-qa/UNIT_TESTING.md` | REGISTERED | — | — |
| Tour testing | `testing-and-qa/TOUR_TESTING.md` | REGISTERED | — | — |
| Performance testing | `testing-and-qa/PERFORMANCE_TESTING.md` | REGISTERED | — | — |

## Domain 13 — Performance

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| ORM performance patterns | `intelligence/v17/architecture/ORM_AND_MODELS.md` | REGISTERED | — | — |
| Caching and prefetch | `intelligence/v17/architecture/ORM_AND_MODELS.md` | REGISTERED | — | — |
| Database indexing guidance | `intelligence/v17/architecture/ORM_AND_MODELS.md` | REGISTERED | — | — |

## Domain 14 — Deployment

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Docker and docker-compose | `official-docs/v17/README.md` | REGISTERED | — | — |
| Nginx and reverse proxy | `official-docs/v17/README.md` | REGISTERED | — | — |
| Configuration parameters | `official-docs/v17/README.md` | REGISTERED | — | — |

## Domain 15 — Upgrades

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| v16 → v17 migration | `official-docs/v17/upgrades/V16_TO_V17_MIGRATION.md` | REGISTERED | — | — |
| v17 → v18 migration | `odoo/cross-version/VERSION_COMPATIBILITY_MATRIX.md` | REGISTERED | — | — |
| Deprecated APIs and features | `odoo/cross-version/DEPRECATION_TRACKER.md` | REGISTERED | — | — |

## Domain 16 — Cross-Module Integration

| Sub-topic | File | Odoo v17 | Odoo v18 | Odoo v19 |
|-----------|------|----------|----------|----------|
| Sales–inventory–manufacturing flow | `intelligence/v17/functional/CROSS_MODULE_INTEGRATION.md` | REGISTERED | — | — |
| Accounting integration points | `intelligence/v17/functional/CROSS_MODULE_INTEGRATION.md` | REGISTERED | — | — |
| Intercompany transactions | `intelligence/v17/functional/CROSS_MODULE_INTEGRATION.md` | REGISTERED | — | — |

---

## OCA Module Index

| Domain | Index file | Status |
|--------|-----------|--------|
| Accounting | `oca/v17/accounting/README.md` | REGISTERED |
| Inventory | `oca/v17/inventory/README.md` | REGISTERED |
| Manufacturing | `oca/v17/manufacturing/README.md` | REGISTERED |
| HR | `oca/v17/hr/README.md` | REGISTERED |
| Project | `oca/v17/project/README.md` | REGISTERED |
| All modules | `oca/MODULE_INDEX.md` | REGISTERED |

---

## Solution Assessment Index

| Domain | Assessment file | Status |
|--------|----------------|--------|
| Framework | `solution-assessment/ASSESSMENT_FRAMEWORK.md` | REGISTERED |
| Accounting | `solution-assessment/by-domain/accounting/README.md` | REGISTERED |
| Inventory | `solution-assessment/by-domain/inventory/README.md` | REGISTERED |
| Manufacturing | `solution-assessment/by-domain/manufacturing/README.md` | REGISTERED |
| HR | `solution-assessment/by-domain/hr/README.md` | REGISTERED |

---

*Update this file in the same commit as any new OAIS document.*
