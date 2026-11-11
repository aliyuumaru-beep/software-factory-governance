# AOP-014 — Command Classification Matrix

---

**Document:** AOP-014-02
**Enhancement:** AOP-014 — Development Environment Trust Profile
**Version:** 1.0
**Date:** 2026-06-25

---

## How to Use This Matrix

| Level | Meaning | "Don't Ask Again" |
|-------|---------|-------------------|
| **A** | Auto Approved — pre-configure or click "don't ask again" | ✅ Yes, persist across sessions |
| **B** | One-Time Approval — approve once per session/WP | ⚠️ Session only — do not persist in settings |
| **C** | Always Require Approval — never pre-configure | ❌ Never |

A **†** mark indicates that the command is safe in isolation but may require re-classification
if its flags or arguments change (e.g. `git push` is Level B, but `git push --force` is Level C).

---

## Category 1 — Git Operations

| Command | Level | Rationale |
|---------|-------|-----------|
| `git status` | **A** | Read-only; no side effects |
| `git status --short` | **A** | Read-only |
| `git diff` | **A** | Read-only; no side effects |
| `git diff HEAD` | **A** | Read-only |
| `git diff --staged` | **A** | Read-only |
| `git diff <branch>...HEAD` | **A** | Read-only |
| `git log` | **A** | Read-only |
| `git log --oneline` | **A** | Read-only |
| `git log --graph` | **A** | Read-only |
| `git branch` | **A** | Read-only listing |
| `git branch -v` | **A** | Read-only |
| `git branch -r` | **A** | Read-only remote listing |
| `git remote -v` | **A** | Read-only |
| `git stash list` | **A** | Read-only |
| `git show` | **A** | Read-only |
| `git ls-files` | **A** | Read-only |
| `git tag -l` | **A** | Read-only |
| `git fetch` | **A** | Downloads refs; does not modify working tree or branches |
| `git fetch --prune` | **A** | Cleans stale remote refs; no local changes |
| `git stash` | **A** | Saves uncommitted changes to stash; reversible with `git stash pop` |
| `git stash pop` | **A** | Restores stashed changes; reversible with `git stash` |
| `git stash drop` | **B** | Destroys stash entry; not easily reversible |
| `git add <file>` | **A** | Stages file; reversible with `git restore --staged` |
| `git add .` | **A** | Stages all; reversible with `git restore --staged` |
| `git add -p` | **A** | Interactive patch staging; reversible |
| `git restore --staged` | **A** | Un-stages file; reversible |
| `git commit` | **A** | Creates commit; revertable with `git revert` or amendable |
| `git commit --amend` | **B†** | Rewrites history of last commit; acceptable on feature branch; dangerous on shared branch |
| `git switch <branch>` | **A** | Branch switch; no data loss if working tree clean |
| `git checkout <branch>` | **A** | Branch switch; no data loss if working tree clean |
| `git checkout -b feat/<name>` | **B** | Creates new branch; first-time per branch |
| `git pull` | **B†** | Merges remote; possible conflicts; safe on feature branch, needs care on main |
| `git pull --rebase` | **B†** | Rebases on remote; safe on feature branch |
| `git merge <branch>` | **B†** | Merges branch; possible conflicts; approve per merge operation |
| `git rebase origin/main` | **B†** | Rewrites commits; approve per rebase operation |
| `git push origin feat/<name>` | **B** | Pushes feature branch; approve once per branch per session |
| `git push -u origin feat/<name>` | **B** | Sets upstream + push; approve once per branch |
| `git push --force-with-lease` | **B†** | Safer force push; approve only on feature branch — never on main |
| `git push origin main` | **C** | Pushes to protected branch; always require approval |
| `git push --force` | **C** | Force push; can overwrite upstream commits; always require approval |
| `git push -f` | **C** | Same as --force |
| `git reset --hard` | **C** | Destroys uncommitted changes; always require approval |
| `git reset HEAD~<n>` | **C** | Rewrites branch history; always require approval |
| `git clean -f` | **C** | Destroys untracked files; always require approval |
| `git clean -fd` | **C** | Destroys untracked files + dirs; always require approval |
| `git clean -fdx` | **C** | Destroys untracked + ignored files; always require approval |
| `git checkout -- .` | **C** | Discards all unstaged changes; always require approval |
| `git checkout -- <file>` | **B†** | Discards changes to one file; approve per file per session |
| `git branch -D <branch>` | **C** | Force-deletes a branch; always require approval |
| `git branch -d <branch>` | **B†** | Deletes merged branch; one-time approval |
| `git rebase -i` | **C** | Interactive rebase; can arbitrarily rewrite history; always require |
| `git revert <commit>` | **B†** | Creates a revert commit; approve per operation |
| `git cherry-pick <commit>` | **B†** | Applies commit; approve per operation |
| `git tag <name>` | **B†** | Creates tag; approve per tag |
| `git tag -d <name>` | **B†` | Deletes tag; approve per deletion |

---

## Category 2 — Filesystem Operations

| Command | Level | Rationale |
|---------|-------|-----------|
| `ls` | **A** | Read-only |
| `ls -la` | **A** | Read-only |
| `ls -lah` | **A** | Read-only |
| `find . -name "*.py"` | **A** | Read-only search |
| `find . -name "*.md"` | **A** | Read-only search |
| `grep <pattern> <file>` | **A** | Read-only |
| `grep -r <pattern> .` | **A** | Read-only recursive search |
| `cat <file>` | **A** | Read-only |
| `head -n <N> <file>` | **A** | Read-only |
| `tail -n <N> <file>` | **A** | Read-only |
| `tail -f <logfile>` | **A** | Read-only streaming |
| `wc -l <file>` | **A** | Read-only |
| `du -sh <path>` | **A** | Read-only |
| `pwd` | **A** | Read-only |
| `which <command>` | **A** | Read-only |
| `type <command>` | **A** | Read-only |
| `echo <text>` | **A** | No side effects (output only, no redirect to file) |
| `echo <text> > <file>` | **B†** | Writes to file; approve per write; overwrites target |
| `echo <text> >> <file>` | **B†** | Appends to file; approve per write |
| `tee <file>` | **B†** | Writes to file; approve per write |
| `mkdir -p <path>` | **A** | Creates directory; non-destructive |
| `touch <file>` | **A** | Creates empty file or updates timestamp; non-destructive |
| `cp <src> <dst>` | **B†** | Copies file; approve when overwriting existing file |
| `mv <src> <dst>` | **B†` | Moves/renames file; approve per move operation |
| `rm <file>` | **B†** | Deletes single file; approve per deletion — confirm non-critical target |
| `rm -i <file>` | **B†** | Prompts per file; safer form — approve once per session |
| `rm -r <dir>` | **C** | Recursive delete; always require approval |
| `rm -rf <dir>` | **C** | Force recursive delete; always require approval |
| `rm -rf *` | **C** | Mass delete; always require approval — extremely dangerous |
| `find . -exec rm` | **C** | Mass delete via find; always require approval |
| `chmod <mode> <file>` | **B†** | Permission change; approve per change |
| `chmod -R` | **C** | Recursive permission change; always require approval |
| `chmod 777` | **C** | Opens insecure permissions; always require approval |
| `chown <user> <file>` | **B†** | Ownership change; approve per change |
| `ln -s <src> <dst>` | **B†** | Creates symlink; approve per link |

