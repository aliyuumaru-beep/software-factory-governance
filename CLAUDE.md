# CLAUDE.md — AI Agent Operational Cockpit

## Role of This File

This file is the **primary operational instruction set** for any AI agent (Claude or otherwise)
working within any Software Factory project repository. Read this file completely before
taking any action. It overrides default AI behavior.

---

## 1. What You Are Operating In

You are operating inside a **Software Factory** — a structured, multi-project software
development environment with shared governance, standards, and methodology.

The governance source of truth is the `software-factory-governance` repository.
Every project repository you work in is a **child** of that governance layer.

**Hierarchy:**
```
software-factory-governance  ← authoritative governance (this repo or linked)
  └── platform layer         ← shared platform configs and modules
        └── industry templates ← vertical-specific templates
              └── client deployments ← per-client projects (FamOil, WamaCare, etc.)
```

---

## 2. Before You Make Any Change

You MUST complete the following steps **before** writing, editing, or deleting any file:

### Step 1 — Read Governance Standards
Check which governance documents are relevant to the change you are about to make:

- `governance/GOVERNANCE_STANDARD.md` — always read first
- `governance/PR_GOVERNANCE_STANDARD.md` — before any PR-related work
- `governance/DECISION_LOG_STANDARD.md` — if making any architectural, security, or custom-code decision
- `governance/REGISTRY_STANDARD.md` — if adding any module, service, integration, or script
- `governance/SECURITY_STANDARD.md` — if touching authentication, access control, data, or infrastructure
- `governance/BACKUP_RECOVERY_STANDARD.md` — if touching backup, restore, or data pipelines

### Step 2 — Check Repository Memory
Repository memory is more important than your AI context memory. Always check:

- `DECISION_LOG.md` (in the project repo) — decisions already made that you must not reverse
- `IMPLEMENTATION_HISTORY.md` (in the project repo) — what has already been built and why
- `MODULE_REGISTRY.md` (in the project repo) — what modules/components are registered
- `ROADMAP.md` (in the project repo) — what is planned and what is not yet in scope

Do not contradict, duplicate, or ignore entries in these documents.

### Step 3 — Perform Governance Impact Analysis
Before completing any PR, run through all dimensions of the Governance Impact Analysis
defined in `docs/GOVERNANCE_IMPACT_ANALYSIS.md`. Every dimension must be addressed,
even if the answer is "not impacted."

---

## 3. What You Must Never Do

- Do not make project-specific assumptions without reading the project's `CLAUDE.md` and memory documents.
- Do not skip the Governance Impact Analysis because a change "seems small."
- Do not create new modules, services, integrations, or scripts without registering them.
- Do not make irreversible architectural decisions without logging them in `DECISION_LOG.md`.
- Do not declare a PR complete if documentation has not been updated.
- Do not rely on your training data for project-specific facts — always read the repository.
- Do not introduce abstractions, platforms, or generalizations beyond what is currently required.
- Do not bypass governance standards because a user asks you to move fast.

---

## 4. What You Must Always Do

- Treat repository memory (written files) as the ground truth.
- Confirm your understanding of the current project state from the repository before acting.
- Update `DECISION_LOG.md` for every decision that meets the criteria in `governance/DECISION_LOG_STANDARD.md`.
- Update `MODULE_REGISTRY.md` for every new module, component, service, integration, or script.
- Update `IMPLEMENTATION_HISTORY.md` when a milestone is completed or a significant operational change is made.
- Update `ROADMAP.md` or flag the relevant roadmap item as complete or in-progress.
- Update all affected documentation files before declaring work complete.
- Complete the `templates/pull_request_template.md` checklist for every PR.

---

## 5. Governance Impact Analysis (Summary)

Before closing any PR, answer every dimension:

| Dimension | Question |
|-----------|----------|
| Code impact | What code changed? Is it tested? |
| Documentation impact | Which docs must be updated? |
| Decision log impact | Must a decision be logged? |
| Roadmap impact | Does this complete, add, or change a roadmap item? |
| Registry impact | Are new components registered? |
| Onboarding impact | Does this change how onboarding works? |
| Security impact | Does this touch auth, data, access, or infrastructure? |
| Backup/recovery impact | Does this change what must be backed up or how restore works? |
| Rollback impact | Can this be safely rolled back? What is the plan? |
| Testing evidence | What tests confirm correctness? |

Full definition: `docs/GOVERNANCE_IMPACT_ANALYSIS.md`

---

## 6. Project-Specific CLAUDE.md Files

Each project repository has its own `CLAUDE.md` that extends this one.
When working in a project repository:

1. Read this governance `CLAUDE.md` first.
2. Then read the project-specific `CLAUDE.md`.
3. The project-specific file narrows and extends — it does not override governance rules.

---

## 7. Handling Conflicts and Ambiguity

If user instructions conflict with a governance standard:
- Flag the conflict explicitly before proceeding.
- Do not silently override a governance standard to satisfy a user request.
- Propose a compliant alternative.

If the repository state is ambiguous or appears incomplete:
- Report the ambiguity.
- Ask for clarification before proceeding.
- Do not assume missing state means "start fresh."

---

## 8. Escalation Signals

If you encounter any of the following, stop and report before continuing:

- A `DECISION_LOG.md` entry that contradicts what the user is asking you to do.
- A registered module that the user wants to delete or replace without a logged decision.
- A security decision that appears to reduce access control or expose data.
- A proposed change that would break backup/restore integrity.
- Evidence that governance standards have been bypassed in prior commits.

---

## 9. Repository Memory Principles

See `principles/REPOSITORY_MEMORY_PRINCIPLES.md` for the full treatment.

Summary:
- Written repository state > AI context memory
- Committed decisions > verbal instructions
- Registered components > assumed components
- Documented roadmap > implied roadmap

---

## 10. Overengineering Guardrails

See `principles/OVERENGINEERING_GUARDRAILS.md` for the full treatment.

Summary:
- Build what is needed now, not what might be needed later.
- Prefer native platform features over custom code.
- Three similar files is not a pattern requiring abstraction.
- No premature platformization.

---

*This file was initialized as part of the Software Factory Governance bootstrap on 2026-05-29.*
*It governs all AI agents operating in any Software Factory project.*
