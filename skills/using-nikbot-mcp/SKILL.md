---
name: using-nikbot-mcp
description: Use when an authorized caller needs Nikbot MCP project jobs, engine discovery, pending approvals, follow-up turns, results or artifacts, especially when execution status is uncertain.
---

# Using Nikbot MCP

**Pack version 0.4.0 — source contract inspected 2026-11-12.** This is a prepared caller reference, not an installed skill, deployment attestation or new wire protocol. The connected server's `tools/list` is authoritative. Use the existing authenticated MCP connection and negotiated MCP transport; never add a pack-version envelope to tool arguments.

## First task: discover, choose, submit, observe

1. Obtain an operator-granted **project ID**, approved task scope and existing authorized connection. There is no project-list tool. Do not guess paths/project IDs, enroll credentials or change server settings.
2. Use standard MCP `tools/list`, then `engine_capabilities()`. Missing tools/fields mean that feature is unavailable on this connection, not permission to use a private endpoint. A transport failure is not evidence a configured engine is absent.
3. If the owner selects a stable route, require `route` in the connected submit schema and `route_selection_supported:true` for that exact identity, then supply `route` and omit `target`. This selects the configured route, not an attested upstream provider. If the owner requires verified upstream identity, stop when that evidence is unavailable. Otherwise unverified health/authentication alone is not a failed probe or a reason to switch routes; an already-authorized bounded task may be submitted, subject to all backend/native gates. Without a route requirement, historical `target` is `codex` or configured `claudecode`, defaulting to `codex`. Choose an advertised model or omit it for the configured default; discovery never grants permissions or entitlement.
4. Persist the exact `submit_job` arguments and a unique stable `key` in the caller's authorized journal **before** submitting. Send a bounded, nonsecret task specifying goal, permitted changes, checks and stop conditions. Preserve the actual returned `job_id`.
5. Poll `job_status(job_id)` with bounded backoff and a caller-side wait deadline. If advertised, read `job_events` metadata using the bounded pagination below. There is no job-event subscription; MCP transport streaming is not job-event delivery. A caller wait deadline is not a runner deadline or cancellation.
6. Fetch `job_result(job_id)`. Handle a pending question or supplemental hold through the paths below. Stop automatic execution/replay on rejection, uncertainty, unfamiliar states or operator-inspection admission closure.

Minimal **request shape**, after substituting a real granted project and authorized task:

```json
{"jsonrpc":"2.0","id":"submit-1","method":"tools/call","params":{"name":"submit_job","arguments":{"project":"REPLACE_ALLOWED_PROJECT","text":"Read README.md if available and summarize readiness. Do not change project files, deploy or call external services. Follow required runner reporting; state missing evidence honestly.","key":"caller_readiness_001"}}}
```

The JSON-RPC `id` correlates one request; it is not the durable idempotency `key`. On an ambiguous submit response, an exact same-arguments/same-key retransmission can recover the existing job ID. Changed content with the same key conflicts. A new key is a new intent, not a recovery technique. Queue deduplication does **not** make subprocess/external effects replay-safe. No provider/route fallback follows an unknown outcome.

## Discovery identities are not dispatch targets

`routes`, when present in capabilities, describes five stable identities:

`claude_gpt_proxy`, `claude_original`, `claude_openrouter`, `antigravity`, `codex_cli`.

**None is a valid `submit_job.target`.** Use the separate optional `route` field only when advertised. This increment supports explicit selection of the one configured Claude identity with the strict permission service; nonconfigured identities and Codex/Antigravity explicit routes reject. There is no auto/recommended selection or fallback. Claude route identity is an operator assertion; binary names/model aliases do not identify providers. Antigravity has no implemented gateway adapter. Authentication/health/effective route/effective model remain unverified without runtime evidence. Requested, configured, resolved and effective models are different facts: requested GPT-proxy default `gpt-6.1-sol` is not installed-default proof. A strict profile cannot be enabled by a caller argument.

Omitted `target` is distinguishable from explicit `codex`: the latter conflicts with a Claude route. Sessions inherit the exact route/configuration binding; resume cannot switch routes or repair a changed binding. `route_unavailable`, `route_target_conflict`, `route_permission_profile_required` and `route_binding_changed` are refusals, not fallback signals. Preserve arguments/key/IDs and obtain authorized operator resolution; do not drop the route, change keys or route around the refusal. Existing target-only sessions report no route selection and are not retroactively attested.

