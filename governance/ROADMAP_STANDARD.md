# Roadmap Standard

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects

---

## 1. Purpose

This standard defines how roadmaps are structured, maintained, and kept distinct across
the four layers of the Software Factory. The goal is to ensure that planning at each layer
is clear, bounded, and does not bleed scope from one layer into another.

A well-maintained roadmap prevents scope creep, makes governance impact analysis easier,
and gives AI agents clear guidance about what is currently in scope vs. what is not.

---

## 2. The Four Roadmap Layers

### 2.1 Software Factory Roadmap
**Owner:** Software Factory governance
**Location:** `software-factory-governance/roadmaps/SOFTWARE_FACTORY_ROADMAP.md`
**Scope:** Governance standards, templates, methodology, CI enforcement, and multi-project maturity.

This roadmap tracks the evolution of the Software Factory itself — not any specific project.
Items here are about making the factory better at building and governing projects.

*Examples: implementing CI governance checks, expanding onboarding standards, launching
the template library, achieving governance maturity Level 4 across all projects.*

### 2.2 Platform Roadmap
**Owner:** Platform engineering team
**Location:** `<platform-repo>/ROADMAP.md`
**Scope:** Shared platform modules, base configurations, and infrastructure that all projects inherit.

This roadmap tracks improvements to the shared platform layer — things that benefit all
projects when delivered.

*Examples: upgrading the Odoo base version, implementing a shared authentication module,
standardizing the backup infrastructure, delivering a shared reporting framework.*

### 2.3 Industry Template Roadmap
**Owner:** Template team / vertical lead
**Location:** `<template-repo>/ROADMAP.md`
**Scope:** Features and improvements specific to a vertical (Oil & Gas, NGO, Hospitality, etc.)
that apply across all client deployments of that template.

*Examples: adding a tank management template module to the Oil & Gas template, adding
donor management to the NGO template, adding room booking to the Hospitality template.*

### 2.4 Client Deployment Roadmap
**Owner:** Project team
**Location:** `<project-repo>/ROADMAP.md`
**Scope:** Features, phases, and milestones specific to a single client deployment.

This is the most granular roadmap. It tracks what has been delivered and what is next
for a specific client — FamOil, WamaCare, NADF, etc.

*Examples: FamOil Phase 2 — procurement and inventory; WamaCare Phase 3 — reporting
and dashboards; NADF Phase 1 — member registration.*

---

## 3. Roadmap Boundary Rules

### 3.1 No Cross-Layer Scope
A client deployment roadmap must not contain items that belong in the platform or
template layer. If a feature would benefit multiple clients, it belongs in the
platform or template roadmap — not in a single client's roadmap.

**Violation example:** FamOil's `ROADMAP.md` includes "Implement shared backup
infrastructure" — this belongs in the Platform Roadmap.

**Correct:** FamOil's `ROADMAP.md` references a Platform Roadmap item as a
dependency: "Depends on: PLATFORM: Shared backup infrastructure."

### 3.2 Dependencies Must Be Declared
When a roadmap item at one layer depends on a roadmap item at another layer, the
dependency must be explicitly declared:

```
## Item: [Feature name]
**Depends on:** PLATFORM: [item name] | TEMPLATE: [item name] | FACTORY: [item name]
```

### 3.3 Completed Items Are Not Deleted
Completed roadmap items are marked `[COMPLETE]` with the completion date. They are
not removed from the roadmap. This preserves the delivery history.

Completed items are additionally recorded in `IMPLEMENTATION_HISTORY.md`.

### 3.4 Deferred Items
Items that were planned but deferred to a later phase must be marked `[DEFERRED]`
with an explanation and the decision log entry reference (if a decision was made).

---

## 4. Roadmap Format

Every roadmap uses the template in `templates/roadmap_template.md`.

Required sections:
- **Summary** — one paragraph describing the scope of this roadmap
- **Current Phase** — what phase is currently active
- **Phase History** — completed phases with dates
- **Upcoming Phases** — planned phases with scope descriptions
- **Backlog** — items identified but not yet assigned to a phase
- **Dependencies** — cross-layer dependencies
- **Last Updated** — date of last roadmap update

---

## 5. Roadmap Maintenance

### 5.1 When to Update
The roadmap must be updated:
- At the start of a new phase.
- When a phase is completed.
- When a significant item is added, deferred, or cancelled.
- In every PR that completes a roadmap item.

### 5.2 Roadmap Review Cadence
- **Software Factory Roadmap:** reviewed at each governance milestone.
- **Platform Roadmap:** reviewed at each platform release.
- **Template Roadmaps:** reviewed at each template version release.
- **Client Deployment Roadmaps:** reviewed at each project phase gate.

### 5.3 AI Agent Responsibility
AI agents must:
- Read the project `ROADMAP.md` before starting any work.
- Not implement items from future phases without explicit user instruction.
- Mark roadmap items as complete in the same PR that delivers them.
- Flag any work requested that appears outside the current roadmap scope.

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
