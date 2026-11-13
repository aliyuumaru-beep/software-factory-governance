#!/usr/bin/env python3
"""Software Factory governance gateway (SPEC-GOV-ENF-001).

One engine, four callers:
  * Claude Code hooks   gov hook session-start | pre-tool | stop   (stdin JSON)
  * Developers / AI     gov status | start | review | verify | onboard | protect
  * Git hooks           gov githook pre-commit | pre-push
  * GitHub CI           gov ci-docs-gate | review --ci

Standard library only; runs on macOS system python3 (3.9+).
"""
import argparse
import concurrent.futures
import datetime
import glob
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys

VERSION = "1.0.0"
HOME = os.path.expanduser("~")
GOV_HOME = os.environ.get("GOV_HOME", os.path.join(HOME, ".claude", "governance"))
CONFIG_PATH = os.path.join(GOV_HOME, "config.json")
STATE_DIR = os.path.join(GOV_HOME, "state")
LOG_DIR = os.path.join(GOV_HOME, "logs")
ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
MARKER = ".governance.json"
REVIEWERS = ("G1", "G2", "G3")
PASSING = ("APPROVED", "APPROVED_WITH_CONDITIONS")
VERDICT_RE = re.compile(
    r"VERDICT:\s*\**\s*(APPROVED[ _]WITH[ _]CONDITIONS|APPROVED|REJECTED|ESCALATE)", re.I)
DEFAULT_WORK_ITEM = r"\b((?:WP|DEC|SPEC|GOV|REQ)-[A-Z0-9][A-Z0-9_.-]*[A-Z0-9])\b"
READ_CMDS = ("cat", "head", "tail", "sed", "less", "more", "bat", "nl", "awk")
REVIEW_CLI_VERSION = "2.1.312"  # CI installs exactly this; local runs warn when they differ (L4 is pinned)


# ─────────────────────────────── utilities ────────────────────────────────

def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def ensure_dirs():
    for d in (GOV_HOME, STATE_DIR, LOG_DIR):
        os.makedirs(d, exist_ok=True)


def log(name, record):
    try:
        ensure_dirs()
        record = dict(record, ts=now())
        with open(os.path.join(LOG_DIR, name), "a") as fh:
            fh.write(json.dumps(record) + "\n")
    except OSError:
        pass


def load_json(path, default=None):
    try:
        with open(path) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")
    os.replace(tmp, path)


def config():
    cfg = load_json(CONFIG_PATH, {}) or {}
    cfg.setdefault("owner_patterns", [])
    cfg.setdefault("repos", [])
    return cfg


def git(repo, *args, check=False):
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(p.stderr.strip() or "git %s failed" % " ".join(args))
    return p.stdout.strip() if p.returncode == 0 else ""


def expand(path, base=None):
    path = os.path.expanduser(os.path.expandvars(path))
    if base and not os.path.isabs(path):
        path = os.path.join(base, path)
    return os.path.realpath(path)


