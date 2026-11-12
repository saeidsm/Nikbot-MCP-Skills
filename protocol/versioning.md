# Caller-pack compatibility

Pack **0.2.0** describes an inspected source contract, not a new wire protocol. Use the existing negotiated MCP transport and standard JSON-RPC `tools/list` / `tools/call`. Never send `pack_version`, `protocol_version`, fabricated owner fields or an execution-envelope wrapper as tool arguments.

`tool-input-schemas.json` records an exact source commit and the actual input schemas advertised by that source's in-process MCP registry. It contains no runtime capability assertions, output schema, credentials or example consent. A connected server may be older, configured differently or unavailable. Check its tools and capabilities first; missing or incompatible features remain unavailable.

Version conventions for this documentation pack:

- Patch: corrected wording or examples without changing the described contract.
- Minor: additive, explicitly negotiated caller capabilities or new reference sections.
- Major: incompatible pack layout or caller-contract changes.

No version is an authorization token or live upgrade signal. Pin a reviewed Git commit; this repository does not install into a client or deploy a server automatically. Refresh snapshots from actual `tools/list` without invoking handlers, revalidate positive and negative examples, and review capability/authority wording before publication.

Never add guessed response/event schemas merely to mirror the historical directive. Current response shapes and uncertainty handling are described in the skill; event subscriptions, cancellation, memory/metrics/cleanup APIs and broad five-route execution remain outside the supported MCP surface described here.