## Actual 14-tool quick reference

Required arguments are shown without `?`. No tool accepts a caller-supplied owner.

| Tool | Arguments | Purpose / limit |
|---|---|---|
| `engine_capabilities` | none | Configuration/catalog discovery, not a live health probe. |
| `host_resources` | none | Bounded host observation for the configured owner with a current registered-project grant; partial readings, not execution headroom or authority. |
| `submit_job` | `project, text, key, target?, model?, route?` | New approved task; explicit configured strict route when supported, otherwise historical default target `codex`. |
| `job_status` | `job_id` | Owner-scoped snapshot. |
| `job_events` | `job_id, after_seq?, limit?` | Currently granted job's ordered coordination metadata. Start at `"0"`; integer limit 1–100, default 100. |
| `job_result` | `job_id` | Output/question and available evidence fields. |
| `resume_job` | `job_id, text, key, model?` | New conversational turn from eligible latest job; target is fixed per session. Omitted model retains current session model; changes require engine support. |
| `answer_question` | `job_id, question_id, text, key` | Answer the actual pending nonsecret question. Stale IDs reject; do not invent a question ID. |
| `permission_pending` | `job_id` | Supplemental approval records, not native permission verdicts. |
| `permission_get` | `approval_id` | Challenge, reason, expiry and live-hook status. |
| `permission_respond` | `approval_id, decision, signature` | Relay a genuine owner-held signature; decision is `allow` or `deny`. |
| `permission_resume` | `approval_id` | Revalidate that exact still-waiting hook; not a job resume or replay. |
| `job_artifacts` | `job_id, cursor?` | Actual artifact pages; initial cursor is `""`. |
| `artifact_file` | `job_id, artifact_id, path` | Previously approved artifact entry, never an arbitrary server path. |

Bounds: IDs are 32 lowercase hexadecimal characters; `project`/`key` are 1–128 ASCII letters/digits/`_`/`-`; `text` is 1–8000 characters; artifact `path` is 1–500 characters. Model syntax is bounded but **only the current reviewed catalog authorizes a model**. Signature input is exactly 88 characters; length validity is not signature validity or consent. Discover the full current schemas with `tools/list`.

## Response envelopes and polling decisions

Check transport/authentication failure and JSON-RPC `error` first. In a returned tool result, check `result.isError` before consuming `result.structuredContent`; HTTP 200 is not success. The private queue's `ok/result/error` framing is unwrapped internally and is not the caller-facing MCP payload.

Successful `structuredContent` has these source-defined shapes (placeholders below describe values, not executable fixtures):

| Tool | Shape / conditional fields |
|---|---|
| `submit_job` | `{job_id, replayed}`. `replayed:true` means exact-key/request recovery returned an existing ID, not a second execution. No state/model echo guaranteed. |
| `job_status` | `{job_id, state}`; owner-controller responses also include `execution_capacity`, nullable `route_selection`, and `handoff` when recorded. Route selection separates requested/configured identity and strict profile from nullable, unverified `effective_route`. |
| `job_result` | Status fields plus `text, question, question_id`. Question fields may be null, output may be empty. Owner evidence fields below are separate facts. |
| `job_events` | `{job_id, available, source:"coordination_events", events:[{seq, phase, created_at}], next_after_seq, has_more}`. Sequence IDs/cursors are decimal strings, not numbers. Unknown phases become `"unknown"`; invalid timestamps become null. |
| `job_artifacts` | `{job_id, enabled, artifacts, next_cursor}`. Disabled delivery: `enabled:false`, empty array, null cursor. |
| `artifact_file` | An artifact view for the approved entry, not a page. With neither configured delivery nor private handoff, it instead returns the disabled envelope above; never assume `file_url` exists. |

Queue `state` vocabulary and safe interpretation:

- `queued`, `running`: bounded polling; neither guarantees progress or success.
- `completed`: fetch and verify evidence; not proof of accepted task effects/tests.
- `awaiting_input`: fetch the actual question/ID and pause for an authorized answer; this can be human review after an execution failure.
- `answered`: historical question consumed into a new turn; follow the new job ID actually returned by the answer operation.
- `denied`: stop automatic execution/retry.
- `uncertain`, `interrupted`: stop replacement execution and seek operator reconciliation; neither proves the process stopped or effects were absent.
- Any unfamiliar state: preserve it and stop automation, rather than invent a transition.

