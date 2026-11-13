# Software Factory governance — applies to EVERY session on this machine

The sponsor (Aliyu Umaru) requires that all software work — by AI or humans — goes through the
Software Factory governance gateways (SPEC-GOV-ENF-001, repo `software-factory-governance`).
User-level hooks enforce this whatever folder a session starts in. Do not try to work around a
governance block; explain it to the user and follow the process.

Before changing anything in a software project:
1. If the git repo belongs to `aliyuumaru-beep` and has no `.governance.json`, it must be onboarded
   (`gov onboard <path> --pod <POD>`), committed on a branch, before other work.
2. Run `gov status` in the repo and read every briefing doc it lists (pod CLAUDE.md, project state,
   next action, approval register).
3. Never work on `main`; create a feature branch.
4. No spec, no code. The work item (WP-/DEC-/SPEC-…) must exist in the repo docs: `gov start <ID>`.
   When the user asks for a new feature with no spec, write the spec/decision entry first, get the
   user's approval for it, then code.
5. Live databases: drill copy first; backup before any live change; the user must confirm.
6. Update the governance docs required by `.governance.json` in the same branch.
7. `gov review` fires G1 (Architecture/Odoo), G2 (Quality/Docs), G3 (Security/Change) as independent
   Claude instances. Report their verdicts to the user verbatim. Never write verdicts yourself.
8. Push / PR only when `gov verify` says READY. Merge is the sponsor's decision; GitHub requires the
   `governance / gate` check (the same G1–G3 reviews in CI) for everyone, admins included.
9. For Odoo workflow features, test every role (including what each must NOT be able to do).
