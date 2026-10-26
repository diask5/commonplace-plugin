# Seamless context update — 0.4.25/runtime58

**Historical 0.4.25 rollout:** it was activated at `20261026-seamless-context-final`.
[0.4.26/runtime59 is now live and installed](TIMEOUT-RECOVERY.md); the evidence
below preserves the earlier release and first benchmark attempts.
All 156 deployed files match the verified bundle. Public desktop/phone, OAuth,
compiled authorize, unauthenticated MCP rejection and six UI asset byte checks pass.
The first activation rolled back after a two-second health timeout. A tested,
bounded 120-second startup check activated the same immutable runtime bundle.
The database and migration set were unchanged; rollback remains in place.

**Not yet consistently seamless.** Production health ranged from 3.144 to 8.508 seconds and timed out at 15.199
seconds under live load on e2-small. Capacity investigation and optional resize are pending.
The Mac has 0.4.25 files installed, with its account, bindings and saved permissions
preserved, and runtime58 is now active after the owner-approved graceful restart. Older
launchers raced the update; they were briefly paused and all resumed. No saved
permissions or account configuration changed.

The default-host ordinary-prompt run retrieved allowed context and handled an
unknown launch time, but also misrouted invitations: it created an empty unrelated
ChatGPT space named Briar Review and tried a browser for acceptance. Browser
approval was denied. The run was stopped; the empty space still needs cleanup.
Those failures are preserved. A separate controlled MCP-only run disables unrelated
apps, browser/computer, command and web-search tools, and skips the denied cases.
It cannot be reported as a default-host success. All five of five executed controlled cases passed, with two previously denied cases skipped and
no external calls. Two real Claude seed chats were created without tool calls;
both notes have complete canonical capture receipts. Five of seven attempted
real-archive cases passed with actual search, source reads and matching citations.
Two hit a transport timeout, whose trailing-period error was not normalized and
misled the host toward authentication recovery. The Claude sequence stopped when
it tried an unapproved setup tool; its final case was not started. A narrowly
scoped 0.4.26/runtime59 correction is packaged and checked; see [its rollout](TIMEOUT-RECOVERY.md). It does not resolve VM
capacity or turn failed first attempts into passes.

See [the verification record](../implementation/seamless-context-verification.json)
and [public checks](../implementation/seamless-public-smoke.json).
The earlier [ordinary-prompt benchmark](NATURAL-PROMPT-BENCHMARK.md) remains intact.

The native instructions now direct normal questions to MCP search and supporting source reads. The
optional local folder is no longer a prerequisite. Space invitation URLs route
to preview/accept tools, and questions about members route through current space
membership and sharing rules. Citations remain private to the owner unless
explicitly shared for the receiving audience. Legacy thread scopes remain intact.

The connector generates request IDs. A transient gateway failure gets one retry
with the same ID; timeouts return promptly with a recovery ID. An identical retry
can recover a short-lived uncertain ID automatically. Successful new requests
always evaluate current rules again. Denials and changed accounts cannot trigger
automatic retries. Write tools keep their write annotations and host approvals.

Search uses authoritative canonical data while the file snapshot rebuilds. Source
changes, exclusions and expiry during either a live or snapshot read withhold its
bytes and require a restart. The live path has bounded size and concurrency; very
large archives still use snapshots. New and changed chats upload ahead of routine
heartbeats, with fair backfill and retries. Unreadable sources and incomplete scans
stay partial and cannot mark missing files unavailable prematurely.

Setup now shows installation-specific received and searchable counts, continued
collection and the latest check-in. Only visible canonical content from that
installation makes its setup ready. Another computer's content or a heartbeat
cannot. Copy/open remain separate from Send, required approval/reload and confirmed
registration. **Spaces / My context** and the compact three space tabs are preserved.

## Verification

527 core tests, 135 UI checks, 15 original product-lifecycle checks, both-alias
packaging, 32 extracted feature/launcher tests, packaged stdio and six-profile
mailbox smoke checks, and 21 deployment checks passed. The synthetic lifecycle
and native-host fixtures do not establish real Google or model behavior.
26 ordered portable patches reproduce 185 implementation files exactly; the final two-file patch changes only deployment readiness and its tests.

A synthetic 400-conversation / 30 MB archive test measures the direct path;
production's largest published archive measured 332 conversations / 35 MB.
Hardware and live traffic differ, so real-host timings are recorded separately.

## Desktop and phone walkthrough

These screenshots use isolated fixture identities, not production accounts.

| Step | Desktop | Phone |
| --- | --- | --- |
| Choose your app | [View](images/seamless/01-choose-1440.png) | [View](images/seamless/01-choose-390.png) |
| Copy, paste and Send | [View](images/seamless/02-copy-primary-1440.png) | [View](images/seamless/02-copy-primary-390.png) |
| Context arriving | [View](images/seamless/03-scanning-1440.png) | [View](images/seamless/03-scanning-390.png) |
| Collection still partial | [View](images/seamless/04-partial-1440.png) | [View](images/seamless/04-partial-390.png) |
| Searchable context ready | [View](images/seamless/05-ready-1440.png) | [View](images/seamless/05-ready-390.png) |

Production sign-in captures: [desktop](images/seamless/production-desktop.png) /
[phone](images/seamless/production-phone.png). These are the public live page;
the authenticated walkthrough table above uses explicitly labeled fixtures.