Owner `job_result` independently reports `execution_state`, `process_state` (`claimed`, `running`, `uncertain`, `unknown`, `closed`, `not_started`), `report_state` (`complete`, `incomplete`, `unknown`) and `effect_state` from available handoff evidence, otherwise `unknown`. Conditional engine evidence includes `response_present`, `final_response_text`, `final_response_redacted`, `final_response_state` and nullable `actual_model`. Legacy `text` may contain a serialized review packet, not final-answer prose. Queue `awaiting_input`, execution `failed`, process `closed` and effects `unknown` can coexist legitimately.

For artifact pagination, start with omitted cursor or `""`; pass the actual nonempty `next_cursor`, and stop at null (do not send null). Cursors are empty or 32 lowercase hex characters. A rejected cursor requires restarting enumeration from the first page, not submitting another job. Published views can contain `artifact_id`, `status`, `delivery_state`, `summary_url`, `browse_url`, `zip_url`, and a selected `file_url`; unavailable/revoked/expired delivery omits links. Private handoff entries may instead provide `status:"private_ready"`, `inline_available:true` and `content`; ZIP content is base64. Interpret the actual view's encoding and verified manifest; do not blindly execute/decode content or treat a link as fetched bytes.

Source anchors: `remote_gateway/local_queue.py:307–365`, `remote_gateway/owner_controller.py:606–653`, `remote_gateway/mcp_bridge.py:130–143`; envelope and artifact checks in `tests/test_mcp_bridge.py`, `tests/test_owner_artifacts.py` and `tests/test_owner_review_handoff.py`. These are prepared-source contracts, not proof an older connected deployment supplies every field.

## Read recorded event metadata

After discovering `job_events`, start with `{"job_id":"ACTUAL_JOB_ID","after_seq":"0","limit":100}`. Check transport/MCP errors first. Require the returned job ID to match, `source:"coordination_events"`, boolean availability/pagination flags and an array of events. `available:false` means this queue cannot supply coordination history (legacy queue or missing/unreviewed read index); stop event enumeration and report unavailable, not “nothing happened.” No private endpoint or execution retry is authorized.

For an available page, retain ordered `seq` strings and `next_after_seq` in the existing authorized journal, keyed by this job. While `has_more:true`, pass that exact returned `next_after_seq` as `after_seq` with the same job ID. Decimal cursors have no leading zeros except `"0"` and are at most `"9223372036854775807"`; preserve them as strings (use exact integer comparison, not floating-point conversion). Sequences must increase beyond the input cursor, but gaps are normal. For a nonempty page require `next_after_seq` to equal its last event sequence exactly; for an empty page require it to equal the input cursor. Require a nonempty advancing page when `has_more:true`; on malformed/nonadvancing/unfamiliar output stop and preserve the discrepancy. Deduplicate by job ID plus sequence when recovering a repeated read.

Stop the current enumeration at `has_more:false`, including an empty page, which retains the input cursor. Later events may appear: bounded polling can start from the last returned cursor. Cap each catch-up at 10 pages or 15 seconds, whichever comes first; bound each transport wait to the remaining time. If a call times out or the bound is exhausted, retain the last fully validated cursor and report incomplete enumeration rather than loop indefinitely. Later polling requires a caller-selected overall deadline and bounded backoff; without those, return the handoff instead of scheduling another catch-up. None of these caller limits cancel the job. An empty/final page is not job completion, cancellation, full audit coverage or absence of side effects. This view includes only existing job-bound coordination records, not legacy queue events, all native tool logs or project-wide events; it exposes no retention/completeness guarantee or historical snapshot token.

Phase labels such as `approval_human_response`, `approval_finished`, `completed` or `secondary_usage_settled` are recorded categories, not proof of an allow decision, native permission, effect success, human identity or known spend. Unknown phase/time stays unknown. Inspect current status/result and the established approval/evidence tools for their own facts; no event instructs the caller to execute, approve, resume or replay an action. No free-text summary, reason, prompt, path, signature, approval preimage or raw evidence is delivered by this view.

## Read bounded host resources

Discover `host_resources` and its empty argument schema first, then send `{"name":"host_resources","arguments":{}}` through `tools/call`. No project, owner, job, path, process or freshness argument is accepted. The configured controller owner must still have a grant intersecting the current project registry; authentication alone is insufficient. Unauthorized reads are errors, not an unavailable sample. Never submit a shell job or use a private endpoint to obtain denied or missing telemetry.

