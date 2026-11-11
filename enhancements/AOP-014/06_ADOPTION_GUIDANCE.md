# AOP-014 — Adoption Guidance

---

**Document:** AOP-014-06
**Enhancement:** AOP-014 — Development Environment Trust Profile
**Version:** 1.0
**Date:** 2026-06-25

---

## 1. Overview

This document explains how to apply the AOP-014 trust profile in Claude Code for each Software
Factory pod. It covers the technical mechanism, the level-by-level implementation, pod-specific
configuration notes, the session protocol, and governance rules for maintaining the profile
over time.

This is guidance for Sponsor decision. **No settings will be modified without Sponsor instruction.**

---

## 2. Claude Code Trust Mechanism

### 2.1 How Claude Code Handles Approval

Claude Code operates in one of several permission modes. In the default interactive mode,
potentially dangerous Bash commands trigger an approval prompt. The Human Sponsor (or developer)
can respond:

| Response | Effect |
|----------|--------|
| **Yes** (once) | Approves for this invocation only |
| **Yes, and don't ask again** | Adds to the session's allow list (or optionally saves to settings) |
| **No** | Denies; Claude Code adapts or stops |

When "Yes, and don't ask again" is chosen, Claude Code may:
- Keep it as a session-only allow rule (does not persist after session ends), OR
- Save it to the project's `.claude/settings.json` or global `~/.claude/settings.json`
  (persists across sessions until removed)

### 2.2 Settings Configuration

Claude Code supports `allowedTools` in `.claude/settings.json` to pre-configure tool permissions.
For Bash commands specifically, patterns can be defined.

**The AOP-014 recommendation is:**
- Level A commands → configure in project-level `.claude/settings.json` (persists; no prompt)
- Level B commands → use "Yes, and don't ask again" (session only; do NOT save to settings)
- Level C commands → never configure; always prompt

---

## 3. Implementation by Level

### 3.1 Level A — Configure in Project Settings

Level A commands should be added to the project's `.claude/settings.json` as allowed commands
so they never prompt. The Human Sponsor approves the settings file once (when adopted) and then
Level A commands run silently thereafter.

**Configuration approach (when Sponsor approves adoption):**

The `.claude/settings.json` file in each pod repository should include the Level A command
patterns from document 03 (Whitelist Recommendation). This is a deliberate, reviewed configuration
change — not a per-command approval.

**Example format (conceptual — for Sponsor review):**
```json
{
  "permissions": {
    "allow": [
      "Bash(git status*)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Bash(git branch*)",
      "Bash(git add*)",
      "Bash(git stash*)",
      "Bash(git switch*)",
      "Bash(git checkout*)",
      "Bash(git commit*)",
      "Bash(git fetch*)",
      "Bash(git remote*)",
      "Bash(ls*)",
      "Bash(find*)",
      "Bash(grep*)",
      "Bash(cat*)",
      "Bash(head*)",
      "Bash(tail*)",
      "Bash(wc*)",
      "Bash(du*)",
      "Bash(pwd)",
      "Bash(which*)",
      "Bash(echo*)",
      "Bash(mkdir -p*)",
      "Bash(touch*)",
      "Bash(python --version)",
      "Bash(python3 --version)",
      "Bash(python -c *)",
      "Bash(python scripts/ci_validate.py*)",
      "Bash(pytest*)",
      "Bash(python -m pytest*)",
      "Bash(python -m flake8*)",
      "Bash(python -m pylint*)",
      "Bash(python -m mypy*)",
      "Bash(pip list*)",
      "Bash(pip show*)",
      "Bash(pip freeze*)",
      "Bash(psql --version)",
      "Bash(psql -l*)",
      "Bash(pg_dump*)",
      "Bash(pg_restore --list*)",
      "Bash(ps*)",
      "Bash(pgrep*)",
      "Bash(lsof*)",
      "Bash(netstat*)",
      "Bash(ss*)",
      "Bash(uname*)",
      "Bash(sw_vers*)",
      "Bash(df -h*)",
      "Bash(vm_stat*)",
      "Bash(env)",
      "Bash(printenv*)",
      "Bash(scripts/backup_nadf.sh*)",
      "Bash(gh pr list*)",
      "Bash(gh pr view*)",
      "Bash(gh issue list*)"
    ]
  }
}
```