def find_git_root(path):
    cur = path if os.path.isdir(path) else os.path.dirname(path)
    while True:
        if os.path.exists(os.path.join(cur, ".git")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


# ───────────────────────────── repo context ───────────────────────────────

class Repo(object):
    """A governed repository (has .governance.json)."""

    def __init__(self, root):
        self.root = root
        self.cfg = load_json(os.path.join(root, MARKER), {}) or {}
        c = self.cfg
        self.pod = c.get("pod", os.path.basename(root))
        self.protected = c.get("protected_branches", ["main"])
        self.briefing = c.get("briefing_docs", ["CLAUDE.md"])
        self.code_paths = c.get("code_paths", [])
        self.required_docs = c.get("required_doc_updates", [])
        self.spec_sources = c.get("spec_sources", ["docs", "DECISION_LOG.md"])
        self.work_item_re = re.compile(c.get("work_item_pattern", DEFAULT_WORK_ITEM))
        self.live_dbs = c.get("live_databases", [])
        self.backup_dirs = c.get("backup_dirs", [])
        self.backup_age = float(c.get("backup_max_age_hours", 6))
        self.default_branch = c.get("default_branch", self.protected[0] if self.protected else "main")

    # git-level helpers -----------------------------------------------------
    @property
    def gitdir(self):
        d = git(self.root, "rev-parse", "--git-common-dir")
        return expand(d, self.root) if d else os.path.join(self.root, ".git")

    def branch(self):
        return git(self.root, "branch", "--show-current")

    def head(self):
        return git(self.root, "rev-parse", "HEAD")

    def base_ref(self):
        for ref in ("origin/" + self.default_branch, self.default_branch):
            if git(self.root, "rev-parse", "--verify", "-q", ref):
                return ref
        return None

    def merge_base(self):
        ref = self.base_ref()
        return git(self.root, "merge-base", ref, "HEAD") if ref else ""

    def changed_since_base(self, include_worktree=False):
        mb = self.merge_base()
        files = set()
        if mb:
            files.update(f for f in git(self.root, "diff", "--name-only", mb, "HEAD").splitlines() if f)
        if include_worktree:
            files.update(f for f in git(self.root, "diff", "--name-only", "HEAD").splitlines() if f)
            files.update(f for f in git(self.root, "diff", "--name-only", "--cached").splitlines() if f)
        return files

    def rel(self, path):
        try:
            return os.path.relpath(expand(path), self.root)
        except ValueError:
            return path

    def is_code(self, relpath):
        return any(relpath == p.rstrip("/") or relpath.startswith(p.rstrip("/") + "/")
                   for p in self.code_paths)

    # tickets & verdicts ----------------------------------------------------
    def ticket_path(self, branch=None):
        b = (branch or self.branch() or "DETACHED").replace("/", "__")
        return os.path.join(self.gitdir, "governance", "tickets", b + ".json")

    def ticket(self, branch=None):
        return load_json(self.ticket_path(branch))

    def verdict_dir(self, sha=None):
        return os.path.join(self.gitdir, "governance", "reviews", sha or self.head())

    def verdicts(self, sha=None):
        out = {}
        for r in REVIEWERS:
            v = load_json(os.path.join(self.verdict_dir(sha), r + ".json"))
            if v:
                out[r] = v
        return out

    def work_item_exists(self, item):
        pat = re.escape(item)
        for src in self.spec_sources:
            p = os.path.join(self.root, src)
            if not os.path.exists(p):
                continue
            cmd = ["grep", "-rlqE", r"(^|[^A-Za-z0-9-])%s([^A-Za-z0-9-]|$)" % pat, p]
            if subprocess.run(cmd, capture_output=True).returncode == 0:
                return True
        return False

    def live_db_backup_ok(self, db):
        newest = 0.0
        for d in self.backup_dirs:
            d = expand(d)
            for path in glob.glob(os.path.join(d, "*")):
                try:
                    newest = max(newest, os.path.getmtime(path))
                except OSError:
                    pass
        age_h = (datetime.datetime.now().timestamp() - newest) / 3600.0 if newest else None
        return (age_h is not None and age_h <= self.backup_age), age_h

    # readiness -------------------------------------------------------------
    def ship_problems(self):
        """Everything that must be true before push / PR (R7)."""
        problems = []
        b = self.branch()
        if not b:
            return ["HEAD is detached — check out a feature branch."]
        if b in self.protected:
            problems.append("You are on protected branch '%s'. Create a feature branch." % b)
        changed = self.changed_since_base()
        code = sorted(f for f in changed if self.is_code(f))
        t = self.ticket()
        if code and not t:
            problems.append("No spec, no code: no work item for branch '%s'. Run: gov start <WORK-ITEM>" % b)
        if code:
            missing = [d for d in self.required_docs if d not in changed]
            if missing:
                problems.append("Code changed but these governance docs were not updated on this branch: "
                                + ", ".join(missing))
        if git(self.root, "status", "--porcelain", "--untracked-files=no"):
            problems.append("Uncommitted changes — commit them before reviews (verdicts are per commit).")
        v = self.verdicts()
        for r in REVIEWERS:
            if r not in v:
                problems.append("%s review missing for HEAD %s. Run: gov review" % (r, self.head()[:8]))
            elif v[r]["decision"] not in PASSING:
                problems.append("%s decision is %s — address findings in %s"
                                % (r, v[r]["decision"], v[r].get("report", "")))
        return problems


def repo_for(path):
    """Return (Repo|None, unonboarded_root|None) for a filesystem path."""
    if not path:
        return None, None
    path = expand(path)
    root = find_git_root(path)
    if not root:
        return None, None
    if os.path.exists(os.path.join(root, MARKER)):
        return Repo(root), None
    remote = git(root, "remote", "get-url", "origin")
    owners = config()["owner_patterns"]
    if remote and any(o in remote for o in owners):
        return None, root
    return None, None


def registered_repos():
    out = []
    for r in config()["repos"]:
        r = expand(r)
        if os.path.exists(os.path.join(r, MARKER)):
            out.append(Repo(r))
    return out


# ───────────────────────────── session state ──────────────────────────────

def session_state(sid):
    # basename: a session id can never address a file outside STATE_DIR (G3 review 2026-11-13)
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", os.path.basename(sid or "")) or "nosession"
    path = os.path.join(STATE_DIR, safe + ".json")
    return path, (load_json(path, {}) or {})


def record_read(sid, path):
    repo, _ = repo_for(path)
    if not repo:
        return
    rel = repo.rel(path)
    if rel not in repo.briefing:
        return
    sp, st = session_state(sid)
    reads = st.setdefault("briefed", {}).setdefault(repo.root, [])
    if rel not in reads:
        reads.append(rel)
        save_json(sp, st)


def unread_briefing(sid, repo):
    _, st = session_state(sid)
    done = set(st.get("briefed", {}).get(repo.root, []))
    return [d for d in repo.briefing if d not in done and os.path.exists(os.path.join(repo.root, d))]


def touch_repo(sid, repo):
    sp, st = session_state(sid)
    touched = st.setdefault("touched", [])
    if repo.root not in touched:
        touched.append(repo.root)
        save_json(sp, st)


# ───────────────────────────── hook responses ─────────────────────────────

def respond(event, decision=None, reason=None, context=None):
    out = {}
    if event == "PreToolUse" and decision:
        out["hookSpecificOutput"] = {"hookEventName": event, "permissionDecision": decision,
                                     "permissionDecisionReason": reason}
    elif event == "SessionStart" and context:
        out["hookSpecificOutput"] = {"hookEventName": event, "additionalContext": context}
    elif event == "Stop" and decision == "block":
        out = {"decision": "block", "reason": reason}
    if out:
        print(json.dumps(out))


BANNER = "GOVERNANCE GATEWAY (SPEC-GOV-ENF-001) — "


def deny(reason, data, rule):
    log("decisions.jsonl", {"decision": "deny", "rule": rule, "tool": data.get("tool_name"),
                            "session": data.get("session_id"), "reason": reason[:500]})
    respond("PreToolUse", "deny", BANNER + reason)


def ask(reason, data, rule):
    log("decisions.jsonl", {"decision": "ask", "rule": rule, "tool": data.get("tool_name"),
                            "session": data.get("session_id"), "reason": reason[:500]})
    respond("PreToolUse", "ask", BANNER + reason)


def briefing_msg(repo, unread):
    return ("Before changing anything in %s (%s) you must read its governance briefing. "
            "Read these files in full, then retry: %s. Also run `gov status` to see branch, "
            "work item and review state." % (repo.root, repo.pod, ", ".join(unread)))


ONBOARD_MSG = ("%s is a Software Factory repository (owner matches) but is not onboarded to "
               "governance. Run `gov onboard %s --pod <POD-NAME>` and commit the result on a "
               "branch before making changes.")


# ───────────────────────────── command parsing ────────────────────────────

SEG_SPLIT = re.compile(r"\s*(?:&&|\|\||;|\n|\|(?!\|))\s*")


def segments(command, cwd):
    """Yield (cwd, argv, raw) for each simple command, following `cd`."""
    cur = cwd
    for raw in SEG_SPLIT.split(command or ""):
        raw = raw.strip()
        if not raw:
            continue
        try:
            argv = shlex.split(raw, comments=True)
        except ValueError:
            argv = raw.split()
        while argv and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", argv[0]):
            argv = argv[1:]
        if not argv:
            continue
        if argv[0] == "cd" and len(argv) > 1:
            cur = expand(argv[1], cur)
            continue
        yield cur, argv, raw


def git_subcmd(argv, cwd):
    """For `git [-C dir] sub ...` return (dir, sub, rest)."""
    if not argv or os.path.basename(argv[0]) != "git":
        return None
    i, d = 1, cwd
    while i < len(argv) and argv[i].startswith("-"):
        if argv[i] == "-C" and i + 1 < len(argv):
            d = expand(argv[i + 1], d)
            i += 2
            continue
        if argv[i] in ("-c",) and i + 1 < len(argv):
            i += 2
            continue
        i += 1
    if i >= len(argv):
        return None
    return d, argv[i], argv[i + 1:]


DB_WRITE_SQL = re.compile(r"\b(UPDATE|INSERT|DELETE|ALTER|DROP|TRUNCATE|CREATE|GRANT|REVOKE)\b", re.I)


def live_db_target(argv, raw):
    """Return (db, why) if this simple command can mutate a database, else None."""
    prog = os.path.basename(argv[0])
    if prog in ("python", "python3") and len(argv) > 1 and argv[1].endswith("odoo-bin"):
        prog, argv = "odoo-bin", argv[1:]
    if prog in ("odoo-bin", "odoo"):
        db = None
        for i, a in enumerate(argv):
            if a in ("-d", "--database") and i + 1 < len(argv):
                db = argv[i + 1]
            elif a.startswith("--database=") or a.startswith("-d="):
                db = a.split("=", 1)[1]
            elif a.startswith("-d") and len(a) > 2 and not a.startswith("--"):
                db = a[2:]
        mut = (any(a in ("-u", "-i", "--update", "--init", "shell") or a.startswith(("--update=", "--init="))
                   for a in argv[1:]))
        if db and mut:
            return db, "odoo-bin update/install/shell"
        return None
    if prog in ("dropdb", "pg_restore", "psql"):
        if prog == "psql":
            # Fail safe: psql reading SQL from stdin (`< file`, a pipe, a heredoc), from -f, or
            # interactively can mutate. Only a -c/--command with no write SQL, or -l, is read-only.
            if any(a in ("-l", "--list") for a in argv[1:]):
                return None
            has_cmd = any(a in ("-c", "--command") or a.startswith("--command=") for a in argv[1:])
            reads_input = ("<" in raw or any(a in ("-f", "--file") or a.startswith("--file=")
                                             for a in argv[1:]))
            if has_cmd and not reads_input and not DB_WRITE_SQL.search(raw):
                return None
            if "<" in argv:
                argv = argv[:argv.index("<")]
        dbs = [a.split("=", 1)[1] for a in argv if a.startswith("--dbname=")]
        for i, a in enumerate(argv):
            if a in ("-d", "--dbname") and i + 1 < len(argv):
                dbs.append(argv[i + 1])
        positional = [a for a in argv[1:] if not a.startswith("-")]
        dbs += positional
        return (dbs, prog) if dbs else None
    return None


# ──────────────────────────────── hooks ───────────────────────────────────

def hook_session_start(data):
    if os.environ.get("GOV_REVIEWER"):
        return
    repos = registered_repos()
    lines = [
        "SOFTWARE FACTORY GOVERNANCE IS ENFORCED on this machine (SPEC-GOV-ENF-001).",
        "Hooks will block work that skips the process. The process for any governed repo:",
        "  1. Read the repo's briefing docs (listed by `gov status <repo>`) before any change.",
        "  2. Work on a feature branch, never main.",
        "  3. No spec, no code: `gov start <WORK-ITEM>` (the WP-/DEC-/SPEC- id must exist in the repo docs).",
        "     If no spec exists, write/get approval for one first (docs edits are allowed).",
        "  4. Live databases: take a backup first; the user must confirm each mutating command.",
        "  5. Before push/PR: update governance docs, commit, then `gov review` — this fires G1",
        "     (Architecture/Odoo), G2 (Quality/Docs), G3 (Security/Change) as independent Claude",
        "     instances. All must APPROVE. ESCALATE (E1-E6) goes to the sponsor.",
        "  6. GitHub enforces the `governance / gate` check on main for everyone, admins included.",
        "Do not try to work around a governance block — explain it to the user instead.",
    ]
    if repos:
        lines.append("Governed repos: " + "; ".join("%s=%s" % (r.pod, r.root) for r in repos))
    errs = os.path.join(LOG_DIR, "hook_errors.log")
    if os.path.exists(errs) and os.path.getsize(errs):
        lines.append("WARNING: governance hook errors were logged in %s — tell the user." % errs)
    cwd = data.get("cwd") or os.getcwd()
    repo, unonboarded = repo_for(cwd)
    if repo:
        lines.append("This session started inside %s (%s). Briefing docs to read first: %s"
                     % (repo.root, repo.pod, ", ".join(repo.briefing)))
    elif unonboarded:
        lines.append(ONBOARD_MSG % (unonboarded, unonboarded))
    respond("SessionStart", context="\n".join(lines))


def hook_pre_tool(data):
    tool = data.get("tool_name", "")
    ti = data.get("tool_input") or {}
    sid = data.get("session_id")
    cwd = data.get("cwd") or os.getcwd()
    reviewer = os.environ.get("GOV_REVIEWER")

    if tool == "Read":
        record_read(sid, expand(ti.get("file_path", ""), cwd))
        return

    if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = expand(ti.get("file_path") or ti.get("notebook_path") or "", cwd)
        if reviewer:
            return deny("Reviewers are read-only.", data, "R6")
        if "/governance/reviews/" in path or "/governance/tickets/" in path:
            return deny("Review verdicts and tickets can only be written by `gov review` / `gov start`.",
                        data, "R6")
        repo, unonboarded = repo_for(path)
        if unonboarded:
            if os.path.basename(path) == MARKER:
                return
            return deny(ONBOARD_MSG % (unonboarded, unonboarded), data, "R1")
        if not repo:
            return
        touch_repo(sid, repo)
        unread = unread_briefing(sid, repo)
        if unread:
            return deny(briefing_msg(repo, unread), data, "R2")
        b = repo.branch()
        if b in repo.protected:
            return deny("Edits on protected branch '%s' of %s are not allowed. Create a feature branch "
                        "(git switch -c feat/<work-item>-<topic>)." % (b, repo.pod), data, "R3")
        rel = repo.rel(path)
        if repo.is_code(rel) and not repo.ticket():
            return deny("No spec, no code: '%s' is code but branch '%s' has no work item. Write or locate "
                        "the approved spec / work package, then run `gov start <WORK-ITEM>` in %s."
                        % (rel, b, repo.root), data, "R4")
        return

    if tool != "Bash":
        return
    command = ti.get("command", "")

    # Shell constructs that can write files. Reading verdicts/settings is fine; writing is not.
    writes = re.search(r"(>|\btee\b|sed\s+-i|\brm\b|\bmv\b|\bcp\b|\btouch\b|\bpython3?\b|\bperl\b|"
                       r"\bruby\b|\bnode\b|\bdd\b|\binstall\b|\bln\b|\btruncate\b|\bchmod\b)", command)
    if re.search(r"governance/(reviews|tickets)/", command) and writes and \
            not command.strip().startswith("gov "):
        return deny("Verdict and ticket files are managed only by `gov`.", data, "R6")
    if re.search(r"\.claude/settings(\.local)?\.json|\.claude/governance/", command) and writes:
        return deny("Changing governance hooks/settings from a session is not allowed; the user must do "
                    "it by hand.", data, "R9")
    # GOV_ALLOW_INSTALL: escape hatch for the user's own shell (e.g. `! GOV_ALLOW_INSTALL=1 ...`) and for
    # the test-suite. A Claude session cannot set it for its hook process (SPEC §3 R9).
    if re.search(r"enforcement/install\.sh", command) and not os.environ.get("GOV_ALLOW_INSTALL"):
        return deny("Installing/updating the governance gateway is done by the user, from merged `main` "
                    "only. Ask the user to run it themselves: `! bash <software-factory-governance>/"
                    "enforcement/install.sh`.", data, "R9")

    for seg_cwd, argv, raw in segments(command, cwd):
        prog = os.path.basename(argv[0])

        # track briefing reads done via shell
        if prog in READ_CMDS:
            for a in argv[1:]:
                if not a.startswith("-"):
                    record_read(sid, expand(a, seg_cwd))
            continue

        if reviewer:
            continue

        # R5 live databases — checked regardless of cwd
        hit = live_db_target(argv, raw)
        if hit:
            dbs, why = hit
            dbs = [dbs] if isinstance(dbs, str) else dbs
            for repo in registered_repos():
                for db in dbs:
                    if db in repo.live_dbs:
                        ok, age = repo.live_db_backup_ok(db)
                        if not ok:
                            return deny("'%s' is a LIVE database of %s and this command can change it (%s). "
                                        "No backup newer than %sh in %s (newest: %s). Take a backup first, "
                                        "and prefer testing on a drill copy." % (
                                            db, repo.pod, why, repo.backup_age, ", ".join(repo.backup_dirs),
                                            "none" if age is None else "%.1fh old" % age), data, "R5")
                        return ask("LIVE database '%s' (%s) will be changed by: %s. Backup is %.1fh old. "
                                   "Confirm only if the user explicitly wants this on live data."
                                   % (db, repo.pod, raw[:200], age), data, "R5")

        g = git_subcmd(argv, seg_cwd)
        if g:
            gdir, sub, rest = g
            repo, unonboarded = repo_for(gdir)
            if unonboarded and sub in ("commit", "push"):
                return deny(ONBOARD_MSG % (unonboarded, unonboarded), data, "R1")
            if not repo:
                continue
            touch_repo(sid, repo)
            branch = repo.branch()
            if sub == "commit":
                unread = unread_briefing(sid, repo)
                if unread:
                    return deny(briefing_msg(repo, unread), data, "R2")
                if branch in repo.protected:
                    return deny("Commits on protected branch '%s' are not allowed." % branch, data, "R3")
                pending = set(git(repo.root, "diff", "--cached", "--name-only").splitlines())
                if "-a" in rest or "--all" in rest or any(x.startswith("-a") for x in rest if not x.startswith("--")):
                    pending |= set(git(repo.root, "diff", "--name-only").splitlines())
                if any(repo.is_code(f) for f in pending) and not repo.ticket():
                    return deny("No spec, no code: this commit touches code but branch '%s' has no work "
                                "item. Run `gov start <WORK-ITEM>`." % branch, data, "R4")
            elif sub == "push":
                if any(x in ("-f", "--force", "--force-with-lease") or x.startswith("--force") or
                       x.startswith("+") for x in rest):
                    return deny("Force-push is not allowed on governed repositories.", data, "R7")
                targets = [x.split(":")[-1] for x in rest if not x.startswith("-")][1:]
                if any(t.replace("refs/heads/", "") in repo.protected for t in targets) or \
                        (not targets and branch in repo.protected):
                    return deny("Direct push to a protected branch is not allowed — open a PR.", data, "R7")
                problems = repo.ship_problems()
                if problems:
                    return deny("Push blocked until governance is satisfied:\n- " + "\n- ".join(problems),
                                data, "R7")
            continue

        if prog == "gh" and len(argv) > 2 and argv[1] == "pr":
            repo, _ = repo_for(seg_cwd)
            if argv[2] == "merge":
                return ask("Merging a PR is a sponsor decision. GitHub will still require the "
                           "`governance / gate` check. Confirm only if the user asked to merge this PR.",
                           data, "R7")
            if argv[2] == "create" and repo:
                problems = repo.ship_problems()
                if problems:
                    return deny("PR creation blocked until governance is satisfied:\n- "
                                + "\n- ".join(problems), data, "R7")
            continue

        if prog == "gh" and len(argv) > 1 and argv[1] == "api" and \
                re.search(r"rulesets|protection", raw) and re.search(r"-X\s*(DELETE|PUT|PATCH|POST)|--method", raw):
            return ask("This changes GitHub branch protection/rulesets — the server-side governance gate. "
                       "Confirm only if the user explicitly asked for this change.", data, "R8")


def hook_stop(data):
    if os.environ.get("GOV_REVIEWER") or data.get("stop_hook_active"):
        return
    sid = data.get("session_id")
    sp, st = session_state(sid)
    nagged = st.setdefault("stop_nagged", [])
    msgs = []
    for root in st.get("touched", []):
        if not os.path.exists(os.path.join(root, MARKER)):
            continue
        repo = Repo(root)
        head = repo.head()
        if not head or head in nagged:
            continue
        changed = repo.changed_since_base()
        if not any(repo.is_code(f) for f in changed):
            continue
        v = repo.verdicts()
        if all(r in v for r in REVIEWERS):
            continue
        nagged.append(head)
        msgs.append("%s branch '%s' has code commits without G1/G2/G3 reviews for HEAD %s."
                    % (repo.pod, repo.branch(), head[:8]))
    if msgs:
        save_json(sp, st)
        respond("Stop", "block", BANNER + " ".join(msgs) +
                " Before handing back, either run `gov review` (and report the verdicts) or tell the user "
                "plainly that the work is unreviewed and cannot be merged yet.")


def cmd_hook(args):
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
        {"session-start": hook_session_start, "pre-tool": hook_pre_tool,
         "stop": hook_stop}[args.event](data)
    except Exception as exc:  # fail open, but loudly (R9)
        import traceback
        ensure_dirs()
        with open(os.path.join(LOG_DIR, "hook_errors.log"), "a") as fh:
            fh.write("%s %s %r\n%s\n" % (now(), args.event, exc, traceback.format_exc()))
    return 0


# ─────────────────────────────── CLI commands ─────────────────────────────

def need_repo(path):
    repo, unonboarded = repo_for(path or os.getcwd())
    if unonboarded:
        sys.exit(ONBOARD_MSG % (unonboarded, unonboarded))
    if not repo:
        sys.exit("Not inside a governed repository (no %s found)." % MARKER)
    return repo


def cmd_status(args):
    repo = need_repo(args.repo)
    print("Governed repo : %s (%s)" % (repo.root, repo.pod))
    print("Branch        : %s%s" % (repo.branch(), "  [PROTECTED]" if repo.branch() in repo.protected else ""))
    t = repo.ticket()
    print("Work item     : %s" % (("%s (since %s)" % (t["work_item"], t["started"])) if t else "NONE — run gov start <WORK-ITEM>"))
    print("Briefing docs : %s" % ", ".join(repo.briefing))
    print("Live DBs      : %s (backup <= %sh in %s)" % (", ".join(repo.live_dbs) or "-", repo.backup_age,
                                                       ", ".join(repo.backup_dirs) or "-"))
    v = repo.verdicts()
    print("Reviews @HEAD : %s" % (", ".join("%s=%s" % (r, v[r]["decision"]) for r in v) or "none"))
    probs = repo.ship_problems()
    print("Ready to ship : %s" % ("YES" if not probs else "NO"))
    for p in probs:
        print("   - " + p)
    return 0 if not probs else 1


def cmd_start(args):
    repo = need_repo(args.repo)
    item = args.work_item.strip()
    if not repo.work_item_re.fullmatch(item):
        sys.exit("'%s' does not look like a work item id (pattern %s)." % (item, repo.work_item_re.pattern))
    b = repo.branch()
    if not b or b in repo.protected:
        sys.exit("Switch to a feature branch first (current: %s)." % (b or "detached"))
    if not repo.work_item_exists(item):
        sys.exit("No spec, no code: '%s' was not found in %s. Write the spec / log the approved decision "
                 "there first (docs-only changes are allowed), then run gov start again."
                 % (item, ", ".join(repo.spec_sources)))
    save_json(repo.ticket_path(), {"work_item": item, "branch": b, "started": now(),
                                   "by": os.environ.get("USER", "")})
    log("decisions.jsonl", {"decision": "ticket", "repo": repo.root, "branch": b, "work_item": item})
    print("Branch '%s' of %s is now working on %s." % (b, repo.pod, item))
    return 0


def governance_repo_dir():
    cfg = config()
    for cand in (os.environ.get("GOV_REPO"), cfg.get("governance_repo_path"),
                 os.path.dirname(ENGINE_DIR)):
        if cand and os.path.exists(os.path.join(cand, "enforcement", "SPEC.md")):
            return cand
    return None


def reviewer_prompt(repo, reviewer, base, head, work_item, pr_text):
    sfg = governance_repo_dir() or ""
    role_path = os.path.join(ENGINE_DIR, "reviewers", reviewer + ".md")
    role = open(role_path).read() if os.path.exists(role_path) else "You are governance reviewer %s." % reviewer
    stat = git(repo.root, "diff", "--stat", base, head)[-6000:]
    return """{role}

# THIS REVIEW
- Repository: {root} (pod {pod})
- Work item claimed: {item}
- Change under review: `git diff {base}..{head}` (run it yourself; also read the changed files in full where needed)
- Governance briefing docs for this repo: {briefing}
- Docs that must be updated when code changes: {req}
- Governance standards repository (read-only reference): {sfg}
{pr}
Diff summary:
```
{stat}
```

You are an INDEPENDENT reviewer. You did not write this change and you owe its author nothing.
You have read-only tools. Verify claims against the files; do not trust commit messages or PR text.
If the work item / spec does not cover what the change does, say so (E1 Scope Increase).

End your answer with exactly one final line in this form:
VERDICT: APPROVED | APPROVED_WITH_CONDITIONS | REJECTED | ESCALATE
""".format(role=role, root=repo.root, pod=repo.pod, item=work_item or "NONE",
           base=base, head=head, briefing=", ".join(repo.briefing), req=", ".join(repo.required_docs) or "-",
           sfg=sfg or "(not available)", pr=("PR text:\n" + pr_text[:4000] + "\n") if pr_text else "",
           stat=stat)


def run_one_review(repo, reviewer, base, head, work_item, pr_text, timeout):
    claude = shutil.which("claude")
    if not claude:
        return reviewer, "ERROR", "claude CLI not found on PATH"
    prompt = reviewer_prompt(repo, reviewer, base, head, work_item, pr_text)
    env = dict(os.environ, GOV_REVIEWER=reviewer)
    allowed = ["Read", "Grep", "Glob", "Bash(git diff:*)", "Bash(git log:*)", "Bash(git show:*)",
               "Bash(git status:*)", "Bash(ls:*)"]
    sfg = governance_repo_dir()
    cmd = [claude, "-p", "--output-format", "text", "--max-turns", "40",
           "--allowedTools"] + allowed + ["--disallowedTools", "Edit", "MultiEdit", "Write", "NotebookEdit",
                                          "WebFetch", "WebSearch", "Agent"]
    if sfg:
        cmd += ["--add-dir", sfg]
    try:
        p = subprocess.run(cmd, input=prompt, capture_output=True, text=True, cwd=repo.root,
                           env=env, timeout=timeout)
    except subprocess.TimeoutExpired:
        return reviewer, "ERROR", "review timed out after %ss" % timeout
    out = (p.stdout or "") + (("\n[stderr]\n" + p.stderr) if p.returncode else "")
    found = VERDICT_RE.findall(out)
    decision = found[-1].upper().replace(" ", "_") if found else "ERROR"
    return reviewer, decision, out


def cmd_review(args):
    repo = need_repo(args.repo)
    reviewers = [r.strip().upper() for r in args.reviewers.split(",")]
    if args.ci:
        base, head = args.base, args.head
        work_item = args.work_item
        pr_text = open(args.pr_text_file).read() if args.pr_text_file and os.path.exists(args.pr_text_file) else ""
    else:
        if git(repo.root, "status", "--porcelain", "--untracked-files=no"):
            sys.exit("Commit your changes first — reviews are recorded against a commit.")
        base, head = repo.merge_base(), repo.head()
        if not base:
            sys.exit("Cannot find the base branch (%s). Fetch origin first." % repo.default_branch)
        t = repo.ticket()
        work_item, pr_text = (t or {}).get("work_item"), ""
    if not args.ci:
        try:
            ver = subprocess.run(["claude", "--version"], capture_output=True, text=True, timeout=20).stdout.split()
        except Exception:
            ver = []
        if not ver or ver[0] != REVIEW_CLI_VERSION:
            print("NOTE: local reviewer CLI is %s; the CI gate runs %s. Verdicts can differ; CI is authoritative."
                  % (ver[0] if ver else "unknown", REVIEW_CLI_VERSION))
    print("Firing %s as independent Claude instances on %s..%s (this takes a few minutes)"
          % (", ".join(reviewers), base[:8], head[:8]), flush=True)
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(reviewers)) as ex:
        futs = [ex.submit(run_one_review, repo, r, base, head, work_item, pr_text, args.timeout)
                for r in reviewers]
        for f in concurrent.futures.as_completed(futs):
            r, decision, out = f.result()
            results[r] = (decision, out)
            print("  %s → %s" % (r, decision), flush=True)
    exit_code = 0
    for r in reviewers:
        decision, out = results[r]
        if args.ci:
            report = os.path.join(args.out_dir or ".", "review_%s.md" % r)
            os.makedirs(os.path.dirname(report) or ".", exist_ok=True)
        else:
            report = os.path.join(repo.verdict_dir(head), r + ".md")
            os.makedirs(os.path.dirname(report), exist_ok=True)
        with open(report, "w") as fh:
            fh.write(out)
        if not args.ci and decision != "ERROR":
            save_json(os.path.join(repo.verdict_dir(head), r + ".json"),
                      {"reviewer": r, "decision": decision, "commit": head, "base": base,
                       "work_item": work_item, "at": now(), "report": report,
                       "sha256": hashlib.sha256(out.encode()).hexdigest()})
        log("decisions.jsonl", {"decision": "review", "repo": repo.root, "reviewer": r,
                                "verdict": decision, "commit": head})
        if decision not in PASSING:
            exit_code = 1
        print("\n===== %s: %s  (full report: %s)" % (r, decision, report))
        print(out[-3000:] if not args.quiet else "")
    return exit_code


