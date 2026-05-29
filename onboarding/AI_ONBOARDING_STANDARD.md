# AI Agent Onboarding Standard

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects

---

## 1. Purpose

Every time an AI agent begins a new session on a Software Factory project, it starts with
no memory of prior sessions. This standard defines the minimum reading and orientation
protocol that an AI agent must complete before taking any action in a project.

Skipping this protocol leads to: repeated mistakes, contradicted decisions, duplicated
modules, stale documentation, and governance defects. This is the AI equivalent of a
surgeon not reading the patient chart before operating.

---

## 2. Mandatory Onboarding Sequence

An AI agent must complete the following sequence at the start of every new session,
before writing any code, making any changes, or advising on any implementation.

### Step 1 — Read the Governance CLAUDE.md
File: `software-factory-governance/CLAUDE.md`

This is the primary operational instruction set. It defines how AI agents must behave
across all Software Factory projects.

### Step 2 — Read the Project CLAUDE.md
File: `<project-repo>/CLAUDE.md`

This extends the governance instruction set with project-specific context, constraints,
and priorities.

### Step 3 — Read the Implementation History
File: `<project-repo>/IMPLEMENTATION_HISTORY.md`

Understand what has been built, when, and in what state. This prevents re-doing
work that is already done and identifies areas that may have known issues.

### Step 4 — Read the Decision Log
File: `<project-repo>/DECISION_LOG.md`

Understand what decisions have already been made and must not be reversed without
a new decision log entry. This is the single most important document for avoiding
contradictions in AI-assisted work.

### Step 5 — Read the Module Registry
File: `<project-repo>/MODULE_REGISTRY.md`

Understand what custom modules, components, services, integrations, automations,
and scripts already exist. This prevents creating duplicates or missing dependencies.

### Step 6 — Read the Roadmap
File: `<project-repo>/ROADMAP.md`

Understand the current phase scope. Do not implement items from future phases unless
explicitly instructed. Do not propose work that is already complete.

### Step 7 — Confirm Understanding
Before proceeding, the AI agent must briefly summarize:
- The current project phase and scope.
- The most recent implementation history entry.
- Any active decisions from the decision log that are relevant to the current task.
- Any concerns or ambiguities identified during reading.

---

## 3. Mid-Session Re-Orientation

If a session is long and covers multiple areas, the AI agent must re-read the relevant
governance documents before entering a new area of work.

For example: if a session moves from working on inventory to working on security
configuration, the agent must re-read `DECISION_LOG.md` entries related to security
before proceeding.

---

## 4. What AI Agents Must Never Assume

- **Never assume the current state from prior session memory.** Repository state may have changed.
- **Never assume a module does not exist** without checking `MODULE_REGISTRY.md`.
- **Never assume a decision has not been made** without checking `DECISION_LOG.md`.
- **Never assume a phase is in scope** without reading `ROADMAP.md`.
- **Never assume documentation is current** — verify against the actual files.

---

## 5. Handling a Missing or Incomplete Governance Document

If a mandatory governance document (DECISION_LOG.md, MODULE_REGISTRY.md, etc.) is
missing or incomplete in a project repository:

1. Report the missing document to the user.
2. Do not proceed with the current task until the document is initialized.
3. Offer to initialize the missing document using the relevant template from `templates/`.
4. After initialization, complete the normal onboarding sequence.

A missing governance document is a governance defect — it must be fixed, not ignored.

---

## 6. Onboarding Completion Confirmation

At the end of the onboarding sequence, the AI agent must state:

> "I have completed the AI onboarding sequence for [project name].
> Current phase: [phase].
> Most recent implementation: [brief summary].
> Active decisions relevant to this session: [list or 'none identified'].
> I am ready to proceed."

---

## 7. AI Agent Limitations and Escalation

AI agents must flag the following conditions and not proceed without explicit user guidance:

- A decision log entry directly contradicts what the user is asking for.
- A roadmap item is marked as out of scope but the user is asking for it.
- A governance standard requires a review that the AI cannot perform (e.g., a security
  review requiring human judgment).
- The implementation history shows a prior attempt at this task that failed or was deferred.

---

*This standard is owned by the Software Factory. All AI agents operating in Software Factory projects must comply.*
