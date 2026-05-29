# Registry Standard

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

The Module Registry is a complete, authoritative inventory of every custom module,
component, service, integration, automation, and script that exists in a project.

It exists because in complex, multi-phase projects — especially ERP deployments —
custom code accumulates silently. Without a registry, teams and AI agents cannot
know what exists, what is active, what is deprecated, or what depends on what.
The registry prevents duplication, uncontrolled growth, and invisible technical debt.

---

## 2. What Must Be Registered

The following categories of project artifacts must be registered:

### 2.1 Custom Modules
Any module that is not a standard platform module (e.g., not a standard Odoo
Community or Enterprise module) must be registered, including:
- Modules written from scratch for this project.
- Copies or forks of standard modules that have been customized.
- OCA (Odoo Community Association) or third-party modules installed in the project.

### 2.2 Custom Components
Significant custom code within a module that warrants separate tracking:
- Custom models (new database tables)
- Custom views or report templates
- Custom wizards
- Custom controllers or API endpoints
- Custom security rules or record rules

### 2.3 Services and Background Processes
Any process that runs outside of the normal user-request cycle:
- Scheduled actions (cron jobs)
- Queue workers
- External daemons or background services
- Webhooks that this system sends

### 2.4 Integrations
Any connection between this system and an external system:
- API integrations (outbound calls to external APIs)
- Webhook receivers (inbound calls from external systems)
- File-based integrations (FTP, SFTP, shared storage)
- Database-to-database connections
- Email automation integrations

### 2.5 Automations
Automated logic that triggers based on system events or schedules:
- Odoo automated actions
- Workflow automations
- Email templates that are triggered programmatically
- Document generation automations

### 2.6 Scripts
Any script run in the context of this project:
- Data migration scripts
- Import/export scripts
- Maintenance scripts
- Shell scripts for deployment or backup
- Python scripts run outside the application

### 2.7 Infrastructure Components
Custom infrastructure that is project-specific:
- Custom Nginx configuration
- Custom Docker containers or Compose files
- Custom CI/CD pipeline steps
- Custom monitoring or alerting rules

---

## 3. When Registration Must Occur

A registry entry MUST be created:
- **Before** or **in the same PR** as the artifact is merged into the main branch.
- Never after the fact as a catch-up exercise (this is a governance defect requiring a `GOVERNANCE_EXCEPTION` entry).

---

## 4. Registry Entry Format

Every registry entry must use the template in `templates/module_registry_template.md`.

Required fields:
- **ID** — unique identifier (e.g., `MOD-001`, `INT-001`, `SCR-001`)
- **Name** — technical name of the module/component/service
- **Type** — category (module, component, service, integration, automation, script, infrastructure)
- **Status** — `ACTIVE`, `DEPRECATED`, `DISABLED`, `PLANNED`
- **Registered Date** — when the entry was added to the registry
- **Introduced In** — PR number or phase reference
- **Purpose** — one to three sentences describing what this does and why it exists
- **Dependencies** — other modules, services, or external systems this depends on
- **Decision Log Reference** — if this was the result of an architectural decision, reference the `DECISION_LOG.md` entry ID
- **Owner** — team member or role responsible for this artifact
- **Notes** — anything important for future maintenance

---

## 5. Registry Location

Each project repository maintains its own `MODULE_REGISTRY.md` at the root level.

The registry is organized by artifact type with a summary table at the top for fast
scanning, followed by detailed entries for each artifact.

---

## 6. Registry Maintenance

### 6.1 Status Updates
When an artifact's status changes (e.g., a module is deprecated or disabled), the
registry entry must be updated in the same PR that makes the change.

### 6.2 Deprecation
When a registered artifact is deprecated:
- Status is updated to `DEPRECATED`.
- A note is added explaining what replaces it (if anything).
- A `DECISION_LOG.md` entry is created if the deprecation was an architectural decision.
- The artifact is not deleted from the registry — the history is preserved.

### 6.3 Deletion
When a registered artifact is deleted from the codebase:
- Status is updated to `DISABLED` and then removed after one full phase cycle.
- The deletion is recorded in `IMPLEMENTATION_HISTORY.md`.
- Dependencies on this artifact in other registry entries are updated.

### 6.4 AI Agent Responsibility
AI agents must:
- Read `MODULE_REGISTRY.md` before adding any new module, component, or integration.
- Check for existing registered artifacts that might already meet the need.
- Register any artifact they introduce before the PR is marked complete.
- Flag any artifact they discover in the codebase that is not yet registered.

---

## 7. Registry ID Prefixes

| Prefix | Type |
|--------|------|
| `MOD-` | Custom module |
| `CMP-` | Custom component within a module |
| `SVC-` | Background service or scheduled action |
| `INT-` | External integration |
| `AUT-` | Automation |
| `SCR-` | Script |
| `INF-` | Infrastructure component |

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
