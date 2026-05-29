# Repository Memory Principles

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects — especially AI agent sessions

---

## 1. What Is Repository Memory?

Repository memory is the collection of governance documents within a project repository
that record the project's decisions, history, components, and future plans. It is the
persistent, version-controlled knowledge base of the project.

Repository memory consists of:

| Document | What It Remembers |
|----------|--------------------|
| `DECISION_LOG.md` | Why things are the way they are |
| `IMPLEMENTATION_HISTORY.md` | What has been built and what happened operationally |
| `MODULE_REGISTRY.md` | What custom components exist |
| `ROADMAP.md` | What is planned and what has been completed |
| `CHANGELOG.md` | What changed in each version |
| `CLAUDE.md` | How AI agents must operate in this project |

---

## 2. The Priority Hierarchy

When there is a conflict between different sources of information, this hierarchy
determines which source is authoritative:

```
1. Repository memory (committed documents)   ← HIGHEST AUTHORITY
2. Code (actual implementation)
3. Comments and inline documentation
4. Verbal instructions from the current session
5. AI agent context memory                   ← LOWEST AUTHORITY
```

**Consequence:** If an AI agent "remembers" something from a prior session that
contradicts what is written in `DECISION_LOG.md`, the decision log wins.

**Consequence:** If a user verbally says "we decided X" but `DECISION_LOG.md` records
a different decision, the decision log is the authoritative version until a new entry
is added.

---

## 3. Repository Memory Over AI Memory

AI agents operate in sessions. Each session starts with no memory of prior sessions.
This means:

- An AI agent cannot reliably recall what it built in a prior session.
- An AI agent cannot reliably recall what decisions were made in a prior session.
- An AI agent cannot reliably recall what the user said in a prior session.

Repository memory solves this problem. When an AI agent reads the governance documents
at the start of a session, it regains project context that would otherwise be lost.

This is why the AI onboarding sequence (see `onboarding/AI_ONBOARDING_STANDARD.md`)
is mandatory — not optional.

---

## 4. Repository Memory Must Be Maintained

Repository memory is only as useful as it is current. A decision log that stops being
updated after Phase 1 provides false confidence — it looks complete but is not.

### 4.1 Obligations

Every developer and AI agent has an obligation to:
- Add decision log entries when decisions are made.
- Update the module registry when components are added or changed.
- Update the implementation history when milestones are reached.
- Update the roadmap when items are completed or plans change.

### 4.2 Stale Memory Is a Governance Defect

A governance document that has not been updated to reflect the current state of the
project is a stale document. Stale documents are governance defects that must be
corrected in the next PR.

An AI agent that discovers stale repository memory must report it before proceeding.

---

## 5. Committed Decisions Supersede Verbal Instructions

A verbal instruction in the current session ("just skip the decision log for this one,
it's quick") does not supersede a governance standard. The governance standard is
written in the repository and is authoritative.

The correct response to such an instruction is:
1. Flag the conflict.
2. Explain what the standard requires.
3. Propose a compliant alternative.
4. Proceed only after the conflict is resolved — either by following the standard or
   by logging a governance exception.

---

## 6. The Repository Is The Truth

When code and documentation disagree, the code reflects what was actually built, but
documentation reflects what was intended. Both are important signals:

- Code reflects *what is*.
- Documentation reflects *what should be* or *why it is that way*.

When they conflict, investigate before assuming either is wrong. The conflict itself
may be the signal of a bug or an undocumented change.

---

## 7. Repository Memory and AI Agents — A Practical Summary

| Scenario | What to Do |
|----------|-----------|
| Starting a new session | Read all mandatory governance documents before acting |
| User says "we already decided X" | Verify in DECISION_LOG.md before accepting as true |
| You want to add a new module | Check MODULE_REGISTRY.md first to avoid duplication |
| User asks you to reverse a decision | Create a new DECISION_LOG.md entry; do not silently reverse |
| You completed a milestone | Add to IMPLEMENTATION_HISTORY.md before closing the session |
| You discover undocumented custom code | Report it as a governance defect; offer to register it |
| Documentation contradicts the code | Report the conflict; investigate before proceeding |

---

*These principles are owned by the Software Factory. They govern all AI agent behavior across all projects.*
