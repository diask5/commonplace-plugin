# Context MVP readiness — 26 October 2026

31 October multiple-account candidate: patch 58 adds isolated native account
profiles and a selected account per actual native chat. Context and messaging pin
that choice; existing threads remain on their original account. Capture in an
explicitly selected profile starts paused and requires the owner choosing to sync
that whole chat. Canonical uploads and pending retries enforce the account fence;
secondary profiles never bulk-upload unassigned histories. Host permissions and
browser account scopes are unchanged. Native 0.4.34/runtime67 packaging is in
progress; it is not installed or active on the Mac. The previous Mac execution
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
53 improves allowed-context admission and bounds provider calls across owners.
The real ten-owner candidate burst shared all 10 public requests with no provider
errors or private disclosure. Some permitted examples still fail classification.
All 640 core tests and exact 53-patch replay pass; the candidate is packaged but
not live because Google Cloud requires reauthentication. Existing production
sharing reliability is not relabeled as fixed by candidate results.

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

29 October [sharing stress evaluation](SHARING-STRESS.md): useful automatic
sharing still fails acceptance. Three answerable question phrasings missed their
source, permitted facts were withheld, and a ten-owner burst hit 30 provider 429s
in 40 calls. A consent-resurrection edge case is fixed in source-only patch 50,
with 625 core tests, 27 browser tests and exact 50-patch replay passing. The live
server and native packages have not changed; the fix is not deployed.

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


Latest release: [current-source retrieval 0.4.28/runtime61](CURRENT-SOURCE-READS.md), published, installed and active. Server `20261026-current-read` is live; ordinary-prompt verification produced seven clean passes and one correctly surfaced synthetic-name conflict. The separate clean synthesis retest stopped after connection errors and an unapproved diagnostic-tool selection; acceptance gates remain. Earlier records below retain their own release dates.

This audit compares the attached 24 October Draft v3 with the owner's later
instructions: context-first Spaces, prompt rules, messages first, group sharing,
automatic private ingestion, and one-request native plugin/MCP setup. Those later
instructions supersede the original Agents home and hosted proxy-answer design.
The original spec remains unchanged in MEET-PROXY-PRODUCT-SPEC.md.

Current release: [0.4.27/runtime60 registration recovery](REGISTRATION-RECOVERY.md).
The native package is installed and active; server `20261026-demand-archives`
is live. Historical Google/Desktop acceptance is in [P0 readiness](P0-NATIVE-READINESS.md). The counts, missing features and 0.4.20 rollout below describe the
earlier MVP milestone and are retained as history. Real Google sign-in and both Desktop handoffs are verified; the P0 record
separates those receipts from clean-install fixtures and continuing collection.

## Readiness decision

The original MVP milestone implemented the core context-sharing journey and
preserved legacy agent-pair conversations. Version 0.4.20 / runtime 55 was
published and deployed; later releases supersede it. [Rollout details](CONTEXT-MVP-ROLLOUT.md) and installed-host verification are tracked in
`implementation/context-mvp-verification.json`; do not infer them from screenshots.

A complete original-spec claim would be inaccurate: answer-only privacy was
intentionally replaced by owner-authorized context excerpts, and the P1 personal
agent and automatic contact-delivery features remain outside this MVP.

## Requirement-by-requirement assessment

