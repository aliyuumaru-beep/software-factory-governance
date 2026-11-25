# Source-Code References — Module Loading and Dependencies (Odoo 17 Community)

**Status:** REGISTERED — not yet populated with verified references
**Odoo Version:** 17
**Edition:** Community
**Repository:** `https://github.com/odoo/odoo` branch `17.0`
**Commit pin:** To be recorded at Phase 2 acquisition
**Decision:** DEC-013

---

## Key files

| File | Purpose |
|------|---------|
| `odoo/modules/loading.py` | Main module loading orchestration |
| `odoo/modules/module.py` | Module discovery and manifest parsing |
| `odoo/modules/graph.py` | Dependency graph construction |
| `odoo/modules/registry.py` | Model registry per database |

## Key functions

*To be populated during Phase 2.*

| Function / Class | File | Brief purpose |
|-----------------|------|---------------|
| `load_modules()` | `loading.py` | Loads and installs modules for a database |
| `load_module_graph()` | `loading.py` | Builds module dependency graph |
| `load_manifest()` | `module.py` | Parses `__manifest__.py` |
| `get_manifest()` | `module.py` | Returns parsed manifest dict |

---

*Populate this file during Phase 2 with actual signatures from the pinned commit.*
