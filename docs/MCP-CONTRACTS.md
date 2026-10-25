# MCP adapter and selected-agent connection contracts

Decision date: 24 October 2026. Candidate: **0.4.19-rc.3**, companion revision **53**.
Paths below are relative to the implementation source checkout. This records the
local implementation; it does not establish installed-host or production support.

## Shared adapter

`apps/commonplace/server/mcp-adapter-source.mjs` is authoritative. `npm run
build:mcp` uses pinned SDK 2.4.0 and esbuild 0.25.12 to produce identical standalone
bundles in both server directories. Generated files include the source digest;
the package builder rejects a stale digest. Each bundle has its dependency
licenses beside it. No runtime download or sibling source directory is needed.

The native stdio plugin, cloud archive tools, cloud network tools and authenticated
account `/mcp` endpoint use the adapter. Existing domain handlers still enforce
identity, scope, receipts and idempotency. The local companion's internal RPC
handlers retain their names and legacy negotiation helper.

Supported wire revisions are 2026-07-28, 2025-11-25, 2025-06-18, 2025-03-26 and
2024-11-05. The SDK owns modern discovery, legacy initialization and framing.
Version claims are never echoed as proof of support. Modern requests carry their
own capabilities; one request cannot authorize another request's Tasks support.

Initialization and catalog discovery are inert: they read existing scope metadata
without connecting accounts, creating databases, starting receivers or claiming
native chats. Native identity comes from the existing host binding, never
`clientInfo` or tool arguments. Real tool use activates the existing receiver
path. `setup_status` retains its diagnostic path.

Tool catalogs are sorted and input validation precedes activation. Schemas have
depth/node limits and cannot fetch external references. Requests are bounded to
256,000 bytes; validator caches are bounded. JSON text results also expose
`structuredContent`; context tools declare output schemas. Modern cache hints
are private with zero TTL. Authentication and authorization are always required
even if a client has cached content.

## Context projection

The archive remains authoritative. Resources call the same authorized list/read
functions as existing tools; they do not crawl the filesystem or grant code access.

- `meetproxy://context/index`: one bounded index page.
- `meetproxy://context/documents/{id}/revisions/{revision}/offsets/{offset}`:
  revision-pinned JSON containing source text, attribution and the next page URI.
- Search tools return resource URIs alongside their existing citation fields.

List cursors encode scope, revision and offset. They are pagination state, never
an access grant. Every underlying read checks access, and the projection rechecks
scope after reading. Revision changes require a fresh list. URI parsing rejects
filesystem paths, traversal and unsupported encodings. The existing local folder
and cloud archive preserve their atomic generation, digest and exclusion behavior.
The parity test compares actual Resource, tool and file content plus citation receipts.

Resource subscriptions are not implemented. Clients refresh through existing
revision-aware tools or Resource reads. MCP does not collect unsupported histories
or wake a sleeping computer. Owner context must remain within the originating
request's disclosure audience when an agent consults it.

## Durable work and clarification

`io.modelcontextprotocol/tasks` adapts the existing cloud task table and queue.
It is advertised on the modern path only. Ordinary run/read/cancel tools remain
the fallback. The adapter supports `tasks/get`, `tasks/update` and `tasks/cancel`;
clients poll at the returned interval. There is no new scheduler or notification
queue. Waiting for a device is reported as waiting work, never as execution proof.

An application failure completes with `isError`; authorization and malformed RPC
failures remain errors. A task needing clarification uses `input_required` when
the request declares form elicitation. Other clients see an actionable status
through ordinary tools and can use `continue_cloud_task`.

Migration 0043 stores accepted clarification text under `(task, revision)`.
Identical replay is idempotent; a changed replay is rejected. Resumption increments
the existing generation so a stale worker cannot commit over it. Cancellation
continues to fence work. Original prompt and selected target remain immutable;
clarification is appended and must stay within the owner's original scope. The
service allows at most 20 clarification rounds. Forms never request credentials.

## Selected-agent connections

`agent-connections.mjs` serves browser routes and native tools. Invitations bind
an inviter's existing agent; acceptance selects an existing attached agent owned
by the recipient. Native tools select the actual calling chat. Account binding,
device revocation and agent availability are checked again server-side. Accepting
an invitation creates no heartbeat, native identity, setup session or takeover.