def cmd_verify(args):
    repo = need_repo(args.repo)
    probs = repo.ship_problems()
    for p in probs:
        print("- " + p)
    print("READY" if not probs else "NOT READY")
    return 1 if probs else 0


# ───────────────────────────────── CI gate ────────────────────────────────

def cmd_ci_docs_gate(args):
    repo = Repo(os.path.realpath(args.repo or "."))
    if not os.path.exists(os.path.join(repo.root, MARKER)):
        print("::error::%s missing — this repository is not onboarded to governance." % MARKER)
        return 1
    changed = [f for f in git(repo.root, "diff", "--name-only", args.base, args.head).splitlines() if f]
    text = (args.pr_title or "") + "\n" + (open(args.pr_body_file).read() if args.pr_body_file else "")
    labels = set(l.strip() for l in (args.labels or "").split(",") if l.strip())
    problems, notes = [], []
    code = [f for f in changed if repo.is_code(f)]
    items = sorted(set(repo.work_item_re.findall(text)))
    found = [i for i in items if repo.work_item_exists(i)]
    if code:
        if not items:
            problems.append("Code changed but the PR title/body cites no work item (WP-/DEC-/SPEC-…). "
                            "No spec, no code.")
        elif not found:
            problems.append("Work item(s) %s cited but not found in %s." % (", ".join(items),
                                                                             ", ".join(repo.spec_sources)))
        missing = [d for d in repo.required_docs if d not in changed]
        if missing:
            problems.append("Code changed but required governance docs not updated: " + ", ".join(missing))
    # enforcement/ is the gate engine itself (governance repo): engine changes reach every child repo.
    gov_files = [f for f in changed if f == MARKER or f.startswith((".github/", ".claude/", "enforcement/"))]
    if gov_files and "governance-change" not in labels:
        problems.append("Governance plumbing changed (%s) — the sponsor must add the `governance-change` "
                        "label." % ", ".join(gov_files))
    notes.append("Changed files: %d (code: %d). Work items: %s" % (len(changed), len(code),
                                                                  ", ".join(found) or "none"))
    for n in notes:
        print(n)
    for p in problems:
        print("::error::" + p)
    if args.output:
        with open(args.output, "a") as fh:
            fh.write("work_item=%s\n" % (found[0] if found else ""))
    return 1 if problems else 0


