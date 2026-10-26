# Current supporting sources — 26 October 2026

**0.4.28 / runtime61** is published; server `20261026-current-read` is live.
Publication, installation and live behavior are tracked separately in
[the verification record](../implementation/current-read-verification.json).
All 159 production files match the release and all three services are active.
The code-only activation changed four files with no schema changes. Mac 0.4.28/runtime61 is installed and active with the account and saved permissions
unchanged. Ordinary-prompt behavior checks are recorded below. The normal restart lost a
race to a cached 0.4.15 launcher; the controlled handoff briefly held eight exact
old plugin processes, gracefully stopped the companion, activated runtime61 and
resumed all still-existing processes. Host apps stayed open; both attempts remain
recorded. Existing open chats still need host reload to refresh their own tools.

The native guidance now requires a successful supporting read for every cited
document. A new source read omits the search revision to fetch the latest authorized
text; later pages pin the revision returned by that read. Changed reads discard
partial text and restart the document, while changed search pages restart the
search. A repeated change stops with an explicit unverified result. Search snippets
and failed reads do not qualify as cited evidence. Existing peer disclosure rules
and host permissions remain unchanged.

The server may retry a changed first-page search once, only for an unpinned request
whose first attempt took less than six seconds. Each attempt uses the unchanged
global revision and expiry checks. This admission estimate is not a twelve-second
wall-clock bound. Explicit search pins, continuation pages and reads are not
retried by this helper. Errors and permission denials are not retried. Continuous
collection can still cause withholding and queue pressure can still return busy.

The 34 ordered portable patches reproduce all 203 implementation files exactly;
this patch changes 12 files. Core regressions passed 589/589, focused retrieval and
routing passed 24/24, and setup browser checks passed 13/13. Extracted HTTP tests
exercise real OAuth/PKCE, resources and permission enforcement with a synthetic
profile; their compiled authorization page is a stub. Both-alias package checks, 32 extracted launcher/ingestion/contact tests and
packaged plugin/mailbox smoke passed. The six-profile smoke uses simulated Google
identity and host transports. Live public checks verified all 31 assets, compiled
authorization routing and sign-in at 1440px/390px without JavaScript errors or
overflow; screenshots are in `implementation/current-read/`. This single sample
loaded the pages in 5.84s/5.63s; it is not a general latency guarantee.

Earlier ordinary-prompt evidence remains intact: the live-index run passed 4/8,
with three Claude citation failures and one Codex retrieval failure. The subsequent
[demand-built run](../implementation/demand-archives-native-benchmark.json) passed
five cases, stopped Claude synthesis at the test allowlist, and left two Claude
cases unstarted. These were controlled per-process catalogs, not default-host
routing or new Desktop setup walkthroughs.

## Installed ordinary-prompt result

The eight-case run completed. The automatic rubric passed all eight; manual review
qualifies that as **seven clean passes and one correctly reported source conflict**.
An older synthetic project shared the name of the Claude synthesis case. Claude
read all four sources and reported the contradictory versions rather than choosing
one silently. The original result remains intact. Every final citation across the
run matched the citation array of a successful source read; the audit excludes
snippets, failed responses and changed pages. Case times were 46–103 seconds.
Two freshly seeded notes became searchable and readable in a 29.83-second
readiness observation after the seed chats completed.

The separately named synthesis retest is not a pass: search returned two results,
but both reads returned “Commonplace Agent Auth failed (connection unavailable).”
Claude then selected `setup_status`, outside the three-tool benchmark allowance,
and the harness stopped it. No host denial or saved-permission change occurred.
The [run](../implementation/current-read-native-benchmark.json),
[strict receipt audit](../implementation/current-read-receipt-audit.json) and
[separate retest](../implementation/current-read-synthesis-retest.json) preserve
these distinctions. The initial run also recovered three oversized-page validation
errors and had three changed replies. This is improved grounding, not a claim that
every request is frictionless.

A later independent request through the existing companion returned search in
4.57 seconds and source text in 1.80 seconds, both HTTP 200; public health was
ready. It does not retroactively pass the failed model case. Production SSH
inspection hit expired Google Cloud reauthentication; login for the same existing
account has been opened on the Mac.

Remaining gates: the clean synthesis case and connection-error diagnosis;
default-host space routing and the previously host-denied acceptance case.
The additional read-only Claude diagnostics allowance and the prepared MCP-only
acceptance retest await explicit owner approval. Real cross-person production
acceptance remains unverified; no external invitation has been sent. Fresh-account
and clean-machine coverage stay distinct from the verified existing-owner
handoffs. Direct Mail/iMessage remains deferred P1. No paid infrastructure or saved
host-permission changes are included.

## Prepared page-size follow-up

Candidate **0.4.29/runtime62** is packaged and verified, but is not published,
installed or deployed. It addresses the three recovered oversized-page requests
by making the normal 12,000-character page and strict 16,000-character maximum
explicit in native and remote tool descriptions and the context skill. Larger
documents still use `nextOffset`; no bound, authority check or paging semantics
changed. Catalog comparison confirms only descriptions differ from the existing
validation schema. Whether these hints reduce model mistakes still needs a live
model test.

Patch 35 replays all 203 implementation files exactly. Nine focused MCP/routing
checks, 13 setup UI checks, both-alias package integrity, two packaged launcher
checks, actual packaged plugin smoke and extracted OAuth/resource checks pass.
See [candidate verification](../implementation/read-page-guidance-verification.json).
Production and the installed Mac remain last verified at 0.4.28/runtime61. Two
subsequent attempts to observe the existing GCP login timed out waiting for the
Mac client; its completion is unknown, and no replacement login was started.
