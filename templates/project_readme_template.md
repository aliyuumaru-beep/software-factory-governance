# [Project Name]

> [One sentence describing what this project is and who it is for.]

**Governed by:** [Software Factory Governance Repository](../software-factory-governance)
**Platform:** Odoo [version] / [other platform]
**Industry:** [Industry vertical]
**Client:** [Client name or "Internal"]
**Current Phase:** Phase [N] — [Phase Name]
**Status:** [Active Development | Maintenance | Stable | Decommissioned]

---

## What This Project Is

<!-- Two to four sentences explaining the business problem this project solves,
     who uses it, and the value it delivers. -->

---

## Technology Stack

| Component | Technology | Version | Notes |
|-----------|-----------|---------|-------|
| ERP Platform | Odoo | 17.0 | |
| Database | PostgreSQL | 15 | |
| Web Server | Nginx | | Reverse proxy |
| OS | Ubuntu | 22.04 LTS | |
| Python | Python | 3.10+ | |

---

## Architecture Summary

<!-- High-level description of the system structure.
     Include a simple ASCII diagram if it helps orientation. -->

```
[Browser / Mobile]
       │
    [Nginx]
       │
   [Odoo 17]
       │
  [PostgreSQL]
       │
  [Filestore]
```

---

## Custom Modules

| Module | Purpose | Status |
|--------|---------|--------|
| [module_name] | [what it does] | ACTIVE |

Full registry: see `MODULE_REGISTRY.md`.

---

## Project Governance Documents

| Document | Purpose |
|----------|---------|
| [`DECISION_LOG.md`](DECISION_LOG.md) | Architectural and security decisions |
| [`IMPLEMENTATION_HISTORY.md`](IMPLEMENTATION_HISTORY.md) | Delivery milestones and operational events |
| [`MODULE_REGISTRY.md`](MODULE_REGISTRY.md) | Inventory of all custom artifacts |
| [`ROADMAP.md`](ROADMAP.md) | Current and planned project phases |
| [`CLAUDE.md`](CLAUDE.md) | AI agent instruction set |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |

---

## Setup and Installation

### Prerequisites
- [List prerequisites]

### Local Development Setup
```bash
# Step-by-step setup commands
```

### Staging / Production Deployment
See `docs/DEPLOYMENT_GUIDE.md`.

---

## Backup and Recovery

- **Backup schedule:** [Daily / Weekly / etc.]
- **Backup location:** [Storage location (do not include credentials)]
- **Last verified restore:** [Date]
- **RPO:** [Recovery Point Objective]
- **RTO:** [Recovery Time Objective]

Full procedure: see `operations/BACKUP_AND_RECOVERY_STANDARD.md`.

---

## Current Status

### What Is Complete
- [Phase N-1] — [brief description] — Completed [date]
- [Feature] — [brief description] — Completed [date]

### What Is In Progress
- [Phase N] — [brief description] — Target [date]

### Known Issues
| Issue | Severity | Notes |
|-------|----------|-------|
|       |          |       |

---

## Contributing

All changes must follow the Software Factory PR Governance Standard.
See `governance/PR_GOVERNANCE_STANDARD.md` and use `templates/pull_request_template.md`.

---

*This project is part of the Software Factory. Governance standards apply.*
