# Meet Proxy Draft v3 compliance

1 November current closeout: native 0.4.44/runtime 77 is published, installed and active; server 20261101-context-throughput (patch 70) is live with 166 files, 47 migrations and four services verified. Balanced database storage and a normal verified/uploaded backup pass. Fresh native Personal progress, an accepted same-owner roundtrip and independent archive reading of the actual final pass. Work's selected Bland receiver is offline; no cross-person answer is confirmed. Patch 71 is published/reviewed, not deployed. The capacity upgrade completed read-only preflight only because Conductor dropped this chat's authorized Mac binding. Health still takes 4.26–5.74 seconds. See [sync closeout](SYNC-CLOSEOUT.md); these are scoped live results, not all-P0 readiness.

1 November sync closeout in progress: native **0.4.44/runtime 77** is published, installed and active on Mac/cloud; server **20261101-resumable-context** is live. The full Mac mirror now passes 823 document digests / 41,196,479 characters, and installed source reading passes.840 core checks, extracted packages, independent reviews and 69-patch replay pass. Final storage performance repair and native/Work reply acceptance remain pending; the selected Bland Work receiver was offline. See [current closeout](SYNC-CLOSEOUT.md).

1 November resumable context candidate (patch 68): native **0.4.43/runtime76** and server **20261101-resumable-context** are packaged and reviewed. Long downloads retain private validated partial progress; legacy file requests scan metadata once. 830 final core checks, 105 extracted-native checks, both-alias integrity, independent review and exact 68-patch replay across 264 files pass. Publication, installation and live acceptance are pending. See [resumable context](RESUMABLE-CONTEXT-PAGES.md) and `implementation/resumable-context-pages-verification.json`.

1 November background throughput (patch 67): server **20261101-background-throughput** is published and live. All 166 files/readability, 47 unchanged migrations, three services and public browser/OAuth checks pass. Background archive builds coalesce during uploads; bounded inbox writes commit atomically. Native **0.4.42/runtime75** remains active and unchanged. 801 core tests, 130 independent checks and exact 67-patch replay across 263 changed files pass. Observed local health latency improved to 2–4.4 seconds from 5.5–9.5 seconds; full large-Mac mirror and native/Work reply checks remain open. See [background throughput](BACKGROUND-THROUGHPUT.md) and `implementation/background-throughput-verification.json`.

1 November patch 66 is published and live as native 0.4.42/runtime75 and server 20261101-context-recovery. Both Mac/cloud companions activated; 166 production files, 47 unchanged migrations, services and public browser checks pass. Fresh native Personal publication/read and the actual prior assistant final in the synced archive pass. The large Mac mirror is still catching up, server requests remain slow, and targeted Work/native reply acceptance remains open. See [live context recovery](LIVE-CONTEXT-RECOVERY.md) and `implementation/live-context-recovery-verification.json`; full-flow readiness is not claimed.

1 November Work/sync repair: [targeted questions and recovery](WORK-SYNC-RECOVERY.md) (patch 65). Native **0.4.41/runtime74** is published, installed and active on the Mac and cloud; server **20261101-work-sync-recovery** is live with 165 files/readability, unchanged 47 migrations and three services verified. Both native aliases and distribution PR #67 are published. 749 core, 36 browser/setup, 47 extracted checks and exact 65-patch replay across 259 files pass; 58 deployment tests ran with one skipped. Account, host permissions, upload/mirror settings and responder settings were preserved/restored. This root long chat completed capture and its marker was read from source. Live Mac uploads are healthy, but the local mirror still times out obtaining the manifest while new uploads advance the archive. Work/native roundtrip checks remain pending. See `implementation/work-sync-recovery-verification.json`; these limits remain release evidence, not an all-host seamlessness claim.

1 November background collection follow-up: [Conductor staging discovery](STAGED-CONDUCTOR-COLLECTION.md) (patch 64, published 0.4.40/runtime73). Two regressions fail before/pass after; 699 core checks, 48 extracted checks and 64-patch replay across 247 files pass. Both aliases and registries are published. Cloud runtime73 is active; a fresh Codex chat loaded 0.4.40, published progress, delivered one native message (101s to acceptance), and its assistant marker was read from the native archive. Mac installation passed, but its last observed runtime was66. Incoming delivery removed the Mac execution binding during a bounded upload pause/update attempt; final activation and finally-based sync restoration are unverified. The long original chat advanced from record94 to577 and remains incomplete. Server `20261101-oob-activation` stays live. Do not claim seamless all-host or full-history readiness.

1 November slow-upload fairness follow-up: [durable upload turns](UPLOAD-FAIRNESS.md) (patch 63, native candidate 0.4.39/runtime72). Two regressions fail before/pass after; 697 core and 34 extracted collector checks pass. All 63 patches replay exactly across 246 files. Publication and activation are tracked in `implementation/upload-fairness-verification.json`; server `20261101-oob-activation` remains live.

1 November activation follow-up: [guarded updates and startup reporting](OOB-ACTIVATION.md) (patch 62, published 0.4.38/runtime71). Five regressions reproduced before/fixed after; 695 core, 53 setup/browser/account checks and 62-patch replay pass. Work membership and this chat’s receiving side were repaired; a synthetic shared message was read by the other selected account. Both registries are updated, runtime71 is active on the Mac and cloud, and server `20261101-oob-activation` is live. Initial context catch-up remains under observation. Installed/active runtime and live evidence remain separate in `implementation/oob-activation-verification.json`. No all-host seamlessness claim.

