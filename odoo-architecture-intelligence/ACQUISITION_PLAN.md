# OAIS — Knowledge Acquisition Plan

**Status:** DRAFT — awaiting Phase 2 approval
**Decision:** DEC-013
**Last updated:** 2026-11-25
**Coverage target:** Odoo 17 Community — all 15 domains

This plan defines how official Odoo documentation and source-code references will be acquired, stored, indexed, and verified. No bulk acquisition is to commence until this plan is approved and a Phase 2 work item is created.

---

## 1. Source repositories

### 1.1 Official Odoo documentation

| Item | Detail |
|------|--------|
| Primary source | Odoo official documentation site |
| GitHub repository | `https://github.com/odoo/documentation` |
| Target branch | `17.0` (version-pinned) |
| Format | RST source files in GitHub; rendered HTML on official site |
| Licence | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) |
| Redistribution restriction | Non-commercial only. Raw RST/HTML must not be redistributed in modified form without attribution. Store locally for internal reference only; do not publish. |

### 1.2 Official Odoo source code

| Item | Detail |
|------|--------|
| Community repository | `https://github.com/odoo/odoo` |
| Target branch | `17.0` |
| Licence | LGPL-3 (framework) / LGPL-3 + proprietary addons |
| Acquisition method | File path and class/method references only — do not copy source files. Record module path, class name, method name, and commit SHA. |
| Redistribution | LGPL-3 allows redistribution with source; however, store references only, not copies, to keep the OAIS lightweight. |

### 1.3 OCA repositories

| Item | Detail |
|------|--------|
| Organisation | `https://github.com/OCA` |
| Target branch | `17.0` branch of each module repository |
| Licence | LGPL-3 (most modules); verify per-module |
| Acquisition method | README, manifest, and key source files; store summary in `oca/v17/{domain}/` |

---

## 2. Acquisition method by content type

### 2.1 Official documentation (Domains 1–15)

**Method:** Clone or sparse-checkout the `odoo/documentation` repository at the `17.0` branch.

```
git clone --branch 17.0 --depth 1 https://github.com/odoo/documentation.git
```

Store the RST source files under `official-docs/v17/` organised by domain.
Do not store the full repository — sparse-checkout only the relevant paths.

**Version pinning:** Record the commit SHA at acquisition time in SOURCE_REGISTER.md.

**Incremental updates:** Re-fetch the specific files when a point release is announced. Compare checksums against previous version; create a new SOURCE_REGISTER entry for updated content.

**Failed downloads:** Log any failed or missing documents in a `DOWNLOAD_FAILURES.md` in the relevant version directory. Do not silently omit a domain.

### 2.2 Source-code references (Domains 1, 2, 5–10)

**Method:** Browse the GitHub web interface or clone locally. Record:
- Repository URL
- Branch and commit SHA
- File path relative to repository root
- Class name(s)
- Key method names and signatures (not full implementations)

Store these references in `source-code-refs/v17/{section}/`.

**Do not copy Odoo source code into this repository.** Record pointers only.

### 2.3 OCA module intelligence

**Method:** For each relevant OCA module:
1. Record the module name, repository, and 17.0 branch commit SHA.
2. Retrieve the module's README.md and `__manifest__.py`.
3. Complete the OCA Module Assessment Template.

Store under `oca/v17/{domain}/{module_name}.md`.

---

## 3. Local storage format

| Content type | Location | Format |
|-------------|----------|--------|
| Official docs (RST source) | `official-docs/v17/{domain}/` | `.rst` files, as retrieved |
| Rendered summaries | `official-docs/v17/{domain}/` | `.md` summaries citing the RST source |
| Source-code references | `source-code-refs/v17/{section}/` | `.md` with file paths and method signatures |
| AI-generated intelligence | `intelligence/v17/{architecture\|functional}/` | `.md` with explicit AI-generated label |
| OCA assessments | `oca/v17/{domain}/{module_name}.md` | `.md` using MODULE_ASSESSMENT_TEMPLATE |

All Markdown files must include a frontmatter block:

```
<!--
oais:version: 17
oais:edition: community
oais:domain: [domain name]
oais:status: [verification state]
oais:source: [SRC-xxx]
oais:retrieved: [ISO date]
oais:checksum: [SHA-256 of source file, if applicable]
-->
```

---

## 4. Indexing method

