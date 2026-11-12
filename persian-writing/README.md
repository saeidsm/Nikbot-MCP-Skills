# persian-writing

Portable agent skill, sanitized public edition. This branch contains only this skill and its documentation.

## Setup
1. Download or clone this skill branch. Review `SKILL.md` and every included file.
2. Copy the directory containing `SKILL.md` into your agent's supported skill root under `persian-writing`. For Claude Code a common user root is `~/.claude/skills/`; for Codex a common user root is `~/.agents/skills/`. Confirm the installed client's current documentation. For other agents use their documented skill mechanism, or attach `SKILL.md` as task guidance. No universal discovery path is assumed.
3. Start a new session or use the client's supported refresh. Do not restart active work just to load a skill. Ask the agent to identify the loaded skill and explain a harmless sample task.
4. Configure project paths, tools, provider/account access, fonts, budget and publication approvals separately. No credentials belong in these files.

No installer, service, automatic updater or permission bypass is included. Markdown guidance does not grant tools or authorization. Existing same-named skills should be backed up and compared, not blindly overwritten. Remove this directory to uninstall; it does not undo actions previously performed.

## Verification and limits
Skill metadata and local file links are validated; instructions are not a claim that your provider, build or publication flow was tested. Run representative acceptance checks in your own environment. This edition intentionally excludes private deployment details and task data. See `PROVENANCE.md` for source scope and omitted assets.
