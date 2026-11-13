# SPEC-GOV-ENF-001 — Enforced Governance Gateway

**Status:** ACTIVE (pending sponsor merge). Implemented 2026-11-13 per the sponsor directive of the same day; G1–G3 review rounds 1–2 recorded in IMP-009.
**Owner:** Sponsor (Aliyu Umaru)
**Decision:** DEC-013 (DEC-GOV-ENF-001), see `DECISION_LOG.md`

## 1. Problem

The Software Factory defines governance roles (A1, D1–D4, G1–G3), escalation
categories (E1–E6) and standards, but on 2026-11-12/13 an audit found that
**nothing enforced them**:

- G1/G2/G3 existed only as prompt text; past gate reports were written by the
  same agent that did the build ("Reviewer: A1 Master Orchestrator").
- Project hooks only loaded when Claude Code was started inside the project
  folder; a session started in `~` bypassed all of them.
- `main` branch protection required 0 approvals and no status checks, so a
  human or AI could merge without any review or test.
- A whole feature (NADF Facilities Management, PR #14) was built, pushed and
  applied to the live database without spec, review or governance records.

The sponsor directive: **every session on every Software Factory project — AI
or human, direct or AI-assisted — must be routed through the governance
gateways and must be forced to fire up the governance reviewers.**

## 2. Design principle

Enforcement is layered. Local layers give early, helpful feedback; the
server-side layer is the one that cannot be bypassed.

| Layer | Who it binds | Bypassable? | Mechanism |
|-------|--------------|-------------|-----------|
| L1 Claude Code user-level hooks | Every Claude Code session on this machine, whatever folder it starts in | Only by editing `~/.claude/settings.json` | `gov hook pre-tool / session-start / stop` |
| L2 Project bootstrap hooks | Claude Code on a machine where L1 is not installed | Only by editing the repo (which L4 sees) | `.claude/settings.json` in each repo blocks writes until `install.sh` is run |
| L3 Git hooks | Human developers (any editor, any AI tool) | Yes (`--no-verify`) — advisory | `core.hooksPath` → `gov githook` |
| L4 GitHub ruleset + `governance / gate` check | Everyone, including repo admins | **No** (no bypass actors) | Reusable workflow in this repo runs docs gate + G1/G2/G3 as independent Claude instances |

## 3. Requirements

R1 **Governed repo detection.** A repo is governed if it contains
`.governance.json`. A git repo whose `origin` belongs to a configured owner
(`aliyuumaru-beep`) but has no `.governance.json` is *un-onboarded*: writes to
it are blocked until `gov onboard` is run.

R2 **Briefing gate.** Before the first write to a governed repo in a session,
the session must have read every file in `briefing_docs` (pod `CLAUDE.md`,
project state, next action, approval register).

R3 **Branch gate.** No commits or file edits on a protected branch (`main`).

R4 **No spec, no code.** Edits or commits touching `code_paths` require a
branch ticket (`gov start <WORK-ITEM>`) whose ID (WP-/DEC-/SPEC-…) exists in
the repo's spec sources.

R5 **Live-data gate.** Commands that can mutate a database listed in
`live_databases` (`odoo-bin -u/-i/shell`, write SQL via `psql`, `pg_restore`,
`dropdb`) require a backup younger than `backup_max_age_hours` and then an
explicit user confirmation (Claude `ask`).

R6 **Independent reviews.** `gov review` runs G1, G2 and G3 as **separate
headless Claude Code processes** with read-only tools. Verdicts are stored
per commit; a new commit invalidates them. The building session cannot write
verdict files (hook-blocked).

R7 **Ship gate.** `git push` and `gh pr create` require: not a protected
branch, branch ticket present, required governance docs updated (when code
changed), and APPROVED / APPROVED WITH CONDITIONS from G1, G2, G3 for HEAD.
`gh pr merge` always asks the user. Force-push is denied.

R8 **Server gate.** Every PR runs `governance / gate`:
docs gate (R4 + required doc updates) then G1/G2/G3 in CI. REJECTED or
ESCALATE fails the gate unless the sponsor adds the `sponsor-override` label
(recorded in the PR). `main` rulesets require this check, block force-push
and deletion, and have **no bypass actors**.

R9 **Audit trail.** Every deny/ask decision is appended to
`~/.claude/governance/logs/decisions.jsonl`; hook errors are logged and
reported at the next session start (hooks fail open, never brick a session).

R10 **New projects.** `gov onboard` writes `.governance.json`, the CI caller
workflow, the Claude bootstrap hooks, `AGENTS.md` (for non-Claude AI tools)
and installs the git hooks. `gov protect` applies the GitHub ruleset.

## 4. Known limits (accepted)

- L1–L3 inspect commands heuristically; an actor determined to evade local
  hooks can. L4 is the guarantee: nothing reaches `main` without the gate.
- A human with direct database access can still change a live database
  outside Git. Mitigation is operational (separate DB roles), tracked as a risk.
- In the governance repo itself the gate runs the PR's own copy of the workflow. Other repos run an
  immutable release tag (`gate-v1`; tag ruleset `software-factory-gate-tags`, no bypass) and receive only
  the two reviewer secrets, never `secrets: inherit` (G3 E3 finding on the first review round).
- `GOV_ALLOW_INSTALL=1` lets the user's own shell (or the test suite) run `install.sh` past R9. A Claude
  session cannot set it for its hook process.
- Command inspection is text-based: a command that merely mentions a protected path while also running
  an interpreter is refused (false positives are accepted; use the dedicated file tools instead).
- R5 treats `psql` as mutating unless it is `-l` or a `-c` command with no write SQL and no input
  redirect, so `psql DB < file`, piped SQL, heredocs and `-f` all need a backup and confirmation
  (fail safe; a read-only `-c` that contains `<` asks unnecessarily).
- The gate *workflow file* is pinned at `gate-vN` for child repos, but the *engine* it runs
  (`govcore.py`, reviewer prompts) is checked out from this repo's `main`. A merged engine change
  applies to every child repo at once, without a tag bump; `main` here is itself gated by G1–G3 and
  the sponsor's merge. This is commented at both checkout steps in `governance-gate.yml`.
- Reviewer prompts include the PR title and the first 4,000 characters of the PR body, so a PR author
  can attempt prompt injection. Mitigations: reviewers run with no write tools, each reviewer reads
  the diff and files itself, only the last strict `VERDICT:` line counts, and a REJECTED/ESCALATE can
  only be overridden by the sponsor's `sponsor-override` label.
- The L2 bootstrap hook (machines without the gateway) is a fence, not a security boundary. Its
  allowlist permits `git show`, `git clone <any URL>` and `bash <path>/software-factory-governance/
  enforcement/install.sh` (any directory). Compound commands, redirects and substitutions are refused,
  so a clone cannot be chained into execution in one command. L4 is the guarantee.

## 5. Acceptance

- `enforcement/tests/test_gov.py` passes (hook decisions for each requirement, the L2 bootstrap and L3 git hooks).
- A session started in `~` is blocked from editing NADF code until briefed and ticketed.
- A PR without G1–G3 approval cannot be merged into `main` by the admin.
