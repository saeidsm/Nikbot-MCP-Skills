# Execution brief template

Use only relevant fields. Replace placeholders with discovered facts; label unknowns. Keep the lead prompt self-contained but link large evidence rather than pasting histories. Choose a terminal-safe prompt language; product content remains the user's requested language and design.

```text
You own delivery of [outcome] for [users/environment]. Continue existing work rather than restarting it.

SUCCESS
[Observable user flow and concrete output; explicit acceptance criteria.]
First usable release: [bounded vertical slice].
Remaining agreed phases: [items that must not disappear].
Not in scope for this release: [optional enhancements].

BASELINE
[Repository, branch/version, live state, active executors, existing artifacts and verified evidence.]
[Known failures/uncertain actions; do not replay without reconciliation.]

AUTHORITY AND CONSTRAINTS
[User-authorized engineering/release steps, data destinations, spending limit, exact restricted actions.]
Continue routine authorized steps without asking repeatedly. Respect real approval requirements and denied controls. Missing access or a blocked action is not permission to switch tools to defeat the restriction. Complete independent work meanwhile.

EXECUTION
1. Reconcile live state, instructions and workers; maintain one owner for shared resources.
2. Make a short implementation/acceptance plan, then execute. Do not return only a new plan.
3. Use bounded workers with clear ownership and the verified model routing below.
4. Establish a working end-to-end path early. Validate data and provider prerequisites before polishing the UI.
5. Freeze this release's scope; integrate targeted fixes and run appropriate regression on the immutable candidate. No endless feature additions between final test runs.
6. Review significant risks independently, fix demonstrated blockers, and release through the project's supported reversible path when authorized.
7. Verify real behavior and deliver working outputs. Retain remaining scope and follow-up triggers.

MODELS/RESOURCES
[Chosen lead, permitted workers, routing evidence, limits. Do not assume model aliases.]

PROOF AND HANDOFF
Report tests, commit/push, merge, deployment, activation and acceptance separately.
Deliver [summary, full report, downloadable artifact] via verified authorized links and machine-readable metadata where supported.
Persist [task status, decisions, next action, owner, exact blocker, review trigger] in the existing project tracker.
Stop only at verified delivery or a specific genuine blocker; do not claim unattended continuation without a supported mechanism.
```

For a new executor include why previous attempts failed and exactly what has already taken effect. For a running executor send a narrow amendment instead of replacing its whole task or context.
