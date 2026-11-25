# Odoo Architecture Intelligence System (OAIS)

**Version:** 1.0.0 — Phase 1 Skeleton
**Established:** 2026-11-25
**Decision:** DEC-013
**Status:** ACTIVE — knowledge acquisition not yet commenced

---

## Purpose

The OAIS is the Software Factory's structured, evidence-based technical knowledge base for Odoo. It equips the Architecture Governor (G1) and all project development agents with deep, version-specific understanding of Odoo internals, native capabilities, OCA modules, and implementation patterns.

It is not a copy of the Odoo documentation. It is an organised, citeable, verification-aware knowledge system that distinguishes what has been verified from what has been inferred.

---

## Who uses this

| Consumer | Primary use |
|----------|-------------|
| G1 Architecture Governor | Evidence base for architecture reviews and solution assessments |
| Project development agents | Reference during implementation; native-first checks |
| G2 Quality Governor | Quality and test pattern reference |
| G3 Security Governor | Security model and access-control reference |
| Human sponsor / reviewers | Architecture decision audit trail |

---

## What this is NOT

- It is not an override of `Autonomous-agent-Team/platform-profiles/23_PLATFORM_PROFILE_ODOO17_COMMUNITY.md`. The platform profile remains authoritative for approach order. The OAIS provides the evidence that informs that approach.
- It is not official Odoo documentation. AI-generated intelligence is clearly labelled and must not be treated as authoritative without independent verification.
- It is not project-specific. Client data, credentials, and project-specific configuration do not belong here.

---

## Directory map

```
odoo-architecture-intelligence/
├── README.md                    ← This file
├── CLAUDE.md                    ← Agent retrieval and usage protocol
├── INDEX.md                     ← Topic → file navigation table (always read first)
├── SOURCE_REGISTER.md           ← All sources with verification metadata
├── ACQUISITION_PLAN.md          ← Knowledge acquisition plan for all 15 domains
│
├── official-docs/               ← Retrieved official Odoo documentation (originals)
├── source-code-refs/            ← Source-code path and class references (no code copies)
├── intelligence/                ← AI-generated interpretations (clearly labelled)
├── architecture-recommendations/ ← Reviewed and approved recommendations
├── verified-findings/           ← LAB_VERIFIED and INDEPENDENTLY_REVIEWED content
│
├── oca/                         ← OCA module intelligence by version and domain
├── solution-assessment/         ← Native vs OCA vs Custom assessments
├── security/                    ← Security and access-control knowledge
├── patterns/                    ← Architecture patterns and anti-patterns
├── testing-and-qa/              ← Testing framework and QA checklists
├── case-studies/                ← Project lessons (no client data)
├── architecture-lab/            ← Future experiments and reproducible tests
└── meta/                        ← Maintenance, contribution, and retrieval guides
```

---

## How agents should use this

**Start here:** Read `INDEX.md` to identify which file(s) are relevant to your question.

Do not load the entire OAIS into every prompt. The index-first protocol in `CLAUDE.md` and `meta/RETRIEVAL_GUIDE.md` explains the retrieval strategy.

For every material architecture decision, the retrieval protocol covers:

1. Identify the target Odoo version and edition.
2. Identify the relevant business domain.
3. Investigate native capabilities (`official-docs/`, `source-code-refs/`).
4. Investigate relevant OCA alternatives (`oca/`).
5. Check existing Software Factory reusable modules (each pod's MODULE_REGISTRY.md).
6. Inspect Odoo source code references where necessary (`source-code-refs/`).
7. Assess cross-module, security, financial, performance and upgrade implications.
8. Cite evidence from `SOURCE_REGISTER.md` and declare unresolved uncertainties.
9. Recommend the least complex suitable solution.

---

## Verification states

All content in this system carries one of the following states:

| State | Meaning |
|-------|---------|
| `REGISTERED` | Source identified but not yet retrieved |
| `RETRIEVED` | Source obtained; content recorded |
| `SOURCE_VERIFIED` | Claim verified against official documentation or source code |
| `LAB_VERIFIED` | Behaviour reproduced in an isolated Odoo environment |
| `INDEPENDENTLY_REVIEWED` | Reviewed by an independent technical reviewer |
| `STALE` | Requires revalidation against current Odoo version |
| `SUPERSEDED` | Replaced by newer guidance; retained for history |

Retrieval alone does not imply technical verification.

---

## Governance

This system is governed by DEC-013. Changes to structure, retrieval protocol, or verification standards require a decision log entry. Content additions follow the contribution guide in `meta/CONTRIBUTION_GUIDE.md`.

*OAIS established 2026-11-25 under Software Factory Governance Standard SPEC-GOV-ENF-001.*
