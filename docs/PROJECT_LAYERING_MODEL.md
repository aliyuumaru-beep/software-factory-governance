# Project Layering Model

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

The Software Factory operates a four-layer model that separates governance, shared
platform concerns, industry-specific templates, and client-specific deployments into
distinct layers with clear boundaries.

Every artifact — a module, a standard, a configuration, a script — belongs to exactly
one layer. Placing it in the wrong layer creates maintenance debt, prevents sharing,
and violates governance boundaries.

---

## 2. The Four Layers

```
┌──────────────────────────────────────────────────────────┐
│                  Layer 1: Software Factory                │
│                                                          │
│  Governance · Standards · Templates · Methodology        │
│  Onboarding · Principles · Operations · Roadmaps         │
│                                                          │
│  Repository: software-factory-governance                 │
└──────────────────────────────────────────────────────────┘
                           ↓ inherits
┌──────────────────────────────────────────────────────────┐
│                   Layer 2: Platform                       │
│                                                          │
│  Shared Infrastructure · Base Odoo Configuration         │
│  Shared Modules · Deployment Scripts · Monitoring        │
│                                                          │
│  Repository: software-factory-platform (future)          │
└──────────────────────────────────────────────────────────┘
                           ↓ inherits
┌──────────────────────────────────────────────────────────┐
│               Layer 3: Industry Template                  │
│                                                          │
│  Vertical-Specific Modules · Demo Data · Configuration   │
│  Oil & Gas · NGO/CBO · Hospitality · Power · Office      │
│                                                          │
│  Repositories: sf-template-oil-gas, sf-template-ngo, …  │
└──────────────────────────────────────────────────────────┘
                           ↓ inherits
┌──────────────────────────────────────────────────────────┐
│               Layer 4: Client Deployment                  │
│                                                          │
│  Client-Specific Config · Custom Modules · Live Data     │
│  FamOil · WamaCare · NADF · Hospitality · Power · Office │
│                                                          │
│  Repositories: famoil-erp, wamacare, nadf-erp, …        │
└──────────────────────────────────────────────────────────┘
```

---

## 3. Layer Definitions

### Layer 1 — Software Factory

**Purpose:** Define how all projects are built, governed, and maintained.

**Owns:**
- Governance standards and binding rules.
- Templates for PRs, decision logs, registries, roadmaps, and onboarding.
- AI agent and developer onboarding standards.
- Architectural principles and overengineering guardrails.
- The Software Factory–level roadmap.
- Operational procedures for backup, release tagging, and change management.

**Does NOT own:**
- Code that runs inside any application.
- Client data or configuration.
- Platform infrastructure.

**Repository:** `software-factory-governance`

---

### Layer 2 — Platform

**Purpose:** Provide shared infrastructure and base configuration that all projects
inherit, eliminating duplication of common setup.

**Owns:**
- Base Odoo configuration (system parameters, base module set).
- Shared Nginx/web server configuration templates.
- Shared backup scripts and automation.
- Shared deployment and environment setup scripts.
- Shared monitoring and alerting configuration.
- Any module that is used, unchanged, across three or more client deployments.

**Does NOT own:**
- Client-specific data or customization.
- Industry-vertical-specific logic.
- Governance standards (those are Layer 1).

**Repository:** `software-factory-platform` (planned)

**Boundary rule:** A feature moves from Layer 4 to Layer 2 only when it is confirmed
to be needed, unchanged, in three or more client projects.

---

### Layer 3 — Industry Template

**Purpose:** Capture the common configuration and module set for a specific industry
vertical, so that new client deployments in that vertical start from a validated,
functional base rather than from scratch.

**Owns:**
- Industry-specific module configurations (e.g., tank management for oil & gas).
- Industry-specific chart of accounts templates.
- Industry-specific product categories and units of measure.
- Industry-specific user roles and security groups.
- Industry-specific demo data.
- Industry-specific documentation and onboarding guides.

**Does NOT own:**
- Client-specific data (real customers, real vendors, real transactions).
- Client-specific customizations.
- Cross-industry shared infrastructure.

**Repositories:** `sf-template-oil-gas`, `sf-template-ngo`, `sf-template-hospitality`,
`sf-template-power`, `sf-template-office` (all planned)

**Boundary rule:** A feature moves from Layer 4 to Layer 3 only when it is confirmed
to apply, with minor variation, across all client deployments in that vertical.

---

### Layer 4 — Client Deployment

**Purpose:** Deliver a working system to a specific client with their specific data,
configuration, and any customizations that are genuinely unique to them.

**Owns:**
- Client-specific module configuration and overrides.
- Custom modules that serve only this client's requirements.
- Client master data (chart of accounts, partners, products, locations).
- Client-specific automation and integrations.
- Client-specific documentation and runbooks.
- All governance documents for this deployment (DECISION_LOG, MODULE_REGISTRY, etc.).

**Does NOT own:**
- Logic that belongs in a template or platform layer.
- Governance standards (those are Layer 1).

**Repositories:** `famoil-erp`, `wamacare`, `nadf-erp`, and others.

---

## 4. Layer Boundary Rules

### 4.1 The Boundary Test
Before placing an artifact at any layer, ask:

> "How many distinct projects need this, and does it vary between them?"

| Answer | Correct Layer |
|--------|--------------|
| Only one client, specific to their data/requirements | Layer 4 |
| All clients in one vertical, same logic | Layer 3 |
| All clients across all verticals, same logic | Layer 2 |
| Applies to how all projects are built/governed | Layer 1 |

### 4.2 The Copy Rule
If you copy the same code or configuration from one client project to another
without modification, that code belongs one layer up. Move it before it proliferates.

### 4.3 The Dependency Direction
Dependencies always flow downward — lower layers depend on higher layers, never the
reverse.

✅ Layer 4 depends on Layer 3, Layer 2, and Layer 1.  
❌ Layer 1 must never depend on anything in Layer 4.  
❌ Layer 2 must never contain client-specific logic from Layer 4.

### 4.4 Cross-Layer PR Rule
A PR that moves code from Layer 4 to Layer 3 or 2 is a significant architectural
event. It requires:
- A decision log entry (`ARCHITECTURE` type).
- Review by the Software Factory lead.
- Verification that the moved artifact is genuinely generic (not just parameterized
  client-specific logic).

---

## 5. Current State

As of 2026-05-29, Layers 2 and 3 do not yet have dedicated repositories. All current
active projects (FamOil, WamaCare) operate at Layer 4 with direct inheritance from
Layer 1 (this repository).

Establishing Layer 2 and Layer 3 repositories is tracked in the Software Factory
Roadmap: `roadmaps/SOFTWARE_FACTORY_ROADMAP.md`.

---

## 6. Layer Identification in Documents

When writing governance documents, roadmaps, or decision log entries, identify the
layer explicitly using the notation:

- `[SF]` — Software Factory layer
- `[PLT]` — Platform layer
- `[TPL:<vertical>]` — Template layer, e.g. `[TPL:oil-gas]`
- `[CLT:<project>]` — Client deployment layer, e.g. `[CLT:famoil]`

---

*This document is maintained by the Software Factory. Updates require a PR with a decision log entry.*
