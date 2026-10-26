# Current supporting sources — 26 October 2026

Candidate **0.4.28 / runtime61**, server `20261026-current-read`, is packaged.
Publication, installation and live behavior are tracked separately in
[the verification record](../implementation/current-read-verification.json).
Current production remains `20261026-demand-archives` until activation succeeds.

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
profile; their compiled authorization page is a stub. Package checks and live
results are recorded as they complete.

Earlier ordinary-prompt evidence remains intact: the live-index run passed 4/8,
with three Claude citation failures and one Codex retrieval failure. The subsequent
[demand-built run](../implementation/demand-archives-native-benchmark.json) passed
five cases, stopped Claude synthesis at the test allowlist, and left two Claude
cases unstarted. These were controlled per-process catalogs, not default-host
routing or new Desktop setup walkthroughs.

Still open: installed ordinary-prompt grounding and latency on this release;
default-host space routing and the previously host-denied acceptance case;
production cross-person acceptance without fixture users. Fresh-account and
clean-machine coverage remain distinct from the verified existing-owner handoffs.
The list-tool benchmark allowance and MCP-only acceptance retest await owner
approval. Direct Mail/iMessage remains deferred P1. No paid infrastructure or
saved-permission changes are included.
