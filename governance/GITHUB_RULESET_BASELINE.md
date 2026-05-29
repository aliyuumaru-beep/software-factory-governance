# GitHub Ruleset Baseline

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects hosted on GitHub  
**Audited Repository:** `aliyuumaru-beep/software-factory-governance`  
**Audit Date:** 2026-05-29

---

## 1. Purpose

This document defines the recommended GitHub repository protection baseline for all
Software Factory projects. It is derived from an audit of the live settings on
`software-factory-governance` and extended with the settings required to enforce
the governance standards defined in `governance/PR_GOVERNANCE_STANDARD.md`.

Every new Software Factory repository should be configured to match the Recommended
Baseline (Section 4) before the first external contributor or AI agent is given
write access to it.

---

## 2. Audit — Current State (`software-factory-governance`, 2026-05-29)

This section captures the exact GitHub settings in place at the time of this audit.
It is a factual record, not a recommendation. The gap between this state and the
Recommended Baseline is shown in Section 3.

### 2.1 Branch Protection

| Setting | Current Value |
|---------|--------------|
| Branch: `main` | **Unprotected** |
| Require pull request before merging | Disabled |
| Required approvals | None |
| Dismiss stale reviews | N/A |
| Require review from code owners | N/A |
| Require status checks to pass | Disabled |
| Required status checks | None configured |
| Require branches to be up to date | N/A |
| Require conversation resolution | Disabled |
| Require signed commits | Disabled |
| Require linear history | Disabled |
| Restrict force pushes | Disabled |
| Restrict deletions | Disabled |
| Allow force pushes | Enabled (default — no restriction) |
| Allow deletions | Enabled (default — no restriction) |

**Assessment:** `main` is fully unprotected. Any authenticated user with write access
can push directly to `main`, force-push over history, or delete the branch.

### 2.2 Rulesets

| Setting | Current Value |
|---------|--------------|
| Repository rulesets | **None configured** |

### 2.3 Merge Strategy

| Setting | Current Value |
|---------|--------------|
| Allow merge commits | **Enabled** |
| Allow squash merging | **Enabled** |
| Allow rebase merging | **Enabled** |
| Default merge method (viewer) | Merge commit |
| Merge commit title format | `MERGE_MESSAGE` |
| Merge commit message format | `PR_TITLE` |
| Squash merge commit title | `COMMIT_OR_PR_TITLE` |
| Squash merge commit message | `COMMIT_MESSAGES` |
| Allow auto-merge | Disabled |
| Delete branch on merge | **Disabled** |
| Allow update branch | Disabled |

**Assessment:** All three merge strategies are available. Developers can choose any
strategy per PR, producing an inconsistent commit history. Branch cleanup after
merge is manual.

### 2.4 Repository Features

| Setting | Current Value |
|---------|--------------|
| Visibility | **Public** |
| Issues | Enabled |
| Projects | Enabled |
| Wiki | **Enabled** |
| Discussions | Disabled |
| Archived | No |

### 2.5 Security and Analysis

| Setting | Current Value |
|---------|--------------|
| Secret scanning | **Enabled** ✓ |
| Secret scanning push protection | **Enabled** ✓ |
| Secret scanning — non-provider patterns | Disabled |
| Secret scanning — validity checks | Disabled |
| Dependabot security updates | **Disabled** ✗ |
| Dependabot alerts | Not confirmed enabled |

**Assessment:** Secret scanning and push protection are active — this is the most
important security control and it is correctly enabled. Dependabot is not active,
which is acceptable for a documentation-only repository but should be enabled for
repositories containing application code dependencies.

### 2.6 Pull Request Template

| Setting | Current Value |
|---------|--------------|
| `.github/PULL_REQUEST_TEMPLATE.md` | **Present and active** ✓ |
| Template auto-loads on PR creation | Confirmed by GitHub API |

---

## 3. Gap Analysis — Current vs Recommended Baseline