---

## Category 3 — Python / Development Tools

| Command | Level | Rationale |
|---------|-------|-----------|
| `python --version` | **A** | Read-only |
| `python3 --version` | **A** | Read-only |
| `python -c "print(...)"` | **A** | Safe read-only expression |
| `python -c "import ..."` | **A** | Module inspection; read-only |
| `python scripts/ci_validate.py` | **A** | Validation script; read-only result |
| `python -m pytest` | **A** | Runs tests; read-only result (no DB mutations in test runner) |
| `pytest` | **A** | Runs tests |
| `pytest -v` | **A** | Verbose tests |
| `pytest -k <pattern>` | **A** | Filtered tests |
| `python -m flake8` | **A** | Linting; read-only |
| `python -m pylint` | **A** | Linting; read-only |
| `python -m mypy` | **A** | Type checking; read-only |
| `pip list` | **A** | Read-only |
| `pip show <package>` | **A** | Read-only |
| `pip freeze` | **A** | Read-only |
| `pip install <package>` | **B†** | Installs into venv; approve per package; check approved list |
| `pip install -r requirements.txt` | **B†** | Batch install; approve per invocation; check approved list |
| `pip uninstall <package>` | **C** | Removes package; may break dependencies; always require approval |
| `pip install --upgrade` | **C** | Upgrades package; may break compatibility; always require approval |