| Spec goal | Current implementation | Evidence / limitation |
| --- | --- | --- |
| 7.1: single Google sign-in | Existing real Google entry and account session; private setup handoff carries sign-in into the native plugin | Browser tests use isolated identities. A fresh real-account walkthrough still needs human Google/host interaction. |
| 7.2: Claude Code and Codex attachment | Direct app links, prominent Copy setup prompt, plugin/MCP installation request, exact chat handoff and automatic collection | Signed API, actual packaged stdio and collector tests; OS launch and host reload are separate live checks. Conductor is an additional supported surface. |
| 7.3–7.4: list and detail | Superseded by Spaces / My context and Messages / My sharing rules / Members; legacy Agents/Inbox retained at /work-agent#agents | Responsive browser journeys and screenshots. No return to an agent-centric home. |
| 7.5: either side initiates in natural language | New create_context_space / create_space_invitation tools return a real URL. Either person can start the space and invite the other. Legacy request/delegate tools remain | Signed remote MCP + native account routes and ownership/scope tests. Direct email/iMessage delivery is P1 and not implemented. |
| 7.6: invite, accept, connected | Inviter-led landing page; one Join action for an authenticated person; destination preserved across sign-in | Two-user browser journey and membership assertions. Joining never silently enables personal-context sharing. |
| 7.7: time and topic | Independent owner rules per space; two-week default and 1/7/14/30-day windows; expired rules withhold before classification | Expiry and expiry-during-evaluation tests. Default prompt keeps family, religion and finances private. Saving renews the displayed window. |
| 7.8: full audit and monothread | Both owners see both sides of legacy pair threads; exact-pair uniqueness preserved. New groups share one board per space and show context exchanges | Ten-account/twenty-agent legacy lifecycle; new sender/recipient browser journey. Multiple project spaces are intentional, not duplicate legacy pair threads. |
| 7.9: private context | Approved excerpts are shared under the later context-only instruction. Raw source IDs, rejected excerpts and checks remain private to the contributor | Membership/revision/rule rechecks and adversarial/provider-error tests. This is not the original agent-written, answer-only model. |
| 7.10: either side can stop access | Members can Leave; owners can Remove or Archive; contributors can pause sharing. Legacy pairs retain either-side Sever and readable audit | Browser and signed API tests, stale-invite refusal and in-flight membership fencing. Leaving a group removes its access; retained group history is not deleted. |
| 8: minimal, friendly design | Cream/lavender/sage/terracotta, minimal top navigation, compact space header, invitation card and subtle SVG setup progress | Phone/tablet/desktop axe, keyboard, touch-target and overflow checks; reduced motion respected. |

## Gaps closed in this audit

- Added six context-space management tools across remote MCP and native accounts:
  create space, create invitation, preview, accept, leave and archive. They keep
  read/write scopes, same-origin invitations, explicit owner intent and workspace
  isolation. No contacts are messaged automatically.
- Added persisted per-owner sharing windows, two-week defaults, expiry state and
  renewal. Existing policies without a window use 14 days after their last save.
  Added only the `cp_space_policy_limits` table; no existing migration was edited.
- Exposed Leave / Archive directly in Members, with a short confirmation.
- Restored legacy invitation/navigation paths under /work-agent so reloads retain
  the intended legacy view. The original spec harness now explicitly enters that
  preserved surface instead of expecting it at the new Spaces home.
- Added a complete new-context browser journey and screenshots, retaining the
  original lifecycle and privacy tests separately.

## Classifier evidence and remaining limits

A fresh real `pplx-decider-v1.2` run evaluated 28 synthetic cases. At the unchanged
0.995 threshold: **23 correct, zero false allows, five false withholds**, no API
errors. Median provider latency was 159 ms, p95 576 ms in this small run.
These scores are not calibrated probabilities or production privacy guarantees.
No real account's private source text was submitted for this benchmark.
The production VM also reached the provider using its configured key; a two-case
probe withheld both a permitted example (score 0.9601) and a disallowed one.
This reinforces the false-withholding limit rather than proving perfect answers.

The gate currently considers up to six complete matching documents and withholds
documents longer than 8,000 characters. Safe long-document chunking and broader
recipient-safe pagination remain unimplemented. Supported visible native history
syncs automatically after setup; arbitrary repositories, web-only chats,
attachments and upstream MCP gateways are not automatically ingested.

Optional selected-document invitation drafts remain a historical secondary flow;
recipient-specific document grants are not implemented. Explicit shared text and
Markdown uploads work. P1 automatic email/iMessage contact delivery and personal
agent support remain pending. No hosted answering model is required for context
retrieval; rule classification uses the configured Perplexity API.

## Screenshots and reproducibility

[Open every current flow](https://kyle-cloud-w3.conductor.show/review) — 14 flows,
each with desktop and phone captures. These are the actual UI and HTTP handlers
with isolated test identities and controlled provider/native fixtures, not proof
of real Google sign-in or a native OS launch. The interactive preview remains
available alongside the images. Raw captures and logs are under
`.context/spec-readiness/`.

`implementation/context-mvp-completion.patch` is the 17th portable source patch,
after copy-setup-prompt.patch. Its manifest records every input/output digest;
the verification file records current test counts, artifact hashes and live state.
