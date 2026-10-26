# Build optional cloud archives when a task needs them

**Candidate packaged; activation pending.** Native 0.4.27/runtime60 is unchanged.

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
an archive, and readiness through the web path. The previous model benchmark is
allowed to finish on its original server release before activation. No deployment
or performance improvement is claimed yet.

[Verification and portable patch](../implementation/demand-archives-verification.json).
