# Developer Onboarding Standard

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

This standard defines the minimum onboarding requirements for any developer — new or
experienced — joining a Software Factory project. The goal is to ensure that every
developer begins work with accurate knowledge of the project state, the governance
requirements, and the technical context.

A developer who skips onboarding is a risk to the project. This is not a courtesy
guide — it is a requirement.

---

## 2. Before You Write a Single Line of Code

Complete the onboarding checklist in `templates/onboarding_template.md`.

This checklist covers:
1. Governance orientation
2. Project state review
3. Environment verification
4. Technical orientation
5. Governance compliance check

Do not begin any development work until the checklist is complete.

---

## 3. Understanding the Software Factory

### 3.1 What You Are Operating In
The Software Factory is a structured, multi-project development environment. Every project
is governed by shared standards. You are not free to ignore these standards because they
seem heavyweight for a small change.

### 3.2 The Four Layers
```
Software Factory Layer  — governance, standards, methodology
Platform Layer          — shared platform modules and base configs
Industry Template Layer — vertical-specific templates
Client Deployment Layer — per-client projects
```

Know which layer the project you are working on belongs to.

### 3.3 The Governance Repository
The `software-factory-governance` repository contains all standards and templates.
Read `software-factory-governance/README.md` to understand the full structure.

---

## 4. Required Reading (In Order)

1. `software-factory-governance/README.md` — understand the Software Factory
2. `software-factory-governance/CLAUDE.md` — understand the AI and developer operating rules
3. `<project>/README.md` — understand the project
4. `<project>/CLAUDE.md` — understand the project-specific context and constraints
5. `<project>/DECISION_LOG.md` — understand what decisions have been made and why
6. `<project>/IMPLEMENTATION_HISTORY.md` — understand what has been built and the current state
7. `<project>/MODULE_REGISTRY.md` — understand what custom code exists
8. `<project>/ROADMAP.md` — understand what is planned and what is in scope now

---

## 5. Development Standards

### 5.1 All Changes via PR
No direct commits to the main branch. All changes go through a Pull Request using
the template in `templates/pull_request_template.md`.

### 5.2 Decision Logging
If you make an architectural decision — any choice that a future developer could not
reverse without significant effort — log it in `DECISION_LOG.md`.

When in doubt: log it.

### 5.3 Registry Maintenance
If you add a new module, component, service, integration, automation, or script,
add a registry entry in `MODULE_REGISTRY.md` in the same PR.

### 5.4 Documentation Updates
Update documentation in the same PR as the code change. Do not create a separate
"docs PR" that follows weeks later. It will not happen.

### 5.5 Commit Messages
Format: `<type>(<scope>): <short description>`

Examples:
- `feat(purchase): add supplier evaluation scoring`
- `fix(inventory): correct lot expiry date calculation`
- `docs(registry): register supplier_eval_ext module`
- `security(auth): restrict manager menu to managers group`

---

## 6. Working with AI Agents

AI agents (Claude) are used extensively in Software Factory projects. When working
alongside an AI agent:

- Do not ask the AI to skip governance steps to save time.
- Do provide the AI with the relevant governance documents at the start of a session.
- Do verify AI-generated changes against the decision log and registry before accepting.
- Do sign off on the final governance declaration in every PR, even if the AI drafted it.

You are responsible for the code you merge, regardless of who wrote it.

---

## 7. Escalation

Escalate to the Software Factory lead when:
- You discover a governance defect (missing documents, undocumented decisions, unregistered modules).
- You need to make a decision that is outside the scope of the current phase.
- You encounter a security concern.
- A prior decision in the log appears to be wrong and needs to be revisited.

---

## 8. Offboarding

When you finish working on a project:
1. Ensure all open PRs are closed or handed over.
2. Update `IMPLEMENTATION_HISTORY.md` if you completed a milestone.
3. Ensure `DECISION_LOG.md` is current for any decisions you made.
4. Hand over any credentials or access through the proper secret management channels.
5. Brief your replacement or the Software Factory lead on any in-progress work.

---

*This standard is owned by the Software Factory. All developers must comply.*
