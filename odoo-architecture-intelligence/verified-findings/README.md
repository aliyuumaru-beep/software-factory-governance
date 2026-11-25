# OAIS — Verified Findings

**Status:** REGISTERED — no findings yet
**Decision:** DEC-013

This directory holds findings that have been verified beyond the RETRIEVED level.

## Subdirectories

| Directory | Verification standard |
|-----------|----------------------|
| `lab-verified/` | Behaviour reproduced in an isolated Odoo environment |
| `independently-reviewed/` | Reviewed by an independent technical reviewer |

## When to add a finding here

Add to `lab-verified/` when you have:
1. A specific, testable claim about Odoo behaviour.
2. A reproducible test script or procedure (stored in `architecture-lab/`).
3. Evidence that the behaviour was observed in an isolated Odoo environment.

Add to `independently-reviewed/` when:
1. A finding from `intelligence/` has been reviewed by an independent G1 session or technical reviewer.
2. The reviewer has explicitly confirmed or corrected the finding.

## Template

```
<!--
oais:type: verified-finding
oais:status: LAB_VERIFIED | INDEPENDENTLY_REVIEWED
oais:version: [Odoo version]
oais:edition: [Community / Enterprise / Both]
oais:domain: [domain]
oais:lab-ref: [architecture-lab/ experiment file, if applicable]
oais:reviewer: [description of reviewer]
oais:date: [ISO date]
-->
```
