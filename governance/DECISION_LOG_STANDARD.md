# Decision Log Standard

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

The Decision Log is the institutional memory of a project. It records every significant
decision — architectural, technical, security-related, or governance-related — in a way
that future developers and AI agents can understand what was decided, why it was decided,
and what alternatives were considered and rejected.

Without a decision log, the rationale behind the codebase is invisible. Future changes
may unknowingly reverse decisions that were made for important reasons.

---

## 2. When a Decision Must Be Logged

A decision MUST be logged whenever any of the following apply:

### 2.1 Custom Code After Native Option Rejected
A native platform feature (e.g., standard Odoo module, built-in framework capability)
was evaluated and rejected in favour of custom code or a third-party module.

*Example: "We evaluated Odoo's native `purchase.order.line` discount field but it
did not support per-product-category discount schedules, so we built a custom
`purchase_discount_ext` module."*

### 2.2 Architecture Choice
A significant architectural pattern, design approach, or structural decision was made.

*Examples: database schema design, module dependency structure, API integration pattern,
multi-company setup approach, permission inheritance model.*

### 2.3 Security Decision
Any decision that affects access control, data visibility, authentication, authorization,
encryption, audit logging, or external-facing APIs.

*Examples: deciding which users can see which records, choosing an API authentication
method, deciding what data is exposed to a portal user.*

### 2.4 Data Model Decision
A decision about how data is structured, stored, or related — especially decisions that
are hard or costly to reverse.

*Examples: using a many2many vs one2many relation, storing a computed field vs computing
on the fly, adding a custom table vs extending an existing one.*

### 2.5 Integration Pattern
A decision about how two systems are connected, how data flows between them, or what
protocol and error handling approach is used.

*Examples: webhook vs polling, sync vs async, Odoo JSON-RPC vs REST API, file-based
vs database-direct integration.*

### 2.6 Governance Exception
A deliberate deviation from a Software Factory governance standard.

*Examples: skipping the PR template for an emergency hotfix, deferring registry
entry for a temporary script, using a non-standard commit format.*

### 2.7 Major Trade-off
Any decision where a known trade-off was accepted — performance vs. correctness,
simplicity vs. flexibility, speed vs. completeness.

*Examples: accepting eventual consistency for a non-critical report, choosing a simpler
data model knowing it will need to be refactored in Phase 3.*

### 2.8 Technology or Dependency Choice
Choosing a specific library, external service, infrastructure provider, or tool.

*Examples: choosing a specific Python library for PDF generation, selecting a cloud
backup provider, choosing a specific Nginx configuration pattern.*

---

## 3. When a Decision Does NOT Need to Be Logged

Routine implementation details that are obvious from the code and carry no significant
future consequences do not require a log entry.

*Examples: variable naming choices, minor UI layout decisions, standard Odoo field types
for simple data.*

If in doubt, log it. Excess entries in a decision log are far less harmful than missing
entries.

---

## 4. Decision Log Format

Every decision log entry must use the template in `templates/decision_log_template.md`.

Required fields:
- **ID** — sequential identifier (e.g., `DEC-001`)
- **Date** — date the decision was made (ISO 8601: YYYY-MM-DD)
- **Type** — category from section 2 above
- **Status** — `ACTIVE`, `SUPERSEDED`, or `REVERSED`
- **Made By** — who made the decision (person and/or AI agent session)
- **Title** — short title (one sentence)
- **Context** — what problem or situation led to this decision
- **Decision** — what was decided
- **Alternatives Considered** — what else was evaluated and why it was rejected
- **Consequences** — what the decision commits the project to, and any known risks
- **Related Entries** — references to other decision log entries or PR numbers

---

## 5. Decision Log Location

Each project repository maintains its own `DECISION_LOG.md` at the root level.

The Software Factory governance repository maintains a `DECISION_LOG.md` for
governance-level decisions (changes to standards, templates, or governance structure).

---

## 6. Decision Log Maintenance

### 6.1 Adding Entries
Entries are added via PR. The PR that implements a decision must include the
decision log entry in the same commit.

### 6.2 Updating Entry Status
When a decision is reversed or superseded:
- The original entry's status is updated to `SUPERSEDED` or `REVERSED`.
- A new entry is created explaining the reversal and referencing the original.
- The reversal itself requires a new decision log entry (type: `ARCHITECTURE_CHOICE`
  or the most relevant type).

### 6.3 AI Agent Responsibility
AI agents must:
- Read `DECISION_LOG.md` before making or proposing any change in an area it covers.
- Not reverse or work around a logged decision without creating a new log entry.
- Flag to the user when a proposed change would contradict a logged decision.

---

## 7. Decision Types Reference

| Type Code | Description |
|-----------|-------------|
| `CUSTOM_CODE` | Custom code chosen over native option |
| `ARCHITECTURE` | Architectural or structural design choice |
| `SECURITY` | Security, access control, or authentication decision |
| `DATA_MODEL` | Database schema or data structure decision |
| `INTEGRATION` | Integration pattern or API design decision |
| `GOVERNANCE_EXCEPTION` | Deviation from a governance standard |
| `TRADE_OFF` | Accepted trade-off between competing concerns |
| `TECHNOLOGY` | Technology, library, or dependency selection |
| `OPERATIONAL` | Operational procedure or infrastructure decision |

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
