# OAIS — OCA Module Intelligence

**Status:** REGISTERED — MODULE_INDEX stub defined; assessments not yet acquired
**Decision:** DEC-013

This directory holds intelligence about Odoo Community Association (OCA) modules — their capabilities, limitations, maintenance status, and suitability for Software Factory projects.

## Critical principle

The existence of an OCA module does not make it suitable for adoption. Every module must be assessed against the criteria in `MODULE_ASSESSMENT_TEMPLATE.md` before recommendation.

## Directory structure

```
oca/
├── README.md                    ← This file
├── MODULE_INDEX.md              ← All known relevant OCA modules across domains
├── MODULE_ASSESSMENT_TEMPLATE.md ← Template for individual module assessments
└── v17/
    ├── README.md
    ├── accounting/
    ├── inventory/
    ├── manufacturing/
    ├── hr/
    └── project/
```

## OCA version note

OCA maintains a separate branch per Odoo major version. All entries in `v17/` refer to modules with an active `17.0` branch. Do not add modules that do not have a `17.0` branch confirmed.

## Licence note

Most OCA modules are LGPL-3. Verify the licence in `__manifest__.py` before including a module in a project. Some OCA repos contain modules with different licences.
