# Context read performance

Status polling scanned source-table pages containing large text bodies. The web
process also trusted a published flag written by a worker whose archive lives in
a different directory, which could make search rebuild the web snapshot before
answering. This server update adds covering indexes and checks the actual local
snapshot before selecting the fast path. Missing or stale snapshots still use
authoritative live reads. All post-read revision, source and expiry checks remain.

**State: reviewed and packaged; activation and live measurements are pending.**
Native 0.4.26/runtime59 is unchanged. Migration 0045 adds three indexes without
changing rows or authority. It requires a verified database backup and migration
rehearsal before activation; older code remains compatible with the indexes.

Archive reads also load the MCP adapter only when serving MCP, skip redundant
permission writes on unchanged read-only sections, and use the small current
pointer when releasing a snapshot. Full byte/hash checks and pin protection remain.
The worker still cleans its separate archive; eager cleanup was not disabled.

551 core checks pass, with zero failures or skips. Independent review found no
blockers and passed 53 focused checks. Deployment checks pass 54 locally, with
the real-Nginx test skipped there (it passed for the preceding asset release).
30 portable patches reproduce 196 implementation files exactly. The bundle has
158 files. Synthetic warm-cache status queries improved from 9.06 ms to 0.16 ms;
these figures do not establish production speed.

[Verification](../implementation/context-read-performance-verification.json)
records hashes and activation. [Public asset delivery](PUBLIC-ASSETS-DELIVERY.md)
remains live. Real-model, citation and default-host routing limitations remain
recorded; no failed attempt has been replaced with a passing fixture.