**Important caveats:**
1. `Bash(git checkout*)` is broad — it covers branch switching (safe) AND `git checkout -- .`
   (destructive). Claude Code's pattern matching may or may not distinguish these. If the
   implementation cannot be argument-specific for checkout, use a more conservative approach:
   whitelist `git checkout <branch>` patterns and keep `git checkout --` at Level B.
2. `Bash(echo*)` covers `echo text` (safe) and `echo text > file` (Level B write). If the
   pattern cannot exclude redirects, keep `echo` with redirects at Level B.
3. The Odoo shell entry `Bash(*/odoo-bin shell*)` should NOT be whitelisted as a broad pattern
   because odoo-bin can also be invoked with `-i`, `-u`, and `-d NADF` in the same invocation.
   Instead, whitelist only `--stop-after-init` variants explicitly.

### 3.2 Level B — Session-Only "Don't Ask Again"

Level B commands should not be in settings. Instead:

1. When D2 requests a Level B command for the first time in a session, Claude Code prompts the
   Human Sponsor with the full command visible.
2. The Human Sponsor reads the command (including target and flags) and approves if correct.
3. "Yes, and don't ask again" may be chosen — but **do not save to settings**. Session-only.
4. Subsequent invocations of the same command pattern in the same session proceed without re-prompt.
5. At the start of the next session, Level B commands are reset and must be re-approved once.

**Level B "don't ask again" use cases during NADF WP-03:**
- `git push origin feat/wp-03-procurement-core` — approve once; repeats in same session do not prompt
- `git checkout -b feat/wp-03-*` — approve once; branch is already created so this is unlikely to repeat
- `scripts/restore_nadf.sh --target=nadf_drill` — approve once per session
- Odoo shell mutations within approved EA-5 authority (after backup confirmed)

### 3.3 Level C — Explicit Approval Every Time

Level C commands must not be added to settings or to "don't ask again" under any circumstances.

**Recommended practice for Level C:**
1. When a Level C command appears in the approval queue, stop and read it completely.
2. Confirm the target (database name, file path, branch name) before approving.
3. Confirm the current work package scope includes this action.
4. For EA-5 actions: confirm the AOP-013 advisory/binding authority grant exists.
5. Approve only after confirmation; do not click reflexively.

**The Human Sponsor's Level C approval is the final safety gate.** This is its purpose.

---

## 4. Pod-Specific Adoption Notes

### 4.1 NADF Pod

**Settings file location:** `/Users/mac/nadf_erp/.claude/settings.json`

**Pod-specific Level A additions:**
- `Bash(scripts/backup_nadf.sh*)` — NADF backup script; always safe
- `Bash(psql -d NADF -c "SELECT*")` — read-only queries against NADF production DB
- `Bash(psql -d NADF -c "\dt*")` — schema inspection against NADF production

**Pod-specific Level C enforcement:**
- All commands with `-d NADF` and a mutating SQL operation are Level C
- `odoo-bin -i * -d NADF` is Level C (production module install)
- `scripts/restore_nadf.sh` with NADF as target is Level C

**Current status:** NADF is the AOP-013 pilot pod. Trust profile adoption is recommended
to coincide with or follow AOP-013 pilot completion (after WP-03/WP-04 close and Sponsor
GRADUATE decision).

### 4.2 FamOil Pod

**Settings file location:** `/Users/mac/odoo17/.claude/settings.json` (or the FamOil-erp directory)

**Pod-specific Level C enforcement:**
- All commands with `-d Famoil` and a mutating SQL operation are Level C
- FamOil has not yet reached Level 1 governance (FamOil Wave 1 pending per ROADMAP.md)

**Adoption recommendation:** Adopt trust profile when FamOil Wave 1 activates and
`.claude/settings.json` is created as part of the FamOil governance bootstrap.

