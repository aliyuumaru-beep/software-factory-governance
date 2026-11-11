# AOP-014 — Risk Assessment

---

**Document:** AOP-014-05
**Enhancement:** AOP-014 — Development Environment Trust Profile
**Version:** 1.0
**Date:** 2026-06-25

---

## 1. Risk Assessment Scope

This risk assessment covers the risks introduced by adopting the AOP-014 trust profile itself —
not the risks of the commands within it. Specifically:

- What could go wrong if Level A commands are auto-approved?
- What could go wrong if Level B commands are one-time approved?
- What residual risk remains for Level C commands?
- What systemic risks does the trust profile create or reduce?

---

## 2. Risk Register

---

### RISK-AOP014-001 — Level A Command Misclassification

| Field | Value |
|-------|-------|
| Risk | A command classified as Level A is actually capable of a destructive side effect in certain invocations |
| Example | `git checkout *` is Level A for branch switching but `git checkout -- .` discards all changes. A wildcard rule could auto-approve the wrong form. |
| Likelihood | Low — matrix uses explicit patterns, not broad wildcards |
| Impact | Medium — could result in lost uncommitted work or unintended state change |
| Mitigation | 1. Whitelist uses explicit command patterns, not broad wildcards. `git checkout <branch>` is different from `git checkout -- <path>`. 2. Claude Code approval patterns support argument-level specificity. 3. Governance review of whitelist before adoption. |
| Residual | Low |

---

### RISK-AOP014-002 — Level B "One-Time Approve" Becoming Effectively Permanent

| Field | Value |
|-------|-------|
| Risk | A Level B command approved once in a session is silently persisted beyond its intended scope if the Human Sponsor clicks "Yes, and don't ask again" without reading the prompt carefully |
| Example | Sponsor approves `git push origin feat/wp-03-*` as "don't ask again" during WP-03 and it persists into WP-04 where a different branch with different content is being pushed |
| Likelihood | Medium — approval fatigue is real; "don't ask again" is easy to click without reading |
| Impact | Medium — unintended branch pushes; misdirected DB restores; wrong module installations |
| Mitigation | 1. Adoption guidance explicitly states Level B = session scope only; settings should not be permanently updated for Level B. 2. Each WP session should start from a clean approval state for Level B commands. 3. Adoption guidance recommends periodic session reset for Level B. |
| Residual | Low-Medium |

---

### RISK-AOP014-003 — Approval Fatigue in Reverse (Over-approval of Whitelist)

| Field | Value |
|-------|-------|
| Risk | The trust profile eliminates approval friction for Level A commands. If a Level C command is injected adjacent to a stream of Level A commands in a session, the Human Sponsor may approve it reflexively without reading |
| Example | A1 runs 30 Level A git/grep commands, then issues `rm -rf /path/to/production` as the 31st — Sponsor approves without reading |
| Likelihood | Low — Level C commands are visually distinctive (destructive keywords: `rm -rf`, `dropdb`, `--force`) |
| Impact | Critical — could destroy data or production systems |
| Mitigation | 1. Level C commands are explicitly listed in the blacklist; Claude Code can be configured to always prompt for these with a prominent warning. 2. Adoption guidance recommends distinct visual treatment for Level C approvals. 3. AOP-013 framework provides an independent gate — Level C actions also require EA authority under the Execution Authority Framework. |
| Residual | Low |

---

### RISK-AOP014-004 — Trust Profile Drift Over Time

| Field | Value |
|-------|-------|
| Risk | As new tools and commands are introduced to the Software Factory workflow, they may be added to the whitelist without formal re-classification, gradually expanding the Level A surface |
| Example | A new deployment helper script is added to `scripts/` and a developer adds it to the whitelist in Claude Code settings without classifying it through AOP-014 governance |
| Likelihood | Medium — settings files are easy to edit; governance process is easier to skip |
| Impact | Medium — new Level A commands may carry hidden risk |
| Mitigation | 1. Adoption guidance designates the whitelist as a governed artifact requiring change through AOP-014 or its successor. 2. Any new command added to Level A requires a logged governance decision (AOP-013 DECISION_LOG format). 3. Annual or per-major-WP review of the whitelist is recommended. |
| Residual | Low |

---

### RISK-AOP014-005 — Odoo Shell Prompt Ambiguity

| Field | Value |
|-------|-------|
| Risk | `odoo-bin shell` is whitelisted as Level A (the launch is safe) but commands run inside the shell may be EA-5 mutations. A Human Sponsor who sees "odoo-bin shell" pre-approved may assume all shell activity is also pre-approved |
| Example | D2 launches shell (Level A, auto-approved) and then silently executes `env.cr.commit()` mutations inside the shell session. The Sponsor approved the shell launch but not the mutations |
| Likelihood | Medium — the distinction between shell launch and shell commands is not immediately obvious |
| Impact | High — unauthorised DB mutations could occur under the cover of a whitelisted shell launch |
| Mitigation | 1. Adoption guidance explicitly documents the shell launch vs. shell command distinction. 2. Mutating shell commands (`env.cr.commit()`, `.write({})`, `.create({})`) are always Level B and must be individually approved. 3. AOP-013 EA-5 authority requirement is an independent gate — D2 must have advisory/binding authority before executing shell mutations. 4. CLAUDE.md files are updated to note this distinction. |
| Residual | Low-Medium |