Migration 0044 adds invitations and pair policies. The existing sorted pair's
unique `cp_mail_conversations` row is the sole thread for the new flow. Both
invitation directions, acceptance retries and later reconnection use that row.
Invitation tokens are random, stored hashed, and expire within seven days;
default connection access lasts two weeks. Each owner has separate topic and
expiry restrictions. The default excludes family, religion, finances and private
source disclosure. The earlier expiry applies to both directions.

New invitations for an active pair cannot extend its lifetime or replace its
existing topic restrictions. They apply the shorter lifetime and both sets of
topic restrictions. Replaying an already accepted invitation does not change
policy. Separate boundary-editing controls remain deferred.

Either owner can sever, including when an agent is unavailable. Future sends
stop; pending/claimed deliveries are blocked. Already dispatching or uncertain
deliveries retain their evidence for reconciliation because the host might have
accepted them. Old accepted invitations cannot reopen a severed connection;
fresh mutual acceptance is required and reuses the same audit thread.

Both owners retain read access to the shared thread after sever/expiry. This
implements the product spec's proposed audit-retention behavior. Connecting
agents defaults to messaging only. The spec-alignment source follow-up adds
explicit per-owner `authorizeAnswers` consent at invite/accept. Only the selected
native agent can read its current mandate through `read_agent_connection`; it
must require `canAnswer=true` before autonomous answers. Both boundaries and the
earlier expiry apply. Existing permitted context/read tools remain subject to
host approval, and private sources never become available to the peer. Existing
private delegation briefings and tools retain their scope and consent model.
This follow-up is not in the originally built or installed RC3 artifacts.

### Legacy migration choice

No bulk merge of legacy shared links or delegation threads is performed. Some
historical records identify a person or receiving session rather than a stable
sender-agent pair; merging them by person would fabricate provenance or widen
access. Earlier conversations remain accessible in the UI. A future migration
must require proven agent pairs, retain original IDs/timestamps and narrower
mandates, and separately review ambiguous records. The new pair-policy service
takes precedence over older general messaging grants for that exact pair once
the pair connection exists, so severing cannot be bypassed by an older grant.

## Remote authorization

Existing OAuth token validation runs before `/mcp` dispatch. Each domain operation
rechecks read/write scope and owner. Foreign origins are rejected; responses use
`Cache-Control: no-store` and vary by authorization/origin. Remote subscriptions
are disabled. The endpoint never creates a native chat identity from a request.
Tests cover owner and scope substitutions, expiry, redirect/resource/PKCE errors,
authorization-code replay and refresh-token reuse revocation.

Prompts (`find_context`, and native `connect_agents`) are explicit user-selected
workflows. Retrieving them validates arguments and performs no action. MCP Apps,
Skills extension publication, Registry/Server Cards, filesystem write proposals
and Channels are not part of this candidate.

## Rollout controls and rollback

These variables default on; setting exactly `0` disables the named adapter
feature for newly created adapters/processes:

| Setting | Effect |
| --- | --- |
| `COMMONPLACE_MCP_MODERN=0` | Uses SDK legacy transports, rejects modern envelope claims, retains legacy initialization/tools. |
| `COMMONPLACE_MCP_RESOURCES=0` | Removes Resource advertisement and handlers; search/read tools still work. |
| `COMMONPLACE_MCP_TASKS=0` | Removes the Tasks extension; ordinary durable-work tools still work. |

The modern SDK serving entries enable their modern versions independently of
the server's version list. Selecting legacy transports and rejecting modern
envelopes before dispatch is therefore necessary for an effective rollback flag.

Flags do not change identity, source access, host permissions, pair policy or
persisted tasks. There is no separate UI flag in this candidate. Restart native
MCP processes to pick up changed flags. Do not roll the service back to code that
ignores pair revocation or accepted task generations after these features are
used. Back up before migrations; prefer disabling protocol enhancements while
retaining the new authorization/fencing service. A whole-release rollback needs
a reviewed compatibility patch and retained durable data, not a database reset.
