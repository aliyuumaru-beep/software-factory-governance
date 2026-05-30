# Decision Log — Software Factory Governance

This log records every governance-level decision made in the Software Factory governance
repository. All decisions affecting standards, templates, methodology, or structure are
recorded here following the standard defined in `governance/DECISION_LOG_STANDARD.md`.

---

## DEC-012

**Date:** 2026-05-29
**Type:** `TRADE_OFF`
**Status:** ACTIVE
**Made By:** Software Factory lead
**PR Reference:** PR #1 (pre-merge configuration change)

### Title
Required approving review count set to 0 — solo development mode, deviation from the recommended baseline of 1.

### Context
`governance/GITHUB_RULESET_BASELINE.md` §4.1 recommends `required_approving_review_count: 1`
as the minimum viable review gate. When ruleset `software-factory-governance-v1` was first
applied the count was set to 1. Before PR #1 could be merged, the count was changed to 0
because the repository has a single developer with no available reviewer, and
`bypass_actors` is empty (`current_user_can_bypass: never`) — meaning there is no
alternative path to merge.

### Decision
Set `required_approving_review_count: 0` for the governance repository.

Rationale: requiring 1 approval on a solo-developer repository with no bypass path
creates a permanent deadlock. The compensating controls that remain active provide
meaningful enforcement without peer review:

- PR is still required before any merge — no direct push to main.
- CI must pass (doc-lint, secret-scan, governance-validate) — though not yet *required* in the ruleset (see IMP-007 open item).
- Stale review dismissal is still active.
- Conversation resolution is still required.
- Squash-only merge and linear history are enforced.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Keep count at 1, add self as bypass actor | Bypass actors can push directly to main without a PR; removes the PR gate entirely for the bypass actor, which is worse than 0-approval PRs |
| Keep count at 1, add a second collaborator | No second collaborator available; deferring all merges until one is added would halt all governance work indefinitely |
| Keep count at 1, use GitHub's "allow force push" as a workaround | Force push is blocked by the `non_fast_forward` rule; this workaround would require weakening a security control to fix a process constraint |

### Consequences
All PRs to this repository can be self-merged by the repository owner without peer review.
The governance process (PR template + GIA + CI checks) remains mandatory and provides
documentation and audit value even without a second reviewer.

When a second developer joins, `required_approving_review_count` must be restored to 1
and this entry's status updated to `SUPERSEDED`.

### Related Entries
DEC-011 (ruleset activation), IMP-007 (CI workflow deployment)

---

## DEC-011

**Date:** 2026-05-29
**Type:** `OPERATIONAL`
**Status:** ACTIVE
**Made By:** Software Factory lead
**PR Reference:** Applied directly to GitHub repository settings (pre-PR-enforcement)

### Title
GitHub Ruleset `software-factory-governance-v1` applied — branch protection and PR enforcement activated on the default branch.

### Context
`governance/GITHUB_RULESET_BASELINE.md` documented the recommended baseline configuration
and identified that the governance repository had no branch protection (Critical gap).
The ruleset was applied to activate enforced governance, transitioning from a state where
standards were documented but unenforceable to one where violations are blocked at the
platform level.

The ruleset was created at 2026-05-29T20:03:45+01:00 and last updated
2026-05-29T20:31:08+01:00. Ruleset ID: 17043434.

### Decision
Apply GitHub Ruleset `software-factory-governance-v1` to the default branch (`~DEFAULT_BRANCH`)
with the following active rules:

**Branch targeting:**
- Condition: `~DEFAULT_BRANCH` — automatically tracks the default branch regardless of name

**Pull request enforcement:**
- PR required before any merge to main — direct push blocked
- `required_approving_review_count`: 0 (see DEC-012 for the deviation rationale)
- `dismiss_stale_reviews_on_push`: true — approval is invalidated if new commits are pushed
- `required_review_thread_resolution`: true — all review comments must be resolved before merge
- `allowed_merge_methods`: `["squash"]` — squash-only enforced at the platform level

**History integrity:**
- `required_linear_history`: true — merge commits are blocked; history is always linear
- `non_fast_forward`: blocks force push — published history cannot be rewritten

**Branch safety:**
- `deletion`: branch deletion blocked — `main` cannot be deleted

**Bypass policy:**
- `bypass_actors`: empty — no actor, including the repository owner, can bypass these rules
- `current_user_can_bypass`: `never`