# ──────────────────────────────── git hooks ───────────────────────────────

def cmd_githook(args):
    repo, unonboarded = repo_for(os.getcwd())
    if unonboarded:
        print(ONBOARD_MSG % (unonboarded, unonboarded), file=sys.stderr)
        return 1
    if not repo:
        return 0
    b = repo.branch()
    if args.name == "pre-commit":
        if b in repo.protected:
            print("governance: commits on protected branch '%s' are not allowed. "
                  "git switch -c feat/<work-item>-<topic>" % b, file=sys.stderr)
            return 1
        staged = git(repo.root, "diff", "--cached", "--name-only").splitlines()
        if any(repo.is_code(f) for f in staged) and not repo.ticket():
            print("governance: No spec, no code — run `gov start <WORK-ITEM>` for branch '%s'." % b,
                  file=sys.stderr)
            return 1
        return 0
    if args.name == "pre-push":
        lines = sys.stdin.read().splitlines()
        for line in lines:
            parts = line.split()
            if len(parts) >= 3 and parts[2].replace("refs/heads/", "") in repo.protected:
                print("governance: direct push to protected branch is not allowed — open a PR.", file=sys.stderr)
                return 1
        probs = repo.ship_problems()
        if probs:
            print("governance: push blocked (server will block the merge anyway):\n- " + "\n- ".join(probs),
                  file=sys.stderr)
            return 1
    return 0