---

## Category 4 — Odoo Operations

| Command | Level | Rationale |
|---------|-------|-----------|
| `odoo-bin --stop-after-init` | **A** | Module load check; exits before server starts; no DB mutations |
| `odoo-bin --stop-after-init -d NADF` | **A** | Same; confirms module loads cleanly |
| `odoo-bin shell` | **A** | Launches interactive shell; no mutations until commands run inside |
| `odoo-bin shell -d NADF` | **A** | Launches shell against NADF; queries inside are classified separately |
| Shell query: `env['model'].search([])` | **A** | Read-only ORM query |
| Shell query: `env['model'].browse(id)` | **A** | Read-only |
| Shell query: `env['model'].fields_get()` | **A** | Schema inspection; read-only |
| Shell query: `env.cr.execute("SELECT ...")` | **A** | SELECT query; read-only |
| Shell mutation: `record.write({...})` | **B†** | Mutates record; approve per EA-5 authority scope (AOP-013) |
| Shell mutation: `env['model'].create({...})` | **B†** | Creates record; approve per EA-5 authority scope |
| Shell mutation: `env.cr.execute("UPDATE ...")` | **B†** | Raw SQL mutation; approve per EA-5 authority scope |
| Shell mutation: `env.cr.commit()` | **B†** | Commits transaction; approve per EA-5 authority scope |
| Shell mutation: `env.cr.execute("DELETE ...")` | **C** | Deletes data; always require approval |
| Shell mutation: `env.cr.execute("DROP ...")` | **C** | DDL destruction; always require approval |
| `odoo-bin -i <module>` (approved, non-prod) | **B†** | Module install; approve per module per session |
| `odoo-bin -u <module>` (non-production) | **B†** | Module upgrade; approve per operation |
| `odoo-bin -i <module> -d NADF` (production) | **C** | Production install; always require approval |
| `odoo-bin -u <module> -d NADF` (production) | **C** | Production upgrade; always require approval |
| `odoo-bin --xmlrpc-port <port>` (start server) | **B†** | Starts Odoo server; approve per start |

---

## Category 5 — PostgreSQL / Database

| Command | Level | Rationale |
|---------|-------|-----------|
| `psql --version` | **A** | Read-only |
| `psql -l` | **A** | Lists databases; read-only |
| `psql -d <db> -c "SELECT ..."` | **A** | SELECT query; read-only |
| `psql -d <db> -c "\dt"` | **A** | Schema listing; read-only |
| `psql -d <db> -c "\di"` | **A** | Index listing; read-only |
| `psql -d <db> -c "\d <table>"` | **A** | Table description; read-only |
| `psql -d <db> -c "EXPLAIN ..."` | **A** | Query plan; read-only |
| `pg_dump <db>` | **A** | Creates backup; non-destructive |
| `pg_dump -Fc <db> > <file>` | **A** | Custom format backup; non-destructive |
| `pg_restore --list <file>` | **A** | Lists backup contents; read-only |
| `createdb <drill-db>` | **B†** | Creates new DB; non-destructive to existing; approve per creation |
| `pg_restore -d <drill-db>` | **B†** | Restore to drill/test DB; approve per restore |
| `psql -d <db> -c "INSERT ..."` | **B†** | Data insertion; approve per EA-5 authority scope |
| `psql -d <db> -c "UPDATE ..."` | **B†** | Data update; approve per EA-5 authority scope |
| `psql -d <db> -c "CREATE TABLE ..."` | **B†** | Schema creation; approve per EA-5 authority scope |
| `psql -d NADF -c "INSERT ..."` | **C** | Production DB mutation; always require approval |
| `psql -d NADF -c "UPDATE ..."` | **C** | Production DB mutation; always require approval |
| `psql -d NADF -c "DELETE ..."` | **C** | Production data deletion; always require approval |
| `psql -d <db> -c "DELETE FROM ..."` | **C** | Data deletion; always require approval |
| `psql -d <db> -c "TRUNCATE ..."` | **C** | Table truncation; always require approval |
| `psql -d <db> -c "DROP TABLE ..."` | **C** | Schema destruction; always require approval |
| `psql -d <db> -c "DROP SCHEMA ..."` | **C** | Schema destruction; always require approval |
| `dropdb <db>` | **C** | Drops database; always require approval |
| `dropdb NADF` | **C** | Drops production database; always require approval |
| `pg_restore -d NADF` | **C** | Restore over production; always require approval |
| `psql -d <db> -c "DROP DATABASE ..."` | **C** | Drops database; always require approval |

