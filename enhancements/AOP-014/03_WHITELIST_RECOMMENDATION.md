# AOP-014 — Whitelist Recommendation

---

**Document:** AOP-014-03
**Enhancement:** AOP-014 — Development Environment Trust Profile
**Version:** 1.0
**Date:** 2026-06-25

---

## Purpose

This document lists the commands recommended for permanent pre-approval ("Yes, and don't ask again"
configured to persist in Claude Code settings) across all Software Factory pods.

These are Level A commands: read-only, trivially reversible, or structurally safe regardless of context.
Approving them unconditionally does not create risk; not approving them creates friction for no benefit.

---

## Section 1 — Git Read-Only Operations

These commands inspect repository state and produce no side effects under any circumstances.

| Command Pattern | Reason to Whitelist |
|----------------|---------------------|
| `git status` | Zero-risk; essential for every commit cycle |
| `git status --short` | Same |
| `git diff` | Read-only comparison |
| `git diff HEAD` | Read-only |
| `git diff --staged` | Read-only |
| `git diff *...HEAD` | Read-only |
| `git log` | Read-only history |
| `git log --oneline *` | Read-only |
| `git log --graph *` | Read-only |
| `git log --all *` | Read-only |
| `git branch` | Lists branches; no side effects |
| `git branch -v` | Read-only |
| `git branch -r` | Read-only remote listing |
| `git remote -v` | Read-only |
| `git stash list` | Read-only |
| `git show *` | Read-only commit inspection |
| `git ls-files` | Read-only |
| `git tag -l` | Read-only |
| `git fetch` | Downloads refs; no working tree changes |
| `git fetch --prune` | Cleans stale remote refs only |

---

## Section 2 — Git Safe Write Operations

These commands produce reversible state changes. The reverse action is always available.

| Command Pattern | Reason to Whitelist | Reverse Action |
|----------------|---------------------|----------------|
| `git add *` | Staging; always reversible | `git restore --staged` |
| `git add -p` | Selective staging; reversible | `git restore --staged` |
| `git restore --staged *` | Unstages files; safe | Re-add if needed |
| `git stash` | Saves uncommitted work; reversible | `git stash pop` |
| `git stash pop` | Restores stash; reversible | `git stash` |
| `git commit *` | Creates commit; revertable | `git revert` |
| `git switch *` | Switches branch; no data loss on clean tree | Switch back |

Note: `git commit --amend` is NOT whitelisted — it rewrites history and requires context-awareness.

---

## Section 3 — Filesystem Read Operations

All read-only filesystem commands. No side effects.

| Command Pattern | Reason to Whitelist |
|----------------|---------------------|
| `ls *` | Directory listing; read-only |
| `find * -name *` | Search; read-only |
| `find * -type f *` | Search; read-only |
| `grep *` | Pattern search; read-only |
| `grep -r *` | Recursive search; read-only |
| `grep -n *` | Line number search; read-only |
| `cat *` | File content; read-only |
| `head *` | File head; read-only |
| `tail *` | File tail; read-only (note: `tail -f` is streaming but still read-only) |
| `wc *` | Word/line count; read-only |
| `du -sh *` | Disk usage; read-only |
| `pwd` | Working directory; read-only |
| `which *` | Command path lookup; read-only |
| `type *` | Command type lookup; read-only |
| `env` | Environment; read-only |
| `printenv *` | Env variable; read-only |
| `echo *` | Output only (without file redirect) |
| `mkdir -p *` | Creates directories; non-destructive |
| `touch *` | Creates empty file or updates timestamp; non-destructive |

---

## Section 4 — Python and Testing

| Command Pattern | Reason to Whitelist |
|----------------|---------------------|
| `python --version` | Version check; read-only |
| `python3 --version` | Version check; read-only |
| `python -c "print(*)"` | Safe print expressions |
| `python -c "import *"` | Module inspection; read-only |
| `python scripts/ci_validate.py` | CI validation; read-only output |
| `pytest` | Runs tests; read-only results |
| `pytest *` | Any pytest invocation (assumes tests do not mutate production DB) |
| `python -m pytest *` | Same |
| `python -m flake8 *` | Linting; read-only |
| `python -m pylint *` | Linting; read-only |
| `python -m mypy *` | Type checking; read-only |
| `pip list` | Package list; read-only |
| `pip show *` | Package info; read-only |
| `pip freeze` | Package versions; read-only |

---

## Section 5 — Odoo Read-Only Operations

| Command Pattern | Reason to Whitelist |
|----------------|---------------------|
| `*/odoo-bin --stop-after-init *` | Module load check; exits cleanly; no DB mutations |
| `*/odoo-bin shell *` | Launches shell; no mutations until commands run inside |

**Important note on `odoo-bin shell`:** The shell launch itself is Level A. Individual Python commands
run inside the shell are classified separately per Category 4 of the matrix. Whitelisting the shell
launch does not whitelist the commands run inside it.

---

## Section 6 — PostgreSQL Read-Only Operations

| Command Pattern | Reason to Whitelist |
|----------------|---------------------|
| `psql --version` | Version check; read-only |
| `psql -l` | Lists databases; read-only |
| `psql * -c "SELECT *"` | SELECT query; read-only |
| `psql * -c "\dt"` | Table listing; read-only |
| `psql * -c "\di"` | Index listing; read-only |
| `psql * -c "\d *"` | Table description; read-only |
| `psql * -c "EXPLAIN *"` | Query plan; read-only |
| `pg_dump *` | Database backup; non-destructive |
| `pg_restore --list *` | Lists backup contents; read-only |

---

## Section 7 — Process and System Inspection

| Command Pattern | Reason to Whitelist |
|----------------|---------------------|
| `ps` | Process list; read-only |
| `ps aux` | Full process list; read-only |
| `pgrep *` | Process search; read-only |
| `lsof -i *` | Port inspection; read-only |
| `netstat *` | Network connections; read-only |
| `ss -tlnp` | Socket stats; read-only |
| `uname -a` | System info; read-only |
| `sw_vers` | macOS version; read-only |
| `df -h` | Disk usage; read-only |
| `vm_stat` | Memory stats; read-only |

---

## Section 8 — NADF Backup Scripts

| Command Pattern | Reason to Whitelist |
|----------------|---------------------|
| `scripts/backup_nadf.sh` | Creates DB backup; non-destructive; required pre-condition for EA-5 |

---

## Section 9 — GitHub CLI (Read-Only)

| Command Pattern | Reason to Whitelist |
|----------------|---------------------|
| `gh pr list *` | Lists PRs; read-only |
| `gh pr view *` | Views PR; read-only |
| `gh issue list *` | Lists issues; read-only |
| `gh api * -X GET *` | Read-only API call |
| `gh status` | GitHub status; read-only |

---

## Whitelist Summary

**Approximate total commands whitelisted: 80–90 command patterns**

All are in one of these categories:
1. Pure read-only (git inspect, filesystem read, psql SELECT, pg_dump, ps, etc.)
2. Safe write with immediate simple reversal (git add, git stash, git commit, git switch)
3. Non-destructive creation (mkdir, touch)
4. Test runners that do not mutate databases

**Excluded from whitelist (despite being low-risk in most contexts):**
- `git push` — state-dependent; Level B
- `git commit --amend` — history-rewriting; Level B
- File write operations (`echo >`, `tee`) — target-dependent; Level B
- `odoo-bin -i` — module install; Level B
- `pip install` — package state change; Level B

---

*AOP-014 Whitelist Recommendation — A1 Master Orchestrator — 2026-06-25*
