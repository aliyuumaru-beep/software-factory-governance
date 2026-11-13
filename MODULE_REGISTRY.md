# Module Registry — Software Factory Governance

Registry of scripts, services and infrastructure components shipped by this repository
(`governance/REGISTRY_STANDARD.md` §2.6–2.7). Created 2026-11-13 under SPEC-GOV-ENF-001.

---

## Registry Summary

| ID | Name | Type | Status | Registered | Purpose (Brief) |
|----|------|------|--------|------------|-----------------|
| MOD-001 | `enforcement/govcore.py` | Service / Script | ACTIVE | 2026-11-13 | Governance gateway engine: Claude hooks, `gov` CLI, git hooks, CI docs gate, reviewer runner |
| MOD-002 | `enforcement/install.sh` | Script | ACTIVE | 2026-11-13 | Installs the gateway for a user (hooks, CLI, git hooks, global CLAUDE.md block) |
| MOD-003 | `enforcement/reviewers/G1.md`, `G2.md`, `G3.md` | Component | ACTIVE | 2026-11-13 | Independent reviewer prompts (base role prompt plus enforcement appendix) |
| MOD-004 | `enforcement/templates/` | Component | ACTIVE | 2026-11-13 | Onboarding templates: `.governance.json`, caller workflow, AGENTS.md, bootstrap hook, git hooks, global CLAUDE.md block |
| MOD-005 | `enforcement/tests/test_gov.py` | Script | ACTIVE | 2026-11-13 | Acceptance suite for R1–R10, L2 and L3 (73 checks) |
| MOD-006 | `.github/workflows/governance-gate.yml` | Infrastructure | ACTIVE | 2026-11-13 | Reusable PR gate (`docs-gate`, then `review-G1..G3`, then `gate`), released as immutable tags `gate-vN` |
| MOD-007 | `.github/workflows/enforcement-tests.yml` | Infrastructure | ACTIVE | 2026-11-13 | Runs MOD-005 on PRs touching `enforcement/` |
| MOD-008 | `.github/workflows/governance.yml` | Infrastructure | ACTIVE | 2026-11-13 | This repository's own call of MOD-006 (local path, PR copy) |

---

## Detailed Registry Entries

### MOD-001 — `enforcement/govcore.py`

**Type:** Service / Script · **Status:** ACTIVE · **Introduced In:** `feat/gov-enforcement-gateway` · **Owner:** Sponsor

#### Purpose

A single engine enforces SPEC-GOV-ENF-001 for four callers: Claude Code hooks (`gov hook`), developers
(`gov status|start|review|verify|onboard|protect`), git hooks (`gov githook`) and CI (`gov ci-docs-gate`, `gov review --ci`).

#### Dependencies

| Dependency | Type | Required / Optional |
|------------|------|---------------------|
| Python 3.9+ standard library | Runtime | Required |
| `git` | Tool | Required |
| `claude` CLI (pinned `@anthropic-ai/claude-code@2.1.312` in CI) | Tool | Required for `gov review` |
| `gh` CLI | Tool | Optional (`gov protect` only) |

#### Configuration

A per-user `config.json` in the gateway home (owner patterns, registered repos). Each governed repo has `.governance.json`.

### MOD-006 — `.github/workflows/governance-gate.yml`

**Type:** Infrastructure · **Status:** ACTIVE · **Owner:** Sponsor

#### Purpose

The server-side guarantee (layer L4). Child repos call it at an immutable tag (`@gate-v1`) and pass only
`CLAUDE_CODE_OAUTH_TOKEN` / `ANTHROPIC_API_KEY`. Releasing a new version means a new `gate-vN` tag, then a PR in each child repo.
