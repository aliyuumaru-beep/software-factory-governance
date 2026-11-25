# OAIS — Source Register

**Status:** Schema defined — no sources registered yet.
**Decision:** DEC-013
**Last updated:** 2026-11-25

This register is the single authoritative record of every source used or identified within the OAIS. Every document in this knowledge base that cites a source must reference an entry here by its SRC-xxx identifier.

---

## Verification status definitions

| State | Meaning |
|-------|---------|
| `REGISTERED` | Source identified by URL or reference; not yet retrieved |
| `RETRIEVED` | Source obtained; raw content stored locally at `local_path` |
| `SOURCE_VERIFIED` | A specific technical claim has been verified against this source |
| `LAB_VERIFIED` | Behaviour described in source has been reproduced in an isolated Odoo environment |
| `INDEPENDENTLY_REVIEWED` | Source and derived content reviewed by an independent technical reviewer |
| `STALE` | Source was previously RETRIEVED or verified; revalidation required |
| `SUPERSEDED` | Source replaced by a newer version; retained for historical reference |

Retrieval alone does not imply technical verification. SOURCE_VERIFIED requires explicit cross-reference to official documentation or source code — not AI training data.

---

## Document type definitions

| Type | Meaning |
|------|---------|
| `OFFICIAL_DOCS` | Official Odoo S.A. documentation |
| `SOURCE_CODE` | Official Odoo source-code repository |
| `OCA_README` | Official OCA module README or documentation |
| `OCA_SOURCE` | OCA module source code |
| `GITHUB_ISSUE` | GitHub issue or PR discussion |
| `FORUM` | Odoo community forum post |
| `BLOG` | Technical blog post |
| `BOOK` | Published technical book |
| `INTERNAL` | Software Factory internal document |

---

## Schema — one row per source

| Field | Required | Description |
|-------|----------|-------------|
| `SRC-ID` | Yes | Sequential identifier, e.g. `SRC-001` |
| `Title` | Yes | Full title of the document or page |
| `Publisher` | Yes | Odoo S.A. / OCA / author name / forum |
| `URL` | Yes | Canonical URL; use version-pinned URL where available |
| `Odoo Version` | Yes | 17 / 18 / 19 / All / N/A |
| `Edition` | Yes | Community / Enterprise / Both / N/A |
| `Topic` | Yes | Domain (e.g. Accounting, ORM, Security) |
| `Doc Type` | Yes | One of the type codes above |
| `Date Accessed` | Yes | ISO 8601 date |
| `Licence` | Yes | Licence for redistribution (e.g. CC BY 4.0, LGPL-3, Proprietary) |
| `Upstream Commit` | No | Git commit SHA where applicable |
| `Local Path` | No | Relative path within `official-docs/` or `source-code-refs/` |
| `Checksum` | No | SHA-256 of local file at retrieval time |
| `Status` | Yes | One of the verification states above |
| `OAIS File` | Yes | Which OAIS file(s) cite this source |
| `Notes` | No | Redistribution restrictions, known inaccuracies, review notes |

---

## Source Register

*No sources registered yet. Phase 2 (Official Documentation Acquisition) will populate this register.*

| SRC-ID | Title | Publisher | Odoo Version | Edition | Topic | Doc Type | Date Accessed | Status | OAIS File |
|--------|-------|-----------|--------------|---------|-------|----------|---------------|--------|-----------|
| — | — | — | — | — | — | — | — | — | — |

---

*Register every source before or simultaneously with the document that cites it.*
*Update this register when a source's status changes.*