1 November production rollout: server **20261101-space-events** is live. Its
165 files and service readability, all 47 migration digests, verified database
backup/rehearsal, fresh worker heartbeat and three services pass. Native
**0.4.37/runtime70** is published in both aliases and the distribution branch;
Mac installation passed with the account and saved permissions preserved.
Runtime66 remains active after 12 supported upgrade attempts returned the active-work
guard; the temporary collection pause was restored and sync is healthy. Runtime70
activation and fresh-host tool loading remain open. Signed production event/cursor
reads, Personal invitation rejection, archived-space denial and cleanup pass.
The earlier 60-second smoke-command timeout is retained. This supersedes the
older source-only/deployment-blocked status below. The explicit new deployment
request restored Mac execution; no permission bypass was used. See
[rollout evidence](SPACE-EVENTS-ROLLOUT.md).

1 November continuous upload candidate: patch 61 removes the six-upload clamp
and five-second backlog pause, using cooperative catch-up slices and an
incremental file index with periodic reconciliation. Server backpressure persists
across restart; account, exclusion, payload and complete-capture fences remain.
A synthetic 6,722-file index with 6,000 queued messages takes one pass instead of
ten, with 90% fewer discovery file checks; mocked-upload processing is 6.56s to
2.29s, not a production throughput measurement. 685 core tests, 17 extracted
checks, both-alias integrity and exact 61-patch replay across 242 files pass.
Native 0.4.37/runtime70 is packaged locally, not published or installed. It includes
the locally packaged Spaces event work; server migration/live activation and the
existing Mac execution block remain. See [continuous sync](CONTINUOUS-CHAT-SYNC.md).

1 November Spaces events candidate: patch 60 makes events common to every Space;
Personal is the private default using the same group/message/change-log system.
MCP subscriptions notify by URI, clients resume durable cursors, and every source
read rechecks current access. Shared events contain approved references only.
Native 0.4.36/runtime69 and a 165-file server bundle are packaged locally, not
published, installed or deployed. 679 core, 41 browser/probe and 16 extracted
checks pass; exact 60-patch replay matches 239 files. Migration 0046 is required.
Host wake is not guaranteed, and the existing Mac execution block is unchanged.
See [Spaces events](PERSONAL-SPACE-EVENTS.md).

31 October upload optimization: patch 59 publishes native 0.4.35/runtime68 and
server `20261031-compressed-context`. Gzip is negotiated
per relay, retaining the 64,000-byte decoded limit, durable retry identity,
complete captures, account ownership, exclusions and sync opt-out. Native batches
rise from 40 to 100 messages within the same six-upload ceiling; JSONL reads use
256 KiB windows. A 30,000-message synthetic backlog uses 77% fewer payload bytes
and 39% fewer requests; this is not a live Mac measurement. 665 core tests,
13 extracted-native checks, both-alias integrity and exact 59-patch replay across
226 files pass. Neither native activation nor production deployment is complete;
the previous Mac execution denial remains. See [faster uploads](FASTER-CHAT-UPLOADS.md).

31 October multiple-account release: patch 58 adds isolated native account
profiles and a selected account per actual native chat. Context and messaging pin
that choice; existing threads remain on their original account. Capture in an
explicitly selected profile starts paused and requires the owner choosing to sync
that whole chat. Canonical uploads and pending retries enforce the account fence;
secondary profiles never bulk-upload unassigned histories. Host permissions and
browser account scopes are unchanged. Native 0.4.34/runtime67 is published. 657 core tests, nine isolation regressions,
five extracted-package checks, both-alias packaging and 58-patch replay across
223 files pass. It is not installed or active on the Mac. The previous Mac execution
block remains; no retry or alternate route was used. See [multiple accounts](MULTIPLE-ACCOUNTS.md).

31 October contextual invitation follow-up: patch 57 is published, NOT deployed,
as `20261031-current-space-invite`. Conductor blocked RunLocalCommand with
“Local execution is not enabled for this session” before execution. No retry or
alternate execution route was used; the live asset still matches
`20261031-setup-activation`. Invite now defaults to the
visible space and explains owner-only invitation access for members instead of
hiding their space. Loading retries keep the selected scope; My context does not
reuse a hidden board selection. All 17 invitation/browser checks and the exact
57-patch replay pass. This does not change permissions or fix work-machine
collection. See [current-space invitations](CURRENT-SPACE-INVITE.md).

31 October setup recovery: patch 56 is published and live as server
`20261031-setup-activation`. All 34 browser checks, 11 setup/protocol checks,
56-patch replay, 160 deployed files/readability and three services pass. Setup now
preflights the existing account and actual host CLI. The browser prepares a
fresh-chat activation using the same unclaimed handoff instead of prescribing
a terminal-only plugin reload in Conductor or Claude Desktop. Send and host
approvals remain explicit; only native claims and collection receipts establish
progress. Native 0.4.33/runtime66 is unchanged. This does not implement account
migration or diagnose the separate work-machine companion failure. See
[setup recovery](SETUP-PREFLIGHT-RECOVERY.md).

31 October invitation shortcut: patch 55 is published and live as server
`20261031-invite-cta`. A top-bar **Invite** button shows the sender’s email and
creates a link for a new or explicitly selected owned space. Private sharing
stays off; existing expiry, acceptance and revocation checks are unchanged.
All 13 invitation/browser checks, 41 broader UI checks, 55-patch exact replay,
160 live files/readability, three services and public TLS/setup/OAuth checks pass.
Native 0.4.33/runtime66 and classifier settings are unchanged. These UI checks
use synthetic accounts; prior P0 limits remain. See [top-bar Invite](INVITE-CTA.md).

