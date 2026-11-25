# AGENTS.md — rules for every developer and AI coding tool

This repository is governed by the Software Factory
(<https://github.com/aliyuumaru-beep/software-factory-governance>, SPEC-GOV-ENF-001).
These rules apply to humans, Claude Code, Cursor, Copilot, Codex and any other tool.

1. Install the gateway once per machine (run interactively — follow the installer prompts):
   `git clone https://github.com/aliyuumaru-beep/software-factory-governance && cd software-factory-governance && gov install`
   If `gov` is already installed, skip this step and verify with `gov --version`.
2. Read `CLAUDE.md` and the files listed under `briefing_docs` in `.governance.json` before changing anything.
3. Never commit to `main`. Work on a feature branch.
4. No spec, no code: the work item (WP-/DEC-/SPEC-…) must exist in the repo docs. `gov start <WORK-ITEM>`.
5. Never change a live database without a fresh backup and the sponsor's go-ahead.
6. Update the governance docs (`required_doc_updates` in `.governance.json`) with the change.
7. Run `gov review` — G1 Architecture, G2 Quality, G3 Security review the change as independent agents.
8. Open a PR citing the work item. GitHub runs `governance / gate` as a CI check. Note: this check
   is a Phase 4 deliverable and is not yet required (see DEC-014). Until Phase 4 activates it,
   the check will appear in CI but will not block merges.
