# OAIS — Maintenance Guide

**Decision:** DEC-013

This guide defines how to keep the OAIS accurate, current, and useful.

---

## 1. Adding a new document

1. Write the document in the correct directory for its type:
   - Official retrieved content → `official-docs/v{n}/{domain}/`
   - Source-code references → `source-code-refs/v{n}/community/{section}/`
   - AI-generated intelligence → `intelligence/v{n}/{architecture|functional}/`
   - Architecture recommendation → `architecture-recommendations/`
   - Verified finding → `verified-findings/{lab-verified|independently-reviewed}/`
2. Add a frontmatter block with: status, Odoo version, edition, source, date.
3. Register the source in `SOURCE_REGISTER.md` before or simultaneously.
4. Update `INDEX.md` in the same commit — no exceptions.
5. Submit via PR on a feature branch.

## 2. Updating a document

1. If the Odoo version is unchanged: update in place; update `SOURCE_REGISTER.md` date and status.
2. If the Odoo version has changed (e.g., v17 → v18): create a new file in the v18 directory; do not modify the v17 file.
3. If a source has changed and content is now potentially stale: downgrade STATUS to `STALE` in both the document frontmatter and `SOURCE_REGISTER.md`.

## 3. Stale content review

Quarterly check:
1. Compare checksums of local files against upstream `17.0` branch HEAD.
2. Files whose upstream source has changed: downgrade to `STALE`.
3. If previously SOURCE_VERIFIED content is now STALE: create a task to re-verify.

## 4. Retiring a document

1. Do not delete documents. Set STATUS to `SUPERSEDED`.
2. Add a note in the document: "Superseded by: [new file path]".
3. Update `INDEX.md` to point to the new file and note the superseded one.

## 5. INDEX.md is mandatory

Every PR that adds or removes a document must update `INDEX.md`. A PR that creates a new file without updating INDEX.md is a governance defect and must not be merged.

## 6. Version isolation

Never copy content from `v17/` to `v18/`. Each version directory is built independently from its own sources. Version-agnostic content goes in `cross-version/`.
