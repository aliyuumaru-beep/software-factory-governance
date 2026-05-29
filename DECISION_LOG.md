# Decision Log — Software Factory Governance

This log records every governance-level decision made in the Software Factory governance
repository. All decisions affecting standards, templates, methodology, or structure are
recorded here following the standard defined in `governance/DECISION_LOG_STANDARD.md`.

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
