# AOP-014 — Development Environment Trust Profile

---

**Document:** AOP-014-01
**Enhancement:** AOP-014 — Development Environment Trust Profile
**Version:** 1.0
**Date:** 2026-06-25
**Prepared By:** A1 Master Orchestrator

---

## 1. Problem Statement

### 1.1 Observed Friction

The current Claude Code development environment prompts for Human Sponsor approval on every
Bash command execution, regardless of risk level. During active Work Package delivery, this
produces approval interruptions for commands such as:

- `git status` — read-only; zero risk
- `git add` — staging; reversible
- `git commit` — creating a commit; revertable
- `pytest` — running tests; read-only result
- `ls`, `grep`, `cat` — filesystem inspection; no side effects
- `odoo-bin --stop-after-init` — module load check; no DB mutations
- `pg_dump` — creating a backup; non-destructive

These commands require approval **dozens of times per work package session**, creating:

1. **Operational friction**: Human Sponsor is interrupted by routine, low-risk commands
2. **Context loss**: Each approval break interrupts agent execution flow
3. **Approval fatigue**: High frequency of low-stakes approvals reduces attention for high-stakes ones
4. **Unattended execution blockage**: Approved work packages cannot run unattended if every step requires manual approval

### 1.2 The Core Risk

The opposite failure mode is equally important: **if too many commands are pre-approved, destructive
or security-sensitive commands can execute without the human noticing.** A well-calibrated trust
profile maximises developer velocity on the safe commands while hardening the gate on the dangerous ones.

### 1.3 Relationship to AOP-013

AOP-013 governs **what** D2 is authorised to execute (authority classification, governance reviews,
register entries). AOP-014 governs **how the toolchain handles approval prompts** for commands D2
runs during authorised execution. They operate at different layers:

```
AOP-013 (Execution Authority Framework)
  └── Answers: Is this action authorised to execute at all?

AOP-014 (Trust Profile)
  └── Answers: Does this command need a human to click 'Approve' each time?
```

A command granted EA-5 authority under AOP-013 still warrants an approval prompt (Level B or C).
A command auto-approved under AOP-014 is still subject to governance classification if it creates
a significant system change.

---

## 2. Design Principles

### P-01 — Risk Proportionality
Approval friction must be proportional to the actual risk of the command. Read-only commands
and reversible writes should not carry the same friction as destructive or irreversible operations.

### P-02 — Destruction Is Always Gated
No command capable of destroying data, dropping databases, force-overwriting history, or
affecting production systems may be pre-approved under any circumstance.

### P-03 — Privilege Escalation Is Always Gated
Any command that escalates privileges (`sudo`, `su`) or modifies security posture (firewall,
credentials, permissions) is always Level C.

### P-04 — Production Is Always Level C
Any command that operates on a production system, production database, or production configuration
is always Level C, regardless of the command type.

### P-05 — Pod Isolation Preserved
Trust profiles are pod-specific. A command auto-approved in the NADF drill environment is NOT
automatically approved when its target changes to the production NADF database.

### P-06 — Backup Precedes Mutation
Any EA-5 / database-mutating command requires confirmation that a backup exists before execution.
This is not relaxed by trust profile — it is an AOP-013 governance condition (G3-WP03-CON-001
is the first instance of this pattern). Level B database mutation commands require backup
confirmation as part of their approval, not instead of it.

### P-07 — Whitelist Is Conservative by Default
When a command is new or uncertain, classify it as Level B (one-time approval) rather than
Level A (auto-approve). Promote to Level A only after confirming it is genuinely read-only
or trivially reversible.

### P-08 — No Bypass of Git Protection
Protected branches (`main` in all pods) are never auto-approved for push operations.
`git push --force` is Level C in all contexts.

---

## 3. Classification Model

### Level A — Auto Approved

**Definition:** Commands that are read-only, read-mostly, or produce trivially reversible state changes
with no security or data risk. These commands may be pre-configured in Claude Code settings as
always-allowed and should be nominated for "Yes, and don't ask again" during interactive sessions.

**Characteristics:**
- No data destruction possible
- No credential or permission changes
- Reversible in < 1 minute if a mistake occurs
- No production system contact
- No external network call that could exfiltrate data or trigger charges

**Examples:** `git status`, `git diff`, `git log`, `pytest`, `ls`, `grep`, `cat`, `pg_dump` (backup),
`odoo-bin --stop-after-init`, `psql -c "SELECT ..."`, `python scripts/ci_validate.py`

