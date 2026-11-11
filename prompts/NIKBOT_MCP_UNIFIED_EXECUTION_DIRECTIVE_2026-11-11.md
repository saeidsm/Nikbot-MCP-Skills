# NikBot MCP — Unified AI Execution Control Plane
## Final autonomous implementation directive for Claude Code / Astra

**Version:** 1.0  
**Date:** 2026-11-11  
**Target repository:** https://github.com/saeidsm/Nikbot-MCP-Skills  
**Execution operator:** Claude Code, launched by the owner in the existing server terminal/tmux, with **Astra** as the implementation agent.  
**Priority:** P0. Make a usable system immediately so SkinCrete ERP development can start on 2026-11-12.

> **EXECUTION ORDER, NOT A RESEARCH REQUEST.** Inspect the actual server, implement in small verified phases, commit and push completed work, and give short Persian progress reports after each phase. Do not stop at a plan. Do not fabricate successful integration, model availability, pricing, quota, testing, or deployment.

---

## 0. Mission, context, and decisions already made

The owner operates an Ubuntu 24.04 DevOps server and an evolving **NikBot/MCP orchestration system** serving **SkinCrete ERP**, **Shahrzad.ai**, **AlumGlassSuperRAG**, **AlumGlass.com**, and related engineering workflows. Existing routing, job execution, state/memory, logging, GPT proxy, OpenRouter, Claude Code, and Codex facilities must be preserved and extended in place.

Build one **MCP AI Command Center**: a five-route, model-selectable execution control plane with agent-initiated overrides, native Antigravity Swarm support where genuinely available, a durable prompt/response/event ledger, Persian TUI + authenticated RTL web UI, host observability, safe disk reclamation, reproducible project memory, and an interoperable agent communication skill pack.

**Five first-class execution routes:**

