# MCP research: sources, coverage and status

Snapshot: 24 October 2026. Companion: [implementation plan](MCP-ADOPTION-PLAN.md).

## Scope and reproducibility

Downloaded all **357 unique Markdown URLs** in the official [documentation index](https://modelcontextprotocol.io/llms.txt). Compared normalized URLs with the official [sitemap](https://modelcontextprotocol.io/sitemap.xml): all **357 sitemap URLs** are covered. The primary corpus contains **5,551,312 bytes**, with zero failed downloads and zero HTML-instead-of-Markdown warnings.

The archive includes released and historical specifications, draft, schema reference, tutorials, SDK/Inspector guides, registry documentation, extensions, published SEPs, all indexed working/interest group charters, governance and roadmap pages. It does not recursively download every linked RFC, video, image, issue, GitHub discussion, third-party website or package artifact. Repository snapshots supplement the main site where extensions keep their normative documentation elsewhere.

All indexed pages were archived. Assessment concentrated on the full current feature surface, relevant security/SDK guidance and product-relevant proposals; downloading a page is not a claim that every line of every historical version was individually reviewed. Historical/governance material remains available for audit and follow-up.

Local artifacts (gitignored research data):

- [Corpus README](../.context/mcp-research-20261024/README.md), [357-page index](../.context/mcp-research-20261024/INDEX.md), [coverage report](../.context/mcp-research-20261024/coverage.json).
- [Primary source manifest](../.context/mcp-research-20261024/manifest.json): original URL, final URL, status, content type, retrieval time, byte count, SHA-256, local path.
- [Downloader](../.context/mcp-research-20261024/download_docs.py) and [offline integrity verifier](../.context/mcp-research-20261024/verify_corpus.py).
- [Supplemental file manifest](../.context/mcp-research-20261024/supplemental-manifest.json), [repository pins](../.context/mcp-research-20261024/supplemental-repos.json), [npm package observations](../.context/mcp-research-20261024/npm-package-status.json).

These local links resolve in this workspace; a fresh checkout contains the tracked plan and this source guide, not the ignored corpus. The official URLs and repository pins below allow reconstruction. Re-fetch into a new dated directory when updating evidence rather than overwriting the reviewed snapshot.

## Evidence precedence

Use the released versioned specification/schema for protocol requirements; the corresponding versioned extension specification for extension behavior; live PR merge/status plus Final SEP for proposal acceptance; published package metadata and tests for SDK availability; actual installed host capability/tests for product support. WG charters and roadmaps explain intent and can be stale. A merged SEP, a downloaded SDK, a live socket and an actual model reply establish different things.

The versioned latest core specification observed is **2026-07-28**. `draft` and old SEPs are not substitutes for its current wire requirements.

## Current core specification: all 31 pages

Each page is archived under `docs/specification/2026-07-28/` inside the corpus. These links are the authoritative public counterparts.

| Page | Assessment disposition |
| --- | --- |
| [Specification](https://modelcontextprotocol.io/specification/2026-07-28/index) | Scope, JSON-RPC and host responsibility |
| [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index) | Keep host/client/server authority distinct |
| [Basic protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index) | Stateless envelopes, schema bounds, metadata and errors |
| [Versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning) | Dual-era implementation and honest compatibility |
| [Transport overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index) | stdio and Streamable HTTP adapters |
| [stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio) | Native plugin transport, discovery/fallback, stdout discipline |
| [Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) | Headers, origin/auth, streaming, retries |
| [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index) | OAuth/resource boundary for remote MCP |
| [Authorization-server discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery) | RFC 9728/8414/OIDC discovery and validation |
| [Client registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration) | CIMD preference, issuer-bound credentials, legacy DCR |
| [Authorization security](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations) | PKCE, issuer/audience, redirects and token handling |
| [Messaging patterns](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/index) | Synchronous, MRTR, subscriptions and Tasks distinctions |
| [MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr) | Continuation integrity and new request IDs |
| [Subscriptions](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions) | Opt-in notification streams; not durable native wake |
| [Progress](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress) | Active-request progress only |
| [Cancellation](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation) | Transport-specific request cancellation and races |
| [Server primitives](https://modelcontextprotocol.io/specification/2026-07-28/server/index) | Tools/resources/prompts control model |
| [Discovery](https://modelcontextprotocol.io/specification/2026-07-28/server/discover) | Required runtime discovery and supportedVersions |
| [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) | Structured output/schema, stable lists, explicit handles, errors |
| [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources) | Read-only context projection and resource links/templates |
| [Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts) | Optional user-selected workflows |
| [Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching) | Required hints, private isolation, MRTR exclusions |
| [Completion](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion) | Optional bounded, authorized suggestions |
| [Pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination) | Opaque cursor semantics and application snapshots |
| [Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging) | Deprecated; use stderr/OpenTelemetry for new work |
| [Elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) | Capability-gated form/URL choices, no secret collection |
| [Roots](https://modelcontextprotocol.io/specification/2026-07-28/client/roots) | Deprecated; no new dependency or assumed sandbox |
| [Sampling](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling) | Deprecated; no new wake/subscription-borrowing design |
| [Schema reference](https://modelcontextprotocol.io/specification/2026-07-28/schema) | Wire-shape source; use pinned schema in implementation tests |
| [Changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) | Confirms architectural changes since 2025-11-25 |
| [Deprecated registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated) | Retain only required legacy compatibility |

Additional relevant guidance: [security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices), [local server security](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/local-server-security), [client best practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices), [Inspector protocol eras](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras), [SDK tiers](https://modelcontextprotocol.io/community/sdk-tiers), [feature lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle), and [roadmap](https://modelcontextprotocol.io/development/roadmap).

## Extensions and supporting repositories

All pins are observed snapshots, not a claim that each HEAD is a published production artifact.

| Repository | Pinned commit | Use |
| --- | --- | --- |
| [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol/tree/dae694f61a31f7a3ec2af3aff709e11f70f61e48) | `dae694f61a31f7a3ec2af3aff709e11f70f61e48` | Spec, schemas, examples and SEPs |
| [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk/tree/951fe5603a7ec0b2dcb6a0b95d92cd86f93ad9e5) | `951fe5603a7ec0b2dcb6a0b95d92cd86f93ad9e5` | Dual-era server/client adapters, migration guide, conformance hooks |
| [ext-tasks](https://github.com/modelcontextprotocol/ext-tasks/tree/b3d28aceaa6d49f5f92258e3d06b61ad6f111e84) | `b3d28aceaa6d49f5f92258e3d06b61ad6f111e84` | Modern task state/methods and requester/receiver SDK distinctions |
| [ext-apps](https://github.com/modelcontextprotocol/ext-apps/tree/266a9e3b70dbd4a4f0546dda95da2a2c1a8be4b7) | `266a9e3b70dbd4a4f0546dda95da2a2c1a8be4b7` | UI resources, capability/metadata, sandboxed bridge |
| [ext-skills](https://github.com/modelcontextprotocol/ext-skills/tree/c1aa87e4c381c82b99aa37471d0eae4ab50f9985) | `c1aa87e4c381c82b99aa37471d0eae4ab50f9985` | Skill discovery, integrity manifests, optional directory reads, implementation matrix |
| [ext-auth](https://github.com/modelcontextprotocol/ext-auth/tree/15ca394e00a66434520b9ade26294999295a43ae) | `15ca394e00a66434520b9ade26294999295a43ae` | Machine/enterprise authorization options |
| [servers](https://github.com/modelcontextprotocol/servers/tree/51b6382a3e827aceb6bce430b1208d69b93d95ea) | `51b6382a3e827aceb6bce430b1208d69b93d95ea` | Reference filesystem tools and their limits |
| [experimental-ext-server-card](https://github.com/modelcontextprotocol/experimental-ext-server-card/tree/526201bbc80231daa40ffcdecfc9da4e54e5dc93) | `526201bbc80231daa40ffcdecfc9da4e54e5dc93` | Card schema/discovery; experimental wording conflicts with Final SEP |

Starting points: [extensions overview](https://modelcontextprotocol.io/extensions/overview), [Tasks](https://modelcontextprotocol.io/extensions/tasks/overview), [Apps](https://modelcontextprotocol.io/extensions/apps/overview), [Skills](https://modelcontextprotocol.io/extensions/skills/overview), [auth extensions](https://modelcontextprotocol.io/extensions/auth/overview), and [client matrix](https://modelcontextprotocol.io/extensions/client-matrix). Matrix blanks are not verified support or verified non-support.

Particularly important repository documents:

- `typescript-sdk/docs/protocol-versions.md`, `docs/migration/support-2026-07-28.md`, `examples/dual-era/README.md`: both eras, published entry points, and the extra stdio probe process.
- `ext-tasks/specification/2026-07-28/tasks.md`: modern `tasks/get/update/cancel`, task lifecycle, error semantics and notifications.
- `ext-tasks/packages/ext-tasks/README.md`: modern requester requires framing/dispatch integration; receiver helper is explicitly for 2025-11-25 sampling/elicitation.
- `ext-skills/docs/implementations.md`: SDK/host implementation readiness differs from specification status.
- `servers/src/filesystem/README.md`: explicit allowed directories, legacy Roots behavior, and non-atomic overwrite caveat.

npm registry observations: `@modelcontextprotocol/server@2.4.0`, `@modelcontextprotocol/client@2.4.0`, `@modelcontextprotocol/sdk@1.32.2`, `@modelcontextprotocol/ext-tasks@0.2.2`. The attempted package name `@modelcontextprotocol/ext-skills` returned 404; this establishes only that exact package lookup failed, not that no implementation exists. No package was installed or executed for this research.

## All indexed working and interest groups

| Working group | Relevance / disposition |
| --- | --- |
| [Filesystems](https://modelcontextprotocol.io/community/working-groups/filesystems) | Directly relevant future Resources writes/CAS; current deliverable Ideating |
| [File Uploads](https://modelcontextprotocol.io/community/working-groups/file-uploads) | Relevant later attachments; charter proposal status is stale |
| [Tasks and Events](https://modelcontextprotocol.io/community/working-groups/tasks-events) | Use released Tasks; monitor stabilization and callback proposals |
| [Transports](https://modelcontextprotocol.io/community/working-groups/transports) | Apply released transport semantics; monitor HTTP-over-stdio |
| [Skills Over MCP](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp) | Published extension, staged host adoption |
| [Progressive Disclosure](https://modelcontextprotocol.io/community/working-groups/progressive-disclosure) | Relevant to large catalogs; explores competing strategies, not a required standard |
| [Server Card](https://modelcontextprotocol.io/community/working-groups/server-card) | Optional discovery; reconcile charter/repo/Final SEP status |
| [Interceptors](https://modelcontextprotocol.io/community/working-groups/interceptors) | Experimental validation/transformation surface; do not rely on it for our privacy enforcement |
| [Registry](https://modelcontextprotocol.io/community/working-groups/registry) | Package/service discovery and distribution, not person pairing |
| [SDK](https://modelcontextprotocol.io/community/working-groups/sdk) | SDK compatibility and conformance; verify package versions, not stale charter targets |
| [Inspector V2](https://modelcontextprotocol.io/community/working-groups/inspector-v2) | Useful test tooling; pin verified release/features, not planned rewrite milestones |
| [Governance](https://modelcontextprotocol.io/community/working-groups/governance) | Proposal process/reference; no product runtime dependency |
| [Infrastructure](https://modelcontextprotocol.io/community/working-groups/infrastructure) | MCP project operations; no product runtime dependency |

| Interest group | Relevance / disposition |
| --- | --- |
| [Agents](https://modelcontextprotocol.io/community/interest-groups/agents) | Converted to IG October 16; evaluating an Agents extension, not a shipped orchestration contract |
| [Auth](https://modelcontextprotocol.io/community/interest-groups/auth) | Watch identity/delegation work; use released auth now |
| [Security](https://modelcontextprotocol.io/community/interest-groups/security) | Guidance and threat modeling, not a replacement for our enforcement |
| [Enterprise](https://modelcontextprotocol.io/community/interest-groups/enterprise) | Optional enterprise requirements later |
| [Enterprise-Managed Authorization](https://modelcontextprotocol.io/community/interest-groups/enterprise-managed-authorization) | Official extension exists; consumer launch does not require it |
| [Tool Annotations](https://modelcontextprotocol.io/community/interest-groups/tool-annotations) | Hints/UX; never treat annotation as trusted permission |
| [Financial Services](https://modelcontextprotocol.io/community/interest-groups/financial-services) | Domain-specific; no current product requirement |
| [Scientific Computing](https://modelcontextprotocol.io/community/interest-groups/scientific-computing) | Domain-specific; no current product requirement |

## Proposal status checks and documentation discrepancies

GitHub API responses are archived under `proposals/`. Status is as retrieved on October 24; re-check before implementation.

| Proposal | Observed evidence | Consequence |
| --- | --- | --- |
| [2571 Resource Submission](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2571) | Closed September 22, `merged: false`; closure calls for WG-led work | Charter's “open” statement is stale; no shipped create/delete standard |
| [2532 Resource Streaming](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2532) | Open, `merged: false` | Do not depend on standardized binary streaming |
| [1708 Client-Brokered Filesystem](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1708) | Closed issue with `state_reason: completed` | This is not a merge/release record |
| [2356 File Inputs](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2356) | Closed, `merged: false`; comment says superseded by 2631 | Charter's Draft status is stale |
| [2631 File Objects and Transfer](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2631) | Closed, `merged: false` | Successor is not a released file-transfer contract either |
| [2127 Server Cards](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127) | Merged October 6; published SEP Final | Charter still says Draft; referenced repo still says experimental. Verify versioned deployment contract before use |
| [1933 Workload Identity Federation](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1933) | Open proposal | Roadmap work, not permission to assume portable delegated native identity |

The current cancellation page requires a server cancellation notification when tearing down a subscription, while the subscriptions page also describes graceful completion results. Implementation should resolve the exact path against pinned SDK/schema/conformance evidence rather than guessing. No upstream issue was filed as part of this research.

## Host evidence and limits

- [Codex MCP documentation](https://developers.openai.com/codex/mcp), archived as `codex-mcp.html`/`.txt`: documents stdio, Streamable HTTP, bearer/OAuth and configuration. It does not prove this installation supports every 2026 feature or extension. The OpenAI Docs skill was used only to guide this host-specific lookup.
- [Claude Code Channels](https://code.claude.com/docs/en/channels.md) and [reference](https://code.claude.com/docs/en/channels-reference.md): native running-session notification capability, research-preview conditions and approved-channel restrictions. Custom channel development bypasses are not a production integration plan.
- [Claude Code MCP](https://code.claude.com/docs/en/mcp.md): host setup and permissions remain distinct from protocol support.
- Bundled [Conductor skill](/conductor/worker/conductor-skill/skills/conductor/SKILL.md): cloud/local environment, host controls and permission boundaries. `CONDUCTOR_IS_LOCAL=0` was observed. No host settings, receiver bindings or accounts were changed.

These are documentation and local code observations. No new live-host capability test, automatic-wake test, model benchmark or deployment was performed in this research turn. The plan names those as implementation exit gates.