---

### Level B — One-Time Approval Then Persist (Session Scope)

**Definition:** Commands that create meaningful state changes but are scoped to the current approved
work package, are reversible with effort, and have been pre-reviewed under AOP-013 governance.
These commands should be approved once per session (or per work package) via "Yes, and don't ask
again" — but NOT pre-configured as permanently always-allowed in settings.

**Characteristics:**
- Creates lasting state (installs software, writes to DB, creates branch, pushes code)
- Reversible but requires deliberate action (revert, restore, uninstall)
- Scoped to an approved WP or explicit governance decision
- No production system contact
- No destructive side effect IF the pre-conditions (backup, reviewed scope) are met

**Examples:** `odoo-bin -i <approved-module>`, `git push origin feat/*`, `git checkout -b feat/*`,
`pg_restore -d nadf_drill`, `python odoo-shell` EA-5 mutations (within approved WP, after backup)

---

### Level C — Always Require Approval

**Definition:** Commands that are destructive, irreversible, security-sensitive, or that affect
production systems. These commands must NEVER be pre-approved. Each execution requires explicit,
deliberate Human Sponsor approval. "Yes, and don't ask again" must never be used.

**Characteristics:**
- Destroys or irreversibly modifies data
- Affects production systems or credentials
- Escalates privileges
- Cannot be trivially reversed
- Could have blast radius beyond the current work package

**Examples:** `rm -rf`, `sudo`, `dropdb`, `git push --force`, `git reset --hard`,
`git push origin main`, `DROP DATABASE`, `TRUNCATE`, production deployment commands

---

## 4. Pod-Specific Rules

### 4.1 NADF Pod Rules

| Rule | Classification |
|------|---------------|
| Commands targeting DB=NADF (production) | Level C regardless of command type |
| Commands targeting DB=nadf_drill or DB=nadf_test | Level B |
| `scripts/backup_nadf.sh` | Level A (backup creation is non-destructive) |
| `scripts/restore_nadf.sh` with target=nadf_drill | Level B |
| `scripts/restore_nadf.sh` with target=NADF | Level C |
| `odoo-bin shell` (launch only — queries inside) | Level A |
| `odoo-bin shell` with `env.cr.commit()` in approved WP | Level B |
| `odoo-bin -i <module>` approved in MODULE_REGISTRY | Level B |
| `odoo-bin -u <module>` (upgrade) on non-production | Level B |
| `git push origin feat/wp-*` | Level B |
| `git push origin main` | Level C |

### 4.2 FamOil Pod Rules

| Rule | Classification |
|------|---------------|
| Commands targeting DB=Famoil | Level C |
| All other rules | Same as NADF |
| Note: FamOil has not yet reached Level 1 governance | Adopt trust profile when FamOil Wave 1 activates |

### 4.3 WamaCare Pod Rules

| Rule | Classification |
|------|---------------|
| Commands targeting DB=wamacare_local | Level B (local dev DB — not production) |
| Commands targeting any wamacare production DB | Level C |
| Note: WamaCare is isolated from NADF/FamOil | Trust profile applies independently per CLAUDE.md isolation rule |

---

## 5. The "Approval Fatigue" Paradox

The most dangerous failure mode of an over-prompting trust profile is that a Human Sponsor, having
approved 40 low-risk commands in a session, approves the 41st without reading it — and the 41st
is `rm -rf /path/to/production`.

**The trust profile is designed to prevent approval fatigue by removing noise from the approval queue.**
When the only commands that reach the Human Sponsor are Level C commands — genuinely dangerous,
genuinely deliberate decisions — each approval carries appropriate weight and attention.

This is the core argument for a well-calibrated whitelist: **fewer approvals = more attention per approval.**

---

## 6. What This Profile Does NOT Change

| Item | Status |
|------|--------|
| AOP-013 governance authority | Unchanged |
| EA-5 backup requirement (G3-WP03-CON-001 pattern) | Unchanged — backup confirmation is an AOP-013 condition, not a trust profile gate |
| Protected branch protection | Unchanged — Level C applies to all protected branch push operations |
| Production database protection | Unchanged — Level C for all production DB mutations |
| Human Sponsor final authority | Unchanged — trust profile reduces noise, not authority |

---

*AOP-014 Development Trust Profile — A1 Master Orchestrator — 2026-06-25*