| Stable route ID | Execution client | Backing access |
|---|---|---|
| \`claude_openrouter\` | existing Claude Code | OpenRouter |
| \`claude_gpt_proxy\` | existing Claude Code | existing GPT Proxy, with Astra/Sol/Terra aliases |
| \`claude_original\` | existing Claude Code | authorized official Anthropic subscription |
| \`antigravity\` | installed or officially installed Antigravity CLI | Google Gemini / eligible Claude models / native Swarm |
| \`codex_cli\` | **already installed Codex CLI** | currently authorized Codex/OpenAI account or API route |

**Operating preferences:** owner requests selectable **root** execution and maximum-autonomy **turbo** operation where actually supported. These must not be silently removed or replaced with mandatory unprivileged execution. Routine, reversible development tasks may proceed autonomously. Authorization for destructive production changes, database destruction, privilege changes to other users, billing purchases, and deployment remains separate. Display the current effective identity and permissions clearly.

**Urgency:** deliver P0 functionality in the current session, not a 14-day pilot. P1/P2 enhancements must never block the ability to execute ERP development tasks tomorrow.

**Critical path preservation:** Do not move, re-clone, rename, flatten, reset, or change the existing local repository directory or currently checked-out branch merely for convenience. First record \`pwd\`, \`git rev-parse --show-toplevel\`, \`git branch --show-current\`, \`git status --porcelain=v1\`, remotes, worktrees and tracked/untracked state. Keep user work intact. Use the existing repo in place, create a short-lived branch only if repository policy requires it, and never force-push. The destination GitHub repository above is the **source-control destination for this implementation and skill pack**; detect whether it is already the local working repository before touching anything. Do not confuse it with the separate SkinCreteERP repository.

### Existing operational context

- SkinCrete ERP: mobile-first Persian RTL UHPC/GFRC factory ERP; unique identity/QR for every **physical panel**, batch, mix, QC, mold, finishing subcontractor team, rack/shipment and precise **installation location** (grid/elevation/zone). Hundreds of panels may share a type code but must remain individually traceable.
- Shahrzad.ai: FastAPI, MongoDB, Celery, Redis, Next.js, React Native/Expo; storytelling, TTS, pictures, music and billing.
- AlumGlassSuperRAG: Persian OCR, project letters, semantic search, Secretariat UI, cited construction-law knowledge and official correspondence. Source integrity and document confidentiality matter.
- Existing DevOps/MCP infrastructure already has job queues, routing, tests, several providers and project memory. Reuse durable mechanisms rather than constructing parallel ones.
- Existing model naming aspirations: **Astra**, **Sol**, **Terra**. Inspect actual proxy mapping; do not infer the provider/model version from an alias name. The desired order is Astra, Sol, Terra and the default for ordinary **Claude Code via GPT Proxy** is **SOL**. The owner launches the implementation using Astra. Keep the executor for this installation separate from the default for future jobs.
- Owner previously requested a shell/tmux entry point for Claude Code. Preserve any existing \`sam\`/\`sam.sh\` wrapper and terminal workflow; repair instead of replacing it.
- Graphify previously created wasteful duplicated copies. Deduplicate *only after proving equivalence and reference safety*. Never perform broad deletion based on filename similarity.

---

## 1. Rules of execution and checkpoints

1. **Inspect before modifying.** Discover actual installed commands, service units, repositories, scripts, database engines, credentials locations (not secrets), provider adapter contracts, and test suites. No assumed filesystem paths.
2. **Preserve original repo path and branch.** Record baseline commit, free disk space and configuration hashes. Make an isolated, recoverable checkpoint; do not create duplicate full repo clones or archives by default.
3. **Work phase by phase autonomously:** inspect → implement → local tests → acceptance proof → commit → push → next phase. If a phase fails, diagnose and fix; if blocked by login, quota, or unsupported capability, mark the exact blocker and continue independent work.
4. **Use existing infrastructure** and naming conventions; prefer surgical changes over rewrites.
5. **Do not fake success** from exit code 0 alone. Verify required artifact, changed files, tests, actual provider/model and recorded job output.
6. **No silent provider/model substitution.** Requested versus actual execution must be visible.
7. **No security theater:** root/turbo are available where possible; show high-impact controls and scope. No unauthorized destruction, exfiltration, production data change or purchase.
8. **Push real changes** to \`saeidsm/Nikbot-MCP-Skills\` in coherent commits, only after tests and secret scanning. Never force push. If the implementation lives in another already-existing repository, keep it there and commit there; push reusable skills, schemas, integration documentation and pointers to this repository, not cloned product code.
9. **Do not fill the server:** bounded logs, TTL for abandoned worktrees, low-overhead monitoring, storage quotas and one canonical Graphify store.
10. Provide concise **Persian status after each phase**: completed, tests, commit SHA, push status, blockers, next step. Continue automatically to the next phase unless explicitly forbidden or truly blocked.

### Build order

- **Phase 0:** environment/baseline, backups and immediate GPT Proxy alias audit.
- **Phase 1:** unified five-route adapter contracts, selection policies, real execution.
- **Phase 2:** durable event/usage ledger and agent protocol skill pack.
- **Phase 3:** terminal configuration UI, project profiles and CLI model selection.
- **Phase 4:** Antigravity Swarm and Codex integration, concurrency and recovery.
- **Phase 5:** Persian RTL web dashboard + host/disk monitoring and safe cleanup.
- **Phase 6:** integration/e2e tests, docs, efficient pruning, push and handoff.
  
Ship a working vertical slice from Phase 1 as soon as possible. Phase 5 visuals must not prevent ERP work from beginning.

---

## 2. Phase 0 — Mandatory actual environment audit and Sol mapping

Run within the owner's **existing** terminal/tmux workflow; do not spawn a duplicate persistent stack.

- Inspect Claude Code version, launcher/wrapper, environment, configured provider endpoints, JSON/settings, model aliases, override mechanism, and effort mappings without printing secrets.
- Verify which *backend model IDs* and effort levels are **actually recognized** by the GPT Proxy and by the runtime, through model listing and harmless live requests where authorization already exists.
- Review the warning if Claude Code shows an unrecognized model name, e.g. \`gpt-6.1-sol\`: distinguish Claude Code's local metadata/context guess from an actual failed API request.
- Register aliases **Astra**, **Sol**, **Terra** in that order, mapped to their **verified** actual model IDs; document exact semantics and supported effort per alias. **Never invent a model name** or silently send an unsupported effort setting.
- Set the **GPT Proxy Claude Code default to SOL**, after testing successful invocation. Confirm the persisted default is effective after restarting the launcher. Do not change the owner's current Astra implementation session.
- Preserve official Claude subscription and OpenRouter credential paths and existing working routes.
- Identify existing Codex CLI and Antigravity CLI versions, model listing, CLI invocation, session/auth state and headless capabilities. Use official documentation for any uncertain flag.
- Inventory storage: \`df\`, \`du\` at known safe scopes, worktrees, Graphify locations, cached models/tooling, and available databases. **Read-only first.**

**Phase 0 gate:** before/after config summary (redacted), Sol mapping verified or documented blocker, baseline tests and rollback method. Commit the configuration/docs, push.

---

## 3. Five-route execution API and per-job agent overrides

Use existing MCP schema conventions and API versioning. A calling agent must be able to specify:

- \`selection_mode\`: \`explicit\` | \`recommended\` | \`auto\`.
- \`route\`: one of the **five stable route IDs**.
- \`model\`: exact discovered provider-specific model identifier; optional logical alias.
- \`reasoning_effort\`: only if adapter supports it.
- \`project\`, \`task\`, \`calling_agent\`, \`recommendation_reason\`, \`idempotency_key\`, priority, timeout, budget, tool permission profile and fallback policy.
- Swarm options: requested coordinator, worker types/models, verifier, requested agent count, isolation, timeouts and continuation policy.
- Job-scoped overrides must **not mutate global defaults** unless explicitly saved.

Example, **illustrative identifiers only**; validate actual model IDs first:

\`\`\`json
{
  "project": "SkinCreteERP",
  "task": "Implement physical-panel QR and installation-location traceability",
  "selection_mode": "recommended",
  "execution": {
    "route": "claude_openrouter",
    "model": "verified-glm-5.3-model-id",
    "reasoning_effort": null,
    "reason": "Good fit for economical implementation",
    "fallback_policy": "approved_routes_only",
    "swarm": { "enabled": false }
  },
  "idempotency_key": "erp-panel-traceability-v1"
}
\`\`\`

Other test cases: OpenRouter with verified GLM-5.3 Flash; Claude via GPT Proxy using Sol; \`codex_cli\` using an available authorized model; \`antigravity\` with an available Gemini/Claude coordinator and verified native Swarm.

**Routing priority:** explicit owner instruction → project access policy → authorized calling-agent selection → budget/quota/availability → project defaults → global defaults → approved fallback. Store *agent recommendation*, *policy decision*, *requested route/model*, *effective route/model* and reason for any change.

Provide tools corresponding to existing MCP naming conventions (names illustrative):

- \`execution_submit\`, \`execution_status\`, \`execution_cancel\`, \`execution_result\`
- \`execution_routes\`, \`execution_models\`, \`execution_health\`
- \`execution_config_get\`, \`execution_config_update\`, \`execution_profiles\`
- \`execution_events\`, \`execution_metrics\`, \`execution_artifacts\`
- \`host_metrics\`, \`storage_cleanup_plan\`, \`storage_cleanup_execute\`

Reject unsupported route/model combinations clearly; optionally offer known alternatives but never pretend fallback happened invisibly. Differentiate \`not_installed\`, \`unauthenticated\`, \`quota_limited\`, \`unavailable\`, \`healthy\`, \`degraded\`, and \`unverified\`.

## 4. Route adapters and subscription accounting

### Claude Code via OpenRouter
Reuse existing transport; discover supported models dynamically. Test specifically GLM-5.3 and GLM-5.3 Flash *if present*, under actual available model IDs. Report token and API cost from provider when available.

### Claude Code via GPT Proxy
Honor Astra/Sol/Terra alias mapping, backend model catalog, per-job effort and real context capacity. Default SOL. Record the logical alias and resolved backend ID. The request must be tested through the proxy; the UI display name is not proof of routing.

### Claude Code via official Anthropic
Respect existing approved subscription authentication; enumerate allowed models and quotas. Do not disguise flat subscription access as per-request actual API billing. Only allocate subscription costs as a separate accounting methodology.

### Antigravity
Use official CLI/protocol and current account capabilities. **Verify** Carbon, Argon, Flash, Opus/Sonnet names and model IDs rather than assuming them. Support configurable native Swarm coordinator/worker/verifier only to the degree supported by the installed CLI. Headless CLI support does **not** prove headless native Swarm support. If native Swarm is interactive-only, evaluate a supervised PTY/session bridge and label the limitations. Never invent a public Swarm API. Track parent-child jobs, model usage, worktree state and cancellation. Distinguish native Swarm from independent parallel tasks.

### Codex CLI — New fifth route
Integrate the **existing installed Codex CLI** directly; do not reinstall/reclone by default. Discover documented command syntax, \`exec\`/noninteractive behavior, model selection, reasoning configuration, JSON/stream events, sandbox/approval modes, resume, session IDs and usage telemetry. Match existing subscription or API access, without assuming billing semantics. Support single-job execution, cancellation, prompt/response capture, tool events, worktree isolation and exit verification. Expose a per-job route/model override and create a disposable-repo end-to-end test. Avoid recursively invoking the same controlling session through MCP without bounded nesting.

### Resource/cost semantics
Store actual API charges, estimates, subscription allocations and unknown usage **separately**. Unknown is NULL/unknown, never zero. Avoid double counting child agent usage, retries, cache credits or subscription attribution. Include pricing table version, estimation method and confidence. Enforce soft budget alerts and hard caps only where measurable and technically enforceable.

---

## 5. Durable Execution Ledger and operational memory

Prefer existing PostgreSQL/relational store if appropriate; inspect before introducing anything new. If no suitable service exists, select a dependable embedded or existing DB with migration/backups and an upgrade path.

Use append-only execution events and normalized projections including:

- \`projects\`, \`jobs\`, \`job_attempts\`, \`child_agents\`, \`execution_routes\`, \`model_catalog\`, \`route_decisions\`
- \`messages\` (prompt, context references, replies), \`tool_calls\`, \`tool_results\`, \`artifacts\`, \`reviews\`, \`test_results\`
- \`usage_events\`, \`cost_events\`, \`subscription_allocations\`, \`job_events\`, \`host_metrics\`, \`cleanup_plans\`, \`cleanup_audit\`
- \`configuration_versions\`, \`project_profiles\`, \`provider_health\`.

For each job persist: who initiated it, project, prompt and authorized context, prompt/version hash, requested and actual route/model, selection reason, timestamps (created, queued, started, first output, finished), queue/execution/end-to-end durations, status, failure category, retries, parent/child references, token breakdown where exposed, provider charge, cost estimate, verification/test results and accepted/rejected outcome.

**Full prompt/response history:** store authorized inputs and returned content for search/research, with ordered events, but redact credentials/tokens/PII according to policy, restrict access by project/role, offer configurable retention and purge/export. Never capture ambient secrets or cross-project private material merely because root access is available. Large binaries go to existing content-addressed artifact store; database holds immutable references/hashes, not arbitrary duplicates.

**Reliability:** idempotent writes, durable queue-state changes, atomic event persistence, reconciler after restart, stable job IDs, cancellation, bounded retry/backoff, no success status without artifact/test evidence. Explicit statuses include queued/running/waiting-for-auth/waiting-for-approval/partial/succeeded/failed/cancelled/quota-blocked.

**Analytics:** cost per **accepted** task; time to accepted result; success rate; latency; rework; quality by task difficulty; usage/cost by project/route/model; native Swarm versus single agent. Avoid misleading comparisons across incomparable task categories.

---

## 6. Agent communication: shared protocol + installable skills

Create **a proper versioned skill pack** in the target repository. Every calling agent (Claude, Codex, Gemini/Antigravity, ChatGPT MCP client, NikBot/Telegram) must learn **how to submit tasks, negotiate capabilities, poll/subscribe to events, interpret errors, retrieve evidence and cancel safely**.

Suggested layout (adapt to actual repo structure):

\`\`\`text
skills/
  mcp-execution-client/SKILL.md
  mcp-routing-and-model-selection/SKILL.md
  mcp-swarm-coordination/SKILL.md
  mcp-execution-ledger/SKILL.md
  mcp-host-observability-and-cleanup/SKILL.md
  mcp-project-memory-handoff/SKILL.md
protocol/
  execution-envelope.schema.json
  execution-event.schema.json
  error-codes.md
  capability-negotiation.md
  versioning.md
  examples/
docs/
  operator-guide-fa.md
  architecture.md
  runbook.md
  rollback.md
  phase-evidence/
\`\`\`

Each skill must include YAML frontmatter if required by the installed skill loader, purpose, triggers, authorized tools, exact request/response examples, error interpretation, retry/cancel semantics, model/route selection, result verification, security and idempotency. Provide short quick-reference versions for token efficiency.

**Protocol minimum:**
- Versioned envelope \`protocol_version\`, \`request_id\`, \`job_id\`, \`parent_job_id\`, \`project_id\`, \`caller\`, \`route/model preference\`, \`permissions\`, \`deadline\`, \`idempotency_key\`, \`payload\`, \`context_refs\`.
- Events: \`accepted\`, \`queued\`, \`started\`, \`agent_spawned\`, \`output_delta\`, \`tool_call\`, \`tool_result\`, \`usage\`, \`artifact\`, \`warning\`, \`approval_required\`, \`completed\`, \`failed\`, \`cancelled\`, \`heartbeat\`.
- Deterministic error codes, human-readable messages, retriable flag, retry-after where appropriate, capability and version negotiation.
- Structured results and artifact checksums, safe escaped text; do not parse arbitrary text as a success signal.
- Message envelopes over the existing MCP JSON-RPC transport; optional streaming, no new proprietary protocol when not necessary.
- Project memory handoff: context summary, decisions, constraints, current status, code branch/commit, open issues and next actions. No need to re-ingest the entire repo or duplicate Graphify index for every agent.

Test the skills by giving an uninformed caller an example task; it must discover routes, submit, poll, interpret provider errors and retrieve verified results without privileged implementation knowledge.

---

## 7. Graphify — avoid duplicate copies and index bloat

**Do not create new Graphify data directories, whole-repository copies, alternate indexes or nested clones unless the existing installation provably lacks a canonical store.**

Audit first: inventory Graphify binaries, services, configuration, index paths, project namespaces, content hashes, disk usage, symlinks and active readers. Distinguish intentional replicas/backups from accidental duplicates.

Implement:
- One configured **canonical Graphify store** with project namespaces, reuse existing path and schema.
- Incremental indexing based on content hash, repo-relative path, revision and namespace; avoid re-indexing unchanged content.
- Content-addressed reuse only where reference semantics allow it.
- Stable Graphify ownership metadata and reader counts/reference checks.
- Storage-budget guardrail and alerts, per-project inventory.
- Dry-run report listing apparent duplicates, references, bytes reclaimable and uncertain entries.
- Manual-review classification for ambiguous or active copies.

**Never delete on filename similarity or blindly merge different snapshots.** Canonicalization may require a migration plan, verification that readers are redirected, consistent checksums, backup of metadata and tests before deleting any old material. No uncontrolled recursive copy, tarball or tree duplication. Do not break legal RAG search or existing project memory.

---

## 8. Git worktree lifecycle and disk safety

Keep the primary repository path, original branch and any in-progress owner work intact.

Use ephemeral worktrees only when helpful for parallel tasks, under **one managed workspace root** discovered/configured at runtime; stable owner/job metadata in DB. Track \`job_id\`, repo, branch, creation time, state, active process/session PID, locks, dirty files, remote status, commits, PR link and artifact retention.

Automate **eligible completed worktree cleanup**, with rigorous checks:

1. Parent/child jobs finished and accepted; no live process, active agent, lock, open PR operation or resumable task needs it.
2. Worktree is **clean**; if dirty, preserve changes, ask for review and do not destroy.
3. Commits are pushed or otherwise durably retained; never discard unique/unmerged commits.
4. Artifacts/logs are persisted outside the worktree with validated hashes.
5. The worktree is managed by this system and is **not** the main worktree or any unmanaged user directory.
6. Apply configured grace period/TTL, retention policy and disk-pressure exception policy.
7. Run \`git worktree remove\` safely, then \`git worktree prune\` only after validation. Do not use force removal by default.
8. Audit what was removed and reclaimable bytes, verify original repo/branch unchanged.

Provide dry-run, reclaim estimates, preview, owner-approved execution and rollback for reversible actions. Worktree deletion may be irreversible, so require explicit confirmation for ambiguous or dirty candidates. Keep periodic housekeeping within bounded quotas and exclude active jobs.

---

## 9. TUI + authenticated Persian RTL Web UI

### Terminal management
Extend existing \`mcpctl\` if present; do not shadow an unrelated command. Main command: \`mcpctl\`, with \`mcpctl routes\`, \`mcpctl antigravity\`, \`mcpctl jobs\`, \`mcpctl host\`, \`mcpctl cleanup\`. Preserve any existing \`sam\` terminal launcher.

Editable controls:
- All **five routes**, connection/auth/quota status, current model list and last successful handshake.
- Agent recommendations versus actual route/model; per-project and per-job overrides.
- Astra/Sol/Terra aliases, **SOL default** for GPT Proxy, effort levels if supported.
- Antigravity coordinator, worker and verifier model, requested agent count, native Swarm, concurrency, timeout, retry, worktree policy.
- Root/unprivileged identity and default/auto/turbo permission profiles, with effective state.
- Project profiles: \`erp-fast\`, \`erp-deep\`, \`rag-development\`, \`shahrzad-fullstack\`, \`low-cost\`, \`critical-review\`.
- Config edit, validation, versioned atomic save, reload, import/export, rollback, dry-run and change audit.
- Jobs, queue, prompts/replies, events, costs, test results, provider errors.
- Host CPU/RAM/swap, mounts/disks/inodes and pressure with timestamps.
- **Safe disk cleanup** dry-run, itemized plan, scoped confirmation and execution.

### Web UI
Build a protected, mobile-friendly **Persian RTL** dashboard using **Vazirmatn** and reusable existing Persian UI components/design system if available. Do not add public exposure by default.

Pages:
1. Overview: health, routes, jobs, queued/running, success, spend and resource pressure.
2. Routes/models: five provider cards, connectivity/auth/quota health, discovered models, effort and policy.
3. Active jobs: progress, nested Swarm workers, event stream, cancellation and evidence.
4. History: searchable authorized prompts/responses/tool calls, project, agent, model, cost, duration, artifact and trace.
5. Cost/performance: model/route/project analytics, estimated vs charged vs allocated subscription cost; accepted task comparisons.
6. Settings: validated per-project profiles, model-role selection, worker count, root/turbo state, routing policy, fallback.
7. Host: CPU load, RAM, swap, **every mounted filesystem's size/used/free/inodes**, growth, Graphify footprint, managed worktrees and caches.
8. Cleanup: **"Safe Disk Cleanup"** action with a dry-run inventory table, bytes reclaimable, risk class, exclusion list, and explicit execution authorization; progress and audit history.
9. Diagnostics: logs, config history, model probe status, last tests, rollback.

### Host telemetry
Use \`/proc\`, system interfaces and validated libraries (e.g. psutil if already suitable); prefer read-only low overhead. Persist sampled trends with bounded retention. Detect mount boundaries and avoid crossing them. Alert on filesystem/inode pressure, memory/swap pressure, log growth and unusually large duplicate Graphify stores. Never present sampled health as real-time if stale.

### Safe disk reclamation protocol
**No button should mean \`rm -rf\` on arbitrary paths.** Implement two-phase plan/apply with per-item risk classification and a dry-run preview.

Allowed *candidates* after validation: completed safe worktrees, abandoned managed temporary files, expired **owned** logs respecting retention, explicitly identified redundant Graphify copies after reference checks, old cache entries with documented rebuildability, stopped containers/images unused by active services *only after independent confirmation*.

Always exclude by default: active repos/main worktree, dirty or unpushed branches, running sessions/jobs, database data and WAL, backups and recovery points, production storage, secret stores, mounted external storage, live containers/volumes, unknown files, active Graphify indexes and uploaded user artifacts.

Before apply: enumerate precise paths/IDs, inspect ownership/locks/references, estimate bytes, check device/mount, capture evidence and request a deliberate UI approval for destructive deletion. Use scoped deletion primitives, never broad globs, never cross mount boundaries. Recheck eligibility immediately before deletion (TOCTOU protection). Record operator, timestamp, result, freed bytes, checksums/IDs and errors. Failed cleanup must leave inventory consistent. Provide an emergency disable switch.

---

## 10. Autonomous phase orchestration, engineering quality and pushing

Use existing branch and repo placement. Do not make N clone copies or new Graphify trees to parallelize.

**Checkpoint workflow after each coherent phase:**
1. Save redacted baseline and config changes.
2. Implement smallest viable slice.
3. Run unit/integration/regression tests and lint/type checks appropriate to changed components.
4. Verify a harmless real job end-to-end where authenticated.
5. Inspect \`git diff\`, untracked files and size growth; scan for secrets, keys, PII and unintended generated binaries.
6. Commit with meaningful conventional message.
7. Push via existing remote/branch, honoring branch protection and never force-pushing.
8. Log commit SHA, test evidence and push result in \`docs/phase-evidence/\`.
9. Report a short Persian checkpoint to owner and continue automatically.

If the local repo's origin differs from the requested GitHub target, do **not** arbitrarily rewrite origin. Establish a separately named remote when authorized and compatible, or push the reusable skill/control-plane content to the requested repository using the existing authenticated workflow. Distinguish code-repo commits from documentation-repo commits. Do not move the product repos.

**Recovery:** backed-up configuration, reversible migrations, feature flags for new routes, previous adapter fallback, independent access to terminal/tmux, backup and restore tests. Avoid breaking currently working CLI sessions.

**Tests required:**
- Each of the five routes enumerates; actual execution tested where authenticated.
- OpenRouter regular + Flash model availability validated; GPT Proxy Astra/Sol/Terra mapping tested, SOL default persists.
- Codex CLI executes, returns structured artifacts, and reports failure correctly.
- Antigravity executes; native Swarm tested separately and not falsely reported if unavailable.
- Per-job route/model overrides and recommendation policies are auditable.
- Calling-agent protocol skill follows submit → status/events → final result → artifact validation.
- Ledger retains prompt/reply, exact route/model, duration and usage status; reboots/retries do not duplicate charges.
- Concurrent jobs preserve DB integrity and rate limits.
- Main repo branch/path unchanged; dirty worktrees survive cleanup; clean complete worktrees safely removed with audit.
- Graphify unchanged files do not trigger duplicate copies/indexes; no reader breakage.
- Host RAM/disk metrics match OS readings; UI cleanup always performs preview and eligibility recheck.
- RTL UI usable, authentication and project-level access enforced; no credential leakage.
- Rollback of configuration/adapter/database migration tested.

---

## 11. ERP-first delivery and agent allocation

Make the control plane usable first. Then initiate an **ERP development readiness job** (not arbitrary production deployment) through MCP, using a profile chosen by the owner or current defaults.

Recommended editable profile \`erp-deep\`:
- Route: Antigravity, *if authenticated and verified*; otherwise approved available fallback.
- Coordinator preference: Carbon, or any **actually available** supported advanced model.
- Worker preference: Argon/Flash or Sonnet, according to availability.
- Verifier preference: Opus or advanced independent model.
- Requested agents: 4 (not a guaranteed native Swarm count).
- Root/turbo selectable, with job/project permissions made explicit.
- Feature branch/worktree isolation where compatible; verify cleanup gate.
- Tests required before accepting work.

Profile \`erp-fast\`: prefer inexpensive available model (GLM Flash, Gemini Flash or Sol through GPT Proxy), single agent or bounded smaller swarm, with verifier on critical changes.

Do not assume the latest named models, pricing, subscription eligibility or number of workers without checking live provider capabilities. Agent may recommend alternative route/model for the task and record rationale; owner may override.

**First ERP task suggestion:** trace a unique physical panel ID through production batch, QC, face-coat/painting subcontractor, shipping and exact installation location; prepare schema/UI/API work items with integration tests. Do not modify live factory data without a separate explicit go-ahead.

---

## 12. Operator documentation and final acceptance

Deliver:
1. Functional five-route execution adapter and correct GPT Proxy Astra/Sol/Terra aliases with **SOL default**.
2. Actual Codex CLI route and actual Antigravity route, truthful native Swarm capabilities.
3. Agent-controllable per-job route/model override with policy engine.
4. Durable prompt/response/event/token/cost/quality ledger, meaningful analytics.
5. Skills and shared versioned agent protocol with example callers.
6. Persian terminal control center and authenticated RTL Vazirmatn web dashboard.
7. CPU/RAM/disk/inode monitors and safe cleanup UI.
8. Graphify deduplication guards and lifecycle-safe worktree cleanup.
9. Tests, evidence, snapshots, recovery procedures, repository pushes.
10. A concise Persian operator guide with actual commands for starting the system and initiating ERP work.

**Final report (in Persian):** precise files modified, active five-route status, exact verified Sol/Astra/Terra mappings, native Swarm support and limitations, CLI commands to open menus, UI address (if actually deployed), database schema, Graphify footprint before/after, worktree count and disk reclaimed, test results, commit hashes, destination GitHub links, blockers and the **next exact command** to start ERP development.

**Do not say complete unless demonstrably complete.** If some P1/P2 items remain, clearly label P0 operational and list outstanding items. Keep working through the phases automatically while permissions, tool access and session allow. Do not invent future asynchronous execution.

## Operator's immediate instruction

Start in the **current** server directory and branch. Inventory, preserve, inspect the GPT Proxy mapping, set **SOL** as verified default, integrate Codex CLI as the fifth route, then deliver working execution + ledger + skills + UIs and cleanup safeguards. After each verified phase, commit/push relevant source or skills to **https://github.com/saeidsm/Nikbot-MCP-Skills** without relocating the repository or generating redundant Graphify copies. Proceed autonomously with testing and concise Persian phase updates.

**BEGIN IMPLEMENTATION NOW.**
