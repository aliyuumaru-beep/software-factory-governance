# PEF_DISCOVERY_REPORT_TEMPLATE.md
## Software Factory — Discovery Report Template

**Template ID:** PEF-TPL-007  
**Framework reference:** 25_PRODUCT_ENGINEERING_FRAMEWORK.md Section 9.2 (Discovery-Before-Implementation Rule); Section 5 (D-21)  
**Produced at:** Start of PEG-7 — before any implementation code is written  
**Produced by:** Software Development Team (or Autonomous Agent Team)  
**Reviewed by:** Product Engineering Team

---

## INSTRUCTIONS FOR USE

This report is **mandatory before a single line of implementation code is written**. For AI agents, this rule is unconditional (PEF Section 9.2).

Complete every section. Do not leave fields blank. Where a check does not apply, write "Not applicable — [reason]". Sections marked **[REQUIRED]** cannot be omitted.

Every check must record an **observed value** and a **PASS / FAIL / CONFLICT** result. A check is **CONFLICT** when the discovered state contradicts an assumption in the Product Transfer Package. All CONFLICT items must be resolved by the Product Engineering Team before implementation proceeds.

Replace all `[PLACEHOLDER]` text with project-specific content.  
Delete these instructions before submitting for review.

---

## DOCUMENT IDENTITY

| Field | Value |
|-------|-------|
| Project name | [PROJECT_NAME] |
| Client | [CLIENT_NAME] |
| Platform (expected) | [Platform name and version from Transfer Package, e.g. "Odoo 17 Community Edition"] |
| Development Team / Agent | [Name(s) or agent identity] |
| Product Engineering reviewer | [Name] |
| Document version | [1.0] |
| Date | [YYYY-MM-DD] |
| PEG stage | PEG-7 (pre-implementation) |
| Status | [Draft / Under Review / Accepted / Conflicts Open] |

---

## SECTION 1 — DISCOVERY SUMMARY **[REQUIRED]**

*2–4 sentences. What was discovered, whether the repository and platform match the Product Transfer Package assumptions, and whether any conflicts block implementation.*

[DISCOVERY_SUMMARY]

| Field | Value |
|-------|-------|
| Total checks run | [N] |
| PASS | [N] |
| FAIL | [N] |
| CONFLICT | [N] |
| Implementation cleared to begin? | [YES / NO — blocked by open conflicts] |

---

## SECTION 2 — REPOSITORY AND VERSION CONTROL **[REQUIRED]**

| Check | Observed value | Result |
|-------|---------------|--------|
| Repository path | [/absolute/path] | [PASS/FAIL/CONFLICT] |
| Git initialised | [Yes/No] | [PASS/FAIL] |
| Current branch | [branch name] | [PASS/FAIL] |
| Commit history present | [N commits; last commit hash/date] | [PASS/FAIL] |
| Remote configured | [remote URL or "none"] | [PASS/FAIL] |
| Main branch protected | [Yes/No — direct push blocked?] | [PASS/FAIL] |
| Feature-branch + PR workflow | [Yes/No] | [PASS/FAIL] |
| Working tree clean | [Clean / N untracked / N modified] | [PASS/FAIL] |

---

## SECTION 3 — CI/CD AND AUTOMATION **[REQUIRED]**

| Check | Observed value | Result |
|-------|---------------|--------|
| CI workflow present | [Yes/No — file path] | [PASS/FAIL] |
| CI status on latest commit | [Passing/Failing/None] | [PASS/FAIL] |
| Lint / static analysis configured | [Yes/No] | [PASS/FAIL] |
| Build verification configured | [Yes/No] | [PASS/FAIL] |

---

## SECTION 4 — PLATFORM AND ENVIRONMENT **[REQUIRED]**

*Platform edition mismatch (e.g. Odoo Community vs Enterprise) is a critical conflict — it cascades through the entire build. Verify the exact version AND edition.*

| Check | Expected (Transfer Package) | Observed value | Result |
|-------|----------------------------|---------------|--------|
| Platform name | [e.g. Odoo] | [Observed] | [PASS/FAIL/CONFLICT] |
| Platform version | [e.g. 17.0] | [Observed] | [PASS/FAIL/CONFLICT] |
| Platform edition | [e.g. Community] | [Observed] | [PASS/FAIL/CONFLICT] |
| Database exists | [DB name] | [Observed name / none] | [PASS/FAIL/CONFLICT] |
| Service port / host | [port/host] | [Observed] | [PASS/FAIL] |
| Runtime / language version | [e.g. Python 3.x] | [Observed] | [PASS/FAIL] |