31 October final rollout: [imported excerpt correction](IMPORTED-CONTEXT-EXCERPTS.md)
is live as `20261031-imported-excerpts`. All 645 core tests, 14 extracted tests,
HTTP/OAuth/MCP smoke and exact 54-patch replay pass. The fresh two-account signed
production check shared the exact allowed message body, withheld private content,
kept checks owner-only, matched both histories and passed removal/old-link denial.
All test sharing and imports were cleaned up. This does not close the retained
false-withholding, independent-human, clean-host or original P0 design gaps.

31 October production update: classifier server `20261031-classifier-reliability`
is published and live; all 160 files and three services pass. The first signed
production public request was still withheld below the unchanged cutoff.
Private withholding, shared history, owner-only audit and revocation passed.
[Exact release and first-attempt evidence](CLASSIFIER-RELIABILITY.md). The
candidate-only and authentication-blocked observations below are historical.

31 October [classifier reliability candidate](CLASSIFIER-RELIABILITY.md): patch
53 keeps the 0.995 cutoff and existing model, improves the original allowed sample
from 8/16 to 12/16, and completes the ten-owner burst with 10/10 public requests
shared and zero provider errors. Forbidden samples remained withheld. All 640
core tests and exact 53-patch replay pass. The server candidate is packaged,
not deployed: Google Cloud reauthentication blocked production preflight.
Remaining false withholding and broader P0 gaps are explicitly retained.

31 October [exact mapping of the ten original P0s](P0-SPEC-MAPPING.md): the new
attachment matches the preserved Draft v3 byte for byte. The original pair-based
inbox and answer-only source protection must be distinguished from the later
Spaces/excerpt-sharing design. Approved excerpts and Space exchange history do
not prove section 7.9 answer-only disclosure or a complete pair-agent Q/A audit.
The mapping records implementation, selected live evidence and outstanding
acceptance separately; it does not undo the owner's later product direction.

31 October [context upload activation](BOUNDED-SYNC-CATCHUP.md): the existing
0.4.33/runtime66 package is now active on the owner's Mac and its saved background
launcher is updated. All 195 discovered sources reached complete capture with no
collection error. Two fresh texts, including one posted after activation, were
successfully read from production at revisions 6603 and 6604. Account and saved
permissions were preserved; no host gate was bypassed. This closes the observed
activation/catch-up gap on this Mac, not clean onboarding or sharing reliability.
[Exact evidence](../implementation/context-upload-activation-verification.json).

29 October [native catch-up update](BOUNDED-SYNC-CATCHUP.md): 0.4.33/runtime66 is published and installed, with 631 core tests, both-alias package checks, packaged stdio and exact 52-patch replay passing. The companion still runs runtime65 while its active-work guard defers activation; bounded retries are queued without forcing a restart. A second fresh marker was successfully read from production on runtime65. This does not close actual-host setup or sharing reliability gates.

29 October [cross-host context sync](CROSS-HOST-CONTEXT-SYNC.md): five explicit app choices, truthful sync status and source-read verification are live on server `20261029-cross-host-sync`. A fresh message from this chat was successfully read from the live Mac archive. 628 core tests, 27 browser checks, 23 extracted-bundle tests and exact 51-patch replay pass. Regular Claude/ChatGPT connections read the library; they do not automatically upload web-only chats. Actual-host onboarding and sharing reliability gates remain open. 159 deployed files and all three services are verified; a long-chat collection delay is addressed in the separate native catch-up update.

29 October sharing stress update: [the cross-person evaluation](SHARING-STRESS.md)
confirms the private retrieval → all-rule classifier → approved shared context
path, but does not pass overall readiness. It found three natural-question
retrieval misses, permitted facts withheld, and 30 provider 429s in a 40-call
ten-owner burst. Patch 50 fixes rejoin restoring an old opt-in at equal/backwards
timestamps, in source only. All 625 core tests, 27 browser tests and the exact
50-patch replay pass. Published and deployed artifacts remain unchanged.

The later [Sam and Zane scenario cut](FULL-VIDEO-RETAKE.md) follows the spec’s
owner-initiated flow with action-focused narration. It uses disclosed scenario
roles and preserves the same open acceptance gates.

29 October video update: the [Claude Desktop and Spaces walkthrough](FULL-VIDEO-RETAKE.md)
uses real moving footage, fresh cursor interaction, narrated chapters and an exact
P0 coverage table. The artifact is complete; unresolved product acceptance gates
remain open. It combines separately labeled retained and new recordings.

29 October: [bounded question discovery](QUESTION-DISCOVERY.md) is live on server
`20261029-question-discovery`; 611 core tests and exact 49-patch replay pass.
The full-sentence private question now finds four withheld candidates. A fresh
public request still withholds both candidates at the unchanged threshold. Native
0.4.32/runtime65 and the pending Claude setup approval are unchanged.


