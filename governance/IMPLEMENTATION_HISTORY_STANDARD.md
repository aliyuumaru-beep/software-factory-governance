# Implementation History Standard

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

The Implementation History is the project's longitudinal record of what was built, when it
was built, and what its current operational status is. Where the Decision Log records *why*
decisions were made, the Implementation History records *what* was delivered and *when*.

This document is critical for:
- Onboarding new developers or AI agents who need a fast, accurate project state summary.
- Continuity when sessions, team members, or contexts change.
- Auditing what was delivered against what was planned.
- Identifying regression risk when touching previously completed areas.

---

## 2. What Must Be Recorded

### 2.1 Phase Completions
When a project phase is completed, an entry must record:
- Phase number and name
- Completion date
- What was delivered in the phase
- Known outstanding issues at phase close
- Status going into the next phase

### 2.2 Module or Feature Completions
When a significant module or feature is delivered to production or staging:
- Module/feature name and identifier
- Delivery date
- Brief description of what was built
- Configuration notes relevant to future maintenance
- Known limitations or deferred items

### 2.3 Significant Operational Changes
Any change to a running production system that affects data, configuration, or behaviour:
- Date of change
- What changed
- Why it changed
- Rollback procedure used (if applicable)
- Confirmation of post-change verification

### 2.4 Emergency Hotfixes
All emergency hotfixes must be recorded here within 24 hours of deployment:
- Date and time of deployment
- What broke, what was fixed
- Root cause (preliminary)
- Whether a proper PR will follow
- Who deployed and who approved

### 2.5 Restore Events
When a backup restore is performed (scheduled drill or emergency):
- Date and scope of restore
- Source backup used (date, type)
- Outcome (success/partial/failure)
- Any data loss or inconsistency identified
- Follow-up actions

### 2.6 Infrastructure Changes
Changes to hosting, server configuration, domain, SSL, or network topology:
- Date
- What changed
- Who authorized it
- Verification steps performed

---

## 3. What Does NOT Belong in the Implementation History

- Routine minor bug fixes that are already captured in `CHANGELOG.md`.
- Internal refactors with no user-facing or operational impact.
- Draft or work-in-progress items.
- Items that were planned but not yet delivered (those belong in `ROADMAP.md`).

---

## 4. Implementation History Format

Every entry uses the template in `templates/implementation_history_template.md`.

Required fields:
- **ID** — sequential identifier (e.g., `IMP-001`)
- **Date** — ISO 8601 date (YYYY-MM-DD)
- **Type** — entry type (see section 2)
- **Title** — one-sentence description
- **Delivered By** — person and/or AI agent session
- **Description** — what was built or changed
- **Scope** — what modules, features, or systems are affected
- **Status** — `COMPLETE`, `PARTIAL`, `IN_PROGRESS`, `DEFERRED`
- **Outstanding Issues** — known issues at time of recording
- **References** — related PR numbers, decision log entries, or roadmap items

---

## 5. Implementation History Location

Each project repository maintains its own `IMPLEMENTATION_HISTORY.md` at the root level.

The Software Factory governance repository maintains its own
`IMPLEMENTATION_HISTORY.md` for governance-level deliveries (bootstrap, governance
updates, template releases).

---

## 6. Maintenance Rules

### 6.1 Timing
Entries must be added:
- At the conclusion of each project phase.
- Within 24 hours of a production deployment.
- Within 24 hours of a restore event (planned or emergency).
- At the conclusion of any significant milestone, even if not a full phase.

### 6.2 AI Agent Responsibility
AI agents must:
- Read `IMPLEMENTATION_HISTORY.md` before starting work in any area of a project.
- Not assume that because code exists, it was properly delivered and verified.
- Add an implementation history entry when completing a phase or milestone.
- Flag to the user when work appears to overlap with a prior implementation history entry.

### 6.3 Stale History
An implementation history that has not been updated in more than 30 days while a project
is actively in development is a governance defect. The next PR must include an update.

---

## 7. Entry Types Reference

| Type Code | Description |
|-----------|-------------|
| `PHASE_COMPLETE` | A project phase was completed |
| `MODULE_DELIVERED` | A module or major feature was delivered |
| `OPERATIONAL_CHANGE` | A change was made to a running system |
| `HOTFIX` | An emergency fix was deployed |
| `RESTORE_EVENT` | A backup restore was performed |
| `INFRASTRUCTURE_CHANGE` | A hosting or infrastructure change was made |
| `GOVERNANCE_UPDATE` | A governance standard or template was updated |
| `ONBOARDING` | A project was onboarded to the Software Factory |

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
