# OAIS — Agent Retrieval Guide

**Decision:** DEC-013

This guide defines how AI agents should retrieve knowledge from the OAIS efficiently, without loading the entire repository into every prompt.

---

## Core principle

The OAIS may eventually contain hundreds of files. No agent should load all of them. The INDEX.md file is the navigation layer. Load what you need, trace evidence back to sources.

---

## Standard retrieval sequence

### Step 1 — Read INDEX.md

Always start here. The INDEX.md maps every topic to its file, organized by the 16 domains. This single file is the entry point for every retrieval.

### Step 2 — Identify version, edition, and domain

Before reading any further file, confirm:
- **Odoo version:** 17 / 18 / 19 (default to 17 unless otherwise stated)
- **Edition:** Community / Enterprise (default to Community per platform profile)
- **Domain:** Which of the 16 domains applies

### Step 3 — Follow the architecture decision sequence

For any material architecture decision, retrieve in this order:

| Step | What to retrieve | Where to look |
|------|-----------------|---------------|
| 1 | Native capability | `official-docs/v17/{domain}/` → `intelligence/v17/{functional|architecture}/` |
| 2 | OCA alternatives | `oca/v17/{domain}/` → `oca/MODULE_INDEX.md` |
| 3 | SF reusable modules | The relevant pod's `MODULE_REGISTRY.md` |
| 4 | Source code references | `source-code-refs/v17/community/{framework|business-logic}/` |
| 5 | Cross-module impact | `intelligence/v17/functional/CROSS_MODULE_INTEGRATION.md` |
| 6 | Evidence verification | `SOURCE_REGISTER.md` — confirm SRC-xxx status |

### Step 4 — Cite sources

Every recommendation must cite at least one `SRC-xxx` from `SOURCE_REGISTER.md`. Claims from AI training data must be labelled `[UNVERIFIED — AI training data only]`.

### Step 5 — Cross-version queries

For anything that might differ between v17 and v18, read:
`odoo/cross-version/VERSION_COMPATIBILITY_MATRIX.md`

---

## How many files to load

Do not impose an arbitrary maximum. Load as many files as are genuinely needed to understand cross-module implications for the decision at hand. For a simple single-domain question, 1–2 files is usually sufficient. For a complex cross-module architecture decision, 5–10 files may be necessary.

The criterion is: "Have I loaded enough evidence to understand the full architectural impact?" — not "Have I loaded the minimum number of files?"

---

## Epistemic hygiene

| Source layer | Trust level | Action required |
|-------------|-------------|----------------|
| `official-docs/` | High | Cite SRC-xxx; note if STALE |
| `source-code-refs/` | High | Confirm commit SHA is correct version |
| `architecture-recommendations/` | High | These are G1-reviewed |
| `verified-findings/` | High for stated conditions | Note the exact conditions |
| `intelligence/` | Moderate | Must not be cited as official; label claims |
| AI training data (not in OAIS) | Low | Must be labelled UNVERIFIED |

---

## Declaring uncertainty

When a material question cannot be answered from OAIS content:

1. State explicitly: "This question is not yet covered in the OAIS."
2. Identify what source would answer it (e.g., "This requires retrieving `{upstream_path}` from the official Odoo docs").
3. Do not invent an answer. Do not cite AI training data as if it were verified.
4. Recommend adding the question to the Phase 2 acquisition backlog.