| Dimension | Current State | Recommended Baseline | Gap |
|-----------|--------------|---------------------|-----|
| Branch protection on `main` | None | Required | **Critical** |
| PR required before merge | No | Yes — minimum 1 review | **Critical** |
| Direct push to `main` allowed | Yes | No (admin override only) | **Critical** |
| Force push to `main` allowed | Yes | No | **High** |
| Branch deletion allowed | Yes | No for `main` | **High** |
| Status checks | None | PR template completion check (Phase 4) | Medium |
| Merge strategies allowed | All three | Squash only | **High** |
| Delete branch on merge | Disabled | Enabled | Medium |
| Auto-merge | Disabled | Disabled | ✓ Correct |
| Secret scanning | Enabled | Enabled | ✓ Correct |
| Secret scanning push protection | Enabled | Enabled | ✓ Correct |
| Dependabot alerts | Disabled | Enabled for code repos | Medium |
| Wiki | Enabled | Disabled (docs live in repo) | Low |
| PR template | Active | Active | ✓ Correct |

**Critical gaps** prevent the PR governance standard from being enforceable at the
platform level. Currently, the PR template exists but nothing prevents a developer
from bypassing it with a direct push to `main`.

---

## 4. Recommended Baseline

This is the target configuration for every new Software Factory repository. Apply it
after the repository is created and before the first non-governance commit.

### 4.1 Branch Protection — `main`

Configure via: **GitHub → Repository Settings → Branches → Add rule → Branch name: `main`**

| Setting | Recommended Value | Rationale |
|---------|------------------|-----------|
| Require a pull request before merging | **Enabled** | Enforces the PR governance standard at the platform level; makes bypassing impossible without admin override |
| Required approvals | **1** | Minimum viable review; prevents solo committing while allowing solo developers with AI agents to still function |
| Dismiss stale pull request approvals | **Enabled** | Prevents a reviewer approving draft state and the PR then being modified and merged without re-review |
| Require review from code owners | Disabled | No CODEOWNERS file required; review-by-anyone satisfies the standard for current team size |
| Require status checks to pass | **Enabled** (when CI exists) | Phase 4 item; enable when GitHub Actions are configured; leave disabled until then |
| Require branches to be up to date before merging | **Enabled** (when CI exists) | Prevents merging a branch that would fail if merged with the current `main`; couple with status checks |
| Require conversation resolution before merging | **Enabled** | Prevents merging a PR that has unresolved review comments — enforces review quality |
| Require signed commits | Disabled | Impractical for the current team structure; revisit at Phase 5 |
| Require linear history | **Enabled** | Combined with squash-only merge strategy, produces a clean, readable commit history; prevents merge commit clutter |
| Lock branch | Disabled | Would prevent the Software Factory lead from making emergency direct commits; admin override suffices |
| Do not allow bypassing the above settings | Disabled | Allows admin (Software Factory lead) to bypass for genuine emergencies; log any bypass as a governance exception |
| Restrict who can push to matching branches | Disabled initially | Enable and list named users/teams when the project has a defined contributor list |
| Allow force pushes | **Disabled** | Force push rewrites published history; the only safe history rewrite is an explicit `git filter-repo` operation logged as an architectural decision |
| Allow deletions | **Disabled** | `main` must never be deleted |

### 4.2 Rulesets (Alternative / Supplementary to Branch Protection)

GitHub Rulesets (available on all plans) offer a more flexible and auditable alternative
to legacy branch protection rules. When setting up a new repository, prefer Rulesets
over Branch Protection rules for the following reasons:
- Rulesets can be applied to multiple branches via pattern matching
- Rulesets are versioned and auditable in the GitHub UI
- Rulesets support `EVALUATE` mode (log violations without blocking) for gradual adoption

**Recommended ruleset for `main`:**

```
Name: Governance Baseline — main
Target: Branch: main
Enforcement: Active

Rules:
  ✓ Restrict deletions
  ✓ Require linear history
  ✓ Require a pull request:
      Required approvals: 1
      Dismiss stale reviews on push: Yes
      Require review of the most recent push: No (Phase 4+)
  ✓ Block force pushes
  ✗ Require status checks (enable in Phase 4 when CI exists)
```

### 4.3 Merge Strategy

Configure via: **GitHub → Repository Settings → General → Pull Requests**

