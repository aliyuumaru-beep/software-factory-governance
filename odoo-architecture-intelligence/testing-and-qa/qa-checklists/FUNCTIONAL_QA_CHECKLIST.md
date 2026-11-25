# Functional QA Checklist

**Status:** REGISTERED — to be expanded during Phase 2
**Decision:** DEC-013

Use this checklist before delivering any Software Factory feature to the sponsor for UAT.

## General

- [ ] Feature works as specified in the work package acceptance criteria
- [ ] Feature tested with realistic data, not just demo data
- [ ] All user roles tested (what they CAN do and what they CANNOT do)
- [ ] Edge cases tested (empty records, zero quantities, missing required fields)
- [ ] No browser console errors during normal use

## Workflows

- [ ] State transitions work correctly and in sequence
- [ ] Automated actions trigger as expected
- [ ] Email notifications sent where required
- [ ] Scheduled actions run without error

## Reporting

- [ ] Reports render without error
- [ ] Report data matches the underlying records
- [ ] Totals and aggregations are correct

## Security

- [ ] Portal users cannot see internal records
- [ ] Users outside the allowed group cannot access the feature
- [ ] No unintended data exposure in list views

---

*Expand and verify this checklist during Phase 2 from official testing documentation.*
