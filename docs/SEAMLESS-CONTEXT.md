# Seamless context update — 0.4.25/runtime58

Packaged and regression-tested. Publication, production activation, installation
and the fresh ordinary-prompt benchmark are tracked separately in
[the verification record](../implementation/seamless-context-verification.json).
The earlier [ordinary-prompt benchmark](NATURAL-PROMPT-BENCHMARK.md) remains intact.

Normal questions now start with MCP search and supporting source reads. The
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
mailbox smoke checks, and 16 deployment checks passed. The synthetic lifecycle
and native-host fixtures do not establish real Google or model behavior.
25 ordered portable patches reproduce 185 implementation files exactly.

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
