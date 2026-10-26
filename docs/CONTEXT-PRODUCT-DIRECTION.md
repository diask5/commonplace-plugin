# Context product direction — 25 October 2026

The owner's current instruction supersedes the agent-centric home/onboarding in
Draft v3. Meet Proxy supplies explicitly authorized context through MCP or a
local context folder; the existing Claude/Codex application supplies inference.
A hosted agent, a model subscription, and an agent-pair connection are not
requirements for browsing or using the owner's context.

## Primary experience

- **Spaces:** the home for shared work. Connections and Shared access are merged.
  A space can contain one person, several people, or a project. A compact rail
  lists spaces separately from exact existing direct threads; names never merge
  histories or permissions. Create a space with any connected people, or start
  alone and add members later.
- **Messages:** the default space view: posts, context requests, approved
  exchanges, incoming/outgoing authors and paged history. Private rule results
  appear only in the contributing owner's view; they are filtered on the server.
- **My sharing rules:** each person's own private rules for this exact space.
  Add up to eight rules and explicitly enable requests. Every candidate checks all
  rules in parallel through Decisions. All must pass the fixed cutoff. Rules are
  stored on the server with revisions. Rejected text is never sent to the group.
- **Files:** review and explicitly upload UTF-8 text/Markdown files up to 16 KB.
  Browser routes use current group membership and the existing revisioned
  workspace document store. Reads are revision-pinned; retries use the same
  operation ID. Existing native workspace tools can read these same documents.
  This does not import or expose private account archives.
- **Messages:** a full channel-style board with history, timestamps, authors,
  live updates, pagination and recovery. Group posts use the real group API with
  idempotent retries. Legacy direct/pair messages retain exact transport scopes,
  consent/expiry and receipts. Groups do not fabricate host-delivery receipts.
- **Members:** see members, invite by a 14-day link, add connected people and remove members as
  the space owner. Membership controls shared files and messages. It does not
  grant another member's private library or native tool permissions.
- **Use in your assistant:** one dialog for Claude Desktop Code, Codex or
  Conductor. It includes the account/server, optional automatic context collection,
  app handoff plus copy fallback, observed chat selection and upload freshness.
  A space destination survives sign-in. Setup never claims a composer opening is
  a registered chat, a source upload or a live reply. Host approvals remain intact.
- **My context:** the owner's private, searchable library with source filters,
  document reading and collection controls. The older explicit-selection review
  remains a secondary flow; its invitation grants are still not implemented.
- **Account profile and Settings:** behind the avatar. Existing authenticated
  MCP setup, source controls, imports and historical chat controls are retained.

The root and `#conversations` open Spaces. Saved `#shared` links also open Spaces;
there is no separate Shared access navigation item. `/context` opens My context,
`/settings` opens Settings, and `/work-agent` preserves earlier flows and scopes.

## Design

The owner's latest instruction supersedes the earlier three-link design: exactly
**Spaces / My context** across the top, plus the account avatar. The space has a
narrow desktop rail; mobile uses a list and a focused space with a back control.
Warm cream, lavender, sage and terracotta carry through the prompt, illustrated
SVG, message board, file dialogs and member controls. Messages open first;
Messages / My sharing rules / Members share one compact header.
Motion is subtle and disabled for reduced-motion preferences. Contrast, overflow,
keyboard focus and touch targets are checked in Chrome across phone, tablet,
laptop and wide desktop widths.


## Sharing flow adapted from the spec

Group invitation links now implement **invite → sign in → join** without creating
a personal archive grant. See [the current implementation and evidence](MESSAGE-FIRST-SPACES.md).

The older document-selection target remains **invite → accept → connected** (§7.5–7.7, §8.1):

1. Choose a connection, press Share context, select documents, and create a link. Exact documents and a two-week
   expiry are visible; changing expiry is optional. No collection form.
2. Recipient opens a page led by the sharer's name and selected context, then
   presses Accept. A signed-in user does not repeat account or app setup.
3. Selected context becomes available to that recipient's existing apps over
   authenticated MCP. Connecting a new app is optional after acceptance.

Shared access should list people, selected context and access state in familiar
rows, with details and revoke one tap away (§7.8, §7.10, §8.2). Requesters should
also be able to request context from their existing app, but only the owner can
choose and authorize the documents. Natural-language initiation remains useful;
it does not require Meet Proxy to host an answering model.

