# Pull Request

## Change Type
<!-- Select exactly one -->
- [ ] `feat` — New feature, module, or capability
- [ ] `fix` — Bug fix or defect correction
- [ ] `refactor` — Code restructuring without behaviour change
- [ ] `docs` — Documentation-only change
- [ ] `security` — Security fix or access control change
- [ ] `ops` — Operational change (backup, deployment, infrastructure)
- [ ] `chore` — Dependency update, config change, housekeeping
- [ ] `test` — Test addition or correction
- [ ] `governance` — Governance documents, standards, or templates

---

## Description
<!-- What does this PR do and WHY was it needed? Do not describe what the code does — describe the reason. -->



---

## Governance Impact Analysis

*Every dimension must be addressed. "Not impacted — [reason]" is a valid answer.  
Full definition: `docs/GOVERNANCE_IMPACT_ANALYSIS.md`*

### 1. Code Impact
<!-- What code changed? Are there tests? What is the test result? -->


### 2. Documentation Impact
<!-- Which docs must be updated? Are they included in this PR? -->


### 3. Decision Log Impact
<!-- Was an architectural, security, data model, integration, or governance decision made?  
     If yes: is the DECISION_LOG.md entry included in this PR? Entry ID: -->


### 4. Roadmap Impact
<!-- Does this complete, add, or change a roadmap item?  
     If yes: has ROADMAP.md been updated in this PR? -->


### 5. Registry Impact
<!-- Are any new modules, components, services, integrations, automations, or scripts introduced?  
     If yes: is the MODULE_REGISTRY.md entry included in this PR? Entry ID: -->


### 6. Onboarding Impact
<!-- Does this change how the system is understood, set up, or maintained?  
     If yes: has onboarding documentation been updated? -->


### 7. Security Impact
<!-- Does this touch authentication, authorization, access control, user data, secrets, or external APIs?  
     If yes: describe the security review performed. -->


### 8. Backup/Recovery Impact
<!-- Does this change what must be backed up, or how restore works?  
     If yes: has BACKUP_RECOVERY_STANDARD been reviewed and ops docs updated? -->


### 9. Rollback Plan
<!-- How is this PR rolled back if it causes problems in production?  
     For DB schema changes, data migrations, or infrastructure changes — provide detail. -->


### 10. Testing Evidence
<!-- What confirms this works correctly? Test output, screenshots, manual verification steps. -->


---

## Repository Memory Review

*Confirm you have read the relevant project memory documents:*

- [ ] `DECISION_LOG.md` — this PR does not reverse a prior logged decision (or a new entry is included)
- [ ] `IMPLEMENTATION_HISTORY.md` — reviewed for context on prior work in this area
- [ ] `MODULE_REGISTRY.md` — all new components in this PR are registered
- [ ] `ROADMAP.md` — this change is within current roadmap scope

---

## New Module / Component / Service Checklist

*Complete only if this PR introduces a new module, component, service, integration, automation, or script.*

- [ ] Entry added to `MODULE_REGISTRY.md` (Entry ID: `___`)
- [ ] Decision log entry created if this was an architectural choice (Entry ID: `___`)
- [ ] Onboarding documentation updated if this changes system understanding
- [ ] `.gitignore` updated if this introduces files that should not be committed

---

## Decision Log Review

*Complete only if an architectural, security, data model, integration, or governance decision was made in this PR.*

- [ ] Entry added to `DECISION_LOG.md` using `templates/decision_log_template.md`
- [ ] Decision log entry referenced above in GIA Section 3
- [ ] Decision status: `ACTIVE`

Decision Log Entry ID: `___`

---

## Final Governance Declaration

- [ ] All mandatory checklist items above are complete.
- [ ] All documentation impacted by this PR has been updated and is included in this PR.
- [ ] This PR satisfies the Software Factory Governance Standard.
- [ ] I am not aware of any outstanding governance defect introduced by this PR.

> **I confirm that this PR satisfies the Software Factory Governance Standard.**
>
> Signed: _________________________ Date: _____________
