# OAIS — Solution Assessments

**Status:** REGISTERED — framework defined; assessments not yet conducted
**Decision:** DEC-013

This directory holds assessments of specific business requirements against the three solution tiers:

1. **Native Odoo** — out-of-the-box capability or configuration-first
2. **OCA module** — community-maintained extension
3. **Custom module** — Software Factory custom development

The Software Factory Architectural Principle 1 (Platform-Native First) governs assessment order.

## Assessment framework

See `ASSESSMENT_FRAMEWORK.md` for the full decision method.

## Directory structure

```
solution-assessment/
├── README.md
├── ASSESSMENT_FRAMEWORK.md
└── by-domain/
    ├── accounting/
    ├── inventory/
    ├── manufacturing/
    └── hr/
```

## Assessment template

Each assessment is a markdown file structured as:
1. Business requirement
2. Native capability evaluation
3. OCA alternatives evaluation
4. Custom development evaluation
5. Recommendation with evidence citations
