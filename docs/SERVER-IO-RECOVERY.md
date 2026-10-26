# Server I/O follow-up

The live 0.4.26 server answered health requests in 12.5–14.7 seconds. A disposable
signed-request probe found four durable commits per authenticated request, while
archive builds rewrote every generated document after a one-document change.
The current server-only follow-up reduces that work. Native 0.4.26/runtime59,
accounts, installed settings, sharing rules and database migrations are unchanged.

Only the SDK's outer throttle counter moves to bounded process memory. Its
fixed-window counts still return HTTP 429 at the limit, active counters are never
evicted, and capacity exhaustion denies new keys. Counters reset on restart and
are per process. JTI replay protection, grants, tokens and per-device quotas remain
durable with SQLite FULL synchronous writes. The measured two-request tool call
falls from nine commits to seven; the durable quota still increments twice.

Archive generation still renders every document from current authorized sources.
An unchanged generated document can be hardlinked from the previous verified
generation only if its identity, path, digest, immutable permissions, size and
actual bytes match. Otherwise it is written fresh. A one-document update reuses
seven of eight documents with output identical to a cold rebuild. Corruption,
writable files, removal and source authority changes retain their checks. FTS is
still rebuilt and all source bytes still validate; this does not remove all I/O.

**State: published and live at `20261026-io-recovery`.** All 536 core tests,
nine focused review checks and the independent source review pass. All 28 ordered
patches reproduce 188 files exactly. The complete runtime bundle has 156 files
matching source. These results establish correctness and reduced writes in
fixtures. Live health improved from 12.5–14.7 seconds to 3.1–6.7 seconds in three samples, but remains slow. A subsequent public browser smoke timed out at 30 seconds waiting for DOM content; that attempt did not pass.

The [verification record](../implementation/server-io-recovery-verification.json)
tracks activation and results. [0.4.26's native benchmark](TIMEOUT-RECOVERY.md)
retains one follow-up pass, one partial citation result and one reconnect/timeout
failure; no failed first attempt is erased. No paid infrastructure change has been
made. Default-host invitation routing and the unintended empty Briar Review
space remain open items.

The fresh installed-host follow-up completed both questions with real searches and source reads. Codex passed; Claude correctly answered the unknown-time question, but one citation only had a search excerpt rather than a completed full read. Both took about 209 seconds. Receipts show repeated archive-revision restarts and one timeout; the strict citation and performance gates remain open. See [sanitized benchmark](../implementation/server-io-native-benchmark.json) and [deployment evidence](../implementation/server-io-production.json).
