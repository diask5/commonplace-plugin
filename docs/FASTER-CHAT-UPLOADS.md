# Faster chat uploads

1 November rollout update: this work is included in published native **0.4.37/runtime70** and live server **20261101-space-events**. The earlier candidate and access-block records below are historical. See [current rollout evidence](SPACE-EVENTS-ROLLOUT.md) for publication, installation and activation separately.

31 October 2026 — patch 59 publishes native **0.4.35/runtime68** and server
**20261031-compressed-context**. Both releases and their asset hashes are verified; neither is
installed or deployed. The server bundle includes the previously published,
undeployed patch 57 invitation changes and targets the exact live patch 56 release,
`20261031-setup-activation`.

Transcript uploads now use up to 100 messages per request instead of 40, within
the existing 64,000-byte request limit and six uploads per tick. JSONL collection
reads 256 KiB windows on demand instead of reading up to 8 MB for every small
batch. The existing 8 MB record scan bound remains. Message and deletion batches
use encoded UTF-8 byte budgets; partial records and incomplete captures remain
incomplete. Existing stored retries retain their original inputs.

When the authenticated status endpoint advertises `gzip-base64-v1`, uploads of
at least 2 KiB use gzip level 1 inside a JSON envelope, but only if the envelope
saves at least 10%. This also compresses native Agent Auth capability arguments;
an HTTP Content-Encoding header alone would not do so. Small or incompressible
inputs stay plain. A relay without the capability continues to receive plain
JSON. Negotiation is refreshed each tick; uncertain writes do not trigger a
second transport attempt. Decompression restores the original input before retry
digest checks. Compressed and plain retries therefore identify the same write.

The receiver checks authentication, upload scope, sync opt-in and rate limits
before decompression. Both the incoming request and decompressed JSON remain
bounded by 64,000 bytes. Malformed, truncated, invalid UTF-8, nested and oversized
payloads are rejected. Sync opt-in is rechecked after asynchronous decompression;
the synchronous ingest transaction rechecks the device, account and source
exclusions. Native account assignment remains locked across compression and
sending. No collection consent, source visibility, sharing rule or classifier
setting changes.

## Measured synthetic backlog

The reproducible benchmark uses 200 chats with 120 messages each and one chat
with 6,000 messages: 30,000 messages total. Every received message was compared
with its original text. It exercises the actual collector and compression code
with a mocked upload sink, including durable state, fair scheduling and heartbeat
traffic. It does not use a production account or network.

| Measurement | Published runtime67 collector | Candidate runtime68 collector with gzip |
| --- | ---: | ---: |
| Upload requests | 774 | 474 |
| Context payload bytes | 9,570,049 | 2,204,610 |
| Collection ticks | 129 | 79 |
| Maximum messages per request | 40 | 100 |
| Logical process reads | 154,912,011 bytes | 24,129,332 bytes |
| Verified complete messages | 30,000 | 30,000 |

This is **77% fewer payload bytes and 39% fewer requests**. Payload sizes include
the base64 envelope but exclude HTTP and authentication overhead. Five-second
scheduling models 640 seconds versus 390 seconds between first and final ticks;
these are not observed upload durations. Exploratory local elapsed times are
retained in the JSON, but unrelated validation ran concurrently, so they are not
an isolated CPU benchmark or evidence of Mac speed. The optimization does not
expand access to web-only Claude/ChatGPT history or diagnose an offline collector.

## Validation and rollout

Eight focused checks cover compression savings and fallback, Unicode, malformed
and oversized inputs, the actual signed Agent Auth relay, retry identity,
account isolation, opt-out, exclusions, changing server capabilities, bounded
window reads, large deletion batches and opt-out during decompression. The last
race was reproduced as a failure on the initial candidate, then fixed; its
original failure log is retained. The final broader suite passes 665 tests. Thirteen extracted-native checks,
both-alias integrity, 35 extracted-server checks and exact 59-patch replay
across 226 files also pass.

Evidence, package hashes and final results are in
`implementation/faster-chat-sync-verification.json`. The portable patch applies
after patch 58 and retains previous release evidence. Native batching improves
an upgraded installation even against the existing server. Gzip requires both
the new native runtime and the server advertising support.

Mac activation and production deployment remain blocked by the earlier
Conductor `RunLocalCommand` result: **“Local execution is not enabled for this
session.”** That denial has not been retried or bypassed. Published assets do
not establish an installed runtime or a live gzip transfer.
