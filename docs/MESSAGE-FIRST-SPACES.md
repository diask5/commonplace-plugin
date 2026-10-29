# Message-first context spaces — 25 October 2026

This implements the owner's latest flow: Messages first; My sharing rules and
Members in the same compact header. Spaces / My context remain the only top-level
links. The change is source plus an interactive preview, **not a production
deployment or a new plugin release**. Published 0.4.19 packages are unchanged.

The later [automatic setup follow-up](LIVE-CONTEXT-SETUP.md) supersedes the
optional collection choice and manual chat selection described below.

## Working flow

1. Sign in, connect an existing assistant, and choose whether to automatically
   collect supported visible work chats into the private account library.
2. Create a space. In Members, invite by link or add an existing connection.
   Invitations survive sign-in, show the account joining, expire after 14 days,
   and open the intended space. The owner can turn off outstanding links.
3. Each member saves their own rules and explicitly enables requests. Membership
   alone does not enable personal-library sharing. Each space has independent
   owner policies; edits use revision checks to prevent overwriting another tab.
4. Messages contains ordinary posts and context requests. The requester chooses
   a contributor. Matching context is privately checked with Perplexity Decisions;
   every rule must pass. Approved excerpts and the query enter shared history.
5. The contributor sees rule-by-rule results and mechanical reasons, including
   below-cutoff scores, provider failures, and interrupted requests. Other members
   never receive the private audit or rejected excerpts. Decisions does not return
   a prose rationale, so the interface does not invent one.
6. The assistant setup dialog offers Claude Desktop Code, Codex and Conductor,
   an app link and copy fallback, the exact account/server/space, observed chat
   selection, collection freshness and receiver selection. A newly opened composer
   is never treated as a connected chat or a successful reply.

Uploaded text/Markdown files remain explicit whole-file contributions outside the
personal-library gate. Previously shared messages/excerpts remain space history
when requests are paused. The enable control discloses that current and future
members can read approved history. Removed members cannot use an old invitation
link to undo their removal. Existing direct threads keep their original scopes.

## Request boundary

`SpaceContext` is shared by authenticated browser routes, remote MCP and the native
account routes. New tools: `list_context_spaces`, `request_space_context`, and
`read_space_activity`. The authenticated account supplies the requester; incoming
arguments cannot nominate an owner identity or access somebody's raw archive.
The native tool definitions are included in source, not the published ZIP.

Rules are 1–8 required checks, at most 4,000 characters total. Each receives the
complete policy and a focused rule, so an allowance cannot override another
rule's restriction. Rule calls run in parallel; candidates are processed in
sequence. All scores must meet 0.995. This is a cutoff, not a measured privacy
success rate. Errors, ambiguity and invalid provider responses withhold.

Source collection remains private. Candidate reads are revision-pinned and use
complete matching documents, never an isolated snippet stripped of confidentiality
context. The current gate examines at most six matches from the first search page,
and withholds documents larger than 8,000 characters. It is not exhaustive. Safe
chunking with inherited restrictions and recipient-safe pagination remain work.
The classification phase has a 20-second total deadline and one in-flight request
per contributor. There is no streaming of partially checked results.

Rules, membership and archive revision are rechecked after evaluation and inside
the transaction that records the exchange. A change discards the response. New
requests always reclassify; an identical nonce retry reads only its already shared
historical exchange. Shared responses never contain raw source IDs, rejected
match counts, private titles, rules or provider errors. Owner audit rows are
separate and selected by the authenticated contributing owner.

Four SQLite tables are created on first use: `cp_space_policies`,
`cp_space_exchanges`, `cp_space_checks`, `cp_space_invites`. Invitation tokens are
stored hashed. Existing source schemas and conversation histories are not merged.
Production configuration reads `PERPLEXITY_API_KEY` from the process environment;
only isolated preview scripts load the existing ignored local key file. No key is
returned to a browser or included in the portable patch.

## Verification and limitations

- Core suite: **419/419 passed**, no skips, including signed remote MCP/native
  API calls, authority races, provider errors and existing account behavior.
- Context UI: **51 checks passed across the final runs**. The full run identified
  a new invite-note contrast issue; the affected 17-check Spaces suite was rerun
  after fixing it. The other 34 checks passed on that run. Coverage includes
  320/390/768/1024/1440/1920 layouts, keyboard tabs, axe, member changes, actual
  fixture registration, uploads, owner switching, invitation login and recovery.
- Policy regression: **45/45 passed**, covering Decisions response validation,
  cancellation, private versus recipient projections and the existing rule tester.
- Full portable replay: **13 patches, 139 changed files match**. This increment
  changes 26 files. Source hashes and evidence are in
  `implementation/message-first-spaces-manifest.json` and its verification JSON.

The real `pplx-decider-v1.2` API was exercised through a browser request using only
synthetic public-release and private-finance documents, with two parallel rules.
The first policy withheld both: the public scores were 0.99434 and 0.99324, just
below cutoff. After explicitly naming current and future members in the allowance,
the public scores were 0.99594 and 0.99543 and it was shared; the private scores
were 0.00112 and 0.00091 and it was withheld. No cutoff was lowered. These two
small probes are **not classifier calibration or a privacy guarantee**; useful
context can still be conservatively withheld. The real runs took about 1.5s and
1.1s respectively, not a general latency benchmark.

Preview: https://kyle-cloud-w3.conductor.show/preview/sample?view=conversations
uses isolated sample identities and the actual UI/HTTP handlers. Google sign-in
in browser tests is simulated. A real Google-to-fresh-Claude/Codex/Conductor
walkthrough and native wake/reply tests are still required after deployment.
App URL schemes are retained as best-effort launch affordances with copy fallback;
no operating-system app launch was verified here. Official documentation fetches
for Codex/Conductor returned HTTP errors in this environment. Upstream MCP source
ingestion and selected-document recipient invitations remain unimplemented.

Local evidence is under `.context/message-first/`: core/UI/policy logs, signed
request tests, both real-provider probes, replay record and desktop/mobile images.
No production account, installation, permission setting or archive was changed.
