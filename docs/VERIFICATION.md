# Caller pack 0.2.0 — verification scope

Prepared 2026-11-12 from `saeidsm/Codex-Cli-MCP` commit `9e7b8d9100f07d092f6460bd06760a95af71778f`. The product repository stays the implementation source of truth. This publication contains no service implementation, live configuration, queue database, credentials or private run artifacts.

## Completed checks

- Source-side validator read actual in-process MCP `tools/list`: **15 schema-valid and 10 schema-invalid examples, all 12 tools covered**. No tool handler invoked.
- Pack snapshot exported from that same registry using synthetic authentication and a queue stub which raises if any handler requests dispatch. Only tool names/input schemas plus explicit source/version metadata were exported.
- Standalone pack validator initially failed because its implementation was absent. After implementation: **7 tests passed**, covering valid pack, malformed input, missing coverage, version mismatch, duplicate cases/tools and invalid JSON-RPC envelope.
- Standalone validation: **15 valid / 10 invalid / 12 tools**. No network, live model or tool dispatch.
- A fresh uninformed caller read only the skill, examples and exported schemas, then authored a bounded caller. The lead inspected it and executed it against the actual in-process ASGI facade and durable queue with synthetic authentication/backend. Normal case: **7 requests, exactly 1 submit and 1 backend invocation**, status/result fetched, disabled artifact delivery correctly left unverified. Authorization-rejection case: **3 requests, 0 jobs, 0 backend invocations**, stopped without replacement work. Simulated response loss after accepted submit: **3 requests, exactly 1 queued job, 0 backend invocations**, original arguments/key preserved and outcome unknown; no replay, resume or fabricated approval. All three checks passed. These are executed isolated caller-contract checks, not live/native task or artifact-delivery acceptance; the temporary exercise code/evidence is intentionally not packaged as an executable client.

- Independent publication-content review: **Approve, no material findings** across the eight publication files plus `.gitignore`. Reviewer independently ran the 7 tests and 15-valid/10-invalid/12-tool validator, compared examples to the original source and checked API/authority wording. A follow-up review approved the updated caller-evidence paragraph and graph exclusions; the reviewer did not independently rerun the temporary caller exercise.

## Not established

- Live OAuth/owner enrollment, operational route/account entitlement, native model execution, actual provider charges or complete approval/cancellation coverage.
- Live server upgrade, merge/release on `main`, automatic installation or broader five-route implementation.
- A real end-to-end job completed by a fresh caller on production, native artifact delivery, browser acceptance or cleanup authority.

The API may advertise input shapes for operations still gated by configuration and authenticated owner/native permission. Satisfying an input schema is never sufficient authority. Required review unavailable, denial and uncertain execution remain non-permitting.

## Reproduce

Use the README's two offline commands with an existing `jsonschema` environment. They do not import the product repository. Compare the snapshot to a new source export before changing versions; a passing old snapshot cannot prove a changed source contract.

The historical directive remains unchanged. Generated navigation graphs and local test evidence are not publication content. No protected recovery, approval signatures, live interlocks, service restarts or permission-policy changes are part of this increment.