# ─────────────────────────────── onboarding ───────────────────────────────

def cmd_onboard(args):
    root = find_git_root(expand(args.path or os.getcwd()))
    if not root:
        sys.exit("Not a git repository.")
    marker = os.path.join(root, MARKER)
    tdir = os.path.join(ENGINE_DIR, "templates")
    if not os.path.exists(marker):
        if not args.pod:
            sys.exit("--pod is required for a new onboarding (e.g. POD-NADF).")
        tpl = load_json(os.path.join(tdir, "governance.json"))
        tpl["pod"] = args.pod
        tpl["briefing_docs"] = [d for d in tpl["briefing_docs"] if os.path.exists(os.path.join(root, d))] or ["CLAUDE.md"]
        save_json(marker, tpl)
        print("wrote %s — review code_paths, required_doc_updates, live_databases." % marker)
    wf = os.path.join(root, ".github", "workflows", "governance.yml")
    if not os.path.exists(wf):
        os.makedirs(os.path.dirname(wf), exist_ok=True)
        shutil.copy(os.path.join(tdir, "caller-workflow.yml"), wf)
        print("wrote %s" % wf)
    agents = os.path.join(root, "AGENTS.md")
    if not os.path.exists(agents):
        shutil.copy(os.path.join(tdir, "AGENTS.md"), agents)
        print("wrote %s" % agents)
    # project-level Claude bootstrap (L2)
    hook_dst = os.path.join(root, ".claude", "hooks", "gov_bootstrap.sh")
    os.makedirs(os.path.dirname(hook_dst), exist_ok=True)
    shutil.copy(os.path.join(tdir, "claude", "gov_bootstrap.sh"), hook_dst)
    os.chmod(hook_dst, 0o755)
    sp = os.path.join(root, ".claude", "settings.json")
    st = load_json(sp, {}) or {}
    hooks = st.setdefault("hooks", {})
    for event, matcher in (("PreToolUse", "Edit|Write|MultiEdit|NotebookEdit|Bash"), ("SessionStart", "*")):
        entry = {"matcher": matcher, "hooks": [{"type": "command", "timeout": 10,
                 "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/gov_bootstrap.sh %s" % event}]}
        lst = hooks.setdefault(event, [])
        if not any("gov_bootstrap.sh" in json.dumps(e) for e in lst):
            lst.append(entry)
    save_json(sp, st)
    print("updated %s (bootstrap hooks)" % sp)
    install_githooks(root)
    register(root)
    print("Onboarded %s. Commit these files on a branch and open a PR labelled `governance-change`." % root)
    return 0