After the normal transport/JSON-RPC/MCP checks, require `{available:boolean, reason, sample}`. `available:true` requires `reason:null` and a sample object; it means an observation returned, **not that every metric is known or the host is healthy**. `available:false` requires `sample:null` and one of these reasons:

| Reason | Caller interpretation |
|---|---|
| `unsupported` | This adapter cannot collect these facts; stop and report unavailable. |
| `closed` | Controller is stopping/closed; stop and hand off. |
| `busy` | One observation is still owned by the controller; no second worker was queued. |
| `timeout` | Server caller wait expired (currently 2 seconds); the real worker may still be running. |
| `observation_failed` | Collection failed; no private exception text or stale sample is returned. |

For `busy`, `timeout`, `observation_failed` or a transport timeout, this read-only operation may be retried only within a caller-selected overall deadline, at most three total calls, with at least one second between calls. Bound every in-flight wait to the remaining deadline; without a deadline return unavailable instead of retrying. Stop on authentication/authorization failure, malformed or unfamiliar output. A local timeout/cancellation does not stop the server worker or any job. The server retains one worker until settlement, discards its completed response, and starts a new observation for a later admitted call; there is no completed host-response cache or stale fallback. CPU sampling has the separate short cache below.

Sample fields and interpretation:

- `measured_at`: UTC ISO timestamp at completion of the fixed host-facts reads. It is not proof that any individual metric succeeded and does not make the whole sample an atomic snapshot. Report the observation time and caller receipt time; if the timestamp is absent/invalid or age cannot be established, freshness is unknown. Choose an explicit maximum acceptable age for the task; old samples must be labelled stale, not silently treated as current.
- `loadavg`: a string of Linux 1/5/15-minute load averages, **not CPU percent**, or `"unavailable"`.
- `mem_total_mib`, `mem_available_mib`: MiB, or `"unknown"`. Available memory is a host observation, not per-job allocation or guaranteed admission headroom.
- `swap_total_mib`, `swap_free_mib`, `swap_used_mib`: MiB or null. Used is total minus free; known zero is distinct from missing data.
- `filesystems`: rows for configured `state` and, when configured, `control` locations only. Each row has `scope`, `status`, nullable `device`, `total_mib`, `used_mib`, `available_mib`, `reserved_mib`, `inodes_total`, `inodes_available`. A status other than `"available"` means unknown readings, not zero. MiB is 2^20 bytes, counts are inodes. Used excludes all free blocks, available is unprivileged-available space, reserved is free minus available. Rows with the same device represent the same filesystem: **do not add them**. No raw paths are exported. `filesystem_scope` states that this is not a complete host mount inventory.
- `cpu`: `{available, percent, reason, interval_seconds, measured_at, scope}`. Host-wide percent is 0–100, not percent of one core or per-process usage. The first sample is normally null with `available:false, reason:"warmup_or_unknown"`; unavailable reads may use `reason:"unavailable"`. Neither means zero load. A known percentage has `reason:null`. The sampler uses cumulative-counter deltas, with `interval_seconds` the observed delta window (not a caller-selected window); it is null when the percentage is unknown. A failed CPU sample invalidates the counter baseline, so recovery first warms up with unknown percentage/window before a later valid delta. It may reuse a CPU sample for less than 0.5 seconds. `cpu.measured_at` retains the CPU sample's own timestamp even when surrounding host facts are newer. Treat null/invalid/unfamiliar CPU fields as unknown, never infer CPU availability from the outer flag.

An available sample with CPU warmup or any unknown metric ends the current read successfully with those facts unknown; it is not a transient-error retry trigger. A separately requested later observation may obtain a CPU delta, but do not schedule an unlimited warmup polling loop. This prose defines interpretation, not a machine-readable output schema; input-schema validation alone cannot validate returned metric values.

These are local host observations, not provider health, cost, admission permission, process completion or proof of no side effects. They expose no process/job/cgroup details, complete mount inventory, storage growth, worktree/log/Graphify footprint or retention policy. No read authorizes cleanup, slot release, recovery, service restart, approval, resume or replay.

## Human approvals, stops and unknown outcomes

