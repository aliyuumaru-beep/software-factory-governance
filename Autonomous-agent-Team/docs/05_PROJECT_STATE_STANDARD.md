# PROJECT_STATE_STANDARD.md

## Purpose

Defines the mandatory project state file for each Project Pod.

PROJECT_STATE.md is the single source of truth for a specific project.

Each Project Pod must maintain its own PROJECT_STATE.md.

The platform profile is defined per Project Pod, not globally.

---

# Template

## Project Identity

Project Name:

Project Code:

Client:

Repository:

Project Pod:

---

## Platform

Platform:

Platform Version:

Platform Edition:

Platform Profile:

Example:

Platform: Odoo

Platform Version: 17

Platform Edition: Community

Platform Profile: PLATFORM_PROFILE_ODOO17_COMMUNITY.md

---

## Current Status

Current Phase:

Current Milestone:

Current Work Package:

Project Status:

* NOT_STARTED
* IN_PROGRESS
* GOVERNANCE_REVIEW
* BLOCKED
* COMPLETE

Overall Completion %:

---

## Completed Milestones

| Milestone | Completion Date | Governance Status |
| --------- | --------------- | ----------------- |

---

## Active Work Package

Work Package ID:

Title:

Owner:

Status:

Start Date:

Target Completion Date:

---

## Next Work Package

Work Package ID:

Title:

Milestone:

Priority:

---

## Open Risks

| ID | Description | Severity | Owner | Status |
| -- | ----------- | -------- | ----- | ------ |

---

## Open Escalations

| ID | Category | Description | Status |
| -- | -------- | ----------- | ------ |

---

## Governance Status

| Governance Area                       | Status | Last Review |
| ------------------------------------- | ------ | ----------- |
| G1 Architecture & Platform Governance |        |             |
| G2 Quality & Documentation Governance |        |             |
| G3 Security & Change Governance       |        |             |

---

## Repository Status

Branch:

Last Commit:

Last Push:

Open PR:

Repository Compliance:

* COMPLIANT
* CONDITIONAL
* NON-COMPLIANT

---

## Continuity Notes

Current Context:

Immediate Next Action:

Known Constraints:

Important Decisions:

---

## Last Updated

Date:

Updated By:

Update Reason:

---

# Rules

1. Every Project Pod must maintain its own PROJECT_STATE.md.
2. Platform Profile must be defined per Project Pod.
3. Orchestrator must read PROJECT_STATE.md before acting.
4. Delivery agents must follow the Platform Profile stated in PROJECT_STATE.md.
5. PROJECT_STATE.md must be updated whenever:

   * Work Package changes
   * Milestone changes
   * Governance status changes
   * Repository status changes
   * Escalation status changes
6. PROJECT_STATE.md supersedes chat history.
