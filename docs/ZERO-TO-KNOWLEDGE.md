# Zero-to-knowledge verification

This records the initial 0.4.21 audit. The newer native startup repair and current
production/read verification are in [the spec recheck](SPEC-RECHECK.md).

**Production:** `20261026-archive-reads` at https://34.27.253.220/.
**Native:** 0.4.21 / runtime56 installed and active on the owner's Mac.

The supported context pipeline works on the real account: a real Claude transcript
was automatically collected and retrieved; all 293 files in its 34.7-million-character
archive passed SHA-256 verification in the local folder. The later archive reached
294 documents. The same account and server were preserved throughout the upgrade. A second message
appended through the real native session also arrived automatically. It was observed
within 310 seconds of the CLI finishing; this is an upper bound from periodic checks,
not an instantaneous-sync guarantee. All 40 discovered local captures were complete
at inspection, with no recorded parse errors.

**The real assistant answer is verified:** after the owner explicitly approved a
per-invocation allowlist for only `search_shared_context` and `read_shared_context`,
a fresh Claude Code test used both tools successfully and returned the exact probe
marker. Its numeric suffix was not supplied in the prompt. The successful read
matched a search result and returned five citations. There were no permission
denials, and before/after checks found no saved permission changes. See
[the exact read permissions](NATIVE-READ-PERMISSIONS.md).

**Latency and clean shutdown remain open:** the answer took 87.95 seconds. MCP
connected in 177 ms, but initial resource listing hit the host's 30-second timeout.
Indexed search took about 3.8 seconds; the first read failed with a transport timeout
and a retry succeeded. The host emitted a successful final result, but the test
harness reached its 110-second process/pipe timeout afterward. This proves the
answer path, not consistently fast or clean process completion. Incremental
collection also remains a performance target; the observed live delay is above.

## What was tested

| Check | Evidence |
| --- | --- |
| Core backend/native protocols and privacy | 431/431 passed on final source |
| Full browser suite | 127/127 passed; final setup checks 20/20 |
| Original product lifecycle | 15/15 passed |
| Archive and mirror regression | 27/27 passed, including 33 MB and interrupted transfer |
| Packaged zero-account knowledge journey | Passed again against final relay source |
| Packaged launcher and distribution integrity | 2/2 launcher; both aliases verified |
| Packaged stdio and idle mailbox | Passed; host sockets and Google identities are fixtures |
| Real Mac collection and local mirror | Full document hashes and real probe verified |
| Fresh real assistant answer | Exact marker verified through successful search/read; temporary two-tool rule, no saved permission changes |
| Native startup/read/exit reliability | Resource discovery and first read timed out; final answer succeeded before harness cleanup deadline |

The zero-account journey uses the production browser UI and packaged native modules.
It covers sign-in, the private setup handoff, five Claude/Codex/child-agent sources,
complete long Unicode text, hidden-reasoning/credential filtering, search, paged MCP
resources, identical local files, appended messages, stale revisions, group creation,
two-person invitation acceptance, rules, actual indexed retrieval, approved excerpts,
private audit, pause and exclusions.

Google identity, native-host identity and classifier scores are fixtures in that
journey. Signed HTTP, database, filesystem ingestion, indexing, UI, and sharing
boundaries are real test components. Fresh real Google sign-in and every OS/app
launch variant were not independently reverified in this audit. Codex Desktop is
not installed on the tested Mac.

## Failures found and repaired

1. Mixed-case transcript paths used locale sorting with a code-unit resume cursor.
   The new regression failed before the fix; collection now uses one consistent order.
2. Each archive download page revalidated thousands of unrelated sections. Current
   authorized snapshots are reused for reads. Returned files and search indexes are
   checked against their hashes; corruption fails closed and triggers repair. Full
   reconciliation still validates everything, and revisions/expiry remain enforced.
3. Production Brotli compression delayed large API responses enough to time out the
   native transport and keep the old companion busy. The production proxy now requests
   gzip upstream. Nginx validated and reloaded successfully. The mirror completed and
   the native runtime then upgraded normally, without killing processes or changing
   account, chat identity, or permissions.

The first parallel-I/O fix alone did not resolve live mirroring. Failed download and
assistant attempts are retained in local evidence. No failed attempt is counted as
an end-to-end pass. All 153 deployed runtime files were checked against the reviewed
bundle; relay, worker and nginx services are active. No schema migration or backfill
was needed. The nginx configuration backup and before/after hashes are retained.

## Scope of “full knowledge”

This means available, supported visible histories and explicit imports. It does not
include arbitrary repository contents, every web-only chat, binary attachments or
upstream MCP services. Cached Conductor history is labeled cached; a sleeping device
cannot upload new context. Exclusions and cross-person sharing limits still apply.
The classifier can withhold allowed information and is not guaranteed perfect.

The current product follows the owner's context-only Spaces / My context direction.
Legacy messaging tests preserve compatibility; owner retrieval requires no hosted AI.

## Reproduce

Apply all twenty portable patches in manifest order. The full chain reproduces 154
source files. Native 0.4.21 remains immutable; the twentieth patch is a server and
production transport follow-up.

```sh
npm test
npm run test:ui
npm run test:spec
COMMONPLACE_E2E_PLUGIN=/absolute/path/to/extracted-plugin npm run test:knowledge
```

Set `ZERO_SCREENSHOTS` to capture each browser stage. Logs and seven walkthrough
screenshots are under `.context/zero-to-knowledge/`. Portable results and artifact
hashes are in `implementation/zero-to-knowledge-verification.json`.
