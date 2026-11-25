# Module Registry — Software Factory Governance

This registry records all components, subsystems, shared capabilities, and infrastructure
elements of the software-factory-governance repository. It follows the standard defined
in `governance/REGISTRY_STANDARD.md`.

---

## Registry Format

| Field | Description |
|-------|-------------|
| ID | Unique registry identifier (REG-NNN) |
| Name | Component name |
| Type | SHARED_CAPABILITY / STANDARD / TEMPLATE / TOOLING / CI |
| Status | ACTIVE / DEPRECATED / PLANNED |
| Path | Root path in this repository |
| Decision | DEC-xxx that authorises this component |
| Added | ISO date of registration |
| Description | One-line description |

---

## Components

| ID | Name | Type | Status | Path | Decision | Added | Description |
|----|------|------|--------|------|----------|-------|-------------|
| REG-001 | Odoo Architecture Intelligence System (OAIS) | SHARED_CAPABILITY | ACTIVE | `odoo-architecture-intelligence/` | DEC-013 | 2026-11-25 | Version-isolated Odoo architecture knowledge base; 16 domains; 6 epistemic layers |
| REG-002 | Governance Standards | STANDARD | ACTIVE | `governance/` | DEC-001 | 2026-05-29 | Master governance standards for all Software Factory projects |
| REG-003 | Governance Templates | TEMPLATE | ACTIVE | `templates/` | DEC-001 | 2026-05-29 | Reusable document templates for governed repositories |
| REG-004 | Autonomous Agent Team / Platform Profiles | SHARED_CAPABILITY | ACTIVE | `Autonomous-agent-Team/` | DEC-001 | 2026-05-29 | Platform profiles restricting project scope (e.g. Odoo 17 Community only) |
| REG-005 | Governance Gate CI Stub | CI | ACTIVE | `.github/workflows/governance.yml` | DEC-014 | 2026-11-25 | Reserves `governance / gate` check name; full G1/G2/G3 CI is Phase 4 |
| REG-006 | Gov Tooling Configuration | TOOLING | ACTIVE | `.governance.json` | DEC-014 | 2026-11-25 | Pod registration and code-path configuration for `gov` CLI tooling |
| REG-007 | Agent Rules (AGENTS.md) | TOOLING | ACTIVE | `AGENTS.md` | DEC-014 | 2026-11-25 | Mandatory agent instructions for all tools working in this repository |

---

## Notes

- Components registered here are those that are shared across projects or that represent
  significant infrastructure. Project-specific modules are registered in their own
  pod's `MODULE_REGISTRY.md`.
- The OAIS (REG-001) is the first shared capability registered in this repository.
  Future shared capabilities (reusable modules, shared scripts) will follow.
- `governance/REGISTRY_STANDARD.md` defines what must be registered and how.
