# OAIS — Contribution Guide

**Decision:** DEC-013

---

## Who may contribute

Any Software Factory agent or developer may contribute to the OAIS. Contributions to `architecture-recommendations/` and `verified-findings/` require G1 Architecture Governor approval.

## Contribution types

| Type | Directory | Reviewer required |
|------|-----------|------------------|
| AI-generated intelligence | `intelligence/` | None — but must be labelled |
| Source-code reference | `source-code-refs/` | None — but must cite commit SHA |
| OCA module assessment | `oca/v{n}/{domain}/` | None — but must follow template |
| Solution assessment | `solution-assessment/by-domain/` | None — but must follow framework |
| Architecture recommendation | `architecture-recommendations/` | G1 Architecture Governor |
| Verified finding | `verified-findings/` | G1 or independent reviewer |
| Official documentation | `official-docs/` | Must be retrieved, not AI-generated |

## Mandatory frontmatter

Every new OAIS document must include a frontmatter comment block:

```
<!--
oais:version: [17 | 18 | 19]
oais:edition: [Community | Enterprise | Both]
oais:domain: [domain name]
oais:status: [REGISTERED | RETRIEVED | SOURCE_VERIFIED | LAB_VERIFIED | INDEPENDENTLY_REVIEWED]
oais:source: [SRC-xxx or NONE]
oais:date: [ISO date]
-->
```

## Epistemic labelling in intelligence/ content

Every material claim in `intelligence/` must carry a label:

| Label | Use when |
|-------|---------|
| `[SOURCE: SRC-xxx — RETRIEVED]` | Claim supported by retrieved official source |
| `[SOURCE: SRC-xxx — SOURCE_VERIFIED]` | Claim explicitly verified against source |
| `[UNVERIFIED — AI training data only]` | Claim from AI training data, not yet verified |

## What is never acceptable

- Presenting AI-generated content as official Odoo documentation
- Adding content to `official-docs/` that was not retrieved from an authoritative source
- Marking content SOURCE_VERIFIED without citing a source
- Copying Odoo source code into this repository (references only)
- Including client data, credentials, or personal data
