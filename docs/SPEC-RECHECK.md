# Draft v3 recheck — 26 October 2026

The latest attachment is byte-identical to [the preserved spec](MEET-PROXY-PRODUCT-SPEC.md):
SHA-256 `1d061a660d1e280c4f33a111fdabb1c5fb8fc52a3aa4cd86ebe4fee5f396091d`.
This audit uses the owner's later instructions as amendments, not as missing
features to undo. The original spec remains unchanged.

The later [completion update](CONTEXT-COMPLETION.md) is live. Current 0.4.24
publication, installation, production and native-host evidence are in
[P0 live readiness](P0-NATIVE-READINESS.md). The 0.4.22 state below is historical.

## Decision

Do not label the entire spec or every real-user journey complete. The core
context-sharing implementation is present, but installed-host coverage and
latency still have limits. The original P1 contact-delivery/personal-agent scope
is also incomplete. Tests with fixture identities are not real Google or host
acceptance tests.

The current product is **Spaces / My context**, with **Messages / My sharing
rules / Members** inside a space. Existing assistants retrieve context through
MCP or a local folder; no hosted answering model is required. Owners explicitly
enable sharing rules, and each new context request invokes the configured
classifier. This intentionally replaces the original private proxy's
answer-only response with approved context excerpts.

## Current release and real-account result

**Published and installed:** [0.4.22 / runtime56](https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-v0.4.22)
on the owner's Mac. The supported plugin manager retained the existing account,
installation and single enabled alias. Fresh Claude CLI processes use the new
plugin; already-open hosts may still need the manager's normal restart/reload.
Saved host permissions were unchanged.

**Live production:** `20261026-revision-fence` at https://34.27.253.220/.
All 153 deployed runtime files match the reviewed bundle, and the web, runtime
and nginx services are active. This code-only deployment changed no migrations
or account data. Desktop and phone public pages clear loading; Google helper,
public module hashes, unauthenticated MCP rejection and the compiled `/authorize`
redirect passed. This does not certify a fresh Google consent journey.

**Real Claude retrieval passed after retry, with a reliability gap:** the first
0.4.22 attempt searched successfully but its read timed out; returning the marker
from search did not count as a read pass. After the server fix, an obsolete read
returned a revision restart promptly, but its next read still timed out. Once
the archive reported its current revision published, the same approved test
session resumed and successfully read the latest first page, returned citations
and the exact complete marker. Its final answer matched that actual read receipt.
The resumed turn took 35.32 seconds and exited normally. No permission denials or
saved permission changes occurred. Search and successful read happened in two
turns of the same session; this is not a clean single-attempt pass.

Native MCP connected in 271 ms in the post-fix test without the former resource
discovery timeout. Large-account context-read latency during ingestion remains
an unresolved reliability issue. Previously observed collection delay was up to
310 seconds between periodic checks, not an instantaneous-sync guarantee.

## Every P0 requirement

| Original requirement | Implemented behavior | Verification and remaining boundary |
| --- | --- | --- |
| Google sign-in | One Continue with Google entry; browser identity carried into the native setup handoff | Real production entry/helper and existing signed-in Mac account checked. Fresh-user Google consent is exercised with fixture identity in automation. |
| Attach Claude Code and Codex | App launch/setup request, bundled runtime, exact native binding, collection receipts | Signed handoff rejects another account, wrong provider, unverified chat, expired/replayed code and receiver changes. Real Claude retrieval passed. Real Codex Desktop installation/launch remains unverified on the tested Mac. |
| Agents list with active connections | Retained on the legacy surface; current home uses Spaces per the owner's amendment | Responsive browser coverage checks both surfaces. An Agents-first home would contradict the current instructions. |
| Either side initiates a natural-language invite | Native create/invite/preview/accept space tools; requester/delegate pair tools retained | Signed MCP tests check current caller, ownership and workspace scope. Shareable URL fallback implemented. Automatic email/iMessage delivery is P1. |
| Named landing page and one-click accept | Inviter-led invitation; a single Join/Accept action for a ready signed-in recipient | Browser tests cover sign-in recovery, first attachment, repeated acceptance and stale invitation rejection. Joining never enables personal-library sharing. |
| Exactly one thread per agent pair | Canonical sorted pair uniqueness; repeat/opposite-direction acceptance reuses its thread | Signed API and ten-owner/twenty-agent lifecycle. Proven narrower legacy pairs are refused or reused without copying private briefings. Group project spaces intentionally have their own boards. |
| Both owners see both sides | Full shared pair history and group exchange board | Both-owner reads, pagination, large bursts and account-switch races tested. Private classifier audits are contributor-only; shared requests and approved excerpts are visible to members. |
| Underlying sources stay private | Legacy answer-only mandates retained; new context flow releases only approved excerpts | Raw archive remains owner-only. Excluded/foreign sources, malformed provider results, expiry and in-flight rule/source/membership changes withhold. Classifier semantics are not a mathematical privacy guarantee. |
| Cannot exceed owner's tool access | Native host approvals still apply; peer messages cannot grant permissions | Real Claude denial observed. Later exact two-tool per-run grant allowed the test; saved permission settings were unchanged. Resource discovery grants no new read access. |
| Either side severs access | Either legacy peer can Sever; group members Leave, owners Remove/Archive, contributors Pause | Pending dispatch and new reads/sends are fenced; stale links cannot restore removed membership. Already delivered content cannot be recalled. |

