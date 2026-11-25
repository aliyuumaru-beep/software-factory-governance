# CLAUDE.md — OAIS Agent Protocol

**Scope:** Any AI agent using the Odoo Architecture Intelligence System.
**Inherits from:** `../CLAUDE.md` (Software Factory Governance)
**Decision:** DEC-013

---

## 1. What this knowledge base is

The OAIS contains Odoo technical knowledge organised into six epistemic layers:

| Directory | Layer | Trust level |
|-----------|-------|-------------|
| `official-docs/` | Retrieved official Odoo documentation | High — treat as authoritative for the stated version |
| `source-code-refs/` | Source-code path, class and method references | High — verify commit reference is correct version |
| `intelligence/` | AI-generated interpretations and summaries | Moderate — must not be cited as official; cite SOURCE_REGISTER entry |
| `architecture-recommendations/` | Reviewed and approved recommendations | High — these have passed G1 review |
| `verified-findings/lab-verified/` | Behaviour verified in isolated Odoo environment | High for exact conditions stated |
| `verified-findings/independently-reviewed/` | Independently reviewed findings | High |

Do not treat `intelligence/` content as official documentation. When a claim matters, trace it to `official-docs/` or `source-code-refs/`.

---

## 2. Mandatory retrieval protocol

**Step 1 — Read INDEX.md first**
One file. Contains the topic→file navigation table covering all 16 domains (Domains 1–15 plus Domain 16 — Cross-Module Integration). Always start here.

**Step 2 — Identify version and edition**
Every OAIS query must specify: Odoo version (17 / 18 / 19) and edition (Community / Enterprise). Content is strictly version-isolated. Do not apply v17 guidance to v18 without reading `odoo/cross-version/VERSION_COMPATIBILITY_MATRIX.md`.

**Step 3 — Follow the architecture decision sequence**
For any material architecture decision:
1. Investigate native capabilities — `official-docs/v{n}/` and `source-code-refs/v{n}/`
2. Investigate OCA alternatives — `oca/v{n}/{domain}/`
3. Check Software Factory reusable modules — the relevant pod's `MODULE_REGISTRY.md`
4. Assess cross-module implications — `intelligence/v{n}/functional/CROSS_MODULE_INTEGRATION.md`
5. Cite sources from `SOURCE_REGISTER.md` by their SRC-xxx reference
6. Declare any unresolved uncertainties explicitly

**Step 4 — Cite evidence**
Every architecture recommendation must cite at least one SRC-xxx entry from SOURCE_REGISTER.md. Uncited claims from AI memory must be labelled as `[UNVERIFIED — AI training data only]`.

**Step 5 — Cross-version questions**
Read `odoo/cross-version/VERSION_COMPATIBILITY_MATRIX.md` before assuming v17 guidance applies to v18 or v19.

---

## 3. What you must NOT do

- Do not load the entire OAIS into a single prompt. Use INDEX.md to identify the 1–5 relevant files.
- Do not present `intelligence/` content as official Odoo documentation.
- Do not copy Odoo source code into this knowledge base. Record file paths, class names, and method signatures with commit references only.
- Do not add client data, credentials, or project-specific configuration to this repository.
- Do not populate `official-docs/` with content you have not retrieved from an authoritative source.
- Do not mark content as SOURCE_VERIFIED, LAB_VERIFIED, or INDEPENDENTLY_REVIEWED without evidence.
- Do not apply v17 content to v18 or v19 directories by copy-paste.

---

## 4. Adding or updating content

See `meta/CONTRIBUTION_GUIDE.md` for the full process. Summary:

1. Every new document must include a frontmatter block with: status, Odoo version, edition, source references, and last verified date.
2. Every new source must be registered in `SOURCE_REGISTER.md` before or simultaneously with the document that cites it.
3. `INDEX.md` must be updated in the same commit as any new document.
4. AI-generated content goes in `intelligence/` only, never in `official-docs/` or `source-code-refs/`.

---

## 5. Retrieval without loading everything

When a user or governance review needs Odoo architecture guidance:

```
1. Read: odoo-architecture-intelligence/INDEX.md
2. Identify: target version, edition, domain
3. Read: the 1-5 files INDEX.md points to
4. If cross-module: also read intelligence/v{n}/functional/CROSS_MODULE_INTEGRATION.md
5. If source verification needed: read source-code-refs/v{n}/[relevant section]
6. Cite: SRC-xxx from SOURCE_REGISTER.md
```

Do not read all files speculatively. Read what the INDEX directs you to, then read more only if the initial files reference other sections.

---

*This protocol is part of OAIS Phase 1 (DEC-013). It governs all agents using this knowledge base.*
