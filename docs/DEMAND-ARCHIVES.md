# Build optional cloud archives when a task needs them

**Published and live: server `20261026-demand-archives`, 159 files verified.** Native 0.4.27/runtime60 is unchanged.

The optional model worker rebuilt its own archive on every collection change,
even when it had no runnable model job. The web process maintains a separate
archive for MCP reads and the native folder, so this duplicated indexing on the
production VM. A read-only inspection found zero queued/running cloud jobs.

This change removes only the worker tick's eager rebuild. A claimed cloud task
still prepares its current snapshot before running the model, checks authority
and expiry, and releases the snapshot afterward. Waiting-device tasks keep their
state and prepare current context on resumption. Native collection is unchanged.
Web status, setup and read requests continue to refresh the web archive; its ready
status may wait for that first poll when no one is using it.

All 583 core tests and 40 focused cloud tests pass. New regressions prove no idle
build, current preparation before a queued model run, subscription setup without
an archive, and readiness through the web path. The prior model benchmark finished
before activation, preserving its four passes and four grounding/retrieval failures.
The new run passed five cases: all four Codex cases and Claude correction. Claude
synthesis received four changed/restart replies, then attempted list_shared_context
outside the test allowance. The guard stopped that case and left two unstarted. This
was not a host denial; saved permissions are unchanged.
[Sanitized model evidence](../implementation/demand-archives-native-benchmark.json).

Public checks passed for all 31 assets, protocol endpoints and desktop/phone sign-in.
One sample measured health at 1.464s and page render at 6.100s/12.376s. The earlier
sample was slower, but loading remains slow and the samples are not a general
performance guarantee. [Screenshots and receipts](../implementation/demand-archives/public-smoke.json).

[Verification and portable patch](../implementation/demand-archives-verification.json).

A read-only isolated probe measured a source read at 435ms through its worker,
while the existing native transport took 4.998s for a source read. Reused indexing
took 4.984s in this sequential probe; real transport search took 14.116s. Ongoing
collection still causes revision restarts. These are separate diagnostic paths,
not an end-to-end pass. The next candidate changes first-read guidance and tests
a bounded retry without changing any authorization or revision fence.
