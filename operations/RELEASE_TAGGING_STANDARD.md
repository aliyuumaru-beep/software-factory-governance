# Release Tagging Standard

**Version:** 1.0.0
**Effective:** 2026-05-29
**Applies to:** All Software Factory projects

---

## 1. Purpose

Release tags create stable, named points in the repository history that correspond to
deployed states of the system. They are essential for:
- Identifying exactly what code is running in production at any time.
- Rolling back to a known good state.
- Correlating issues with specific deployments.
- Auditing deployment history.

---

## 2. When to Tag

A release tag must be created:

| Event | Tag Required |
|-------|-------------|
| Production deployment | Yes — always |
| Staging deployment (milestone) | Yes — at phase milestones |
| Phase completion | Yes |
| Pre-upgrade snapshot | Yes — always before an upgrade |
| Emergency hotfix deployment | Yes — within 24 hours |

Tags are optional for development and feature branch builds.

---

## 3. Tag Naming Convention

### 3.1 Standard Release

```
v<MAJOR>.<MINOR>.<PATCH>
```

- **MAJOR** — incompatible changes (schema breaking changes, major module removals)
- **MINOR** — new features or modules (backward compatible)
- **PATCH** — bug fixes, minor corrections

Examples:
- `v1.0.0` — initial production release
- `v1.1.0` — added purchase approval module
- `v1.1.1` — fixed invoice date validation bug

### 3.2 Phase Milestones

```
v<MAJOR>.<MINOR>.<PATCH>-phase<N>
```

Examples:
- `v1.0.0-phase1` — Phase 1 complete
- `v2.0.0-phase3` — Phase 3 complete

### 3.3 Pre-Upgrade Snapshots

```
v<current-version>-pre-upgrade-<YYYYMMDD>
```

Example: `v1.2.0-pre-upgrade-20260529`

### 3.4 Emergency Hotfixes

```
v<MAJOR>.<MINOR>.<PATCH>-hotfix-<YYYYMMDD>
```

Example: `v1.2.1-hotfix-20260529`

---

## 4. Tagging Procedure

```bash
# Ensure you are on the correct commit (main branch, after merge)
git checkout main
git pull origin main

# Create an annotated tag with a message
git tag -a v1.0.0 -m "Phase 1 complete — purchasing and inventory live in production.

Deployed: 2026-05-29
Changes: See CHANGELOG.md v1.0.0
PR: #NNN"

# Push the tag to the remote
git push origin v1.0.0

# Verify the tag appears on the remote
git ls-remote --tags origin
```

---

## 5. Tag Annotation Requirements

Every annotated tag message must include:
- **Version** — matches the tag name.
- **Deployment date** — when this was deployed to the target environment.
- **Brief description** — what this release contains or represents.
- **CHANGELOG reference** — where to find the full change list.
- **PR reference** — the PR number(s) included in this release.

---

## 6. GitHub Releases

For significant milestones (phase completions, major version releases), create a
GitHub Release from the tag:

```bash
gh release create v1.0.0 \
  --title "Phase 1 — Purchasing and Inventory" \
  --notes "$(cat << 'EOF'
## Phase 1 Release

First production deployment. Includes purchasing, inventory, and basic accounting.

### What's Included
- Purchase order management
- Inventory with lot tracking
- Basic financial accounting

### Deployment
Deployed to production: 2026-05-29

See CHANGELOG.md for full details.
EOF
)"
```

---

## 7. Rollback Using Tags

To roll back to a prior release:

```bash
# Identify the target tag
git tag -l | sort -V

# Check out the tagged commit on a branch for review
git checkout -b rollback/v1.0.0 v1.0.0

# Review, test, then deploy this state
# Document the rollback in IMPLEMENTATION_HISTORY.md
```

---

## 8. Recording Releases

Every production release tag must be recorded in `IMPLEMENTATION_HISTORY.md` with:
- The tag name.
- The deployment date.
- What was included in the release.
- Who approved and deployed.

---

*This standard is owned by the Software Factory. Changes require a PR with a decision log entry.*