def install_githooks(root):
    hooks_dir = os.path.join(GOV_HOME, "githooks")
    if os.path.isdir(hooks_dir):
        cur = git(root, "config", "--get", "core.hooksPath")
        if cur and expand(cur) != expand(hooks_dir):
            print("NOTE: %s already uses core.hooksPath=%s — not overriding; merge manually." % (root, cur))
            return
        subprocess.run(["git", "-C", root, "config", "core.hooksPath", hooks_dir])
        print("git hooks → %s" % hooks_dir)


def register(root):
    # A linked worktree registers its main checkout (worktrees come and go).
    common = git(root, "rev-parse", "--git-common-dir")
    if common:
        common = expand(common, root)
        if os.path.basename(common) == ".git":
            root = os.path.dirname(common)
    cfg = config()
    if root not in [expand(r) for r in cfg["repos"]]:
        cfg["repos"].append(root)
        save_json(CONFIG_PATH, cfg)


def cmd_protect(args):
    """Apply the main-branch ruleset (R8). Requires gh with admin rights."""
    repo = need_repo(args.repo)
    slug = args.slug or re.sub(r"(\.git)?$", "", git(repo.root, "remote", "get-url", "origin").split("github.com")[-1][1:])
    checks = [{"context": c} for c in (args.checks or "governance / gate").split(",") if c.strip()]
    body = {
        "name": "software-factory-main",
        "target": "branch",
        "enforcement": "active",
        "bypass_actors": [],
        "conditions": {"ref_name": {"include": ["~DEFAULT_BRANCH"], "exclude": []}},
        "rules": [
            {"type": "deletion"},
            {"type": "non_fast_forward"},
            {"type": "pull_request", "parameters": {
                "required_approving_review_count": 0, "dismiss_stale_reviews_on_push": True,
                "require_code_owner_review": False, "require_last_push_approval": False,
                "required_review_thread_resolution": True}},
            {"type": "required_status_checks", "parameters": {
                "strict_required_status_checks_policy": False,
                "required_status_checks": checks}},
        ],
    }
    if args.linear_history:
        # Opt-in (sponsor decision): blocks merge commits, so PRs must be squashed or rebased.
        body["rules"].append({"type": "required_linear_history"})
    existing = subprocess.run(["gh", "api", "repos/%s/rulesets" % slug], capture_output=True, text=True)
    rid = None
    if existing.returncode == 0:
        for rs in json.loads(existing.stdout or "[]"):
            if rs.get("name") == body["name"]:
                rid = rs["id"]
    method, path = ("PUT", "repos/%s/rulesets/%s" % (slug, rid)) if rid else ("POST", "repos/%s/rulesets" % slug)
    # Governance repo only (--gate-tags): make gate release tags (gate-v*) immutable, so child repos
    # that pin `governance-gate.yml@gate-vN` cannot be silently re-pointed (G3 E3 finding, 2026-11-13).
    tag_body = {"name": "software-factory-gate-tags", "target": "tag", "enforcement": "active",
                "bypass_actors": [],
                "conditions": {"ref_name": {"include": ["refs/tags/gate-v*"], "exclude": []}},
                "rules": [{"type": "update"}, {"type": "deletion"}, {"type": "non_fast_forward"}]}
    if args.dry_run:
        print(method, path)
        print(json.dumps(body, indent=2))
        if args.gate_tags:
            print(json.dumps(tag_body, indent=2))
        return 0
    p = subprocess.run(["gh", "api", "-X", method, path, "--input", "-"], input=json.dumps(body),
                       capture_output=True, text=True)
    print(p.stdout[:500] or p.stderr)
    if p.returncode or not args.gate_tags:
        return p.returncode
    tid = None
    for rs in json.loads(existing.stdout or "[]") if existing.returncode == 0 else []:
        if rs.get("name") == tag_body["name"]:
            tid = rs["id"]
    method, path = ("PUT", "repos/%s/rulesets/%s" % (slug, tid)) if tid else ("POST", "repos/%s/rulesets" % slug)
    p = subprocess.run(["gh", "api", "-X", method, path, "--input", "-"], input=json.dumps(tag_body),
                       capture_output=True, text=True)
    print(p.stdout[:500] or p.stderr)
    return p.returncode