Later 28 October retake: server `20261028-bounded-classification` is live, with
610 core tests and the exact 48-patch replay passing. The fresh public query
completes with 26 audit entries (20 below threshold, six provider HTTP 429)
but shares no excerpt; useful sharing and provider reliability remain open. The private query completes with four candidates withheld.
Native 0.4.32/runtime65 is unchanged. New source-change/deadline observations
do not explain prior historical failures. The replacement full video is still
blocked by native setup approval; Chrome capture is now verified without
permission edits. New browser footage covers rules and private withholding.
[Current evidence](BOUNDED-CLASSIFICATION.md) · [recording status](FULL-VIDEO-RETAKE.md).

28 October live closeout update: server `20261028-sharing-diagnostics` is live
with native 0.4.32/runtime65 unchanged. The corrected public excerpt and a
completed private-withholding request pass with the owner's two selected accounts;
both see the approved history while checks remain owner-only. Browser owner
removal blocks signed requests/activity (404) and old-invitation acceptance (403).
The temporary space is paused, invitations revoked and archived. Three earlier
unavailable requests remain unexplained; clean-machine, independent-human and
broader default-host acceptance remain open. All 607 core tests pass.
[Evidence and limits](PRIVATE-NATIVE-TITLES.md).

An additional default-mode Claude Desktop run created a space, generated its
invitation, and archived it through native tools. The second selected account's
signed acceptance passed; request/old-invitation attempts after archival were
rejected. [Receipts](../implementation/p0-native-space-lifecycle-verification.json)
retain the distinction from recipient-host model acceptance.
[The new narrated footage](P0-LIVE-VIDEO-UPDATE.md) is a separate update to the
preserved original walkthrough.

28 October follow-up: [0.4.32/runtime65](P0-EXCERPTS-RELEASE.md) packages the
visible-only collector and exact-message excerpt fixes. The server is deployed,
runtime65 is active on the Mac, and a corrected four-turn native source read
passes. Both permanent registries are now 0.4.32. This earlier release
record predates the sharing fixes above; its first unavailable production
request during recapture is preserved.

28 October walkthrough finding: the real Perplexity classifier withheld a public
synthetic launch update under both example and explicit sharing rules, because
scores stayed below the unchanged 0.995 threshold. No context leaked, but useful
approved sharing did not pass this recording. The replacement annotated browser
demo verifies an explicit file upload and second-account read using isolated
sample identities, separately from the withheld private-library request. It does
not close all P0 gates. See [walkthrough evidence and coverage](P0-VIDEO-WALKTHROUGH.md).

27 October live update: 0.4.31/runtime64 is published, runtime64 is active on the
Mac, and server `20261027-context-guidance-r2` is live after a tested deployment
permission correction and verified rollback of the first attempt. Two distinct
native CLI synthesis checks pass with strict citation grounding. Claude/Codex
permanent installations are verified at 0.4.31, with two successful installed-package
source reads after deployment. [Installed receipts](../implementation/p0-installed-release-verification.json). [Live receipts](../implementation/p0-live-release-verification.json)
supersede the historical staging state below. Real-person sharing/revocation,
clean Google/Desktop setup and broader default-host acceptance remain open.

Original staging evidence: [0.4.31/runtime64](P0-READY-CANDIDATE.md) packages the
tested space-routing/source-read guidance, bounded diagnostics and recoverable
archive input errors. The full core suite passes 594/594. Both aliases and the
server update were verified GitHub drafts at that stage. Native aliases are now
published/installed and corrected server-r2 is live; broader P0 gates stay open. [Staging and remaining inputs](P0-LIVE-ACCEPTANCE.md).
[Exact evidence](../implementation/p0-ready-candidate-verification.json).

The [P0 closeout checklist](P0-CLOSEOUT.md) orders the remaining live work.
The transport diagnostic delta preserves a bounded failure category without
changing retries, authentication, public errors or permissions; 15 focused tests
pass. It is now packaged in **0.4.30/runtime63**, with both-alias integrity, extracted
launcher and actual stdio/signed-HTTP smoke checks. It remains unpublished,
uninstalled and undeployed; uploaded 0.4.29 assets are unchanged. See
[package verification](../implementation/cloud-closeout-runtime-verification.json).
The failed-read cause is still unknown. The authorized [cloud benchmark](CLOUD-P0-BENCHMARK.md)
is complete. Baseline routing/grounding failures remain recorded; source-only
patches 38–39 passed distinct 3/3 space and 8/8 retrieval model regressions. Every
candidate final citation had a successful same-session source read. These patches
are absent from local 0.4.30 packages and now live in 0.4.31/server-r2.

A packaged 0.4.29/runtime62 page-size guidance candidate addresses observed invalid
model arguments. Native and server assets are verified GitHub drafts; it is not live. See
[the candidate record](../implementation/read-page-guidance-verification.json).

Historical 26 October release: [current-source retrieval 0.4.28/runtime61](CURRENT-SOURCE-READS.md), published, installed and active. Server `20261026-current-read` is live; ordinary-prompt verification produced seven clean passes and one correctly surfaced synthetic-name conflict. The separate clean synthesis retest stopped after connection errors and an unapproved diagnostic-tool selection; acceptance gates remain. Earlier records below retain their own release dates.

## Current P0 acceptance

The owner's Spaces/context-sharing amendments supersede agent-centric screens
and hosted answering. **P0 is not fully accepted.** Passing service fixtures does
not close the live model or real-user coverage gaps below.