### 4.3 WamaCare Pod

**Settings file location:** `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/.claude/settings.json`

**Pod-specific notes:**
- `wamacare_local` is the local development database (not a production database in the same sense
  as NADF or Famoil). Mutations against `wamacare_local` are Level B, not Level C.
- Any production WamaCare database (if deployed) is Level C.
- WamaCare is port 8070; NADF is 8071 — no port conflict.

**Adoption recommendation:** Adopt at the same time as NADF if the Sponsor chooses
"ADOPT — NADF ONLY" first; otherwise adopt in the same Sponsor instruction.

---

## 5. Session Protocol with Trust Profile Active

The following protocol governs a standard delivery session under the trust profile:

### 5.1 Session Start
1. Verify current branch: `git status` (Level A — no prompt)
2. Read current WP and backlog state (file reads — Level A)
3. Review any outstanding Level B actions from previous session

### 5.2 During Delivery
- Level A commands proceed without interruption (git reads, filesystem reads, tests, backups)
- First Level B command in the session: Human Sponsor reads and approves; "don't ask again" in session
- Level C command encountered: stop; Human Sponsor reads full command; confirms scope; approves deliberately

### 5.3 Before First EA-5 Action (AOP-013 + AOP-014 combined)
1. Confirm AOP-013 advisory/binding authority exists (check EXECUTION_AUTHORITY_REGISTER.md)
2. Confirm backup is current (Level A — backup check or creation)
3. Confirm G3 condition satisfied (backup confirmed)
4. Approve the shell mutation command (Level B — one-time approval for this session)

### 5.4 Session End
- No Level B session approvals carry to next session (session resets)
- Level A settings persist (configured in settings file)
- Level C gates are always fresh (never configured)

---

## 6. Governance Rules for Trust Profile Maintenance

### Rule 1 — Whitelist Is a Governed Artifact
The Level A whitelist (document 03 and the `.claude/settings.json` file) is a governed document.
Any addition, removal, or modification to the whitelist requires:
1. A logged decision in the pod's `DECISION_LOG.md` (or the governance repo `DECISION_LOG.md`)
2. A rationale explaining why the new command meets the Level A criteria
3. Human Sponsor approval

### Rule 2 — Blacklist Is Absolute
The blacklist (document 04) may not be overridden by convenience arguments. If a blacklisted
command needs to be executed, it requires explicit Level C approval at execution time — period.
No exception may be written into settings.

### Rule 3 — Annual Review
A1 reviews the trust profile once per major milestone (M1 close, M2 close, etc.) to confirm:
- No new risky commands have been added to Level A
- No new tools or scripts have been introduced that are unclassified
- The Level B session discipline is being maintained

### Rule 4 — Pod Isolation Is Preserved
The trust profile for NADF does not automatically apply to FamOil or WamaCare. Each pod
maintains its own `.claude/settings.json`. Cross-pod contamination of settings is prohibited
(consistent with the CLAUDE.md isolation rule and the M-C incident history).

### Rule 5 — Level B Discipline
"Yes, and don't ask again" is a session tool, not a settings tool, for Level B commands.
If a Level B command appears in `.claude/settings.json`, it is a trust profile violation
and must be removed.

---

## 7. Adoption Decision Summary

| Scope | Recommended Action | Timing |
|-------|-------------------|--------|
| NADF | Adopt Level A whitelist immediately; Level B/C guidance immediately | On Sponsor adoption approval |
| FamOil | Defer to FamOil Wave 1 activation | When FamOil governance bootstrap begins |
| WamaCare | Adopt with NADF or separately | On Sponsor adoption approval |

**Recommended first step for Sponsor:** Approve adoption for NADF only. Review the Level A
patterns above carefully. Instruct A1 to create the `.claude/settings.json` configuration
in `/Users/mac/nadf_erp/`. Validate over one WP that the profile reduces friction without
removing meaningful gates.

---

*AOP-014 Adoption Guidance — A1 Master Orchestrator — 2026-06-25*