# ─────────────────────────────────── main ─────────────────────────────────

def main(argv=None):
    ap = argparse.ArgumentParser(prog="gov", description="Software Factory governance gateway v" + VERSION)
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("hook"); s.add_argument("event", choices=["session-start", "pre-tool", "stop"])
    s = sub.add_parser("status"); s.add_argument("repo", nargs="?")
    s = sub.add_parser("start"); s.add_argument("work_item"); s.add_argument("--repo")
    s = sub.add_parser("review")
    s.add_argument("--repo"); s.add_argument("--reviewers", default="G1,G2,G3")
    s.add_argument("--timeout", type=int, default=1500); s.add_argument("--quiet", action="store_true")
    s.add_argument("--ci", action="store_true"); s.add_argument("--base"); s.add_argument("--head")
    s.add_argument("--work-item"); s.add_argument("--pr-text-file"); s.add_argument("--out-dir")
    s = sub.add_parser("verify"); s.add_argument("--repo")
    s = sub.add_parser("ci-docs-gate")
    s.add_argument("--repo"); s.add_argument("--base", required=True); s.add_argument("--head", required=True)
    s.add_argument("--pr-title"); s.add_argument("--pr-body-file"); s.add_argument("--labels")
    s.add_argument("--output")
    s = sub.add_parser("githook"); s.add_argument("name", choices=["pre-commit", "pre-push"])
    s.add_argument("rest", nargs="*")
    s = sub.add_parser("onboard"); s.add_argument("path", nargs="?"); s.add_argument("--pod")
    s = sub.add_parser("protect"); s.add_argument("--repo"); s.add_argument("--slug")
    s.add_argument("--checks"); s.add_argument("--dry-run", action="store_true")
    s.add_argument("--gate-tags", action="store_true",
                   help="governance repo only: also make gate-v* tags immutable")
    s.add_argument("--linear-history", action="store_true",
                   help="also require linear history (no merge commits; squash or rebase only)")
    sub.add_parser("version")
    args = ap.parse_args(argv)
    handlers = {"hook": cmd_hook, "status": cmd_status, "start": cmd_start, "review": cmd_review,
                "verify": cmd_verify, "ci-docs-gate": cmd_ci_docs_gate, "githook": cmd_githook,
                "onboard": cmd_onboard, "protect": cmd_protect,
                "version": lambda a: print("gov", VERSION) or 0}
    if not args.cmd:
        ap.print_help()
        return 0
    return handlers[args.cmd](args) or 0


if __name__ == "__main__":
    sys.exit(main())
