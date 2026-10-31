# Classifier reliability candidate — 31 October 2026

Patch 53 is published and live as server **20261031-classifier-reliability**.
Existing-account Google authentication completed; the checked rollout verified
all 160 files, service-account readability and all three healthy services.
The production login page, TLS certificate, OAuth discovery, unauthenticated MCP
rejection and desktop/phone rendering pass. Native 0.4.33/runtime66 is unchanged.
The previous server remains retained for rollback.

A fresh two-account signed production check imported two synthetic notes,
created and accepted a disposable Space invitation, enabled two rules, requested
public/private context and removed the requester. The public answer was withheld
at **0.9921505**, below 0.995. The private candidate was found and withheld at
0.0006600. Both accounts saw the same shared history; only the owner saw checks.
Removal rejected requests/history (404) and the old invitation (403). Sharing
was paused, links revoked, the space archived and both imports deleted.
This is a real signed API/browser-session check using two selected accounts,
not independent-human or recipient-host model acceptance.

## Changes

The selected Decisions prompt is version 5. It evaluates owner-authorized scope
without requiring a second approval for every fact within an allowed category,
or treating factual uncertainty and negative news as disclosure prohibitions.
Every rule still applies, restrictions override allowances, the full audience
must be permitted, and source confidentiality and incomplete-context checks
remain. The exact proposed excerpt is never rewritten or redacted.

A shared FIFO schedules calls from all classifier instances using the same
credential and endpoint in one process. It permits at most four active calls,
spaces starts at least 125 ms apart and bounds the waiting queue to 128 calls.
Queueing consumes the existing provider deadline; cancellation removes queued
work before transmission. Overflow, timeouts, invalid responses and HTTP errors
withhold context. There are no automatic retries or fallback models. Queue-full
diagnostics are visible only in the contributing owner's existing checks.

The model remains `pplx-decider-v1.2`; the cutoff remains **0.995**. No owner rules,
membership, expiry, source revision fences, host permissions or provider account
limits changed. The scheduler does not coordinate other processes or applications
using the same API credential.

## Actual provider results

All evaluation content and accounts were synthetic. There were 367 actual
provider calls across the repeated baseline, selected candidate and retained
rejected experiments, with one attempt per case per candidate.

| Exercise | Baseline | Selected candidate |
| --- | --- | --- |
| Original corpus plus native archive cases: 16 permitted excerpts | 8 shared, 8 withheld | 12 shared, 4 withheld |
| Original corpus plus native archive cases: 30 forbidden excerpts | None shared | None shared |
| Additional fixed corpus: 20 permitted excerpts | 1 shared, 19 withheld | 12 shared, 8 withheld |
| Additional fixed corpus: 20 forbidden excerpts | None shared | None shared |
| Ten-owner burst: 10 public requests, 40 provider calls | 0 public requests shared; 30 HTTP 429s | All 10 public requests shared; no provider errors |
| Ten-owner burst: private content and private metadata | None disclosed | None disclosed |

The candidate burst completed in 5.229 seconds and measured at most three active
network calls; 40 decisions were pending concurrently. It used injected synthetic
candidates with real SpaceContext authority, persistence and provider calls.
Separate native cases used actual archive search/read with synthetic records.
Neither test invokes a recipient host model or proves a production user journey.

The additional corpus was written and hashed before candidate prompt changes,
then used to compare candidates. It was authored by this agent and is not an
independently authored final holdout. These small samples do not calibrate the
model's scores or establish a universal privacy guarantee.

Prompt version 4 made the original corpus worse and was rejected. An inverted
withholding-question prototype, labeled version 6, offered little gain over
version 5 while changing score interpretation; it was not selected. Their exact
reports remain beside the selected candidate. The original 29 October evidence
is unchanged.

## Verification and release

- All **640 core tests** pass, including queue bounds, shared-instance capacity,
  FIFO scheduling, cancellation, timeout, overflow and no retry on HTTP 429.
- The focused sharing run passed 88 tests before the final queue-audit regression
  was added; that additional regression passes in the full 640-test run.
- Eight scheduler/provider tests pass against the extracted bundle. HTTP, OAuth,
  MCP, read-only scope and origin checks also pass with a disposable profile,
  a compiled-authorization placeholder and the local source dependency tree.
- All **53 ordered patches replay exactly across 217 changed files**.
- The runtime bundle contains 160 files. Only `perplexity-decisions.mjs`,
  `policy-context.mjs` and the new `decisions-scheduler.mjs` differ from the
  prior server; no migration or native package changes are required.
- Bundle SHA-256:
  `bc4c6c60f709a8773cd78fecd87e060b38196c807026452a52ed119f36324c12`.

The first preflight stopped at Google Cloud reauthentication. That failure and
the initial draft-release evidence remain intact. The subsequent authentication
and deployment succeeded without an alternative account or host-policy change.
The first live sharing failure is also retained; publication and service health
do not establish useful-sharing readiness.

Permitted content is still sometimes withheld. Retrieval recall, answer-only
privacy, full shared Q/A, clean onboarding and independent-human acceptance
remain open. This is a measured reliability improvement, not all-P0 completion.

[Verification and artifact hashes](../implementation/classifier-reliability-verification.json)
· [Portable patch order](../implementation/classifier-reliability-manifest.json)
· [Preserved stress baseline](SHARING-STRESS.md)

Source and evidence: [PR #48](https://github.com/diask5/commonplace-plugin/pull/48).
The [published server release](https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-server-20261031-classifier-reliability)
contains four verified assets, pinned to source commit
`5982da69ccfea5fa2dd1e387690e2e46d8828824`. The checked deployment verified the exact
prior release and limited the runtime diff to three modules. The original draft
asset hashes and authentication-blocked observations remain historical evidence.
