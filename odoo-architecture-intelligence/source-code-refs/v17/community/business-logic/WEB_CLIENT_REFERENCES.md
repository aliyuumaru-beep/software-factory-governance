# Source-Code References — Web Client and Controllers (Odoo 17 Community)

**Status:** REGISTERED — not yet populated
**Odoo Version:** 17
**Edition:** Community
**Decision:** DEC-013

## Key files

| File | Purpose |
|------|---------|
| `odoo/http.py` | HTTP routing, `Controller` base, `route()` decorator |
| `odoo/addons/web/controllers/main.py` | Main web client controller |
| `addons/web/static/src/` | OWL-based JavaScript frontend (v17 uses OWL framework) |

## Key classes (Python)

| Class / Function | File | Brief purpose |
|-----------------|------|---------------|
| `Controller` | `odoo/http.py` | Base class for all HTTP controllers |
| `route()` | `odoo/http.py` | Decorator to register a URL route |
| `request` | `odoo/http.py` | Thread-local request object |

## Note on OWL

Odoo 17 uses OWL (Odoo Web Library) for the web client, replacing the legacy widget system. OWL is a component-based JavaScript framework. Key OWL components live under `addons/web/static/src/`.

---

*Populate with specific method signatures and OWL component paths during Phase 2.*
