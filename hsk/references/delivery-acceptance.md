# Acceptance examples

Choose a short set matching actual impact and risk; these are examples, not a mandate to test every scenario. Preserve mandatory project checks. Demonstrate the complete agreed product through staged releases, not a throwaway MVP.

## Product/UI
- A permitted real role can open the original input, perform the task, recover saved progress and reopen the result.
- Test actual data associations, not only populated fixtures. Cover letters are not their attached scans.
- Test mobile/desktop as relevant; show what is local-only, server-saved, queued or converted. A provider listed in configuration is not proven usable.
- Validate access separation and meaningful failure states. Do not solve usability problems by deleting unsent work on navigation.

## Agent/MCP execution
- Authenticated request → selected runtime → read/edit → test/build → output retrieval → terminal state and released capacity.
- Exercise denied action, timeout/disconnection, cancellation and restart where relevant. Preserve uncertain outcomes and prevent duplicate external effects.
- A successful Read/Write canary is not proof of all adapters or arbitrary tool execution. Test one supported release path first; report unsupported routes plainly.
- Test continuation after real permission resolution. A secondary model's verdict does not substitute for actual native approval.

## Data and migration
- Match originals with identifiers, hashes and source evidence. Keep ambiguous associations separate; do not fabricate source records or transcription.
- Back up/restore appropriately; compare preserved records, roles and counts, and test idempotency/concurrency.
- No global queue draining or paid retry merely to test a small feature. Scope live probes and enforce their authorized ceiling.

## Capacity and usability
- Declare workload, active/concurrent user target and test environment; measure a bounded representative load and report latency, errors and resource saturation. Do not treat registered users as simultaneous jobs.
- Do not claim hundreds-user readiness from mocks or a health check. State measurement limits and the next scaling trigger.
- Inspect rendered responsive UI and exercise the main interaction; check readable hierarchy, controls, progress and error recovery.

## Artifact delivery
- Original output included, bytes/hash match, intended recipient can download, unauthorized access fails where required.
- Evidence tied to exact source/version and job; timestamps and expiry explicit when known.
- Keep private bearer links private. Never report publishing success from merely creating a local report file.

## Release evidence matrix
| Stage | Required evidence |
|---|---|
| Implemented | inspected diff or files |
| Tested | command, exact source, result, scope |
| Pushed | verified remote reference |
| Merged | actual merged reference |
| Deployed | running version/source and health |
| Enabled | effective gate/provider/role state |
| Accepted | representative user flow and retrievable output |

Evidence can justify only its stage. Record incomplete stages without dressing them up as success.
