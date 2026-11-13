# Execution brief template

Use only relevant fields. Replace placeholders with discovered facts; label unknowns. Keep the lead prompt self-contained but link large evidence rather than pasting histories. For sam terminals, prefer English; product content remains the user's requested language and design.

```text
You own delivery of [outcome] for [users/environment]. Continue existing work rather than restarting it.

SUCCESS
[Observable user flow and concrete output; explicit acceptance criteria.]
Final product: [complete agreed ready-to-use scope, not a disposable MVP].
Early visible phases: [working checkpoints toward that product].
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
2. Plan all agreed journeys, component/data/permission connections, recovery and deployment before coding. Keep the plan compact; then execute in visible phases. Do not return only a new plan.
3. Use bounded workers with clear ownership and the verified model routing below.
4. Establish a working end-to-end path early. Validate data and provider prerequisites before polishing the UI.
5. Freeze each phase; run risk-based changed-path and integration checks. Run full regression only when project rules or broad impact require it. No invented thousands of tests, endless scope growth or repeated unchanged expensive runs.
6. Review significant risks independently, fix demonstrated blockers, and release through the project's supported reversible path when authorized.
7. Verify real behavior and deliver working outputs. Retain remaining scope and follow-up triggers.

CAPACITY AND UX
[Target active/concurrent users, representative workload, latency/resource limits and bounded measurement. Separate target from demonstrated capacity.]
[Design system, desktop/mobile/RTL requirements and real interaction acceptance.]

MODELS/RESOURCES
[Chosen lead, permitted workers, routing evidence, time/token/spend limits. Use bounded logs and concise handoffs; do not repeatedly read entire repositories. Do not assume model aliases.]

PROOF AND HANDOFF
Report tests, commit/push, merge, deployment, activation and acceptance separately.
Deliver [working link/artifact and concise evidence summary; full report only when needed] via verified authorized links and machine-readable metadata where supported.
Persist [task status, decisions, next action, owner, exact blocker, review trigger] in the existing project tracker.
Stop only at verified delivery or a specific genuine blocker; do not claim unattended continuation without a supported mechanism.
```

For a new executor include why previous attempts failed and exactly what has already taken effect. For a running executor send a narrow amendment instead of replacing its whole task or context.
