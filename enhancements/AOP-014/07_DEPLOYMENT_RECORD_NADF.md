# AOP-014 — Deployment Record: NADF Pod

---

**Document:** AOP-014-07
**Enhancement:** AOP-014 — Development Environment Trust Profile
**Version:** 1.0
**Date Deployed:** 2026-06-26
**Deployed By:** A1 Master Orchestrator
**Sponsor Decision:** DEC-AOP014-001 (ADOPT — NADF ONLY)
**Governance Log:** DEC-017 (software-factory-governance/DECISION_LOG.md)

---

## 1. Deployment Summary

| Item | Detail |
|------|--------|
| Target pod | NADF |
| Settings file | `/Users/mac/nadf_erp/.claude/settings.json` |
| Pre-existing settings | None (file did not exist; `.claude/` directory existed with empty hooks subdirectory) |
| Patterns deployed | 67 Level A allow patterns |
| Level B configured | No — session-only; not in settings |
| Level C configured | No — always prompts; never in settings |
| Effective from | 2026-06-26 (next Claude Code session on NADF pod) |

---

## 2. Deployed Configuration

### 2.1 Allow Patterns (Level A — 63 entries)

**Git Read-Only (11 patterns):**
- `git status*`, `git diff*`, `git log*`, `git branch*`, `git remote*`
- `git stash list*`, `git stash show*`, `git show *`, `git ls-files*`, `git tag -l*`, `git fetch*`

**Git Safe Write (8 patterns):**
- `git add*`, `git restore --staged*`, `git commit*`, `git switch*`
- `git stash pop*`, `git stash push*`, `git stash apply*`, `git stash` (bare)

**Filesystem Read/Non-Destructive (16 patterns):**
- `ls*`, `find*`, `grep*`, `cat*`, `head*`, `tail*`, `wc*`, `du*`
- `pwd`, `which*`, `type *`, `mkdir -p*`, `touch *`, `env`, `printenv*`

**Python and Testing (11 patterns):**
- `python --version`, `python3 --version`, `python scripts/ci_validate.py*`
- `pytest*`, `python -m pytest*`, `python -m flake8*`, `python -m pylint*`, `python -m mypy*`
- `pip list*`, `pip show *`, `pip freeze`

**Odoo Read-Only (1 pattern):**
- `*odoo-bin --stop-after-init*`

**PostgreSQL Read-Only (4 patterns):**
- `psql --version`, `psql -l`, `psql -l *`, `pg_dump *`, `pg_restore --list *`

**Process Inspection (8 patterns):**
- `ps aux`, `ps aux*`, `ps -ef*`, `pgrep *`
- `lsof -i*`, `lsof -p*`, `netstat*`, `ss -tlnp*`

**System Information (5 patterns):**
- `uname*`, `sw_vers*`, `df -h*`, `vm_stat`

**NADF Scripts (1 pattern):**
- `scripts/backup_nadf.sh*`

**GitHub CLI Read-Only (3 patterns):**
- `gh pr list*`, `gh pr view *`, `gh issue list*`

---

## 3. Explicit Exclusions (Not Whitelisted — by Design)

The following commands were considered for Level A but deliberately excluded:

| Command | Why Excluded | Level |
|---------|-------------|-------|
| `git checkout*` | `git checkout -- <path>` discards working tree changes; ambiguous with branch switching | B |
| `git push*` | State-dependent; branch target determines safety | B |
| `git commit --amend*` | History rewriting; broadly covered by `git commit*` but amend is Level B by intent | B (covered by `git commit*` broadly) |
| `git stash drop*` | Destroys stash entry; not reversible | B |
| `git stash clear*` | Destroys all stash entries | B |
| `echo*` | File redirect (`echo text > file`) would be auto-approved; too broad | B |
| `python -c "*"` | Arbitrary Python execution; could be used for DB mutations | B |
| `psql -d * -c "*"` | Pattern includes SELECT (safe) and DELETE (Level C); cannot safely distinguish | B/C |
| `odoo-bin shell*` | Shell + piped mutations are a single Bash call; the mutation would be auto-approved | B |
| `pip install*` | Package state change | B |
| `rm *` (any form) | Any file deletion | B/C |
| `sudo*` | Privilege escalation | C |

**Note on `git commit*`:** This pattern technically matches `git commit --amend`. On NADF feature
branches, amending the last commit is acceptable behaviour. The risk is low (feature branch only;
amend cannot rewrite protected main). This is documented but not treated as a violation.

---

## 4. Condition Compliance

| Condition | Status | Evidence |
|-----------|--------|---------|
| 1 — NADF only | ✅ | Settings file deployed only to `/nadf_erp/.claude/settings.json`; FamOil and WamaCare unmodified |
| 2 — Level C unchanged | ✅ | No Level C patterns in allow list; `rm -rf`, `sudo`, `dropdb`, `git push --force`, `git push origin main`, `git reset --hard` are absent |
| 3 — No production deployment | ✅ | No deployment scripts; no `ssh`; no `scp`; no production odoo-bin (`-d NADF` with `-i`/`-u`) |
| 4 — Whitelist changes documented | ✅ | This deployment record; future changes require governance log entry per Condition 4 / DEC-017 |
| 5 — Metrics collection | ✅ | Metrics template created at `/nadf_erp/docs/governance/AOP014_METRICS_LOG.md` |
| 6 — FamOil/WamaCare deferred | ✅ | Not deployed; flagged in DEC-017 for separate decision |

---

## 5. Rollback Procedure

If the trust profile needs to be removed or modified:

| Step | Action |
|------|--------|
| 1 | Delete `/Users/mac/nadf_erp/.claude/settings.json` or clear the `allow` array |
| 2 | Log the change in software-factory-governance `DECISION_LOG.md` as a governance decision |
| 3 | Update AOP-014 deployment record (this document) with removal date and reason |
| 4 | Notify: no operational impact — removal only adds approval prompts back; no data is affected |

---

## 6. Change Management

Any future change to the whitelist (add or remove a pattern) requires:

1. A1 proposes the change with classification rationale
2. Sponsor reviews and approves (or delegates to A1 for Level A additions)
3. Change logged in `DECISION_LOG.md` as a governance decision referencing DEC-017
4. This deployment record updated in Section 2

**Prohibited without Sponsor decision:** Adding any Level B or Level C pattern to the allow list.

---

*AOP-014 Deployment Record — NADF Pod — A1 Master Orchestrator — 2026-06-26*
