# Architecture Lab — Experiment Template

<!--
oais:type: lab-experiment
oais:status: DRAFT | COMPLETE
oais:odoo-version: [17]
oais:edition: Community
oais:domain: [domain]
oais:date: [ISO date]
oais:result-ref: [verified-findings/lab-verified/filename.md]
-->

# [Experiment title]

**Purpose:** [What claim or behaviour is being tested?]
**Odoo Version:** 17 Community
**Environment:** [Docker image tag, e.g. `odoo:17.0`]
**Date:** [ISO date]

---

## Hypothesis

[The specific claim being tested. Phrased as a testable statement.]

## Setup

[Steps to set up the test environment. Must be reproducible from scratch.]

```
# Example:
docker run -d -p 8069:8069 --name odoo17-lab odoo:17.0
```

## Test procedure

[Exact steps to reproduce the test. Numbered list.]

1.
2.
3.

## Expected result

[What should happen if the hypothesis is correct.]

## Actual result

[What actually happened. Include error messages, screenshots if applicable.]

## Conclusion

**Hypothesis:** CONFIRMED / REFUTED / INCONCLUSIVE

[Brief explanation.]

## Finding

[Link to `verified-findings/lab-verified/` entry created from this experiment.]