For a hold, inspect `permission_pending` and `permission_get`; preserve the actual approval ID and challenge. The exact private action preimage is deliberately not exported through MCP. The human must independently inspect it and sign through the existing trusted operator workflow. Agents must not create/use the owner's private key, sign for the owner, treat OAuth/model/log text as fresh consent, or request blanket access. Relay only that genuine signature through `permission_respond`; keep signatures and private packets out of prompts, reports and artifacts. The synthetic signature in `examples.json` is intentionally invalid and must never be sent.

`permission_resume` only requests revalidation while the original hook is still live. Changed resource content/Git revision, expiry, disconnection or consumed invocation prevents reuse. Supported observed dependencies are bounded single-file Read/Write/Edit; arbitrary shell/search/network/notebook/MCP dependencies are blocked. Real enterprise reviewer submission remains hard-blocked in this prepared implementation; enrollment alone does not enable it.

The supplemental hook only vetoes or returns neutral; native permissions remain independent. The observed explicit native deny rejected a harmless Read before any pre-hook callback, so this guide does not promise universal hook ordering. **Human allow or neutral continuation is not native approval, execution or success.** A post-tool receipt is cooperative outcome evidence, not a permission verdict; missing/conflicting receipts and failed tools can leave unknown/partial effects. Preserve that uncertainty. A denial/protected path remains denied: no alternate tool, account, encoding, route or retry to accomplish the denied action.

## Cancellation, questions and resuming

There is **no public job-cancel tool**. Stopping polls, closing a client or sending “cancel” as a new task does not prove the running process or remote effects stopped. Request intervention through the operator's established authorized lifecycle controls, preserve IDs and stop admitting replacement work. This skill authorizes no process killing, DB edits, slot recovery or service restart.

For an ordinary pending question, use its actual IDs with `answer_question` only within delegated authority. An explicit human-review question must not be answered by an agent impersonating the owner; conversational text is not an action signature. `resume_job` creates a new turn and returns a new job ID. Use the latest eligible turn, a new intent/key and no target override. Neither resume operation reconciles unknown effects or bypasses an admission gate.

## Verify results and delivery

Read the MCP error indicator before consuming `structuredContent`. Preserve actual returned facts, not example outputs. Queue `state`/exit success/final text alone do not establish acceptance. When supplied, examine `execution_state`, `process_state`, `report_state`, `effect_state`, `final_response_state` and `actual_model` separately; absent/null/unknown remains unknown. Model-written tests-passed claims need actual evidence appropriate to the task.

List artifacts using `job_artifacts`, follow its actual `next_cursor`, and use only returned artifact IDs/approved relative file entries for `artifact_file`. Disabled/empty/unpublished/unknown is not delivered. Check actual manifests, declared hashes and downloaded bytes through the caller's already-authorized access; do not invent URLs or assume the MCP tool fetched them. Issued bearer-path links are usable by their holders: keep private links private.

End with a factual handoff in the caller's **existing authorized** journal: project, intent/key, job/question/approval/artifact IDs, requested versus observed target/model, last state/evidence, unresolved effects and next owner action. Exclude secrets/signatures/private packets.

## Not available through this MCP surface

No all-five-route execution, automatic/recommended routing, native Swarm orchestration, full event replay/subscriptions, cancellation/reconciliation, memory CRUD/search, per-job metrics/spend queries or complete host inventories, cleanup/retention controls, project listing, arbitrary filesystem/shell access or caller-supplied execution receipts. No per-job effort/budget/deadline/permission-profile fields. Do not emulate these through undocumented APIs or backdoor jobs; ask for the missing approved operator capability.

## Examples, validation and publication

[examples.json](examples.json) contains request-only schema fixtures for all 14 tools plus invalid counterexamples. IDs/project/model/signature values are synthetic placeholders; no successful responses, working credentials or consent are supplied. Do not execute the fixture collection as a workflow.

From this pack checkout, maintainers can run `python scripts/validate_pack.py` with an existing Python environment providing `jsonschema`. It validates fixtures against the [source-derived schema snapshot](../../protocol/tool-input-schemas.json), invoking **no tool handlers**. To re-export/compare against the source's actual in-process registry, use `docs/caller-skills/validate_examples.py` in the pinned source repository with its existing MCP/test dependencies. Neither check proves live authentication, native execution, deployment readiness or human comprehension.

See the [pack README](../../README.md) for installation, exact source provenance and publication limitations. A feature-branch push is not a merged release, local installation, server deployment or permission grant.
