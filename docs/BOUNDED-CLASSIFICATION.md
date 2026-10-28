# Bounded classification — 28 October 2026

The fresh Juniper Lantern walkthrough exposed two distinct stopped requests. One
owner-only audit observed a source revision change during classification; another
observed the 20-second deadline with unchanged source and authority. These are new
observations, not explanations for earlier historical failures. A preceding long
query selected only the summary conversation and all 13 candidates were withheld.
All three attempts remain preserved.

Patch 48 evaluates source candidates in bounded batches. The number of concurrent
candidates is `floor(8 / ruleCount)`, retaining the existing maximum of eight
provider calls in flight per request. Every rule still sees the complete policy
and original private context. The candidate limit, threshold, provider model,
prompt, timeout and consent/source/expiry checks remain unchanged. A failed fence
cancels the outstanding batch; there is no streaming or partial disclosure.
Excerpts and owner-only audits retain source order regardless of completion order.

All 610 core tests pass. Dedicated tests cover the combined concurrency ceiling
for one, three and eight rules, order preservation, cancellation, and revocation
before a later batch. The existing service test now expects four concurrent calls
for two candidates with two rules, rather than the previous two. The original
failed assertion and successful rerun are retained. All 48 patches replay exactly
across 206 files. Extracted-server HTTP/OAuth checks pass with synthetic identity
and a placeholder compiled authorization page.

The candidate is packaged; deployment and live retest are pending. Native
0.4.32/runtime65 is unchanged. This does not make a safety-rate or all-P0 claim.

The new demo records actual prompt submission and responses in Claude Desktop.
Browser recording was refused by macOS, and linking the new space through
`finish_context_setup` was denied by Claude's automatic review as Data Exfiltration.
These require the owner's host approval; no alternate capture or setup route was
used. A full replacement walkthrough is not complete. The previous video remains
unchanged and must not be presented as the requested new end-to-end recording.
