# AOP-013 — Architecture Impact Assessment

---

**Document:** AIA-AOP-013
**Enhancement:** AOP-013 Execution Authority Framework
**Version:** 1.0
**Date:** 2026-06-25
**Author:** G1 Architecture & Odoo Governance

---

## 1. Purpose

This document assesses the architectural impact of implementing AOP-013 on the existing Agent OS v1.0 architecture. It identifies what changes, what does not change, what must be added, and what risks arise.

---

## 2. Current Architecture (Agent OS v1.0)

```
Human Sponsor
     │
     ▼
A1 Master Orchestrator
     │
     ├── G1 Architecture & Odoo Governance
     ├── G2 Quality & Documentation Governance
     ├── G3 Security & Change Governance
     │
     ├── D1 Functional Architect
     ├── D2 Solution Builder
     ├── D3 Quality & Validation
     └── D4 Knowledge & Documentation
```

**Flow for execution:**
1. D2 identifies work to execute
2. A1 requests human confirmation
3. Human Sponsor confirms
4. D2 executes

**Architectural characteristics:**
- Human Sponsor is synchronous gatekeeper for execution
- Governance agents provide review but not authority
- A1 coordinates but does not issue binding decisions
- No formal authority register exists
- No execution authority lifecycle management

---

## 3. Target Architecture (Agent OS v2.0)

```
Human Sponsor
     │ (EA-6, Scope, Budget, Production, Portfolio only)
     ▼
A1 Master Orchestrator
     │ (issues EXECUTION AUTHORITY GRANTED/DENIED/REVOKED)
     │
     ├── G1 Architecture & Odoo Governance (classifies, reviews)
     ├── G2 Quality & Documentation Governance (reviews)
     ├── G3 Security & Change Governance (reviews)
     │
     ├── D1 Functional Architect
     ├── D2 Solution Builder (verifies authority, references EA-ID)
     ├── D3 Quality & Validation
     └── D4 Knowledge & Documentation
```

**Flow for execution:**
1. D2 identifies work to execute
2. D2 requests authority from A1
3. G1/G2/G3 complete parallel reviews
4. A1 issues authority decision
5. D2 verifies authority ID
6. D2 executes within bounded scope
7. Human Sponsor informed

---

## 4. Structural Changes

### 4.1 New Components

| Component | Type | Purpose |
|-----------|------|---------|
| Execution Authority Register | Governance artifact | Records all authority grants, denials, and revocations |
| Authority Classification Standard | Standard | Defines EA-1 through EA-6 |
| Authority Decision Log | Audit log | Immutable record of A1 authority decisions |
| Authority lifecycle in A1 | A1 capability | GRANT / DENY / REVOKE decisions |

### 4.2 Modified Components

| Component | Current State | Modified State |
|-----------|--------------|----------------|
| A1 role | Coordinator | Coordinator + Authority Issuer |
| G1 role | Technical reviewer | Technical reviewer + Risk Classifier |
| G2 role | Quality reviewer | Quality reviewer + Traceability Validator |
| G3 role | Security reviewer | Security reviewer + Change Impact Validator |
| D2 role | Executes on human approval | Executes on authority grant |
| AUTHORITY_MATRIX.md | Stub (7 lines) | Full matrix per EA-1 through EA-6 |
| ESCALATION_POLICY.md | E1-E6 defined | E1-E6 retained; EA-6 added as human-required |
| ACTIVE_AGENT_CONFIGURATION.md | Version 1.0 | Version 2.0 |

### 4.3 Unchanged Components

| Component | Reason Unchanged |
|-----------|-----------------|
| Claude Code runtime permissions | Not in scope — OS-level control |
| Project pod structure (D1-D4) | Structure retained |
| Governance agent structure (G1-G3) | Structure retained; roles extended |
| Escalation policy triggers E1-E6 | All retained without change |
| EA-6 human requirement | Production authority remains with Human Sponsor |
| Per-project work packages | NADF/FAMOIL/WAMACARE WPs not affected |
| Platform profiles | Unchanged |

---

## 5. Agent Prompt Impact

The following agent prompts require revision for Agent OS v2.0:

| Prompt File | Required Change |
|-------------|----------------|
| `PROMPT_A1_SOFTWARE_FACTORY_ORCHESTRATOR.md` | Add: authority issuance protocol, GRANT/DENY/REVOKE decisions, authority register maintenance |
| `PROMPT_G1_ARCHITECTURE_ODOO_GOVERNANCE.md` | Add: authority class classification, architectural preconditions, architectural constraints block |
| `PROMPT_G2_QUALITY_DOCUMENTATION_GOVERNANCE.md` | Add: traceability validation against authority request, documentation completeness gate |
| `PROMPT_G3_SECURITY_CHANGE_GOVERNANCE.md` | Add: change impact validation, rollback confirmation, risk exposure assessment for authority request |
| `PROMPT_D2_SOLUTION_BUILDER.md` | Add: authority verification before execution, authority ID reference in all execution actions, halt-on-expiry rule |

Prompts not requiring change: D1, D3, D4 (their roles do not interact directly with authority grants).

---

## 6. Documentation Architecture Impact

### New Documents Required

| Document | Location |
|----------|----------|
| EXECUTION_AUTHORITY_REGISTER.md | Per project pod root |
| AUTHORITY_CLASSIFICATION_STANDARD.md | `Autonomous-agent-Team/docs/` |
| AUTHORITY_DECISION_LOG.md | Per project pod root |

### Existing Documents Requiring Revision

| Document | Change |
|----------|--------|
| `Autonomous-agent-Team/docs/02_AUTHORITY_MATRIX.md` | Replace stub with full EA matrix |
| `Autonomous-agent-Team/docs/03_ESCALATION_POLICY.md` | Add EA-6 human requirement clause |
| `Autonomous-agent-Team/ACTIVE_AGENT_CONFIGURATION.md` | Increment to v2.0, add authority settings |
| `Autonomous-agent-Team/docs/01_SOFTWARE_FACTORY_AGENT_FRAMEWORK.md` | Add authority grant flow to framework description |

---

## 7. Configuration Architecture Impact

`ACTIVE_AGENT_CONFIGURATION.md` requires the following new fields for v2.0:

```
Agent OS Version: 2.0
Execution Authority: Enabled
Authority Classes: EA-1 through EA-6
EA-6 Requires Human: true
Authority Register: Per Project Pod
Authority Decision Log: Per Project Pod
Authority Validity: Work Package Scope
```

---

## 8. Data Architecture Impact

### Execution Authority Register

Each authority grant record contains:

```
Authority ID         : EA-{PROJECT}-WP{XX}-{NNN}
Authority Class      : EA-1 | EA-2 | EA-3 | EA-4 | EA-5 | EA-6
Project              : NADF | FAMOIL | WAMACARE
Work Package         : WP-XX
Authorized Actions   : [list]
G1 Approval          : Approved / Denied / N/A with date
G2 Approval          : Approved / Denied / N/A with date
G3 Approval          : Approved / Denied / N/A with date
A1 Decision          : GRANTED | DENIED | REVOKED
Decision Date        : ISO date
Validity Scope       : WP reference
Status               : Active | Executed | Revoked | Expired
Outcome              : [result after execution]
```

This is a flat, append-only register. Records are never deleted. Status transitions are logged.

---

## 9. Architectural Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Authority scope creep | D2 acts beyond granted scope | Authority ID must be referenced per action; scope is explicit in register |
| Governance review bottleneck | G1/G2/G3 become new bottleneck | Reviews are designed to be concurrent; low-risk classes (EA-1/EA-2) require fewer reviewers |
| Register staleness | Expired authorities remain Active | Status transitions must be enforced; A1 responsible for lifecycle |
| Prompt non-compliance | Agents ignore authority requirement | Authority check is a pre-condition in D2 prompt; non-reference is a governance violation |
| Authority register location | Per-pod placement risks drift | Standard location and naming defined in Authority Classification Standard |

---

## 10. Architectural Assessment

**Assessment:** AOP-013 is architecturally compatible with Agent OS v1.0.

The enhancement is additive. No existing architectural components are removed. The human approval gate is formally replaced by an equivalent multi-reviewer governance gate. The escalation policy is strengthened, not weakened.

The primary architectural risk is prompt non-compliance during transition. This is addressed in the Migration Plan and Pilot Plan.

**Architectural Recommendation:** Approve for implementation.

---

*AOP-013 Architecture Impact Assessment — G1 Architecture & Odoo Governance*
*Software Factory Governance Authority — 2026-06-25*