| Requirement | Verified evidence | Remaining acceptance |
| --- | --- | --- |
| Google → Claude/Codex Desktop → automatic private collection | Both real existing-owner Desktop handoffs completed at 0.4.24; exact host identities and installation receipts recorded. Both permanent registries are 0.4.32; runtime65 returns a verified four-turn source through each installed package. | A clean machine/new-account walkthrough has not been completed. Older open chats can require host reload. |
| Ordinary questions find current context and read supporting sources | 0.4.28: seven clean passes, one correctly surfaced synthetic-name conflict; every final citation matched a successful read. | The uniquely named synthesis replacement failed two reads, then stopped at an unapproved diagnostic selection. Its historical transport cause remains unconfirmed. Later 0.4.31 installed reads and distinct synthesis checks pass; broader default-host coverage remains open. |
| Invite → accept → connected, in natural language | Ordinary-prompt Claude Desktop creation/invitation and archival pass on the installed release; the selected second account previewed and accepted through the signed production API. Earlier disposable Conductor MCP acceptance also passed. | An earlier model acceptance case attempted a denied browser route. Recipient-host/default-host model acceptance, independent-human acceptance and clean onboarding remain open; API acceptance does not close them. |
| Messages first; both sides see exchanges | Deployed Spaces / My context UI, compact Messages / My sharing rules / Members header; browser and signed-service audit checks pass. Both fixture owners saw the same approved exchange. The two selected real accounts now see the same approved production excerpt; private checks remain owner-only. | Independent-human/default-host cross-person walkthrough remains unverified; the selected-two-account API/browser path is verified. |
| Private rules govern every context request | Parallel classifier checks, approved-only chunks, private rejection/check views, authority/source/expiry fences and pagination have passing regressions. Real classifier benchmark has zero false allows in its small synthetic sample. | The provider-refused private-data model case is not a classifier pass and is not being retried around the refusal. No claim of universal classifier accuracy. |
| Either side can revoke access | Service/browser leave, removal, expiry and old-invitation fences pass; model leave revoked stored membership. Production owner removal blocks the selected requester's requests/activity (404) and old invitation (403). Native Claude archival blocks signed requests and the old invitation (404). | Earlier model follow-ups chose unrelated tools, including baseline cross-space fallback. The distinct scope candidate passed 3/3. Post-revocation follow-ups through the recipient's default model host remain unverified; the new rejection checks used the signed API. |
| Host permissions remain authoritative | Saved settings stayed unchanged; host denials and test-tool guards stopped dependent work. | Exact additional test allowances were authorized; no saved/global permission changes. The owner later reopened Mac access. Current upgrades preserve saved permissions and respect the active-work guard. |
| Production matches reviewed artifacts | 159 readable files and all three services verified for `20261028-native-excerpts`; public health is ready. | Google reauthentication is complete. Both permanent registries are updated. Live sharing acceptance remains open. |

Supporting records: [current retrieval](CURRENT-SOURCE-READS.md),
[real Desktop setup](P0-NATIVE-READINESS.md),
[original natural-prompt failures](NATURAL-PROMPT-BENCHMARK.md), and
[candidate package verification](../implementation/read-page-guidance-verification.json).
The 0.4.29 draft does not close these gates. The unintended empty ChatGPT space
still requires owner cleanup. Direct Mail/iMessage sends remain deferred P1;
proposed details and the old selected-document sharing flow are not new P0 gates.

## Earlier release records

Previous server release: [demand-built archives](DEMAND-ARCHIVES.md), with native
0.4.27/runtime60. Production then was `20261026-demand-archives`.
All 159 deployed files match the release; 583 core regressions pass. All 31 public
assets, protocol checks and desktop/phone sign-in passed. These do not certify
model behavior or a fresh authenticated setup.

The completed live-index ordinary-prompt benchmark passed 4/8. Three Claude
answers cited a source found only in search without a successful supporting read;
one Codex case could not retrieve an answer after restarts/timeouts. Receipt checks
confirmed these gaps; correct facts alone do not satisfy grounding. The demand-built release passed five cases, hit one test allowlist guard and left
two unstarted. [Completed model evidence](../implementation/live-index-reuse-native-benchmark.json).

Default-host invitation routing, the host-denied acceptance case and production
retrieval latency remain open. Cleanup of the unintended empty ChatGPT space still
awaits its owner. Cross-person live acceptance is not certified by fixture users;
fresh-account/clean-machine coverage is separate from the verified existing-owner
Google/Desktop handoffs. Direct Mail/iMessage delivery stays deferred P1.
Earlier failures remain in their original records.

The following paragraph records the preceding 0.4.24 behavioral baseline.

Latest behavioral check: [ordinary-prompt benchmark and approved retest](NATURAL-PROMPT-BENCHMARK.md).
**Not yet consistently seamless:** the baseline Codex host answered four generic
context questions correctly, but only three read full sources and one cited them.
With the owner's exact per-run allowance, space creation/invitation, filtered
context retrieval and leaving completed. Acceptance chose a blocked browser
route; two questions missed the space-context tools; the provider rejected the
private-data case before execution. Claude's metadata call now succeeds, but
additional file-read approvals and a search timeout still prevented an answer.
The 58 passing service regressions are separate evidence, not completed model
flows. Neither benchmark changed deployment or saved permissions.

Previous release and acceptance evidence: [P0 native readiness](P0-NATIVE-READINESS.md)
and [machine-readable verification](../implementation/p0-native-readiness-verification.json).
**0.4.24/runtime57 is published and installed; production is
`20261026-native-p0-final`.** The prior Mac access block is resolved. Existing
accounts, permissions and scopes were preserved. All 495 core tests and final
package/identity checks passed. UI 129/129 and original lifecycle 15/15 remain
valid for the unchanged product flow.