## Remaining spec sections

| Section | Disposition |
| --- | --- |
| 3: setup in minutes | Supported setup flow is implemented. Large-account collection and intermittent read delays prevent a blanket latency claim. |
| 7.2: repeated agents/provider types | Signed fixture lifecycle attaches twenty agents for ten owners, including repeated types. |
| 7.4: detail view | Existing legacy agent details show connections and boundaries. Current spaces expose the equivalent member/rule controls. |
| 7.7: time and topic (P1) | Implemented: two-week default, 1/7/14/30-day options, editable owner rules, expiry and renewal. Family/religion/finances remain private in default rules. |
| 8: Partiful/iMessage design | Inviter-first acceptance, simple lists, minimal navigation and compact message board. The owner later requested the Slack-style board. Responsive/accessibility tests are automated; aesthetic resemblance is not a binary test result. |
| P1: contact delivery | Dedicated automatic local-contact/email/iMessage adapter is not implemented; the shareable-link fallback is. |
| P1: personal agents | Not implemented as a new attachment type. Existing Claude Code/Codex remain the supported baseline. |
| P2: per-agent people permissions | Deferred as the spec requests. |
| Proposed details/open questions | Retain their proposed status. Google profile photos/type artwork are not completion gates. Legacy human typing/source display remain open; human group messages are a later explicit request. |

The later context product also still lacks upstream MCP ingestion, safe sharing
of long documents and recipient-safe pagination across larger candidate sets.
The gate currently checks up to six matching whole documents and withholds those
over 8,000 characters. These are real limits, not claimed completion.

## Repair found in this recheck

Native MCP `resources/list` fetched the account profile and archive while Claude
was starting the plugin. On the real Mac this hit a 30-second host timeout and
left tools displayed as connecting. The released plugin now advertises the static
context index and document template locally. Explicit index/document reads keep
the existing account, scope, revision and exclusion checks. Remote and pinned
archive catalogs retain their existing document enumeration.

A regression failed before the fix. Tests now exercise actual modern and legacy
stdio discovery through stdin closure, with no account bootstrap, companion,
receiver or files created. No host permission, identity or account settings are
changed by this repair.

A second regression showed that an outdated page waited for archive rebuilding
before returning its revision mismatch. The server now returns the current
revision immediately, before opening a snapshot; it retains the second revision
check after snapshot preparation for concurrent changes. This is a server-only
follow-up, with no schema change or native ZIP replacement.

## Evidence

On the final source: **433/433 core**, **127/127 browser**, **15/15 original
lifecycle**, and **20/20 focused MCP** tests passed. The packaged empty-account
knowledge journey, both-alias integrity, two launcher tests, actual packaged
stdio and six-profile mailbox smoke passed. These suites overlap and must not
be added as distinct product scenarios. All 22 portable patches reproduce 154
source files exactly.

Current machine-readable results and release state are recorded in
[`spec-recheck-verification.json`](../implementation/spec-recheck-verification.json).
Logs and current screenshots are under `.context/spec-recheck/`. The earlier real
archive/read result and its limitations remain in
[Zero-to-knowledge verification](ZERO-TO-KNOWLEDGE.md).
