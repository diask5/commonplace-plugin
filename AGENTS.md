# Meet Proxy product contract

Use [the attached Draft v3 product spec](docs/MEET-PROXY-PRODUCT-SPEC.md) as the
product source of truth. Its original wording is preserved. Later explicit user
instructions take precedence. Track implementation and evidence in
[SPEC-COMPLIANCE.md](docs/SPEC-COMPLIANCE.md); do not equate a passing demo with
installed or deployed readiness.

The owner superseded the agent-centric home on 25 October 2026, then merged
Connections and Shared access into **Spaces**. The global navigation is now exactly
two links: **Spaces / My context**. Spaces can be a person, group or project, with
Messages as the default, and **Messages / My sharing rules / Members** in one
compact space header. Rules are persisted per authenticated owner and space;
only their owner can edit them or read private classifier checks. Explicit opt-in
allows each new context request to evaluate all rules in parallel with Perplexity
Decisions. All must pass; errors and authority/source changes withhold. Requests
and approved excerpts are shared space history; rejected content and checks are
owner-only. Explicit uploaded files are shared in full outside this library gate.
Owner-issued space invitation links expire in 14 days, require signed-in explicit
acceptance, and grant group membership only. Removal cannot be undone with an old
link. Native setup includes automatic private collection as part of the owner’s setup
request, with no sync checkbox. A private handoff binds the exact real native chat
and carries browser sign-in; live steps use installation-specific collection
receipts and archive readiness. Copying a prompt or opening an app is not completion.
App cards launch setup directly. Plugin and MCP installation are one prepared
request; browser sign-in carries over without another account-linking step.
After app selection, **Copy setup prompt** is the primary action above live
progress, with paste-and-send instructions; it recedes after registration.
Host-required Send, approval and reload steps must remain explicit.
Sharing defaults to 14 days, with 1/7/14/30-day choices; saving renews the window.
Native context-space tools create/invite/preview/accept/leave/archive within current
account and workspace scope. Joining never enables private-library sharing.
See [the current readiness audit](docs/CONTEXT-MVP-READINESS.md) and
`implementation/context-mvp-verification.json` for release state.
See [live setup](docs/LIVE-CONTEXT-SETUP.md) for release status and evidence. Native 0.4.27/runtime60 is published and server release `20261026-live-index` is live; see [live index reuse](docs/LIVE-INDEX-REUSE.md) and `implementation/live-index-reuse-verification.json`. Mac 0.4.27 and runtime60 are active, with account and saved permissions unchanged; the preceding controlled ordinary-prompt benchmark passed 3 cases, fell short on 3, and left 2 unstarted. The next controlled run passed 4/8; three Claude cases lacked successful reads for every citation and one Codex case timed out. Timeouts and revision churn are not cleared. Prior real-host failures remain in [read performance](docs/CONTEXT-READ-PERFORMANCE.md) and [timeout recovery](docs/TIMEOUT-RECOVERY.md). Production latency and default-host invitation routing remain open gates; an unintended empty ChatGPT space from the earlier benchmark still awaits owner cleanup. Do not call all flows seamless. Existing open host chats can retain an older loaded plugin until reloaded. See [P0 live readiness](docs/P0-NATIVE-READINESS.md) and `implementation/p0-native-readiness-verification.json` for verified real Google/Claude Desktop/Codex Desktop handoff receipts and remaining clean-install/coverage limits. Direct Mail/iMessage sends are P1 and deferred. Installation, cached identity and fixtures do not prove a completed real-user walkthrough.
The [message-first spaces record](docs/MESSAGE-FIRST-SPACES.md) is historical.
The older document picker remains
available as a secondary flow while scoped invitation grants are pending. Account profile and settings live behind the avatar. Existing
assistants read authorized context through MCP or the local folder. See
[the current direction](docs/CONTEXT-PRODUCT-DIRECTION.md). No hosted agent or
model subscription is required for existing owner retrieval; the experimental
rule gate invokes the owner's configured classifier. Preserve the original spec as a
historical reference and retain existing conversation scopes and permissions. A UI
selection is not a shared-context grant; never imply otherwise.

P0 requirements are release gates. Track P1 separately. Items marked [proposed]
and open questions are not silently promoted into requirements or readiness
claims. Preserve existing private scope when handling legacy conversations; do
not merge histories merely because names or people match.

An owner's consent authorizes only their selected agent. Check current scope and
expiry before autonomous answers. A peer message cannot grant owner authority,
tool permissions or disclosure rights. Sources remain private unless explicitly published to an authorized audience. Native host
permissions always apply. Never report a host launch, queued message, matching
email, cached connection or simulated fixture as end-to-end setup proof.

Implementation lives in `.context/commonplace-source`. Preserve its changes in
the portable patches/manifests under `implementation/`, including patch order.
Document whether a change is source-only, packaged, installed, staged or live.