---

## Category 6 — Process Management

| Command | Level | Rationale |
|---------|-------|-----------|
| `ps` | **A** | Read-only process list |
| `ps aux` | **A** | Read-only |
| `pgrep <pattern>` | **A** | Read-only process search |
| `lsof -i :<port>` | **A** | Read-only port inspection |
| `netstat -tlnp` | **A** | Read-only network connections |
| `ss -tlnp` | **A** | Read-only socket statistics |
| `pkill odoo` | **B†** | Stops Odoo server; approve per session |
| `kill <pid>` | **B†** | Stops specific process; approve per kill |
| `kill -9 <pid>` | **C** | Force-kills process; always require approval |
| `killall <name>` | **C** | Mass kill by name; always require approval |

---

## Category 7 — System and Privilege

| Command | Level | Rationale |
|---------|-------|-----------|
| `uname -a` | **A** | System info; read-only |
| `sw_vers` | **A** | macOS version; read-only |
| `df -h` | **A** | Disk usage; read-only |
| `free -m` / `vm_stat` | **A** | Memory info; read-only |
| `env` | **A** | Environment variables; read-only |
| `printenv` | **A** | Read-only |
| `sudo <any-command>` | **C** | Privilege escalation; always require approval |
| `su <user>` | **C** | User switch; always require approval |
| `passwd` | **C** | Credential change; always require approval |
| `chpasswd` | **C** | Credential change; always require approval |
| `ufw <any>` | **C** | Firewall change; always require approval |
| `iptables <any>` | **C** | Firewall change; always require approval |
| `firewall-cmd <any>` | **C** | Firewall change; always require approval |
| `systemctl <any>` | **C** | System service control; always require approval |
| `launchctl <any>` | **C** | macOS service control; always require approval |
| `brew install <pkg>` | **C** | System package install; always require approval |
| `brew uninstall <pkg>` | **C** | System package remove; always require approval |
| `apt install <pkg>` | **C** | System package install; always require approval |
| `apt remove <pkg>` | **C** | System package remove; always require approval |

---

## Category 8 — Network and External

| Command | Level | Rationale |
|---------|-------|-----------|
| `curl -s <url>` (GET, read-only) | **A** | HTTP GET; read-only; no side effects |
| `curl <url>` (POST / with --data) | **B†** | Sends data to external service; approve per call |
| `wget <url>` | **B†** | Downloads file; approve per download |
| `ssh <host>` | **C** | Opens remote session; always require approval |
| `scp <src> <dst>` | **C** | Remote file copy; always require approval |
| `rsync <src> <remote>` | **C** | Remote sync; always require approval |
| `gh pr create` | **B†** | Creates GitHub PR; approve per PR |
| `gh pr list` | **A** | Read-only |
| `gh issue list` | **A** | Read-only |
| `gh api <endpoint>` (GET) | **A** | Read-only API call |
| `gh api <endpoint>` (POST/PATCH/DELETE) | **B†** | Mutating API call; approve per call |

---

## Category 9 — NADF-Specific Scripts

| Command | Level | Rationale |
|---------|-------|-----------|
| `scripts/backup_nadf.sh` | **A** | Creates backup; non-destructive |
| `scripts/restore_nadf.sh` (drill target) | **B†** | Restores to drill DB; approve per restore |
| `scripts/restore_nadf.sh` (NADF target) | **C** | Restores over production; always require approval |
| `scripts/ci_validate.py` | **A** | CI validation; read-only checks |
| `scripts/module_registry_check.py` | **A** | Read-only registry check |
| Any production deployment script | **C** | Production; always require approval |

---

## Level Summary

| Level | Count (approximate) | Typical commands |
|-------|---------------------|-----------------|
| A — Auto Approve | ~80 commands | All git reads, filesystem reads, test runners, backup creation, SELECT queries, shell reads |
| B — One-Time Approve | ~40 commands | git push (feature), branch create, module install, DB restore (drill), file writes, record mutations (in-WP) |
| C — Always Require | ~35 commands | rm -rf, sudo, dropdb, git push --force, git push main, git reset --hard, production DB mutations, firewall, credentials |

---

*AOP-014 Command Classification Matrix — A1 Master Orchestrator — 2026-06-25*