The product remains Spaces / My context. P0 requires shareable invitation
links/codes; direct email/iMessage delivery is P1 and explicitly deferred.
Real Google consent and desktop app handoff acceptance must be recorded
separately from CLI retrieval and fixtures. Do not claim every journey is
complete from publication or cached identity alone. The real classifier
benchmark withheld seven of 32 synthetic cases, with zero false allows at the
unchanged 0.995 threshold.

Historical milestones below preserve their evidence and do not override the
current release record or the owner's context-sharing design amendments.

## Historical implementation milestones

Authoritative document: [Meet Proxy Product Spec](MEET-PROXY-PRODUCT-SPEC.md),
24 October 2026, Draft v3. This is an unchanged copy of the owner's latest
attachment, SHA-256 `1d061a660d1e280c4f33a111fdabb1c5fb8fc52a3aa4cd86ebe4fee5f396091d`.

Assessment: **not yet fully compliant or ready to certify end to end**. The
selected-agent service implements most core mechanics. Native attachment,
deployment of the new consent path and a real-model test using that path remain
release gates. P1 contact delivery and personal-agent support are incomplete.
Historical test reports describe earlier builds; this document records the
latest source changes and their limits.

## Required behavior

| Spec | Contract | Current evidence and remaining work |
| --- | --- | --- |
| 1–3, 6 | An accepted Chief of Staff answers for an unavailable owner | New persisted owner consent connects acceptance to an exact-agent answer mandate. Native signed API tests verify it. The new path still needs installed-plugin and independent real-model verification. |
| 7.1 | One “Continue with Google” entry, first use goes to attachment, returning users to Agents | Label corrected. First-use home now shows Claude Code and Codex attachment tiles directly. Returning home remains agent rows. Fixture browser flow tested; staging Google authentication was configured previously, not re-certified here. |
| 7.2 | Dedicated “Attach your agents”; Claude Code and Codex; any number including repeated types; finish on Agents | Source now uses the exact title, direct native setup, provider tiles and an explicit return to Agents. Ten-user/twenty-agent demo covers duplicate providers. Real installation/reload and staging attachment are still unverified. |
| 7.3 | All attached agents in scannable rows, visibly active connections, detail on tap | Existing service and browser tests cover owner-isolated rows, active count/indicator, offline state and detail. No dashboard/table replaces the Agents home. |
| 7.4 | Agent data, every active peer with owner/type/boundaries, thread link and sever | Implemented and tested from detail and thread. |
| 7.5 | Requester and owner natural-language invitation, shareable link/code fallback | Both directions use native pair tools. Updated tool instructions, workflow and bundled skills use this path. Earlier model samples used the former mandate harness; the revised model harness is prepared but has not been rerun with an independent model. |
| 7.5, P1 | Contact lookup and delivery by email/iMessage | No dedicated contact/delivery adapter. Skills may use an already permitted host tool on an explicit send request; otherwise return the link. No delivery should be claimed without evidence. |
| 7.6 | Named invite, choose attached agent, one primary Accept action establishes connection | Browser consent is included in Accept without a second approval step. Tests cover signed-out recovery, first attachment, existing-agent acceptance, forged selection and repeated acceptance. Link and code entry both work before sign-in and recover to the same one-action acceptance. Foreign-origin links are rejected without navigation. |
| 7.7, P1 | Editable-at-creation time/topic boundaries, defaults 14 days and no personal family/religion/finances | Stored per owner; both sets apply, earlier expiry wins. Model-facing mandate enforces disclosure instructions; server fences expiry/sever. Repeat invitations retain narrower topic/time restrictions. |
| 7.8 | Exactly one thread per connected agent pair; every new request continues there | Canonical sorted pair is unique. Repeat acceptance, opposite direction and reconnection retain it; another agent gets its own thread. Tested over signed API and browser. Legacy person/session-based histories remain a separate migration gap, not an exception hidden as compliance. |
| 7.8 | Both owners see both agents' full messages | Both browser views and signed native reads tested, including multi-page history and a large live burst. Other owners cannot read it. |
| 7.9 | Share answers, keep underlying sources private | Cross-owner context/history endpoints are denied. New mandate tells the selected agent to provide minimal answers without raw sources/identities/transcripts. Semantic nondisclosure depends on model behavior and needs new adversarial model evidence; transport tests alone are insufficient. |
| 7.10 | Either owner can sever from detail/thread, shown on both sides | Tested; new sends and pending dispatch stop, audit remains readable. An already submitted host turn cannot be recalled; it must re-read current authority before answering. |
| 8 | Partiful-style invite and iMessage-style lists; minimal home chrome | Named invite, one Accept action, simple agent/inbox rows. Added direct attachment tiles; core screens are covered by keyboard, mobile and accessibility checks. Visual inspiration does not imply pixel-identical styling. |
| 9, P0 | Agents cannot exceed their owner's tool permissions | Mandate permits only already authorized context/read tools and preserves native host approval. Requester content cannot authorize mutations or permission changes. Actual native permission prompts still require live host verification. |
| 9, P1 | Personal agents | Not implemented; the spec also describes this as stretch scope. Current P0 attachment choices remain Claude Code and Codex. |
| 4, 9, P2 | Per-agent list of friends/colleagues with access | Deferred as the spec requests. Peer owners shown in connection detail are part of 7.4, not a separate people-permissions product. |