1. Every new file must be added to `INDEX.md` in the same commit.
2. The INDEX.md topic→file table is the primary navigation mechanism.
3. No additional search tooling is required at Phase 2; INDEX.md is sufficient for agent navigation.
4. If the index grows beyond 300 rows, split into domain-specific sub-indexes and add a master table pointing to them.

---

## 5. Source verification method

| Verification level | Method |
|--------------------|--------|
| `RETRIEVED` | File downloaded; checksum recorded in SOURCE_REGISTER.md |
| `SOURCE_VERIFIED` | A specific technical claim cross-referenced against the retrieved document or source-code reference |
| `LAB_VERIFIED` | Behaviour reproduced in an isolated Odoo 17 Community Docker environment; test script and result stored in `architecture-lab/` |
| `INDEPENDENTLY_REVIEWED` | A technical reviewer (human or independent G1 agent session) confirms the finding |

---

## 6. Licence and redistribution considerations

| Source | Licence | Storage permitted | External publication | Redistribution |
|--------|---------|------------------|----------------------|----------------|
| Odoo official docs | CC BY-NC-SA 4.0 | Yes — internal reference only | No — non-commercial restriction | Attribution required; no commercial use |
| Odoo source code | LGPL-3 | References only (paths, signatures) | References are facts, not protectable | LGPL-3 applies to full source, not references |
| OCA modules | LGPL-3 (mostly) | Yes — summaries and references | With attribution | LGPL-3 |
| Blog / forum posts | Varies | Excerpts with citation | Not without author permission | Cite with URL |

---

## 7. Incremental update mechanism

1. Each source entry in SOURCE_REGISTER.md records its `upstream_commit` and `checksum`.
2. On each Odoo minor/patch release announcement, re-fetch only the affected files.
3. Compare checksums. If changed: update local copy, increment STATUS to RETRIEVED, update `date_accessed`.
4. If previously SOURCE_VERIFIED content changes, downgrade to RETRIEVED and flag for re-verification.
5. Run a quarterly sweep: compare local checksums against the upstream `17.0` branch HEAD.

---

## 8. Coverage measurement

Coverage is tracked per domain in this table. Update after each acquisition sprint.

| Domain | Files identified | Files retrieved | Source-verified | Lab-verified |
|--------|-----------------|----------------|-----------------|--------------|
| ORM and model architecture | 0 | 0 | 0 | 0 |
| Security and access rights | 0 | 0 | 0 | 0 |
| Views and web client | 0 | 0 | 0 | 0 |
| Controllers and HTTP | 0 | 0 | 0 | 0 |
| Business workflows | 0 | 0 | 0 | 0 |
| Accounting | 0 | 0 | 0 | 0 |
| Inventory | 0 | 0 | 0 | 0 |
| Manufacturing | 0 | 0 | 0 | 0 |
| Procurement | 0 | 0 | 0 | 0 |
| Sales | 0 | 0 | 0 | 0 |
| Website and portal | 0 | 0 | 0 | 0 |
| Testing | 0 | 0 | 0 | 0 |
| Performance | 0 | 0 | 0 | 0 |
| Deployment | 0 | 0 | 0 | 0 |
| Upgrades | 0 | 0 | 0 | 0 |
| Cross-module integration | 0 | 0 | 0 | 0 |
| **Total** | **0** | **0** | **0** | **0** |

---

## 9. Failed-download and missing-document reporting

- Any URL that returns a non-200 response must be logged in `official-docs/v17/DOWNLOAD_FAILURES.md`.
- If an entire domain is missing from the upstream documentation, record it in this file under a "Missing domains" section with the retrieval date and the URL that was attempted.
- Do not silently skip a domain. A missing domain is a coverage gap and must be visible.

---

## 10. Phase 2 scope boundary

Phase 2 is limited to:

- Odoo 17 Community official documentation for all 15 domains.
- Odoo 17 source-code references for all 11 source-code intelligence sections.
- OCA module index for the 5 initial domains (accounting, inventory, manufacturing, HR, project).

Phase 2 does NOT include:
- Odoo 18 or 19 content.
- Enterprise edition content.
- Lab verification (Phase 3).
- OCA module assessments beyond the index (Phase 3).
- Architecture recommendations (Phase 4 — after SOURCE_VERIFIED content is available).

---

*This plan requires a Phase 2 work item (WP- or DEC-) before acquisition commences.*