---

### RISK-AOP014-006 — Pod Target Confusion

| Field | Value |
|-------|-------|
| Risk | A command approved for one pod (e.g. `pg_restore -d nadf_drill`) is mistakenly reused against another pod's production database in a multi-pod session |
| Example | During a session working across NADF and FamOil, `pg_restore -d Famoil` is approved under the assumption it is a Level B "drill restore" when it is actually a production restore |
| Likelihood | Low — sessions are typically pod-isolated; CLAUDE.md rules enforce pod isolation |
| Impact | High — production database overwrite |
| Mitigation | 1. Level B approval is session-scoped and target-specific. Approving `pg_restore -d nadf_drill` does not auto-approve `pg_restore -d Famoil`. 2. CLAUDE.md isolation rules (Pod-NADF isolation, WamaCare isolation) are a first-line defence. 3. Adoption guidance recommends single-pod sessions where possible. |
| Residual | Low |

---

### RISK-AOP014-007 — Trust Profile Reduces Discovery of Process Problems

| Field | Value |
|-------|-------|
| Risk | Approval prompts sometimes surface process problems (e.g. "Why is git push being called here? This shouldn't be happening."). Auto-approving these commands removes a human checkpoint that may catch unexpected behaviour |
| Example | A1 issues `git push origin feat/wp-03` earlier than expected. Under the current model, the Sponsor sees this and flags it. Under the trust profile, the push happens silently |
| Likelihood | Low-Medium — trust profile applies during normal delivery; A1 still narrates its actions |
| Impact | Low — process deviation would be caught at PR review gate in any case |
| Mitigation | 1. A1 narrates major actions in text output even when they are auto-approved at the tool level. 2. Git operations are fully auditable via `git log`. 3. The PR review gate is an independent human checkpoint for all repository mutations. |
| Residual | Low |

---

## 3. Risk Summary

| Risk ID | Description | Likelihood | Impact | Residual |
|---------|-------------|-----------|--------|---------|
| RISK-AOP014-001 | Level A misclassification | Low | Medium | **Low** |
| RISK-AOP014-002 | Level B persistence beyond scope | Medium | Medium | **Low-Med** |
| RISK-AOP014-003 | Reverse approval fatigue (Level C injection) | Low | Critical | **Low** |
| RISK-AOP014-004 | Trust profile drift over time | Medium | Medium | **Low** |
| RISK-AOP014-005 | Odoo shell ambiguity | Medium | High | **Low-Med** |
| RISK-AOP014-006 | Pod target confusion | Low | High | **Low** |
| RISK-AOP014-007 | Removes discovery checkpoint | Low-Med | Low | **Low** |

**Overall residual risk: Low.** The highest concern is RISK-AOP014-003 (reverse approval fatigue
leading to Level C auto-approval), but the impact is mitigated by AOP-013's independent authority
gate and by the visual distinctiveness of Level C command keywords.

---

## 4. Risk Comparison: Profile vs. No Profile

| Scenario | Risk Without Profile | Risk With Profile |
|----------|---------------------|------------------|
| Approval fatigue from 30+ low-risk approvals per session | **HIGH** — Sponsor may approve dangerous commands reflexively | **LOW** — Level A filtered out; Sponsor only sees Level B/C |
| Destruction by pre-approved Level C command | **LOW** (all commands prompt) | **LOW** (Level C never pre-approved) |
| Slowdown preventing effective unattended execution | **HIGH** — every command blocks | **LOW** — Level A runs freely |
| Unauthorised DB mutation during approved WP | **LOW** (prompts catch it) | **LOW** (AOP-013 is independent gate) |
| Missed detection of unexpected agent behaviour | **LOW** (many checkpoints) | **LOW-MED** (fewer checkpoints; narration compensates) |

**Conclusion:** The adoption of a well-calibrated trust profile **reduces** the most significant
operational risk (approval fatigue leading to careless approval of dangerous commands) while
**preserving** protection for the genuinely dangerous command categories.

---

## 5. Recommended Risk Controls

1. **Whitelist governed as an artifact**: Any addition to Level A requires a logged decision.
2. **Level B session scope enforced**: Adoption guidance must be clear: Level B = session only.
3. **Odoo shell distinction documented**: In CLAUDE.md and adoption guidance.
4. **Level C visual highlighting**: Adoption guidance recommends configuring distinctive approval UI for Level C commands (if supported by Claude Code version).
5. **Annual whitelist review**: A1 reviews the Level A list after each major milestone (M1, M2, etc.) to confirm no drift has occurred.

---

*AOP-014 Risk Assessment — A1 Master Orchestrator — 2026-06-25*