## Proposed details and open questions

These remain distinct from committed requirements:

| Proposed detail | Disposition |
| --- | --- |
| No extra first-sign-in forms | Implemented. |
| Google profile avatar | Initials only; profile-photo support deferred. |
| Personal/other-agent “coming soon” tiles | Deferred; do not imply unsupported attachment works. |
| Attached tile state, finish after one, add more later | Implemented through tile counts, confirmation and Agents. |
| Agent type icons/avatars | Provider text is shown; dedicated type artwork deferred. |
| Active count, always-visible attach, one-tap Agents/Inbox | Implemented. |
| Delivery confirmation and ambiguous-contact choice | Instructions require honest confirmation and an unambiguous recipient; native contact adapter absent. |
| Invite shows boundaries, signed-out recipient recovers after attachment, success opens thread | Implemented and tested. |
| Edit boundaries later | Deferred; currently choose during invite/accept, or sever and establish a new consent. |
| Thread per agent pair rather than person; row agents/owners/preview/time; header boundaries/sever | Implemented. |
| Read history after expiry/sever; immediate revocation; sever confirmation | Implemented, with the documented limit on already submitted host work. |
| Requester never sees sources in thread | Implemented at the data-access boundary; model behavior still requires sampled validation. |
| Human owners typing directly into an agent-pair thread | Open question; current pair thread is read-only for humans. |
| Owner seeing their own agent's underlying sources in thread | Open question; sources are not included in the shared transcript. |

## Consent and compatibility

`authorizeAnswers=true` is an explicit choice made for the caller's own agent
when inviting or accepting. Browser create/accept explains the choice beside
the primary action. The inviter cannot authorize the recipient's agent.
Absent consent stays messaging-only, including existing stored connections.
Accepted-invitation retries do not change consent. A new invitation can record
a new explicit owner choice while preserving narrower active time/topic limits.

`read_agent_connection` verifies the bound participant and returns `canAnswer`
plus the current mandate. Another agent, including one owned by the same human,
cannot borrow it. Expiry, severing or an unavailable agent suppress the mandate.
The recipient re-reads it before each answer. The public audit contains shared
messages and boundaries; private source material is never attached to the grant.

No schema migration is needed: the consent flag is additive in the existing
per-owner policy JSON. Legacy delegation IDs, private briefings and narrower
mandates keep their original semantics. No existing account or conversation was
moved or expanded.

## Evidence and deployment

Verified on 25 October 2026: **370 backend tests, 53 UI tests, and 14 concrete
product scenarios (15 Node tests including the parent)** passed. Additional
focused runs overlap these counts. The three portable patches apply cleanly to
the original base and reproduce all 70 changed files byte for byte.

See `implementation/spec-alignment-verification.json` for exact run counts and
artifact state, and `.context/spec-alignment/` for test logs/screenshots. The
updated benchmark harness reads persisted invite/accept authority instead of
injecting a private mandate into its model prompt; its transport smoke passed.
That is not a completed model evaluation.

This alignment pass is **source-only**. Staging still has the earlier app-launch
overlay, and the user's installed plugin remains unchanged. New server code,
native tool/skill updates and UI consent must be packaged and verified together
before claiming the Chief of Staff journey works on staging or production.

Release gates, in order:

1. Package and install matching native/server changes in isolated staging; prove
   real Google account, exact agent identity and exact server origin.
2. Run requester invite → owner Accept → autonomous permitted answer while the
   owner is away → both-owner audit, using real host delivery and a real model.
3. Exercise disclosure attacks, expiry, either-side sever, offline recovery and
   denied host tools on that same installed path.
4. Resolve the legacy-thread migration gap
   before an “exactly follows the spec” claim.
5. Deliver or explicitly revise P1 local contact delivery and personal-agent scope.


## Product flow and visual design follow-up

The primary journey now uses the spec’s contact-list and invitation references:
Agents/Inbox navigation, dedicated provider tiles, distinct connected-agent rows,
a person-first invite with one large Accept action, and shared message bubbles.
Secondary social/cloud/context navigation is under More. Default boundaries are
editable without an extra required step. The selected agent and owner consent
remain explicit. See [the walkthrough and design report](PRODUCT-FLOW-DESIGN.md).

This fourth source patch is available in the labeled Conductor demo. It is not
packaged, installed, or deployed to real-account staging or production. The real
host/model and legacy migration gates above are unchanged. Final regression and
clean-patch-chain results are recorded in
`implementation/product-flow-design-verification.json`.

Final design verification: 370 backend tests, 55 UI tests, and all 14 product
scenarios passed. The four ordered patches reproduce 80 source files exactly.
Seven screens were checked at 320/390/1280px with no axe violations or horizontal
overflow. These are source/fixture results, not a new live readiness claim.

## Production preparation — 25 October, 0.4.19/runtime54

The fifth ordered source patch and prepared release artifacts supersede the
source-only packaging status above. The candidate is still **not published,
installed or deployed**. Conductor's `RunLocalCommand` lost its authorized Mac
binding, blocking the production backup/rehearsal, installation and live checks.
See [the rollout record](PRODUCTION-ROLLOUT.md) and
`implementation/production-readiness-verification.json` for exact evidence.

- Consent now rejects stale answer grants after both active-policy changes and
  expiry/reconnection. A fresh grant cannot revive expired queued deliveries.
