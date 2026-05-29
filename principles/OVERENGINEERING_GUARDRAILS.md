# Overengineering Guardrails

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects

---

## 1. Purpose

Overengineering is one of the most common and costly failure modes in software projects.
It manifests as:
- Building abstractions before they are needed.
- Platformizing features that serve only one project.
- Writing generic frameworks for specific, well-understood problems.
- Adding flexibility for hypothetical future requirements that may never arrive.
- Replacing simple, working solutions with "better" complex ones unnecessarily.

These guardrails define hard rules to prevent overengineering in Software Factory projects.
They exist to protect project velocity, maintainability, and the ability of future
developers and AI agents to understand and modify the codebase.

---

## 2. The Core Rules

### Rule 1 — Build What Is Needed Now

Do not build for hypothetical future requirements. Build what is explicitly needed for
the current phase. If future requirements arrive, refactor then.

**Violation signal:** "We might need this later" / "This is more flexible" /
"What if the client wants..."

**Correct approach:** Build the simple solution. If the requirement does arrive, refactor.
Refactoring a simple solution is almost always faster than maintaining a complex one
that was built for a scenario that never happened.

---

### Rule 2 — Prefer Native Platform Features

Use the platform's built-in features before writing custom code. Odoo provides extensive
native functionality. A native feature that is "80% right" is almost always better than
a custom solution that is "100% right" — because the custom solution requires maintenance
through every upgrade.

**Violation signal:** Writing a custom module when an existing Odoo module would work
with minor configuration.

**Correct approach:** Configure the native feature. If it genuinely cannot meet the
requirement after fair evaluation, log the decision in `DECISION_LOG.md` and build
the minimum necessary custom extension.

---

### Rule 3 — Three Similar Lines Is Not a Pattern

Do not abstract three similar lines of code into a shared function or module without
a clear, immediate use case. Premature abstraction creates indirection without benefit.

**Violation signal:** "I noticed we're doing this in three places, so I created a
utility module..."

**Correct approach:** Let the three occurrences exist. If they grow to five or six,
and the abstraction would genuinely reduce maintenance burden, then refactor — with
a decision log entry.

---

### Rule 4 — No Premature Platformization

Do not extract client-specific features into a platform or template layer until there
is a confirmed second use case. Platform and template code must serve multiple projects
to justify the overhead of maintaining it at a shared layer.

**Violation signal:** "We're building this for FamOil but let's make it generic so
other projects can use it."

**Correct approach:** Build it in FamOil. When WamaCare or another project needs
something similar, evaluate whether platformization makes sense at that point.

---

### Rule 5 — No Excessive Custom Code for Standard Problems

Standard ERP problems have standard ERP solutions. Odoo has been solving these problems
for millions of users. Before writing custom code for purchasing, inventory, accounting,
HR, or any other standard ERP domain — read the Odoo documentation.

**Violation signal:** Writing a custom purchase approval workflow without first
checking Odoo's native three-way approval.

**Correct approach:** Read the native documentation, test the native feature, evaluate
it honestly. Custom code is the last resort, not the first impulse.

---

### Rule 6 — No Half-Finished Abstractions

Do not introduce an abstraction layer, base class, mixin, or shared module unless
it is complete and fully used. Half-finished abstractions that exist "for future use"
are dead weight that confuses future readers and AI agents.

**Violation signal:** A base class with two abstract methods that are only implemented
in one subclass.

**Correct approach:** Write the concrete implementation. When the second subclass
is needed, introduce the abstraction.

---

### Rule 7 — Complexity Must Justify Itself

Every layer of complexity added to the system must justify its existence with a
concrete, measurable benefit. The burden of proof is on complexity, not simplicity.

Questions to ask before adding complexity:
1. What specific problem does this solve that the simpler approach cannot?
2. How often will this complexity be used?
3. How much harder will this make the system to understand for a new reader?
4. How much harder will this make the system to upgrade or maintain?

---

### Rule 8 — Avoid Configuration Explosions

Do not add configuration options for every possible variation of behaviour. Configuration
options have a cost: they must be documented, tested in every combination, and
maintained through upgrades.

Build the behaviour the project needs. If genuinely configurable behaviour is required,
log the decision and build only the configuration options that are needed now.

---

## 3. AI Agent Guardrails

AI agents are particularly prone to overengineering because they have been trained on
a vast corpus of "best practices" that are correct in large-scale contexts but wrong
for a specific project.

AI agents must NOT:
- Introduce abstract base classes without a concrete second use case.
- Create utility modules for functions used only once.
- Add configuration flexibility without explicit user request.
- Recommend "the proper way to build this at scale" when scale is not a stated requirement.
- Refactor working code to make it "more maintainable" without being asked.
- Add error handling for scenarios that cannot happen in the current architecture.
- Create factory patterns, strategy patterns, or similar OOP patterns for straightforward logic.

---

## 4. When These Rules Can Be Broken

These rules are guardrails, not absolute laws. They can be broken when:

1. There is a concrete, current, documented reason why the simpler approach is
   insufficient.
2. The exception is logged in `DECISION_LOG.md` with type `ARCHITECTURE` or `TRADE_OFF`.
3. The user explicitly requests the more complex approach and understands the trade-off.

Breaking these rules without documentation is a governance defect.

---

*These guardrails are owned by the Software Factory. Changes require a PR with a decision log entry.*
