# OAIS — Official Odoo Documentation

**Status:** REGISTERED — not yet acquired
**Decision:** DEC-013

This directory holds official Odoo documentation retrieved from `https://github.com/odoo/documentation`.

Content is stored version-by-version. Do not mix content from different Odoo versions.

**Licence:** CC BY-NC-SA 4.0. Internal reference only. Do not publish or redistribute.

## Directory structure

```
official-docs/
├── v17/   ← Odoo 17 (Community priority)
├── v18/   ← Not yet applicable
└── v19/   ← Not yet applicable
```

## Rules for this section

- Every file must cite its SRC-xxx source register entry in its frontmatter.
- Store RST source files as retrieved; do not rewrite or summarise in this section.
- If a rendered summary is needed, create it in `intelligence/v{n}/` with an explicit AI-generated label.
- Record the upstream commit SHA and checksum in SOURCE_REGISTER.md at retrieval time.

Acquisition begins in Phase 2. See `../ACQUISITION_PLAN.md`.
