#!/usr/bin/env bash
# Install / update the Software Factory governance gateway for this user (SPEC-GOV-ENF-001).
#   bash enforcement/install.sh [--owner <github-owner>] [repo-path ...]
# Idempotent. Installs:
#   ~/.claude/governance/        engine, reviewers, templates, git hooks, config, logs
#   ~/.local/bin/gov             CLI
#   ~/.claude/settings.json      user-level hooks → fire in EVERY Claude Code session
#   ~/.claude/CLAUDE.md          global governance rules block
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
SFG="$(dirname "$SRC")"
GOV_HOME="${GOV_HOME:-$HOME/.claude/governance}"
OWNER="aliyuumaru-beep"
REPOS=()
while [ $# -gt 0 ]; do
  case "$1" in --owner) OWNER="$2"; shift 2 ;; *) REPOS+=("$1"); shift ;; esac
done

mkdir -p "$GOV_HOME"/{state,logs,githooks} "$HOME/.local/bin"
cp "$SRC/govcore.py" "$GOV_HOME/govcore.py"
rm -rf "$GOV_HOME/reviewers" "$GOV_HOME/templates"
cp -R "$SRC/reviewers" "$SRC/templates" "$GOV_HOME/"
cp "$SRC"/templates/githooks/* "$GOV_HOME/githooks/"
chmod +x "$GOV_HOME"/githooks/* "$GOV_HOME/govcore.py"
cat > "$HOME/.local/bin/gov" <<WRAP
#!/usr/bin/env bash
exec python3 "$GOV_HOME/govcore.py" "\$@"
WRAP
chmod +x "$HOME/.local/bin/gov"

python3 - "$GOV_HOME" "$SFG" "$OWNER" "${REPOS[@]+"${REPOS[@]}"}" <<'PY'
import json, os, sys

def atomic_text(path, text):
    # write-then-rename so an interrupted install never leaves a truncated file (G1/G3 2026-11-13)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        fh.write(text)
    os.replace(tmp, path)

def atomic_json(path, data):
    atomic_text(path, json.dumps(data, indent=2) + "\n")

gov_home, sfg, owner, repos = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
home = os.path.expanduser("~")

# config
cp = os.path.join(gov_home, "config.json")
cfg = json.load(open(cp)) if os.path.exists(cp) else {}
cfg["governance_repo_path"] = sfg
cfg.setdefault("owner_patterns", [])
if owner not in cfg["owner_patterns"]:
    cfg["owner_patterns"].append(owner)
cfg.setdefault("repos", [])
for r in repos:
    r = os.path.realpath(os.path.expanduser(r))
    if r not in cfg["repos"]:
        cfg["repos"].append(r)
atomic_json(cp, cfg)

# user-level hooks
sp = os.path.join(home, ".claude", "settings.json")
st = json.load(open(sp)) if os.path.exists(sp) else {}
bak = sp + ".bak_pre_governance"
if os.path.exists(sp) and not os.path.exists(bak):
    open(bak, "w").write(open(sp).read())
engine = os.path.join(gov_home, "govcore.py")
want = {
    "SessionStart": ("*", "session-start", 15),
    "PreToolUse": ("Read|Edit|Write|MultiEdit|NotebookEdit|Bash", "pre-tool", 20),
    "Stop": ("*", "stop", 30),
}
hooks = st.setdefault("hooks", {})
for event, (matcher, arg, timeout) in want.items():
    lst = [e for e in hooks.get(event, []) if "govcore.py" not in json.dumps(e)]
    lst.append({"matcher": matcher, "hooks": [{"type": "command", "timeout": timeout,
                "command": "python3 \"%s\" hook %s" % (engine, arg)}]})
    hooks[event] = lst
atomic_json(sp, st)

# global CLAUDE.md block
cm = os.path.join(home, ".claude", "CLAUDE.md")
block = open(os.path.join(gov_home, "templates", "GLOBAL_CLAUDE_BLOCK.md")).read()
start, end = "<!-- SOFTWARE-FACTORY-GOVERNANCE:START -->", "<!-- SOFTWARE-FACTORY-GOVERNANCE:END -->"
text = open(cm).read() if os.path.exists(cm) else ""
if start in text:
    text = text[:text.index(start)] + text[text.index(end) + len(end):]
text = text.rstrip() + ("\n\n" if text.strip() else "") + start + "\n" + block.strip() + "\n" + end + "\n"
atomic_text(cm, text)
print("config:", cp)
print("hooks :", sp)
print("rules :", cm)
PY

for r in "${REPOS[@]+"${REPOS[@]}"}"; do
  if [ -f "$r/.governance.json" ]; then
    cur=$(git -C "$r" config --get core.hooksPath || true)
    if [ -z "$cur" ] || [ "$cur" = "$GOV_HOME/githooks" ]; then
      git -C "$r" config core.hooksPath "$GOV_HOME/githooks"; echo "git hooks: $r"
    else echo "NOTE: $r has core.hooksPath=$cur — left unchanged"; fi
  fi
done
case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *)
  echo "NOTE: add ~/.local/bin to PATH (e.g. echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.zshrc)";;
esac
echo "Governance gateway $(python3 "$GOV_HOME/govcore.py" version) installed. Restart Claude Code sessions to load the hooks."