**Security layer (repository-level, separate from ruleset):**
- `secret_scanning`: enabled — detects committed secrets retroactively
- `secret_scanning_push_protection`: enabled — blocks pushes containing known secret patterns before they enter history
- `dependabot_security_updates`: disabled (documentation-only repository; no dependency manifest)

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Classic branch protection rules | Rulesets are versioned, auditable, and offer `EVALUATE` mode; preferred over legacy branch protection per `governance/GITHUB_RULESET_BASELINE.md` §4.2 |
| Apply protection after Phase 4 CI is set up | Delaying protection leaves the main branch unguarded during active governance work; protection and CI should be active simultaneously |
| Allow admin bypass | Creating a bypass path undermines the integrity of the protection; governance exceptions should go through the PR process with the exception logged, not through bypassing the gate entirely |

### Consequences
All changes to the governance repository must flow through a PR. The first such PR
(PR #1, commit `6eddf5fdaf748514d8380c28bc691237848097d4`) successfully used the full PR
template and passed all CI checks, confirming the mechanism works end-to-end.

CI status checks run on every PR but are not yet *required* to pass before merge — this
is the remaining gap to full Level 3 governance maturity. Adding `required_status_checks`
to the ruleset closes this gap (see IMP-007).

When CI status checks are added as required to the ruleset, a new decision log entry
(`OPERATIONAL` type) must be created to record the updated rule set and the check names.

### Related Entries
DEC-012 (required approvals set to 0), IMP-007 (CI workflow deployment and merge)

---

## DEC-010

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (adoption strategy session)
**PR Reference:** Adoption strategy commit 005579b

### Title
FamOil git repository root is `/Users/mac/odoo17`; only `custom_addons/`, `docs/`, `scripts/`, and governance root files are committed — Odoo core source and venv are excluded.

### Context
FamOil has no git repository (Known Issue #7). When initialising one, the repository
boundary must be decided before the first `git add`. `/Users/mac/odoo17` contains:
- `odoo/odoo/` — the full Odoo 17 Community source (~200k files, ~1.5 GB)
- `odoo/venv/` — the Python virtual environment (~500 MB)
- `custom_addons/` — two custom modules (project code, ~50 files)
- `docs/` — project documentation
- `scripts/` — four operational scripts
- `odoo.conf` — runtime configuration containing database passwords

Getting this wrong on the first commit is not easily reversible — rewriting git history
with `git filter-branch` or `git-filter-repo` is destructive and disruptive.

### Decision
- **Repository root:** `/Users/mac/odoo17`
- **Committed:** `custom_addons/`, `docs/famoil_erp_template/`, `scripts/`, and all
  governance root files (`CLAUDE.md`, `README.md`, `DECISION_LOG.md`, etc.)
- **Excluded via `.gitignore`:**
  - `odoo/odoo/` — Odoo core source (installed dependency, not project code; version
    pinned in deployment notes, not in git)
  - `odoo/venv/` — Python venv (~500 MB; never committed)
  - `odoo.conf` — contains database password; never committed
  - `~/Library/Application Support/Odoo/filestore/Famoil/` — binary attachment store;
    backed up separately, not version-controlled
  - `__pycache__/`, `*.pyc` — compiled Python artefacts

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Use `custom_addons/` as the git root, not `/Users/mac/odoo17` | Would require a second directory for governance root files and docs; splits the project across two repos or forces a sub-directory structure that complicates AI agent orientation |
| Commit the Odoo core source alongside custom code | Bloats the repo to GB scale; obscures project code in noise; makes `git diff` and `git log` unusable for project-level review; Odoo source is an upstream dependency, not project code |
| Track `odoo.conf` with secrets redacted | Partial redaction is error-prone and frequently incomplete; env var injection is the correct pattern and requires no version-controlled config file |

### Consequences
- Odoo version is not tracked in git; it must be recorded in `IMPLEMENTATION_HISTORY.md`
  and `README.md` as a configuration note (`17.0.1.3 Community`).
- The `.gitignore` for FamOil must explicitly exclude Odoo-specific paths in addition to
  the standard governance `.gitignore` exclusions.
- Any developer or AI agent setting up FamOil must install Odoo 17 separately; the repo
  does not self-contain the runtime.

### Related Entries
DEC-009 (FamOil as pilot), IMP-005 (FamOil readiness assessment)

---

## DEC-009

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (adoption strategy session)
**PR Reference:** Adoption strategy commit 005579b

### Title
FamOil ERP is selected as the Phase 2 governance adoption pilot ahead of WamaCare and NADF ERP.

### Context
Phase 2 requires one project to serve as the pilot for governance adoption — proving the
four-wave process, validating the `.github/PULL_REQUEST_TEMPLATE.md` in real use, and
producing the first `DECISION_LOG.md` migration from a pre-governance format. Three active
projects were eligible: FamOil ERP, WamaCare, and NADF ERP.

### Decision
FamOil ERP is the Phase 2 pilot.

Rationale:
1. **Highest commercial urgency.** Phase 3 commercialisation framework is complete (8.5/10
   readiness). The next step is first client deployment (groundnut oil mill). Governance
   must be in place before client-facing work begins.
2. **Most complex existing custom code.** Two custom modules (`stock_crude_oil_tank_restriction`,
   `mrp_component_availability_check`) and four scripts represent the hardest migration case.
   A pilot that succeeds on the hardest case validates the playbook for simpler projects.
3. **Pre-existing decision log to migrate.** FamOil has DEC-001 to DEC-010 in its own
   non-standard format. Migrating them exercises the most demanding part of Wave 2 and
   surfaces any gaps in the migration procedure.
4. **No git repository.** Initialising git for FamOil exercises Wave 1 (the highest-risk
   wave) end-to-end, producing a reusable `.gitignore` pattern for all subsequent Odoo
   projects.
5. **WamaCare is isolated.** The WamaCare project is explicitly kept isolated from FamOil
   (different port, different DB). Piloting on FamOil does not risk WamaCare contamination.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| WamaCare as pilot | DB restore is pending; unstable baseline makes it a poor pilot; isolation rules make cross-referencing risky |
| NADF ERP as pilot | Not yet started as an Odoo deployment; no existing code or docs to validate migration procedures against |
| Both FamOil and WamaCare simultaneously | Parallel adoption with no proven playbook creates double the risk; serial adoption (FamOil first, WamaCare second) validates the process before the second project is touched |

### Consequences
- WamaCare adoption begins only after FamOil reaches Wave 4 (first governed PR).
- NADF ERP is a greenfield adoption — it will use the validated playbook from FamOil without a migration phase.
- The FamOil `.gitignore` becomes the reference template for all future Odoo project `.gitignore` files.

### Related Entries
DEC-010 (FamOil git boundary), IMP-005 (FamOil readiness assessment)

---

## DEC-008

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Commit 58ceb8a (initial bootstrap), self-compliance fix PR

### Title
Root-level ROADMAP.md required by the governance standard; detailed roadmap may reside in `roadmaps/` subdirectory for governance-layer repositories.

### Context
`GOVERNANCE_STANDARD.md` §3.1 lists `ROADMAP.md` as a mandatory root-level file for all governed repositories. During bootstrap, the governance repo's roadmap was placed at `roadmaps/SOFTWARE_FACTORY_ROADMAP.md` because the `roadmaps/` directory was designed to hold multi-layer roadmaps. This created a self-compliance gap discovered in the Governance Maturity Review (2026-05-29).

### Decision
Add a root `ROADMAP.md` that provides the current phase summary and delegates to `roadmaps/SOFTWARE_FACTORY_ROADMAP.md` for the full multi-phase detail. Amend `GOVERNANCE_STANDARD.md` §3.1 with a note that governance-layer repositories satisfying the root `ROADMAP.md` requirement via a summary-and-delegate pattern are compliant. Project repositories that have only one roadmap must keep it at `ROADMAP.md`.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Move full roadmap to root ROADMAP.md, delete `roadmaps/` | `roadmaps/` is designed to hold multiple roadmap files as the factory matures; eliminating it removes that extensibility |
| Amend the standard to remove the root ROADMAP.md requirement entirely | The standard exists for good reasons across all project repos; creating a blanket exemption weakens it |

### Consequences
Governance repo now has both a root `ROADMAP.md` (summary) and `roadmaps/SOFTWARE_FACTORY_ROADMAP.md` (full detail). All other governed repositories use only root `ROADMAP.md`. The distinction is documented in `GOVERNANCE_STANDARD.md`.

### Related Entries
DEC-001 (governance as standalone repo), IMP-003 (self-compliance fixes)

---

## DEC-007

**Date:** 2026-05-29
**Type:** `GOVERNANCE_EXCEPTION`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Self-compliance fix PR

### Title
Bootstrap commit (58ceb8a) pre-dates the governance standard and is exempt from its own PR and decision log requirements.

### Context
The initial bootstrap commit that created all 33 governance files was a direct commit to `main` with no PR, no GIA, and no prior `DECISION_LOG.md` to log into. This is a structural bootstrapping paradox: governance documents must exist before governance can be enforced, but the governance documents themselves cannot be created under the governance they define.

### Decision
The bootstrap commit (58ceb8a, 2026-05-29) is granted a permanent governance exception for the direct-commit-to-main rule and the absent PR template. All subsequent commits to this repository must follow the full governance standard. The bootstrap decisions are back-logged into this `DECISION_LOG.md` as part of the self-compliance fix.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Retroactively squash and re-create bootstrap as a PR | Git history rewrite provides no value; the bootstrapping paradox is a known category of governance exception |
| Leave undocumented | Violates the principle that governance exceptions must be logged |

### Consequences
The governance repo's git history will always show one direct commit to main (the bootstrap). All subsequent changes go through PRs. This is explicitly logged and does not set a precedent for other repositories.

### Related Entries
DEC-001, IMP-001

---

## DEC-006

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Commit 58ceb8a

### Title
Governance standards and operational procedures are separated into `governance/` and `operations/` directories with a principle-vs-procedure distinction.

### Context
Backup/recovery, change management, release tagging, and restore procedures can be documented either as binding governance requirements (what must happen) or as operational step-by-step procedures (how to make it happen). Mixing both in one file creates documents that are too long for a governance reviewer and too abstract for an operations engineer.

### Decision
Establish two distinct directories: `governance/` for binding standards (the "what and why") and `operations/` for operational procedures (the "how"). Governance standards reference the corresponding operations standard for procedural detail. Operations standards reference the governance standard for the binding requirement.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Single `standards/` directory with all documents | Creates bloated documents that mix audience and purpose; makes it harder to find the document a specific reader needs |
| Embed procedures directly in governance standards | Governance reviewers do not need bash scripts; operations engineers do not need re-reading policy rationale |

### Consequences
Every backed-up domain (backup, change management) has two documents: one in `governance/` and one in `operations/`. Readers must know which one to read first. Cross-references in each file mitigate this. Any new operational domain requires coordinated creation in both directories.

### Related Entries
DEC-001

---

## DEC-005

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Commit 58ceb8a

### Title
"A backup is only trusted after a successful restore" is adopted as a non-negotiable governance principle, not a best-practice recommendation.

### Context
Backup systems are frequently set up, never tested, and discovered to be non-functional only when a restore is attempted in a real incident. Financial and personal data in ERP systems (FamOil, WamaCare) make this failure mode unacceptable. A recommendation-level backup testing requirement is routinely skipped; a governance-level requirement is enforceable.

### Decision
The restore verification requirement is elevated to a binding governance principle stated as the first line of `governance/BACKUP_RECOVERY_STANDARD.md`. Projects that do not have a recorded, successful restore drill do not have a functioning backup system. This is enforced via the Governance Impact Analysis (Dimension 8) and the `IMPLEMENTATION_HISTORY.md` restore event log.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Treat restore testing as a best-practice recommendation | Recommendations are skipped; the entire motivation for governance is that important things need teeth, not suggestions |
| Require restore drills only for production, not staging | Staging drift from production is one of the most common sources of failed production restores; staging drills are required on a longer cadence |

### Consequences
Projects must conduct and record restore drills on a defined schedule. A project that cannot produce a recent drill record fails the governance audit. This creates operational overhead that is deliberate and necessary.

### Related Entries
IMP-001

---

## DEC-004

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Commit 58ceb8a

### Title
Repository memory (committed documents) is designated as the highest-authority source of truth, above code, comments, verbal instructions, and AI context memory.

### Context
Software Factory projects are heavily AI-assisted. AI agents (Claude) begin each session with no memory of prior sessions. Without a clear authority hierarchy, an AI agent may act on stale context, overridden verbal instructions, or misremembered decisions — leading to contradicted decisions, duplicate modules, and governance defects.

### Decision
The authority hierarchy is: (1) committed repository documents, (2) actual code, (3) inline comments, (4) current-session verbal instructions, (5) AI context memory. This hierarchy is codified in `principles/REPOSITORY_MEMORY_PRINCIPLES.md` and enforced via `CLAUDE.md`. AI agents must read repository memory documents before acting, regardless of what they believe they know from prior context.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Treat AI context memory as equivalent to repository documents | AI memory is unreliable across sessions, unverifiable, and unauditable; it cannot serve as ground truth |
| Treat verbal session instructions as highest authority | Verbal instructions are ephemeral and unrecorded; elevating them above committed documents would undermine the entire decision log concept |

### Consequences
AI agents are required to read governance documents at session start before taking any action. This adds latency to AI sessions but prevents contradictions with prior decisions. Users cannot verbally override committed governance decisions without creating a new log entry.

### Related Entries
DEC-001, IMP-001

---

## DEC-003

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Commit 58ceb8a

### Title
A 10-dimension Governance Impact Analysis (GIA) is required for every PR, with no exempt PR types.

### Context
PR reviews in software projects routinely miss non-code impacts: documentation becomes stale, modules go unregistered, architectural decisions go unlogged, and rollback plans are absent. These omissions compound over time into governance debt that makes projects unmaintainable. A structured checklist forces explicit consideration of each impact dimension.

### Decision
Define 10 dimensions that every PR must address: code impact, documentation impact, decision log impact, roadmap impact, registry impact, onboarding impact, security impact, backup/recovery impact, rollback impact, and testing evidence. No PR type is exempt. "Not impacted — [reason]" is a valid answer for any dimension. The full definition is in `docs/GOVERNANCE_IMPACT_ANALYSIS.md`.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Exempt `docs` and `chore` PRs from the full GIA | Any change can have security, rollback, or registry implications; a blanket exemption creates a bypass route that will be misused |
| Fewer dimensions (e.g., 5) | Fewer dimensions lose coverage of the most commonly missed impacts (registry, onboarding, backup); the 10 were chosen to map to specific failure patterns, not for completeness theatre |
| Optional GIA at reviewer discretion | Optional compliance is not compliance |

### Consequences
Every PR requires a completed 10-dimension GIA. For trivial documentation changes, most dimensions will be "not impacted." The overhead is low for simple changes and meaningful for complex ones. Compliance fatigue is a known risk; the governance maturity review (2026-05-29) flagged this and recommended a lightweight fast-path for pure `docs` PRs as a future refinement.

### Related Entries
DEC-001

---

## DEC-002

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Commit 58ceb8a

### Title
A four-layer model (Software Factory / Platform / Industry Template / Client Deployment) is adopted as the canonical architectural separation model for all Software Factory projects.

### Context
Without a defined layering model, shared code accumulates in client projects (because it is convenient), cross-project reuse never happens (because there is no shared layer to put it in), and governance cannot define clear boundaries for what belongs where. As the number of projects grows from 2 to 6+, this becomes unmanageable.

### Decision
Adopt the four-layer model: Layer 1 (governance, this repo), Layer 2 (shared platform, future repo), Layer 3 (industry templates, future repos), Layer 4 (client deployments). Each layer has defined ownership, boundary rules, and cross-layer dependency direction (dependencies flow downward only). The full definition is in `docs/PROJECT_LAYERING_MODEL.md`.

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Two layers only (governance + projects) | Insufficient separation once 3+ projects share common infrastructure; would require duplicating shared modules across projects |
| Three layers (governance + platform + projects) | Drops the industry template layer; vertical-specific patterns (oil & gas, NGO) would have nowhere to live between platform and client, forcing either duplication or over-genericization |
| Five or more layers | Excessive for the current scale; adds governance overhead without proportionate benefit at this stage |

### Consequences
Layers 2 and 3 do not yet have repositories. Until they are created, all projects operate as Layer 4 directly inheriting from Layer 1. This is explicitly documented as the current state in `docs/PROJECT_LAYERING_MODEL.md` §5. Creating Layer 2 and Layer 3 repositories is a Phase 6 roadmap item.

### Related Entries
DEC-001, IMP-001

---

## DEC-001

**Date:** 2026-05-29
**Type:** `ARCHITECTURE`
**Status:** ACTIVE
**Made By:** Software Factory lead / Claude Sonnet 4.6 (bootstrap session)
**PR Reference:** Commit 58ceb8a

### Title
The Software Factory governance is housed in a dedicated standalone repository, not embedded in any project or platform repository.

### Context
Governance standards need to be accessible to all projects without any single project having ownership of them. Embedding governance in the FamOil repo (for example) would make FamOil the de facto owner, create a circular dependency when governing FamOil itself, and require all other projects to reference across repository boundaries to a project repo they do not otherwise depend on.

### Decision
Create `software-factory-governance` as a standalone, project-agnostic repository. It is not a code repository — it contains only governance documents, standards, templates, and operational procedures. All governed projects reference it as the governance source of truth. It has its own versioning (`CHANGELOG.md`) and follows its own governance standards (self-applicable).

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Embed governance in a shared monorepo alongside all projects | Creates a single point of failure and entangles governance changes with project changes in the same commit history |
| Embed governance in the platform repository (Layer 2) | Platform repository does not yet exist; governance is needed now; creates a dependency inversion where governance depends on a layer it should sit above |
| Distribute governance standards into each project repo | Each project would maintain its own copy of the standards; they would immediately diverge; there would be no single source of truth |

### Consequences
The governance repository must be explicitly referenced or cloned by anyone working on a governed project. AI agents operating in a project repository must know to read the governance `CLAUDE.md` from this repository before reading the project `CLAUDE.md`. This cross-repo dependency is managed via `CLAUDE.md` links and the AI onboarding standard.

### Related Entries
DEC-002, IMP-001
