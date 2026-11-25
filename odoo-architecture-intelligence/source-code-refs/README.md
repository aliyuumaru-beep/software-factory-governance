# OAIS — Source-Code References

**Status:** REGISTERED — not yet populated
**Decision:** DEC-013

This directory holds source-code references for the Odoo codebase — file paths, class names, method signatures, and commit SHAs. It does NOT contain copies of Odoo source code.

## Purpose

Agents and reviewers need to know where specific behaviour is implemented in the Odoo codebase without navigating the full repository. These reference files provide:

- Repository and branch
- File path relative to repository root
- Class and method names with brief purpose descriptions
- Commit SHA at time of reference
- Link to the GitHub permalink

## What belongs here

- File paths and class references: `odoo/models.py`, class `BaseModel`
- Method signatures: `def _search(self, domain, offset=0, limit=None, order=None)`
- Brief description of what the method does (1–2 sentences)
- The commit SHA the reference was recorded at

## What does NOT belong here

- Full method implementations
- Copied source files
- Paraphrased logic presented as official documentation

## Directory structure

```
source-code-refs/
├── v17/
│   ├── REPOSITORY_MAP.md         ← Repo URLs, branches, commit pins
│   ├── community/                ← Odoo Community (LGPL) references
│   │   ├── framework/
│   │   └── business-logic/
│   └── enterprise/
│       └── README.md             ← Note: Enterprise source not publicly available
└── v18/
    └── README.md                 ← Not yet applicable
```
