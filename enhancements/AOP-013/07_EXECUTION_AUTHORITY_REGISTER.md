# Execution Authority Register

---

**Document:** EAR-NADF-001
**Project:** NADF ERP MVP
**Version:** 1.1
**Date Initialised:** 2026-06-25
**Last Revised:** 2026-06-25 — G3-CON-001 remediation: Mode field added to register format, all entries, and template
**Maintained by:** A1-NADF Master Orchestrator
**Status:** Active — AOP-013 Pilot

---

## 1. Purpose

This register records all execution authority grants, denials, and revocations for the NADF project pod. It is the authoritative audit trail for D2 execution actions under Agent OS v2.0.

This register is append-only. Records are never deleted. Status transitions are logged with date and reason.

---

## 2. Register Format

Each entry follows this structure:

```
Authority ID         : EA-{PROJECT}-WP{XX}-{NNN}
Authority Class      : EA-{N} — {Class Name}
Project              : {PROJECT}
Work Package         : WP-{XX} — {WP Name}
Requested By         : D2
Request Date         : ISO date
Authorized Actions   :
  - {action}
G1 Review            : {APPROVED | DENIED | CONDITIONAL | N/A} — {date} — {brief rationale}
G2 Review            : {APPROVED | DENIED | CONDITIONAL | N/A} — {date} — {brief rationale}
G3 Review            : {APPROVED | DENIED | CONDITIONAL | N/A} — {date} — {brief rationale}
A1 Decision          : {EXECUTION AUTHORITY GRANTED | DENIED | REVOKED}
A1 Decision Date     : ISO date
A1 Rationale         : {rationale}
Validity Scope       : WP-{XX} only
Conditions           : {any conditions from conditional approvals, or NONE}
Mode                 : Advisory | Binding | Pre-Pilot
Status               : {Active | Executed | Revoked | Expired | Denied}
Execution Date       : ISO date (when executed) or —
Outcome              : {result description} or —
```

**Mode field values:**
- `Pre-Pilot` — entry created retrospectively for v1.0 operations before the AOP-013 pilot window
- `Advisory` — entry created during the AOP-013 pilot window (WP-03/WP-04); decision is non-binding; D2 proceeds under v1.0 Human Sponsor flow
- `Binding` — entry created after Sponsor activates binding mode; decision gates D2 execution

---

## 3. Authority Register — NADF

---

### Entry 001 — Pilot Demonstration Entry

```
Authority ID         : EA-NADF-WP01-001
Authority Class      : EA-4 — Module Installation Authority
Project              : NADF
Work Package         : WP-01 — Foundation Hardening
Requested By         : D2
Request Date         : 2026-06-25 (retrospective — modules installed under v1.0)
Authorized Actions   :
  - Install mis_builder 17.0.1.5.0
  - Install purchase_request 17.0.2.3.4
  - Install helpdesk_mgmt 17.0.1.10.4
  - Install report_xlsx 17.0.1.0.2 (dependency)
  - Install date_range 17.0.1.2.1 (dependency)
G1 Review            : APPROVED — 2026-06-25 — All modules on OCA approved list; deps verified; no conflicts
G2 Review            : APPROVED — 2026-06-25 — Traceable to WP-01 AC-WP01-01/02; MODULE_REGISTRY updated
G3 Review            : APPROVED — 2026-06-25 — No new external integrations; rollback confirmed (uninstall path)
A1 Decision          : EXECUTION AUTHORITY GRANTED
A1 Decision Date     : 2026-06-25
A1 Rationale         : All G1/G2/G3 reviews approved; EA-4 scope; modules verified on OCA; no escalation trigger
Validity Scope       : WP-01 only
Conditions           : NONE
Mode                 : Pre-Pilot
Status               : Executed
Execution Date       : 2026-06-25 (actual install date per NADF project records)
Outcome              : mis_builder, purchase_request, helpdesk_mgmt + deps successfully installed; registry exit 0; 100 modules loaded; AC-WP01-06 PASS
```