The older selected-document picker, review sheet and acceptance preview remain
available as secondary UI. Their recipient-specific grant flow is still pending.
The newer space flow instead uses explicit owner rules, current group membership,
a request-time classifier and server-filtered exchange results. See
[MESSAGE-FIRST-SPACES.md](MESSAGE-FIRST-SPACES.md) for the implemented contract.

## Access model

Reading a source through MCP discloses that source to its recipient. The original
spec's answer-only privacy model and two-agent conversation audit do not describe
this direct-context model. An explicitly shared document set needs its own
server-enforced membership, expiry, revocation and access audit. Agent invitations
must never implicitly grant archive access. Nothing in this UI migration expands
any actual account's disclosure scope.

Existing owner-only archive search, revision-pinned reading, native sync and MCP
resources are reused. Selected-document peer grants are still backend work;
the secondary picker says so rather than claiming a share succeeded.

## Delivery state

This is a source implementation and interactive design preview. It is not yet
packaged or deployed. Production remains 0.4.19 with the previously deployed
Agents/Inbox interface. The preview runs the application and existing HTTP
handlers against disposable sample accounts and context. It cannot verify the
owner's real Google login or native app setup.

## Historical sixth-patch verification

Current verification is in [message-first spaces](MESSAGE-FIRST-SPACES.md). The
following counts describe the older sixth-patch UI, not the latest source.

The final focused sharing/context/profile/conversation suite passes **21/21**.
The full UI suite passes **78/78** on the same source, including authenticated
social API and route regressions. Axe and overflow checks cover Connections,
Context, Shared access, account profile, Settings, the sharing pane, document
picker, sharing/acceptance previews and app setup at 320, 390, 768 and 1440 pixels.

Sharing tests cover recipient binding, search-preserved selection, read recovery,
late-response isolation, account reset and disabled grant actions.
The board tests use real local service messages and verify exact-thread
deduplication, both sides of same-owner exchanges, live updates, 108-message
history with a burst gap, earlier-page ordering, read retry, mobile navigation
and clearing delayed responses on account switch. Entry-path checks cover signing
out and reopening the populated sample, recovering a persisted empty sample, and
using Connections while the archive is still loading. A monotonic sequence field
was exposed from the already authorized mailbox read for stable message order.
No browser agent-send API, native identity, consent or membership was added.

The sharing UI baseline reproduces 19 files through the sixth patch. Its counts,
log hashes and scope are in `implementation/context-product-ui-verification.json`.
The subsequent [automatic collection follow-up](AUTOMATIC-CONTEXT-COLLECTION.md)
is a seventh patch: direct Add context setup, collection status, automatic
library updates and project-grouped catalogs. Its separate verification record
covers the latest combined source.

The preview at https://kyle-cloud-w3.conductor.show/ requires the normal Conductor
viewer sign-in. Its application entry is explicitly labeled Open sample account
and opens the populated Alex Morgan sample. It does not authenticate with Google.
The preview-only /preview/sample route restores this sample after an empty sample
account was left in the browser. Real authentication behavior is unchanged. Screenshots are under `.context/context-product/sharing-first-screenshots/`.
No real account context, credentials or production data were used for this review.
# Latest amendment: prompt-based sharing

On 25 October 2026 the owner requested a Perplexity Decisions experiment: choose
a recipient and write sharing rules, then classify every candidate excerpt before
disclosure. This replaces manual source selection as the intended primary flow.
The older picker described below remains available during evaluation. See
[implementation and limits](PROMPT-BASED-CONTEXT-SHARING.md). The experiment uses
synthetic context and does not activate peer access to any real archive.


## Latest Spaces delivery

The follow-up is preserved in `implementation/shared-spaces.patch` after the
11-patch sharing-interactions chain. The local sample preview uses the actual
group, message, membership and revisioned document APIs with disposable accounts;
no real Google identity or private archive is used. The preview runs the new UI,
while production packages/deployment remain unchanged. Verification and exact
source digests are in `implementation/shared-spaces-verification.json` and its
manifest. The standalone rule preview retains the Perplexity experiment and
its explicit synthetic-data boundary.
