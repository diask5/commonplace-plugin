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

Server `20261028-bounded-classification` is published and deployed. All 159 files
are verified and readable; all three services are healthy and migrations are
unchanged. Native 0.4.32/runtime65 is unchanged. The same short query completed
with 26 audit entries: 20 scored below the unchanged 0.995 cutoff and six
were withheld after provider HTTP 429. These are not 26 successful classifications.
The highest public-source score was 0.991195. This is evidence of completion,
not a useful-sharing pass. Public withholding remains a usability gap. An
incidental plain message caused by the post-rollout form reset is retained and
not counted as a context request. No safety-rate or all-P0 claim is made.

The new demo records actual prompt submission and responses in Claude Desktop.
Browser recording was refused by macOS, and linking the new space through
`finish_context_setup` was denied by Claude's automatic review as Data Exfiltration.
These require the owner's host approval; no alternate capture or setup route was
used. A full replacement walkthrough is not complete. The previous video remains
unchanged and must not be presented as the requested new end-to-end recording.