---

### Entry 002 — Retrospective: 2FA Configuration

```
Authority ID         : EA-NADF-WP01-002
Authority Class      : EA-3 — Configuration Authority
Project              : NADF
Work Package         : WP-01 — Foundation Hardening
Requested By         : D2
Request Date         : 2026-06-25 (retrospective)
Authorized Actions   :
  - Set auth_totp.policy = required (global 2FA enforcement)
G1 Review            : APPROVED — 2026-06-25 — Consistent with platform profile; no arch side effects
G2 Review            : APPROVED — 2026-06-25 — Traceable to WP-01 security AC; documented in IMPLEMENTATION_HISTORY
G3 Review            : APPROVED — 2026-06-25 — Strengthens security posture; exceeds minimum requirement; reversible via ir.config_parameter
A1 Decision          : EXECUTION AUTHORITY GRANTED
A1 Decision Date     : 2026-06-25
A1 Rationale         : Security configuration; all reviews approved; strengthens posture; DEC-2FA-002 logged
Validity Scope       : WP-01 only
Conditions           : NONE
Mode                 : Pre-Pilot
Status               : Executed
Execution Date       : 2026-06-25 (actual date per NADF records)
Outcome              : TOTP 2FA enabled globally; DEC-2FA-002 logged; AC passed
```

---

### Entry 003 — Template: Open Slot for WP-03 (First Pilot Entry)

> SUPERSESSION NOTICE: Original template referenced WP-02. Superseded by Sponsor Decision
> AOP-013-SD-001 Condition 4. Pilot window is WP-03 and WP-04. Mode is Advisory.

```
Authority ID         : EA-NADF-WP03-001
Authority Class      : [To be assigned by G1]
Project              : NADF
Work Package         : WP-03 — [WP Name TBC]
Requested By         : D2
Request Date         : [Date of request]
Authorized Actions   :
  - [To be specified in authority request]
G1 Review            : PENDING
G2 Review            : PENDING
G3 Review            : PENDING
A1 Decision          : PENDING
A1 Decision Date     : —
A1 Rationale         : —
Validity Scope       : WP-03 only
Conditions           : —
Mode                 : Advisory
Status               : Pending Review
Execution Date       : —
Outcome              : —
```

---

## 4. Denied Authorities

No denied authorities at this time.

---

## 5. Revoked Authorities

No revoked authorities at this time.

---

## 6. Register Statistics

| Metric | Value |
|--------|-------|
| Total grants issued | 2 (retrospective) |
| Active grants | 0 |
| Executed grants | 2 |
| Denied | 0 |
| Revoked | 0 |
| Pending | 1 (template) |

---

## 7. Usage Instructions for Future Entries

1. A1 creates a new entry when D2 submits an authority request.
2. Set Status: Pending Review.
3. Route to G1/G2/G3 per approval matrix.
4. Update each reviewer's field as reviews come in.
5. Issue A1 decision and update Status: Active (GRANTED) or Denied.
6. After D2 execution, update Status: Executed and record Outcome.
7. On revocation, update Status: Revoked with date and reason.

---

## 8. Template for New Entries

Copy this block for each new authority entry:

```
Authority ID         : EA-{PROJECT}-WP{XX}-{NNN}
Authority Class      : EA-{N} — {Class Name}
Project              : {PROJECT}
Work Package         : WP-{XX} — {WP Name}
Requested By         : D2
Request Date         : YYYY-MM-DD
Authorized Actions   :
  - {action 1}
  - {action 2}
G1 Review            : PENDING
G2 Review            : PENDING
G3 Review            : PENDING
A1 Decision          : PENDING
A1 Decision Date     : —
A1 Rationale         : —
Validity Scope       : WP-{XX} only
Conditions           : —
Mode                 : Advisory
Status               : Pending Review
Execution Date       : —
Outcome              : —
```

---

*Execution Authority Register — NADF Project Pod*
*Maintained by A1-NADF Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
