# AOP-014 — Blacklist Recommendation

---

**Document:** AOP-014-04
**Enhancement:** AOP-014 — Development Environment Trust Profile
**Version:** 1.0
**Date:** 2026-06-25

---

## Purpose

This document lists commands that must **never** be pre-approved in Claude Code settings and must
**never** be nominated for "Yes, and don't ask again." Every execution of these commands must
receive explicit, deliberate Human Sponsor approval at the moment of execution.

These are Level C commands: destructive, irreversible, privilege-escalating, or production-touching.

**The blacklist is not advisory. It is a hard constraint on the trust profile.**

---

## 1. The Core Principle

The blacklist exists because these commands share one property: **their blast radius exceeds the
scope of a single work package.** A mistaken `rm -rf` can destroy the entire repository. A
mistaken `dropdb NADF` destroys all production data. A mistaken `git push --force origin main`
can rewrite protected branch history.

No convenience gain from pre-approval is worth the risk of executing these commands unattended.

---

## 2. Destructive Filesystem Operations

| Command | Why Blacklisted |
|---------|----------------|
| `rm -rf <path>` | Recursively and irreversibly deletes files and directories. No undo. |
| `rm -rf *` | Deletes everything in the current directory. Catastrophic if in wrong directory. |
| `rm -r <path>` | Recursive delete without force flag is only marginally safer — still blacklisted. |
| `find . -exec rm {} \;` | Mass deletion via find; pattern could match unintended targets. |
| `find . -delete` | Mass deletion; same risk. |
| `find . -exec rm -rf {} \;` | Equivalent to recursive `rm -rf`; blacklisted. |

---

## 3. Git History and Branch Destructive Operations

| Command | Why Blacklisted |
|---------|----------------|
| `git push --force` | Overwrites upstream history; can destroy commits permanently. |
| `git push -f` | Same as --force. |
| `git push origin main` | Pushes to protected branch; protected branches must never be auto-pushed. |
| `git push origin master` | Same; protected branch. |
| `git reset --hard` | Destroys all uncommitted changes permanently. No undo for uncommitted work. |
| `git reset --hard HEAD~<n>` | Destroys n commits from the branch. |
| `git clean -f` | Irreversibly deletes all untracked files. |
| `git clean -fd` | Irreversibly deletes all untracked files and directories. |
| `git clean -fdx` | Includes ignored files — destroys build artifacts, .env files, etc. |
| `git checkout -- .` | Discards all unstaged changes; no undo. |
| `git checkout -- *` | Discards changes to matching files; no undo. |
| `git branch -D <branch>` | Force-deletes a branch even if unmerged; can destroy work. |
| `git rebase -i *` | Interactive rebase; arbitrarily rewrites history; context-dependent danger. |

---

## 4. Database Destructive Operations

| Command | Why Blacklisted |
|---------|----------------|
| `dropdb <db>` | Drops an entire database. Irreversible. |
| `dropdb NADF` | Drops the NADF production database. Catastrophic. |
| `dropdb Famoil` | Drops the FamOil production database. Catastrophic. |
| `dropdb wamacare_local` | Drops the WamaCare database. |
| `psql -c "DROP DATABASE *"` | SQL-level database drop. |
| `psql -c "DROP TABLE *"` | Drops a table; data loss; schema destruction. |
| `psql -c "DROP SCHEMA *"` | Drops an entire schema; cascades to all tables. |
| `psql -c "TRUNCATE *"` | Empties a table; data loss; not easily reversible in production. |
| `psql -c "DELETE FROM *"` | Deletes records; scope depends on WHERE clause; blacklisted due to risk. |
| `pg_restore -d NADF *` | Overwrites production database with backup; may replace current state. |
| `psql -d NADF -c "INSERT *"` | Production DB insertion; any production DB mutation is Level C. |
| `psql -d NADF -c "UPDATE *"` | Production DB update; always Level C. |
| `psql -d NADF -c "DELETE *"` | Production DB deletion; always Level C. |
| `psql -d Famoil -c *` (mutating) | FamOil production DB mutation; always Level C. |

---

## 5. Privilege Escalation

| Command | Why Blacklisted |
|---------|----------------|
| `sudo <any-command>` | Superuser escalation; any command run as root can have unbounded blast radius. |
| `sudo su` | Full root shell; no limits on what can be executed. |
| `sudo -s` | Same as `sudo su`. |
| `su <user>` | User switch; could be used to escalate to root or access other user data. |

**Policy:** `sudo` is blacklisted as a prefix pattern, not per-command. There are no `sudo` commands
that are safe to pre-approve. Every `sudo` execution requires explicit Human Sponsor confirmation.