- Proven exact-native legacy pairs are rejected as duplicates. Exact-address
  mailbox history is reused with its narrower active time preserved. Private
  legacy briefings and ambiguous histories remain separate; a universal legacy
  migration is still not implemented.
- MCP/OAuth/Agent Auth and API requests now use the new production wrapper.
  Local tests exercise the real wrapper with a compiled-site placeholder; the
  VM's actual compiled `/authorize` compatibility remains unverified.
- The required UI and latest synthetic lifecycle suites pass: 57 UI tests and
  15 lifecycle tests. The width matrix is now 320/390/768/1280px, with 28 core,
  8 native-setup and 16 recovery checks for accessibility, overflow and controls.
- The broad regression suite passes 379 tests. Native regressions pass 131 tests;
  extracted launchers, both alias packages and actual stdio/signed-HTTP smoke
  checks pass. These suites overlap and should not be added as independent cases.
- All 15 deployment-helper tests pass, including backup integrity, rollback,
  dependency isolation and preparing a candidate without activating it. The
  extracted server passes local OAuth/MCP/resource checks with isolated pinned
  dependencies on production's Node v22.23.2 and all 45 migrations.
- The five-patch chain reproduces 95 changed source files byte for byte.

The receiving host model can read its own account context through MCP resources
or the local mirror; hosted inference is not required for retrieval. Pair consent
does not expose peer source files. Explicitly published workspace documents retain
their existing member access. No disclosure or host-permission expansion was made.

The separate agent passed 11/11 synthetic behavior cases, including an allowed
answer, disclosure refusals, missing information, no acknowledgment loop and no
send after expiry. Sampling is recorded in the verification manifest. It does not
replace installed-host, real Google or production verification. P1 contact
delivery and personal-agent support retain the earlier scope and readiness gaps.


Production rollout update: the owner’s next message restored Mac access. A verified
production backup was migrated successfully and the actual compiled server passed
its isolated HTTP rehearsal using the real HTTPS configuration. Activation is
running as a durable VM job; see the rollout record for final serving state.


Live server update: production now serves `20261025-product-0.4.19`. All 45
migrations and fresh web/worker health checks passed. Existing profiles, devices,
agent bindings and thread mappings are preserved. Public phone/desktop pages
clear loading and open the real Google helper. This does not assert completion
of a human Google login or installed-host autonomous pair exchange.
# Later owner amendment: prompt-based sharing experiment

The 25 October request replaces mandatory source picking with natural-language
sharing rules and per-excerpt Perplexity Decisions checks. The source-only
[experiment](PROMPT-BASED-CONTEXT-SHARING.md) has real-model benchmark evidence,
but persistent grants and production routing remain incomplete. Existing product
readiness claims below do not imply this new sharing flow is live.


## Latest override: message-first context spaces (25 October 2026)

The owner requested one compact Messages / My sharing rules / Members header,
per-person parallel rule checks and seamless native setup. The source follow-up
now includes persisted opt-in rules, filtered context request APIs/MCP tools,
owner-only audit projection, real group invitations across sign-in and native
registration/collection verification. It remains unreleased. See
[MESSAGE-FIRST-SPACES.md](MESSAGE-FIRST-SPACES.md) and
[the portable verification](../implementation/message-first-spaces-verification.json).
Original hosted-agent requirements are not silently reinstated. Large-document
chunking, upstream MCP ingestion, real Google/native host verification and
production rollout remain separate gates; a local fixture is not their proof.

### Automatic setup refinement (source only, 25 October)

The owner removed the collection setting from onboarding. The app setup request
now authorizes automatic private collection; a one-time handoff carries the
browser identity to the exact native chat. The UI observes plugin/account
registration, installation-specific receipts and indexed context, with no manual
chat picker. Context availability remains separate from native delivery proof.
[Implementation, verification and release gates](LIVE-CONTEXT-SETUP.md).

The next refinement makes each app card launch the complete installation request
directly. Plugin and MCP setup are combined; the live UI has three steps with no
separate account-link row. Working installs are reused, app/account response
races are fenced, and manual copying is a recovery flow. The 15th portable patch
and `seamless-plugin-setup-verification.json` record the source/preview checks.
Host approval/reload and OS deep-link verification remain distinct live gates.

## Seamless-context follow-up (0.4.25 candidate)

The ordinary-prompt failures led to MCP-first source retrieval and space routing,
connector-generated IDs, bounded retry handling, prioritized changed-chat uploads,
and live authoritative search while the snapshot builds. Setup readiness now
requires actual visible canonical content from the selected installation. Existing
private audience, rule, expiry, host approval and legacy thread boundaries remain.
The [rollout record and walkthrough](SEAMLESS-CONTEXT.md) separate deterministic
checks from publication, installation and the fresh model benchmark. Passing
fixtures alone do not close the natural-prompt acceptance gap.

## Claude Desktop recording follow-up — 28 October

The [native demo record](CLAUDE-DESKTOP-DEMO.md) adds observed automatic collection,
a source-backed answer in another Desktop chat, real question/reply and follow-up,
private-finance refusal, and direct-link disconnection. It does not close useful
library sharing: the live public sample was withheld. Patch 43 fixes host-envelope
collection in source only, with privacy-preserving recapture migration. Native
installation and live classifier acceptance remain pending. The recordings were
recovered after the owner restored Mac access. The demo library policy is now
paused, its second member removed, and all demo capture processes stopped.
The native video edit preserves the public-sharing failure; media and playback
results are recorded separately from product acceptance.
