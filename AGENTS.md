# Meet Proxy product contract

31 October contextual invitation follow-up: patch 57 is published, NOT deployed,
as `20261031-current-space-invite`. Conductor blocked RunLocalCommand with
“Local execution is not enabled for this session” before execution. No retry or
alternate execution route was used; the live asset still matches
`20261031-setup-activation`. Invite now defaults to the
visible space and explains owner-only invitation access for members instead of
hiding their space. Loading retries keep the selected scope; My context does not
reuse a hidden board selection. All 17 invitation/browser checks and the exact
57-patch replay pass. This does not change permissions or fix work-machine
collection. See [current-space invitations](docs/CURRENT-SPACE-INVITE.md).

31 October setup recovery: patch 56 is published and live as server
`20261031-setup-activation`. All 34 browser checks, 11 setup/protocol checks,
56-patch replay, 160 deployed files/readability and three services pass. Setup now
preflights the existing account and actual host CLI. The browser prepares a
fresh-chat activation using the same unclaimed handoff instead of prescribing
a terminal-only plugin reload in Conductor or Claude Desktop. Send and host
approvals remain explicit; only native claims and collection receipts establish
progress. Native 0.4.33/runtime66 is unchanged. This does not implement account
migration or diagnose the separate work-machine companion failure. See
[setup recovery](docs/SETUP-PREFLIGHT-RECOVERY.md).

31 October invitation shortcut: patch 55 is published and live as server
`20261031-invite-cta`. A top-bar **Invite** button shows the sender’s email and
creates a link for a new or explicitly selected owned space. Private sharing
stays off; existing expiry, acceptance and revocation checks are unchanged.
All 13 invitation/browser checks, 41 broader UI checks, 55-patch exact replay,
160 live files/readability, three services and public TLS/setup/OAuth checks pass.
Native 0.4.33/runtime66 and classifier settings are unchanged. These UI checks
use synthetic accounts; prior P0 limits remain. See [top-bar Invite](docs/INVITE-CTA.md).

31 October imported-excerpt correction: patch 54 is published and live as
server `20261031-imported-excerpts`, with all 160 files/service readability and
three healthy services verified. The first signed two-account synthetic check
passed exact-body public sharing, private withholding, matching history, owner-only
checks, removal (404), old-link denial (403) and cleanup. This is not independent-
human or recipient-host acceptance. Imported conversations use exact stored message
bodies; generated message IDs and source titles remain private while complete
source context governs classification. Model, prompt v5, cutoff 0.995, rules and
native 0.4.33/runtime66 are unchanged. All 645 core tests, 14 extracted tests,
HTTP/OAuth/MCP smoke and exact 54-patch replay pass. Two additional prompt
experiments were rejected; neither is deployed. False withholding and broader
P0 acceptance remain open. See [imported excerpts](docs/IMPORTED-CONTEXT-EXCERPTS.md)
and `implementation/imported-context-excerpts-verification.json`.

31 October classifier follow-up: [candidate results](docs/CLASSIFIER-RELIABILITY.md)
and `implementation/classifier-reliability-verification.json` retain 367 actual
provider calls across baseline and candidate evaluations with synthetic content.
Selected prompt v5 shares 12/16 permitted original examples (baseline 8/16) and
12/20 additional examples (baseline 1/20); forbidden examples remain withheld.
A credential/endpoint-shared per-process FIFO (four active, 125 ms start spacing,
128 queued, existing deadlines) removes provider errors in the ten-owner burst:
10/10 public requests shared, no private content/metadata shared. Cutoff 0.995,
model, rules, authority and source fences are unchanged. Rejected prompt variants
and original failures remain retained. All 640 core tests, eight extracted queue
tests, extracted HTTP/OAuth/MCP checks and exact 53-patch replay across 217 files
pass. Server `20261031-classifier-reliability` is published and live: all 160
files/readability, three services, TLS and public setup/OAuth checks pass. The
first two-account signed production request still withheld an allowed imported
answer at 0.9921505. Private withholding, owner-only checks, matching shared
history, removal (404) and old-invitation denial (403) passed; test imports and
sharing were cleaned up. Original failures remain. Native 0.4.33/runtime66 is
unchanged. False withholding, cross-process capacity, recall and full P0
acceptance remain open. See PR #48.

29 October sharing stress follow-up: [results](docs/SHARING-STRESS.md) and
`implementation/sharing-stress-verification.json` preserve 96 real-provider calls
with synthetic data, ten-owner load and ordinary-question recall. The context
store classifies exact excerpts before disclosure; requester assistants answer
from approved shared context. Useful sharing remains unreliable: permitted facts
withheld, three recall misses, and 30 provider 429s in a 40-call burst. Patch 50
invalidates old opt-in explicitly when a removed member rejoins, fixing equal or
backwards timestamp resurrection. It was source-only at the stress run; patch 50 is now live in server
`20261029-cross-host-sync`. The original evidence is retained.
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
Host-required Send and approval steps must remain explicit. For newly installed tools in Conductor or Claude Desktop, use the browser’s fresh-chat activation; do not prescribe a terminal-only reload command.
Sharing defaults to 14 days, with 1/7/14/30-day choices; saving renews the window.
Native context-space tools create/invite/preview/accept/leave/archive within current
account and workspace scope. Joining never enables private-library sharing.
See [the current readiness audit](docs/CONTEXT-MVP-READINESS.md) and
`implementation/context-mvp-verification.json` for release state.
Cross-host setup patch 51 is live: five explicit app choices, current
versus paused/offline/error sync status, and source-read connection verification.
628 core tests, 27 setup/browser checks, 23 extracted-server checks and exact
51-patch replay pass. A fresh visible message from this chat was read successfully
from the live Mac archive after following phrase-search pagination. Regular Claude
and ChatGPT connections retrieve existing context; they do not collect web-only
chat history. Server `20261029-cross-host-sync` includes patch 50; all 159 files and three
services are verified, with public asset/OAuth/desktop/phone checks passing. See [cross-host sync](docs/CROSS-HOST-CONTEXT-SYNC.md).
Published native 0.4.33/runtime66 adds patch 52: progressing long-chat chunks
use spare upload slots before ordinary heartbeats, with the same six-upload
ceiling, atomic capture, exclusions and durable retries. Three new regressions
fail before/pass after; 631 core tests, both-alias packaging and 52-patch replay
pass. It is published and installed in both registries. On 31 October the
supported restart guard accepted runtime66 activation, and the persistent
background launcher was updated to 0.4.33. All 195 discovered sources reached
complete capture with no sync error; two fresh production source reads passed
at revisions 6603/6604, including text posted after activation. Account and saved
permissions were preserved, with no forced companion signals. The earlier
12-attempt deferral and runtime65 reads remain historical evidence. The initial
31 October check found runtime49 from an older loaded plugin; why runtime65
stopped is not established. See `implementation/context-upload-activation-verification.json`.
Source PR #45 and distribution PR #46 are
merged; the default distribution branch remains unchanged. See
[bounded catch-up](docs/BOUNDED-SYNC-CATCHUP.md).
The previous native release was **0.4.32/runtime65**; runtime66 is now active
on the verified Mac. Server
**20261029-cross-host-sync** is live; the prior question-discovery release
is retained. Patch 49 fixes empty full-question discovery
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
