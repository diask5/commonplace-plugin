# Meet Proxy product contract

29 October sharing stress follow-up: [results](docs/SHARING-STRESS.md) and
`implementation/sharing-stress-verification.json` preserve 96 real-provider calls
with synthetic data, ten-owner load and ordinary-question recall. The context
store classifies exact excerpts before disclosure; requester assistants answer
from approved shared context. Useful sharing remains unreliable: permitted facts
withheld, three recall misses, and 30 provider 429s in a 40-call burst. Patch 50
invalidates old opt-in explicitly when a removed member rejoins, fixing equal or
backwards timestamp resurrection. It is SOURCE ONLY, not packaged/installed/live.
625 core tests, 27 browser tests and exact 50-patch replay across 211 files pass.
No threshold/model/prompt/host permission or production settings changed.

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
Cross-host setup candidate patch 51 is verified: five explicit app choices, current
versus paused/offline/error sync status, and source-read connection verification.
628 core tests, 27 setup/browser checks, 23 extracted-server checks and exact
51-patch replay pass. A fresh visible message from this chat was read successfully
from the live Mac archive after following phrase-search pagination. Regular Claude
and ChatGPT connections retrieve existing context; they do not collect web-only
chat history. Server candidate `20261029-cross-host-sync` includes patch 50 and
is not yet deployed. See [cross-host sync](docs/CROSS-HOST-CONTEXT-SYNC.md).
Current published native release is **0.4.32/runtime65**, installed in both
permanent registries with runtime65 active on the Mac. Server
**20261029-question-discovery** is live; patch 49 fixes empty full-question discovery
within the existing search budget. 611 core tests and the exact 49-patch replay pass.
The private question now finds four withheld candidates; useful public sharing
still withholds both new candidates below the unchanged 0.995 threshold.
See [question discovery](docs/QUESTION-DISCOVERY.md). The prior
**20261028-bounded-classification** release is retained; all 159 files/readability and three
services are verified. Patches 46–47 keep native source titles private and add
bounded owner-only stopped-request observations. No native package, threshold,
classifier prompt/model, permission, deadline or authority fence changed.
The 610-test core suite and exact 48-patch replay pass. Patch 48 batches source
classification under the existing eight-provider-call ceiling, with unchanged
threshold, model, prompt, deadline and privacy fences. The fresh Juniper Lantern
query completes with 26 audit entries (20 below threshold, six provider HTTP 429)
but still withholds every public excerpt; the
private query completes with all four candidates withheld. Its earlier source-change
and deadline stops remain preserved. Demo sharing is paused. A 5:22 Claude-centered replacement video now includes
real native messaging and fresh cursor-driven website interaction with narration.
It labels separate recorded examples and does not claim all-P0 readiness.
A later Sam-and-Zane scenario cut uses sections 6/7.5 and action-focused narration;
roles are disclosed as demo accounts, not independent human participants.
See `implementation/spec-scenario-video-verification.json`.
Claude blocked `finish_context_setup` as Data Exfiltration; two denied attempts
are retained, and the editing continuation did not retry or bypass the gate.
The earlier Chrome capture failed. A later Settings/read-only permission check
showed recording already enabled; the unchanged recorder completed a five-second
check and four real browser takes without permission edits. Claude setup approval
remains pending. Recorded private-topic checks withhold all four candidates; a
full-sentence query matched none and is not counted as a privacy pass. Sharing is
paused again. No host gate was bypassed. See [bounded classification](docs/BOUNDED-CLASSIFICATION.md) and
[the recording status](docs/FULL-VIDEO-RETAKE.md). The prior
`20261028-sharing-diagnostics` release remains retained.

The earlier selected-account checks follow. One signed public request
shares the approved launch answer; a later private request completes with all
12 candidates withheld. Both selected accounts see the approved history and
only the owner sees checks. Browser owner removal blocks requests/activity
(404) and the old invitation (403). The test space is paused, invitations revoked
and archived. Three earlier unavailable requests remain unexplained, not privacy
passes; reliability and independent-human/clean-machine/default-host gates remain
open. See [private native titles](docs/PRIVATE-NATIVE-TITLES.md),
`implementation/space-request-diagnostics-verification.json` and
[installed release evidence](docs/P0-EXCERPTS-RELEASE.md). The original
`20261028-native-excerpts` release and prior failures are retained.
An additional ordinary-prompt Claude Desktop check passed native space creation,
invitation generation and archival. The selected second account accepted through
the signed API; after native archival, a request and old invitation were rejected.
No host denial or private-sharing opt-in occurred. This is not recipient-host model
or clean-machine acceptance. See `implementation/p0-native-space-lifecycle-verification.json`
and [the real-footage video update](docs/P0-LIVE-VIDEO-UPDATE.md).
The previous published release is **0.4.31/runtime64**; runtime64 was active on the Mac
and server `20261027-context-guidance-r2` was live. Claude and Codex permanent
registries then used 0.4.31; two postdeployment installed-package source reads pass.
See `implementation/p0-installed-release-verification.json` and
`implementation/p0-live-release-verification.json`.
The previous 0.4.28/runtime61 and server `20261026-current-read` remain retained.
See [current-source retrieval](docs/CURRENT-SOURCE-READS.md)
and `implementation/current-read-verification.json` for exact source, package,
installation and production evidence. Candidate 0.4.29/runtime62 is packaged with
native/server GitHub drafts uploaded, not published, installed or deployed; `implementation/read-page-guidance-verification.json`
records its page-size guidance and preserved bounds. Existing open chats can retain older loaded
plugins until host reload. Account and saved permissions are preserved.