| Setting | Recommended Value | Rationale |
|---------|------------------|-----------|
| Allow merge commits | **Disabled** | Merge commits produce a non-linear history that obscures the change stream; every change should be a single atomic commit |
| Allow squash merging | **Enabled** | Squash + conventional commit title (`<type>(<scope>): description`) produces a clean, linear, readable history where every line corresponds to one PR |
| Allow rebase merging | **Disabled** | Rebase merging re-writes commit timestamps and authors, making `git log` and `git blame` misleading; squash is preferable for governance projects |
| Squash merge commit title | `PR_TITLE` | The PR title follows the conventional commit format; using it as the squash commit title keeps the history consistent |
| Squash merge commit message | `BLANK` | The GIA and PR description belong in the PR on GitHub, not in the commit message body; a blank message keeps `git log` scannable |
| Allow auto-merge | **Disabled** | Auto-merge bypasses the human review moment; AI-generated PRs must still be reviewed by a human before merge |
| Automatically delete head branches | **Enabled** | Keeps the branch list clean; branches can be restored from PR history if needed |

### 4.4 Repository Features

| Setting | Recommended Value | Rationale |
|---------|------------------|-----------|
| Visibility | **Private** (code repos) / Public (governance repo) | Client ERP projects contain business logic and configuration that should not be publicly accessible; the governance repo is intentionally public as a reference |
| Issues | **Enabled** | Used to track known issues that do not yet have a PR |
| Projects | Disabled | Project tracking is done in the roadmap document; GitHub Projects adds overhead without proportionate value for the current team size |
| Wiki | **Disabled** | All documentation lives in the repository as Markdown files under version control; the GitHub Wiki is a separate, unversioned system that will drift |
| Discussions | Disabled | Not required at current scale |

### 4.5 Security and Analysis

| Setting | Recommended Value | Rationale |
|---------|------------------|-----------|
| Secret scanning | **Enabled** | Detects committed secrets retroactively; must be enabled on all repositories |
| Secret scanning push protection | **Enabled** | Blocks pushes that contain known secret patterns before they enter the repository; the only setting that prevents the problem rather than detecting it after the fact |
| Secret scanning — non-provider patterns | **Enabled** (where available) | Catches project-specific secret patterns beyond the GitHub default list |
| Dependabot alerts | **Enabled** (code repos) | Alerts on known CVEs in declared dependencies; low noise for governance-only repos, high value for Python/Odoo repos |
| Dependabot security updates | **Enabled** (code repos) | Creates PRs to update vulnerable dependencies automatically; governs itself through the standard PR process |

### 4.6 Pull Request Template

| Setting | Recommended Value | Rationale |
|---------|------------------|-----------|
| `.github/PULL_REQUEST_TEMPLATE.md` | **Required — copy from governance templates** | GitHub auto-loads this file when any PR is created; without it, the governance checklist is opt-in and will be skipped |

---

## 5. Configuration Instructions

### 5.1 Applying Branch Protection via GitHub UI

```
1. Navigate to: Repository → Settings → Branches
2. Click "Add classic branch protection rule"
3. Branch name pattern: main
4. Check: Require a pull request before merging
   - Required approving reviews: 1
   - Dismiss stale pull request approvals when new commits are pushed: ✓
5. Check: Require conversation resolution before merging
6. Check: Require linear history
7. Under "Rules" at bottom:
   - Allow force pushes: ✗ (leave unchecked)
   - Allow deletions: ✗ (leave unchecked)
8. Save changes
```

### 5.2 Applying Merge Strategy via GitHub UI

```
1. Navigate to: Repository → Settings → General → Pull Requests
2. Allow merge commits: ✗ uncheck
3. Allow squash merging: ✓ check
   - Default commit message: Pull request title
4. Allow rebase merging: ✗ uncheck
5. Allow auto-merge: ✗ leave unchecked
6. Automatically delete head branches: ✓ check
7. Save
```

### 5.3 Applying via GitHub CLI

```bash
# Apply merge strategy
gh api repos/OWNER/REPO \
  --method PATCH \
  --field allow_merge_commit=false \
  --field allow_squash_merge=true \
  --field allow_rebase_merge=false \
  --field delete_branch_on_merge=true \
  --field squash_merge_commit_title="PR_TITLE" \
  --field squash_merge_commit_message="BLANK"

# Apply branch protection
gh api repos/OWNER/REPO/branches/main/protection \
  --method PUT \
  --field required_status_checks=null \
  --field enforce_admins=false \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null \
  --field required_linear_history=true \
  --field allow_force_pushes=false \
  --field allow_deletions=false \
  --field required_conversation_resolution=true
```

