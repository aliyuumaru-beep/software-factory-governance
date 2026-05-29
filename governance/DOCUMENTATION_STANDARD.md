# Documentation Standard

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects

---

## 1. Purpose

Documentation is not optional. It is a first-class deliverable, treated with the same
importance as working code. The purpose of this standard is to define what documentation
is required, how it must be maintained, and what constitutes a documentation defect.

The primary consumers of project documentation are:
1. AI agents onboarding to a new project session.
2. Developers joining a project mid-flight.
3. The project team performing maintenance or auditing compliance.
4. Future projects inheriting patterns from this project.

---

## 2. Required Documentation Per Project

| Document | Location | Purpose |
|----------|----------|---------|
| `README.md` | Root | Project overview, architecture, setup, usage |
| `CLAUDE.md` | Root | AI agent instruction set |
| `CHANGELOG.md` | Root | Version history of deliveries |
| `DECISION_LOG.md` | Root | Architectural and governance decisions |
| `IMPLEMENTATION_HISTORY.md` | Root | Delivery milestones and operational events |
| `MODULE_REGISTRY.md` | Root | Inventory of all custom artifacts |
| `ROADMAP.md` | Root | Current and planned project phases |
| `docs/` | Root | Technical documentation for specific topics |

---

## 3. Documentation Update Rules

### 3.1 Same-PR Rule
Documentation must be updated in the **same PR** as the code change it describes.
A PR that adds a new module without updating `MODULE_REGISTRY.md` and relevant
`docs/` files is incomplete and must not be merged.

### 3.2 No Stale Documentation
Documentation that describes code, configuration, or behaviour that no longer exists
or has changed is a governance defect. The PR that changes the behaviour must update
the documentation.

### 3.3 AI Agent Compliance
AI agents must not declare a PR complete unless all documentation impacted by the
change has been updated. This is a hard stop — not a suggestion.

---

## 4. README.md Requirements

Every project `README.md` must contain:

1. **Project Name and Description** — what this project is and who it is for.
2. **Technology Stack** — platform, version, key dependencies.
3. **Architecture Summary** — the high-level structure, enough to orient a new reader.
4. **Setup and Installation** — how to run the project locally or in staging.
5. **Module Overview** — brief description of each major custom module.
6. **Governance Links** — links to `DECISION_LOG.md`, `ROADMAP.md`, `MODULE_REGISTRY.md`.
7. **Current Status** — what phase the project is in, what is complete.

---

## 5. CLAUDE.md Requirements

Every project `CLAUDE.md` must contain:

1. **Governance inheritance declaration** — "This project is governed by the Software Factory Governance Standard."
2. **Link to the governance `CLAUDE.md`** — AI agents must read the governance file first.
3. **Project-specific context** — what makes this project different from others.
4. **Current phase and status** — where the project is in its roadmap.
5. **Known sensitive areas** — parts of the codebase requiring extra care.
6. **Out-of-scope list** — what should NOT be touched or assumed.
7. **Key decision summary** — the 3–5 most important decisions from `DECISION_LOG.md`.

---

## 6. Code Documentation Rules

### 6.1 Comments Are Not Substitutes for Governance Documents
Inline code comments do not substitute for registry entries, decision log entries, or
implementation history entries.

### 6.2 When to Write a Comment
Write a comment only when the **why** is non-obvious: a hidden constraint, a
workaround for a known bug, or behaviour that would surprise a future reader.

### 6.3 What Not to Comment
- Do not comment what the code does — the code itself should do that.
- Do not write comments referencing external tickets, issues, or conversations.
- Do not write multi-paragraph comment blocks.

---

## 7. Documentation Quality Standards

### 7.1 Completeness
A document is complete when a person unfamiliar with the project can understand its
subject without needing to read the code.

### 7.2 Accuracy
Every statement in a document must reflect the current state of the system.
Out-of-date statements must be corrected immediately.

### 7.3 Clarity
Write for a technically capable reader who does not know this project. Avoid jargon
that is not defined, acronyms that are not expanded on first use, and unexplained
system names.

### 7.4 Brevity
Documents should be as short as they can be while remaining complete. Avoid padding,
repetition, and explanations of things that are obvious.

---

## 8. Documentation Review

Documentation changes are reviewed as part of the PR review process. Reviewers must
verify that documentation updates accurately describe the changes being made — not just
that some documentation was written.

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