The [P0 closeout checklist](docs/P0-CLOSEOUT.md) records the remaining execution
order. Patch 36 adds bounded transport diagnostics only; 15 focused tests pass.
It is now included in locally packaged 0.4.30/runtime63 (patch 37), while uploaded
0.4.29 assets remain unchanged. The new candidate is not published, installed or
deployed. See `implementation/cloud-closeout-runtime-verification.json` for
package, smoke and independent review evidence. Diagnostics do not fix or identify
the failed-read cause, change permissions, or close live acceptance.

The newer [0.4.31/runtime64 candidate](docs/P0-READY-CANDIDATE.md) combines the
diagnostics with patches 38–39 and recoverable remote archive input errors
(patches 40–41). Both aliases are now published. The original server draft remains
unchanged; the separately published r2 server uses patch42's permission-preserving
deployment helper. Its first rollout failed with EACCES under umask077 and safely
rolled back. The corrected rollout verifies 159 live/readable files and healthy
services. See [deployment modes](docs/DEPLOYMENT-SOURCE-MODES.md). Merged PR #37 contains
the source and evidence. Original candidate hashes remain unchanged.
See `implementation/p0-ready-staging-verification.json` and
[live acceptance](docs/P0-LIVE-ACCEPTANCE.md). The full core suite passes 594/594.
See `implementation/p0-ready-candidate-verification.json` for exact hashes and
checks. Broader default-host, real-person sharing/revocation and clean-onboarding
gates remain open; installed retrieval and server rollout checks passed.

The [Conductor cloud benchmark](docs/CLOUD-P0-BENCHMARK.md) is complete.
Published-0.4.28 synthetic baseline: five clean lifecycle passes, one post-leave
scope-routing failure (no context leaked), and two retrieval routing failures;
Claude also cited one search-only source. Original failures and six unstarted
retrieval cases remain preserved. Patches 38–39 clarify owner-selected
space routing and successful-read requirements. Distinct candidate runs passed
3/3 space cases and 8/8 retrieval cases across Claude/Codex; all final citations
have supporting reads in the same session. Existing regression suites pass 8/8
and 26/26. See `implementation/cloud-p0-benchmark-verification.json` for the
39-patch replay, full catalog, fixture/provenance and host-isolation limits.
Temporary project settings were restored and all six scored-fixture servers
stopped. These guidance changes are now published, installed and deployed in
0.4.31/server-r2; they remain absent from local 0.4.30 packages. Cloud remote-MCP fixtures do not close installed-native or production
acceptance, the Mac failed-read diagnosis, or clean Google/Desktop setup.

The current ordinary-prompt run has seven clean passes and one correctly reported
synthetic name conflict; every final citation has a successful source read. The
separate uniquely named synthesis retest hit two connection-unavailable reads then
a harness guard on setup_status. See `implementation/current-read-native-benchmark.json`
and `current-read-synthesis-retest.json`. No host denial or permission change.
The owner authorized the exact additional diagnostic and disposable MCP acceptance
test tools, then directed execution to new Conductor cloud sessions. The latest Mac
command was explicitly denied at that point. On 27 October the owner explicitly
reopened this Mac, completed the existing GCP account sign-in, and directed repair.
The supported native candidate tests exposed an active-work upgrade guard and
old loaded launchers racing a graceful restart. A controlled handoff now runs
runtime64 with the account and saved permissions preserved. Two distinct
Claude/Codex synthesis checks pass with every final citation supported by a
successful current source read. See `implementation/p0-live-native-verification.json`.
Standalone nested model CLIs failed authentication before product tool calls;
actual Conductor-native sessions completed the separate synthetic benchmark.
Production SSH was verified after existing-account Google reauthentication. The
historical connection-unavailable read cause remains unconfirmed. Prior runs remain in
[read performance](docs/CONTEXT-READ-PERFORMANCE.md), [timeout recovery](docs/TIMEOUT-RECOVERY.md),
[live-index reuse](docs/LIVE-INDEX-REUSE.md) and [demand-built archives](docs/DEMAND-ARCHIVES.md).
The live-index run passed 4/8; demand-built passed five, hit one test allowlist
guard and left two unstarted. Production retrieval reliability and default-host
invitation routing remain open. The unintended empty ChatGPT space still awaits
owner cleanup. Do not call all flows seamless.

See [live setup](docs/LIVE-CONTEXT-SETUP.md), [P0 live readiness](docs/P0-NATIVE-READINESS.md)
and `implementation/p0-native-readiness-verification.json` for verified real
Google/Claude Desktop/Codex Desktop handoff receipts and clean-install/coverage
limits. Direct Mail/iMessage sends are P1 and deferred. Installation, cached
identity and fixtures do not prove a completed real-user walkthrough.
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
