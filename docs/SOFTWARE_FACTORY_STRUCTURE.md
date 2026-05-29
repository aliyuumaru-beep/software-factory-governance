# Software Factory Structure

**Version:** 1.0.0  
**Effective:** 2026-05-29

---

## 1. What Is the Software Factory?

The Software Factory is the organizational and technical structure through which
software projects are designed, built, governed, deployed, and maintained. It is
not a single application — it is a system of systems, each at a different layer
of abstraction, each with a defined scope and governance boundary.

The Software Factory exists to:
- Ensure consistent quality across all projects.
- Prevent repeated mistakes by capturing decisions and history.
- Enable faster project delivery by reusing tested patterns.
- Make projects maintainable by humans and AI agents who were not present at inception.

---

## 2. The Repository Structure

### 2.1 Governance Repository (This Repository)

`software-factory-governance`

The top-level repository. Contains all standards, templates, principles, and
operational procedures. Every other repository in the Software Factory is a
governed child of this one.

**What lives here:**
- Governance standards (`governance/`)
- Reusable templates (`templates/`)
- Onboarding standards (`onboarding/`)
- Operations procedures (`operations/`)
- Software Factory roadmap (`roadmaps/`)
- Architectural and operational principles (`principles/`)
- Structure documentation (`docs/`)

**What does NOT live here:**
- Project-specific code or configuration.
- Client data.
- Platform or infrastructure code.

### 2.2 Platform Repository (Future)

`software-factory-platform` (or equivalent)

A shared platform repository containing base configurations, shared modules,
and infrastructure that all Odoo projects inherit.

*Example contents:* shared Nginx configuration templates, base Odoo module
configuration, shared backup scripts, shared monitoring setup.

### 2.3 Industry Template Repositories (Future)

`sf-template-oil-gas`, `sf-template-ngo`, `sf-template-hospitality`, etc.

One repository per vertical/industry. Contains the module configuration,
demo data, and documentation specific to that vertical that is shared across
all client deployments of that type.

### 2.4 Client Project Repositories (Current)

`famoil-erp`, `wamacare`, `nadf-erp`, etc.

One repository per client deployment. Contains the client-specific
configuration, custom modules, data, and governance documents.

---

## 3. Current Repository Inventory

| Repository | Type | Status | Description |
|------------|------|--------|-------------|
| `software-factory-governance` | Governance | Active | This repository |
| FamOil ERP (`odoo17` or similar) | Client | Active | Soybean oil production ERP |
| WamaCare | Client | Active | NGO/CBO management platform |
| NADF ERP | Client | Planned | Agricultural development ERP |
| Hospitality ERP | Client | Planned | Hotel and hospitality ERP |
| Office ERP | Client | Planned | Office administration ERP |
| Power Sector ERP | Client | Planned | Power utility ERP |

---

## 4. How Governance Flows

```
software-factory-governance
  │
  ├── Standards and templates inherited by all projects
  │
  ├── FamOil ERP
  │     ├── CLAUDE.md (extends governance CLAUDE.md)
  │     ├── DECISION_LOG.md
  │     ├── IMPLEMENTATION_HISTORY.md
  │     ├── MODULE_REGISTRY.md
  │     └── ROADMAP.md
  │
  ├── WamaCare
  │     ├── CLAUDE.md (extends governance CLAUDE.md)
  │     ├── DECISION_LOG.md
  │     ├── IMPLEMENTATION_HISTORY.md
  │     ├── MODULE_REGISTRY.md
  │     └── ROADMAP.md
  │
  └── [Future projects follow the same pattern]
```

---

## 5. Who Owns What

| Scope | Owner |
|-------|-------|
| Governance standards and templates | Software Factory lead |
| Platform-level modules and configuration | Platform engineering |
| Industry template modules | Template/vertical lead |
| Client project implementation | Project team |
| Security decisions at any layer | Requires Software Factory lead sign-off |

---

## 6. File Naming Conventions

| Context | Convention |
|---------|-----------|
| Governance standards | `UPPER_SNAKE_CASE.md` |
| Templates | `lower_snake_case.md` |
| Project root documents | `UPPER_SNAKE_CASE.md` |
| General documentation | `UPPER_SNAKE_CASE.md` |
| Odoo module directories | `lower_snake_case/` |
| Odoo Python files | `lower_snake_case.py` |

---

*This document is maintained by the Software Factory. Updates require a PR.*