---

## SECTION 5 — INSTALLED AND CUSTOM MODULES **[REQUIRED]**

| Check | Observed value | Result |
|-------|---------------|--------|
| Installed modules conflicting with authorised platform profile | [List any prohibited/Enterprise-only modules, or "None"] | [PASS/FAIL/CONFLICT] |
| Existing custom modules | [List module names, or "None"] | [PASS/FAIL] |
| Modules expected by Transfer Package but absent | [List, or "None"] | [PASS/FAIL/CONFLICT] |

**Prohibited / unexpected modules detail:**

| Module | Why it is a problem | Action required |
|--------|--------------------|-----------------|
| [MODULE] | [e.g. Enterprise-only; conflicts with Community profile] | [Remove / escalate / document] |
| *Add rows as needed* | | |

---

## SECTION 6 — BACKUP AND RECOVERY **[REQUIRED]**

| Check | Observed value | Result |
|-------|---------------|--------|
| Backup strategy documented | [docs/BACKUP_STRATEGY.md exists? Yes/No] | [PASS/FAIL] |
| Restore procedure documented | [Yes/No] | [PASS/FAIL] |
| Last backup timestamp | [YYYY-MM-DD HH:MM, or "none"] | [PASS/FAIL] |

---

## SECTION 7 — PRODUCT MEMORY SYSTEM **[REQUIRED]**

*Confirm the nine mandatory files (PEF Section 8.3) are present in the repository scaffold. Note `CHANGELOG.md` lives at the repository root; the other eight live under `docs/`.*

| File | Present? | Result |
|------|---------|--------|
| `docs/NEXT_ACTION.md` | [Yes/No] | [PASS/FAIL] |
| `docs/PRODUCT_STATE_INDEX.md` | [Yes/No] | [PASS/FAIL] |
| `docs/CONTROL_TOWER.md` | [Yes/No] | [PASS/FAIL] |
| `docs/PRODUCT_BACKLOG.md` | [Yes/No] | [PASS/FAIL] |
| `docs/MILESTONE_REGISTER.md` | [Yes/No] | [PASS/FAIL] |
| `docs/DECISION_LOG.md` | [Yes/No] | [PASS/FAIL] |
| `docs/IMPLEMENTATION_HISTORY.md` | [Yes/No] | [PASS/FAIL] |
| `CHANGELOG.md` (repository root) | [Yes/No] | [PASS/FAIL] |
| `docs/session_logs/` directory | [Yes/No] | [PASS/FAIL] |

---

## SECTION 8 — CONFLICTS REGISTER **[REQUIRED]**

*Every CONFLICT result from Sections 2–7 is recorded here. Implementation does not begin until all conflicts are Resolved.*

| Conflict ID | Source check | Description | Severity | Resolution | Resolved by / date |
|-------------|-------------|-------------|----------|-----------|--------------------|
| DC-001 | [e.g. §4 Platform edition] | [What was assumed vs what was found] | [Critical/High/Medium/Low — per PEF 11.4] | [How resolved, or "Open"] | [Name, YYYY-MM-DD] |
| *Add rows as needed* | | | | | |

---

## SECTION 9 — DISCOVERY OUTCOME AND REVIEW **[REQUIRED]**

| Field | Value |
|-------|-------|
| All checks PASS or CONFLICTs Resolved? | [YES / NO] |
| Implementation authorised to begin? | [YES / NO] |
| Reviewed by (Product Engineering Team) | [NAME] |
| Date | [YYYY-MM-DD] |

**By accepting this Discovery Report, the Product Engineering Team confirms:**
1. The discovered repository and platform state has been reviewed
2. No open conflicts contradict the Product Transfer Package assumptions
3. The Software Development Team (or Autonomous Agent Team) is cleared to begin implementation

*If any conflict remains Open, implementation must not begin. Escalate per PEF Section 8.2 (Conflict Resolution).*

---

*PEF_DISCOVERY_REPORT_TEMPLATE.md v1.0 — Software Factory governance standard*
