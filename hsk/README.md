# HSK — حسن کچل

An autonomous delivery playbook: turn an ambitious task into a bounded execution contract, coordinate workers, deliver a usable slice, test real behavior and finish with verified release evidence. Use `HSK this task`, `HSK کن`, or `$hsk` where supported.

## Portable installation
Clone this branch, inspect the Markdown, then copy the `hsk` folder to your agent’s supported skill directory. For example, from the repository root:

```sh
mkdir -p "$HOME/.claude/skills"
cp -R hsk "$HOME/.claude/skills/hsk"
```

Use a new destination or compare an existing installation first; do not overwrite custom work blindly. Codex can use its supported skills directory (commonly `$HOME/.agents/skills`); for other clients follow their current skill loader documentation. Start a new session or use a documented skill reload. No model, proxy, MCP server, dependency, credential or service is installed. Model routing is supplied by the operator.

## Usage
Provide the outcome, current repository/work, acceptance example and existing authority/budget. HSK can prepare a brief, execute an authorized task, or resume existing work. It does not grant permissions or promise unattended execution. Templates and acceptance examples are in `references/`.

## Validation
Instruction-format validation and scenario review cover handoff vs execution, blocked dependencies, and owner reprioritization. These are not proof of any downstream product deployment.
