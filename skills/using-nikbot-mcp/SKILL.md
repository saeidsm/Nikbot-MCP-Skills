---
name: using-nikbot-mcp
description: Use when an authorized caller needs Nikbot MCP project jobs, engine discovery, pending approvals, follow-up turns, results or artifacts, especially when execution status is uncertain.
---

# Using Nikbot MCP

**Pack version 0.2.0 — source contract inspected 2026-11-12.** This is a prepared caller reference, not an installed skill, deployment attestation or new wire protocol. The connected server's `tools/list` is authoritative. Use the existing authenticated MCP connection and negotiated MCP transport; never add a pack-version envelope to tool arguments.

## First task: discover, choose, submit, observe

1. Obtain an operator-granted **project ID**, approved task scope and existing authorized connection. There is no project-list tool. Do not guess paths/project IDs, enroll credentials or change server settings.
2. Use standard MCP `tools/list`, then `engine_capabilities()`. Missing tools/fields mean that feature is unavailable on this connection, not permission to use a private endpoint. A transport failure is not evidence a configured engine is absent.
3. If the owner selects a stable route, require `route` in the connected submit schema and `route_selection_supported:true` for that exact identity, then supply `route` and omit `target`. This selects the configured route, not an attested upstream provider. If the owner requires verified upstream identity, stop when that evidence is unavailable. Otherwise unverified health/authentication alone is not a failed probe or a reason to switch routes; an already-authorized bounded task may be submitted, subject to all backend/native gates. Without a route requirement, historical `target` is `codex` or configured `claudecode`, defaulting to `codex`. Choose an advertised model or omit it for the configured default; discovery never grants permissions or entitlement.
4. Persist the exact `submit_job` arguments and a unique stable `key` in the caller's authorized journal **before** submitting. Send a bounded, nonsecret task specifying goal, permitted changes, checks and stop conditions. Preserve the actual returned `job_id`.
5. Poll `job_status(job_id)` with bounded backoff and a caller-side wait deadline. No job-event stream/subscription API exists; MCP transport streaming is not job-event delivery. A caller wait deadline is not a runner deadline or cancellation.
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

## Actual 12-tool quick reference

Required arguments are shown without `?`. No tool accepts a caller-supplied owner.

| Tool | Arguments | Purpose / limit |
|---|---|---|
| `engine_capabilities` | none | Configuration/catalog discovery, not a live health probe. |
| `submit_job` | `project, text, key, target?, model?, route?` | New approved task; explicit configured strict route when supported, otherwise historical default target `codex`. |
| `job_status` | `job_id` | Owner-scoped snapshot. |
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

No all-five-route execution, automatic/recommended routing, native Swarm orchestration, event replay/subscriptions, cancellation/reconciliation, memory CRUD/search, metrics/spend queries, cleanup/retention controls, project listing, arbitrary filesystem/shell access or caller-supplied execution receipts. No per-job effort/budget/deadline/permission-profile fields. Do not emulate these through undocumented APIs or backdoor jobs; ask for the missing approved operator capability.

## Examples, validation and publication

[examples.json](examples.json) contains request-only schema fixtures for all 12 tools plus invalid counterexamples. IDs/project/model/signature values are synthetic placeholders; no successful responses, working credentials or consent are supplied. Do not execute the fixture collection as a workflow.

From this pack checkout, maintainers can run `python scripts/validate_pack.py` with an existing Python environment providing `jsonschema`. It validates fixtures against the [source-derived schema snapshot](../../protocol/tool-input-schemas.json), invoking **no tool handlers**. To re-export/compare against the source's actual in-process registry, use `docs/caller-skills/validate_examples.py` in the pinned source repository with its existing MCP/test dependencies. Neither check proves live authentication, native execution, deployment readiness or human comprehension.

See the [pack README](../../README.md) for installation, exact source provenance and publication limitations. A feature-branch push is not a merged release, local installation, server deployment or permission grant.
