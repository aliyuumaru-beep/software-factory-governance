# Architectural Principles

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects

---

## Purpose

These principles are binding guidelines for all architectural decisions across Software
Factory projects. They do not prescribe every implementation detail, but they establish
the non-negotiable constraints within which every architecture must operate.

When a decision conflicts with a principle, log the conflict and the resolution in
`DECISION_LOG.md` before proceeding.

---

## Principle 1 — Platform-Native First

**Use the platform's built-in capabilities before building custom solutions.**

Before writing any custom code, verify that the platform (Odoo, or whatever platform
is in use) does not already provide the required capability natively or through a
supported extension.

Custom code has a cost: it must be maintained, upgraded, and documented. Every line
of custom code is technical debt relative to a native solution.

When a native capability is rejected in favour of custom code, the reason must be
logged in `DECISION_LOG.md` with type `CUSTOM_CODE`.

---

## Principle 2 — Layer Discipline

**Keep each layer's concerns within that layer.**

- Software Factory governance → applies to all projects.
- Platform changes → go in the platform layer, not in a client project.
- Vertical/industry features → go in the industry template, not in a client project.
- Client-specific customizations → go in the client project only.

Cross-layer bleeding (putting platform-level code in a client project for convenience)
creates long-term maintenance debt and prevents other projects from benefiting from
the work. When you find yourself writing something in a client project that would
benefit multiple projects, escalate it to the appropriate layer.

---

## Principle 3 — Reversibility

**Prefer reversible decisions over irreversible ones.**

When two approaches achieve the same goal but one is easier to reverse, prefer the
reversible one unless there is a compelling reason otherwise.

This applies to: database schema choices, module architecture, integration patterns,
and infrastructure decisions.

When an irreversible decision must be made, log it and confirm that the consequences
are understood and accepted.

---

## Principle 4 — Explicit Over Implicit

**Make dependencies, configurations, and behaviours explicit.**

- Explicit module dependencies in manifest files.
- Explicit access control rules, not relied-upon defaults.
- Explicit configuration in documented environment variables, not magic defaults.
- Explicit security decisions in the decision log, not assumed safe.

Implicit behaviour that is not documented is a maintenance risk. Future developers
and AI agents will not discover it — they will break it.

---

## Principle 5 — Separation of Data and Logic

**Keep business data separate from application code.**

- Configuration data (product categories, account codes, tax rules) belongs in the
  database, not hardcoded in Python.
- Master data setup belongs in documented data files or a setup procedure, not in
  a migration script that runs once and is forgotten.
- Business rules that change frequently should be configurable, not hardcoded.

---

## Principle 6 — Fail Loudly

**Errors should be visible and traceable, not silently swallowed.**

- Do not catch exceptions broadly without logging the error.
- Do not return empty results when an error occurred — raise or report the error.
- Integration failures must produce visible alerts, not silent empty responses.
- Background jobs that fail must log their failure somewhere auditable.

---

## Principle 7 — Security by Design

**Security is not added after the fact — it is designed in.**

- Access control is defined before a feature is deployed, not after.
- The minimum viable security posture is applied to every feature from day one.
- Security decisions are logged.
- Secrets are never in code.

See `governance/SECURITY_STANDARD.md` for the full security requirements.

---

## Principle 8 — Idempotent Operations

**Operations that modify state should be safely repeatable.**

Data migrations, setup scripts, configuration installers, and restore procedures
should be designed to be run multiple times without causing duplicate data or
inconsistent state.

An idempotent operation checks the current state before making a change:
"If this already exists, skip it; if it doesn't exist, create it."

---

## Principle 9 — Documented Interfaces

**Any component that another component depends on must have a documented interface.**

- Modules that provide APIs must document those APIs.
- Integrations must document the contract (input format, output format, error behaviour).
- Scheduled actions must document their trigger conditions and what they do.
- Custom models that are used by other models must document their key fields and methods.

---

## Principle 10 — Minimize Custom Code Surface

**The total custom code surface should be kept as small as possible.**

More custom code means more maintenance, more upgrade risk, more documentation burden,
and more failure surface. The goal is always to do the most with the least.

This is not about speed or laziness — it is a deliberate risk management strategy.

See `principles/OVERENGINEERING_GUARDRAILS.md` for the rules that operationalize
this principle.

---

*These principles are owned by the Software Factory. Changes require a PR with an architecture decision log entry.*