---

## 6. Conditions Under Which the Baseline Should Change

The baseline is not permanent. The following conditions require a review and potentially
a change, logged as an `ARCHITECTURE` or `OPERATIONAL` entry in `DECISION_LOG.md`.

### 6.1 Increase Protection (tighten)

| Trigger | Recommended Change |
|---------|--------------------|
| Phase 4 CI is active | Add required status checks for commit message lint and PR template validation |
| Team grows beyond 2 developers | Add CODEOWNERS file; enable "Require review from code owners" |
| A direct push to `main` bypass is used | Review whether admin bypass should be further restricted |
| A security incident involves a committed secret | Verify secret scanning non-provider patterns are enabled; review `.gitignore` coverage |
| Project goes into production client use | Enable "Do not allow bypassing" for the PR requirement; emergencies go through a hotfix PR, not direct push |

### 6.2 Decrease Protection (loosen — requires explicit justification)

| Trigger | Recommended Change | Justification Required |
|---------|--------------------|----------------------|
| Solo developer with no reviewer available for a critical hotfix | Temporary admin bypass — log as `GOVERNANCE_EXCEPTION` in `DECISION_LOG.md` | Yes — must be logged and follow-up PR created within 24 hours |
| Automated governance bot creates PRs that require self-approval | Enable auto-merge for bot-created PRs only after thorough review of bot output | Yes — decision log entry required |

### 6.3 Merge Strategy Changes

The squash-only recommendation holds unless:
- The project adopts a mono-repo model where feature branches have meaningful sub-commit history
  that must be preserved (log as `ARCHITECTURE` decision if changed)
- The team explicitly requests merge commits for auditability of individual commits within a PR
  (acceptable if commit message discipline is verified to be high)

### 6.4 Visibility Changes

| Trigger | Action |
|---------|--------|
| A client project that was private is open-sourced | Governance review required; ensure no credentials, client data, or proprietary business logic is in history |
| The governance repo is moved to an organisation | Review team access permissions; update this document with organisation-level settings |

---

## 7. Compliance Checklist — Repository Setup Gate

Use this checklist when setting up any new Software Factory repository:

- [ ] Repository created with correct visibility (Private for code repos, Public for governance)
- [ ] `.github/PULL_REQUEST_TEMPLATE.md` copied from governance templates
- [ ] `.gitignore` created (adapted from governance baseline + project-specific exclusions)
- [ ] Branch protection applied to `main` per Section 4.1
- [ ] Merge strategy set to squash-only per Section 4.3
- [ ] Delete branch on merge: enabled
- [ ] Wiki: disabled
- [ ] Secret scanning: confirmed enabled
- [ ] Secret scanning push protection: confirmed enabled
- [ ] Dependabot alerts: enabled (code repositories)
- [ ] Repository setup recorded in `IMPLEMENTATION_HISTORY.md` (type: `INFRASTRUCTURE_CHANGE`)
- [ ] Any deviations from this baseline logged in `DECISION_LOG.md` (type: `OPERATIONAL`)

---

## 8. Current Non-Compliance — `software-factory-governance`

The governance repository itself does not currently comply with the Recommended Baseline.
The following settings need to be applied:

| Setting | Required Action |
|---------|----------------|
| Branch protection on `main` | Apply per Section 5.1 |
| Merge strategy | Disable merge commits and rebase; enable squash-only per Section 5.2 |
| Delete branch on merge | Enable |
| Wiki | Disable |
| Dependabot alerts | Enable (low priority — documentation-only repo, but sets the example) |

**These settings are not applied automatically by this document.** They require a
deliberate action by the repository owner. Each setting change should be recorded
in `IMPLEMENTATION_HISTORY.md` as type `INFRASTRUCTURE_CHANGE`.

The non-compliance is logged here rather than silently. The Software Factory lead
should apply these settings and record the action before Phase 2 adoption of any
project repository begins, so FamOil and WamaCare are set up correctly from the start.

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
