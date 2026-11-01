# Continuous catch-up and incremental history scanning

1 November rollout update: this work is included in published native **0.4.37/runtime70** and live server **20261101-space-events**. The earlier candidate and access-block records below are historical. See [current rollout evidence](SPACE-EVENTS-ROLLOUT.md) for publication, installation and activation separately.

The owner challenged the six-upload-per-pass cap and repeated rescanning of a
6,722-file library. Inspection confirmed both in the existing collector:
`Math.min(this.budget, 6)` limited each pass, and the companion scheduled another
pass only every five seconds. Each pass walked every root and called realpath
and lstat for every candidate. Gzip reduced bytes but did not remove those costs.

Patch 61 removes that six-upload clamp. The automatic collector drains useful
backlog during a cooperative two-second work slice and immediately schedules its
next slice while progress remains. The slice yields to other companion work;
it does not add a five-second sleep. Explicit small test budgets still work.
The old protocol's compatibility uploader retains its existing bounded behavior.

The current protocol uses a disposable local file index. Filesystem events update
changed paths; untouched continuation passes reuse the index. A full scan every
30 seconds recovers missed/unsupported watcher events, and a restart rebuilds it.
Selected files still revalidate their real path and root before reading. Partial
or inaccessible scans never imply a source was deleted. Conductor preparation is
reused for at most five seconds during immediate catch-up; ordinary checks still
refresh it. Coverage includes preparation, scan and upload timing measurements.

Uploads retain one ordered durable in-flight payload per collector. This change
does not add parallel requests or remove the server's existing 120-per-minute
sync limit. HTTP 429 pauses the pump using Retry-After when available, with a
60-second fallback; transient failures back off. The pause is saved across a
restart, and the pending chunk is retried exactly before newer content. Idle and
disconnected collectors do not spin. The account-assignment lock, opt-out,
exclusions, complete-capture publication, 64,000-byte decoded payload bound and
visible-text filter remain in force.

## Evidence

The benchmark creates 6,722 real local files, seeds 6,721 complete checkpoints,
and uploads a 6,000-message backlog to an immediate mocked endpoint. Baseline and
candidate runs are sequential. This isolates directory traversal, collection and
serialization; it is not a network, live Mac or production throughput test.
The prior gzip benchmark remains available with an explicit six-upload budget so
its historical compression comparison is reproducible.

The baseline performed 67,220 discovery file checks across 10 passes; the
candidate performed 6,722 in one pass. Both transmitted and verified all 6,000
backlog messages in 60 bounded uploads. Sequential local processing measured
6.561 seconds versus 2.290 seconds. 685 core tests, 19 focused recovery/cross-host
checks, 17 extracted-native checks, both-alias integrity and exact 61-patch replay
across 242 files pass. Extracted native tests use the unchanged extracted patch-60
server candidate and existing source dependencies.

See [verification](../implementation/continuous-chat-sync-verification.json) for
exact measurements, hashes, regression results and extracted-package checks.
Initial failures are retained: recovery tests expected an immediate retry before
the new persisted backoff; their clocks now advance to retry time. A legacy
Conductor fixture exposed inappropriate preparation caching outside catch-up;
legacy/ordinary checks now refresh it. A package check correctly detected a
build started before the final collector edits; the final artifacts were rebuilt.

## Release state

Native **0.4.37/runtime70** is a locally packaged candidate containing patch 60's
Spaces events work plus this uploader fix. It is not published, installed,
activated or deployed. Patch 61 changes no server files or production settings.
The event system still needs patch 60's server migration before live activation.
Production remains the previously verified `20261031-setup-activation`.

The existing Mac execution block remains: `mcp__conductor__RunLocalCommand`
reported “Local execution is not enabled for this session.” No retry or alternate
execution route was used. This work does not establish the other agent's active
installed version, repair an inaccessible work machine, or collect unsupported
web-only chat history.
