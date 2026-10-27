# Deployment source modes — 27 October 2026

The first 0.4.31 server rollout failed with EACCES during web startup and
automatically restored `20261026-current-read`. All three services and a fresh
worker heartbeat were verified after rollback. The account database was not
replaced or migrated.

The deployment runner used umask 077 for private evidence. The original deployer
recreated runtime source with that inherited mask, producing mode 0600 rather
than the baseline's 0644. This is distinct from the historical native
connection-unavailable read; it does not explain that earlier failure.

Patch 42 explicitly preserves existing source-file modes and uses 0644 for new
source, with 0755 for newly created source directories. It unlinks candidate
hardlinks/symlinks before writing, preserving previous-release bytes and modes.
Database backups and private rollout records keep their separate permissions.

A real `deploy.main()` regression reproduces 0600 against the original helper.
The corrected deployment suite has 57 passes and one existing skip across 58
tests. Independent review found no material blocker. The 42-patch replay
reproduces all 204 changed source files. Native ZIPs and the runtime bundle are
unchanged; the corrected helper is a distinct server-r2 artifact with a new hash.

[Exact evidence](../implementation/deployment-source-modes-verification.json).
Original failed artifacts and logs remain intact. The corrected live retry is
verified in [release receipts](../implementation/p0-live-release-verification.json):
all 159 files match and are service-readable, all three services are active, and
the worker heartbeat is fresh. The previous release remains available.