---

## 6. Security and Credential Operations

| Command | Why Blacklisted |
|---------|----------------|
| `passwd` | Changes the current user's password. |
| `chpasswd` | Bulk password change. |
| Any modification to `~/.ssh/` | SSH key changes could lock out access or grant unauthorized access. |
| Any modification to credential files (`.env`, `secrets.*`) | Credential file changes; sensitive by definition. |
| `openssl genrsa` / `openssl req` (production cert) | Certificate generation for production. |
| `chmod 777 <file>` | Opens insecure permissions; security vulnerability. |
| `chmod -R 777 <path>` | Mass permission change to world-writable; security disaster. |
| `chmod -R <mode> <path>` | Any recursive permission change requires approval. |

---

## 7. Firewall and Network Security

| Command | Why Blacklisted |
|---------|----------------|
| `ufw allow *` | Opens firewall port; security impact. |
| `ufw deny *` | Closes firewall port; could lock out services. |
| `ufw enable` / `ufw disable` | Enables/disables firewall entirely. |
| `iptables *` | Any iptables change; firewall rules. |
| `firewall-cmd *` | Any firewalld change. |
| `pfctl *` | macOS packet filter; firewall changes. |

---

## 8. Process Force-Kill and Mass Kill

| Command | Why Blacklisted |
|---------|----------------|
| `kill -9 <pid>` | Force-kills a process; no graceful shutdown; data loss risk. |
| `killall <name>` | Kills all processes matching name; mass kill risk. |
| `pkill -9 *` | Force-kills processes matching pattern. |

---

## 9. System Package Management

| Command | Why Blacklisted |
|---------|----------------|
| `brew install <pkg>` | System-level package change; may alter PATH, libraries, or system tools. |
| `brew uninstall <pkg>` | Removes system package; may break dependencies or tools. |
| `brew upgrade <pkg>` | Upgrades system package; may introduce incompatibilities. |
| `apt install <pkg>` | System package installation. |
| `apt remove <pkg>` | System package removal. |
| `apt-get *` | Any apt-get operation. |
| `pip install --upgrade *` | Upgrades Python packages; may break existing code. |
| `pip uninstall *` | Removes Python packages; may break dependencies. |

---

## 10. Production Deployment and Remote Operations

| Command | Why Blacklisted |
|---------|----------------|
| `ssh <any-host>` | Opens remote session; scope is unknown without Human review. |
| `scp <src> <remote>:*` | Copies files to remote; may affect production. |
| `rsync * <remote>:*` | Syncs to remote; may overwrite production files. |
| Any production deployment script | Production impact; always Level C. |
| Any production rollback script | Production impact; always Level C. |

---

## 11. Odoo Production Operations

| Command | Why Blacklisted |
|---------|----------------|
| `odoo-bin -i <module> -d NADF` | Installs module in production NADF. |
| `odoo-bin -u <module> -d NADF` | Upgrades module in production NADF. |
| `odoo-bin -d NADF` (server start with prod DB) | Starts Odoo against production; any startup may trigger migrations. |
| `scripts/restore_nadf.sh` (NADF target) | Restores over production NADF database. |

---

## Blacklist Summary

**Categories: 11**
**Total command patterns blacklisted: ~50**

The blacklist is defined by five underlying principles:

| Principle | Commands Covered |
|-----------|-----------------|
| Irreversibility | `rm -rf`, `dropdb`, `git reset --hard`, `git clean -fd` |
| Production contact | All NADF/Famoil production DB mutations, production deployment scripts |
| Privilege escalation | All `sudo`, `su` |
| History rewriting | `git push --force`, `git rebase -i`, `git branch -D` |
| Security posture | Firewall, credentials, permissions |

---

## A Note on "Conditional" Blacklisting

Some command patterns are Level B for safe targets and Level C for production targets:

| Command | Level B Context | Level C Context |
|---------|-----------------|-----------------|
| `psql -c "UPDATE ..."` | `-d nadf_drill` | `-d NADF` |
| `pg_restore -d *` | `-d nadf_drill` | `-d NADF` |
| `odoo-bin -i *` | Non-production DB | Production DB |
| `scripts/restore_nadf.sh` | Drill target | NADF target |

In these cases, the **target database or system is the classification determinant**, not the command
itself. The safest approach is to classify the whole command as Level B and rely on the one-time
approval to catch production targets — the Human Sponsor can read the command and see the target
before approving.

---

*AOP-014 Blacklist Recommendation — A1 Master Orchestrator — 2026-06-25*
