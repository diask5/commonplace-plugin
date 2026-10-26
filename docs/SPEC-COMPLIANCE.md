# Meet Proxy Draft v3 compliance

A packaged 0.4.29/runtime62 page-size guidance candidate addresses observed invalid
model arguments. Native and server assets are verified GitHub drafts; it is not live. See
[the candidate record](../implementation/read-page-guidance-verification.json).

Latest release: [current-source retrieval 0.4.28/runtime61](CURRENT-SOURCE-READS.md), published, installed and active. Server `20261026-current-read` is live; ordinary-prompt verification produced seven clean passes and one correctly surfaced synthetic-name conflict. The separate clean synthesis retest stopped after connection errors and an unapproved diagnostic-tool selection; acceptance gates remain. Earlier records below retain their own release dates.

## Current P0 acceptance

The owner's Spaces/context-sharing amendments supersede agent-centric screens
and hosted answering. **P0 is not fully accepted.** Passing service fixtures does
not close the live model or real-user coverage gaps below.

| Requirement | Verified evidence | Remaining acceptance |
| --- | --- | --- |
| Google → Claude/Codex Desktop → automatic private collection | Both real existing-owner Desktop handoffs completed at 0.4.24; exact host identities and installation receipts recorded. 0.4.28/runtime61 is installed and active. | A clean machine/new-account walkthrough has not been completed. Older open chats can require host reload. |
| Ordinary questions find current context and read supporting sources | 0.4.28: seven clean passes, one correctly surfaced synthetic-name conflict; every final citation matched a successful read. | The uniquely named synthesis replacement failed two reads, then stopped at an unapproved diagnostic selection. Its transport cause and clean answer remain open. |
| Invite → accept → connected, in natural language | Disposable real-service creation/invitation passed; signed API and browser membership tests pass. | The model acceptance case attempted a denied browser route. Explicit approval for the prepared MCP-only retest is pending. Default-host routing and new cross-person production acceptance are unverified. |
| Messages first; both sides see exchanges | Deployed Spaces / My context UI, compact Messages / My sharing rules / Members header; browser and signed-service audit checks pass. Both fixture owners saw the same approved exchange. | New cross-person production walkthrough remains unverified. |
| Private rules govern every context request | Parallel classifier checks, approved-only chunks, private rejection/check views, authority/source/expiry fences and pagination have passing regressions. Real classifier benchmark has zero false allows in its small synthetic sample. | The provider-refused private-data model case is not a classifier pass and is not being retried around the refusal. No claim of universal classifier accuracy. |
| Either side can revoke access | Service/browser leave, removal, expiry and old-invitation fences pass; model leave revoked stored membership. | The later model question chose unrelated tools; model-path post-removal verification is incomplete. |
| Host permissions remain authoritative | Saved settings stayed unchanged; host denials and test-tool guards stopped dependent work. | Additional Claude test tools and the MCP-only acceptance route await exact approval. |
| Production matches reviewed artifacts | 159 files and all three services verified for `20261026-current-read`; public asset/protocol and desktop/phone checks pass. | Further VM diagnostics/deployment wait for completion of the existing-account GCP browser reauthentication already started on the Mac. |

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
