# Context status and backup throughput

1 November 2026. Patch 70 is published and live in server `20261101-context-throughput`. All 166 deployed files and service readability, 47 unchanged migrations, four services and fresh worker heartbeat pass. Public browser/OAuth checks pass. Native 0.4.44/runtime77 is unchanged.

Status polling previously scanned aliases separately for every legacy row. A metadata-only owner/device pass and synchronous snapshot now preserve the same counts and exact prefix semantics without that repeated scan. Coverage also selects metadata without loading source bodies. A warmed synthetic fixture matching the observed 4,385 rows and 700 aliases improved from a 1,459 ms median to 15 ms; this is not a production latency claim.

Backups resolve the real database location before choosing their private snapshot directory. This puts verification on the balanced database volume after the storage cutover. Snapshot consistency, integrity verification, upload destination, permissions, retention on failure and timeouts are unchanged. The normal backup completed at 04:39:40 UTC with snapshot verification and successful remote upload. Two prior production backup timeouts remain failures.

All 853 core checks pass. Nine status/coverage and four backup regressions pass, with before-change failures retained. Exact 70-patch replay matches 267 changed files. The extracted 166-file server passes 13 focused tests and local HTTP/OAuth/MCP smoke checks. Those smoke checks used linked unchanged dependencies; they are not independent dependency packaging or real Google/native-host acceptance.

Only three runtime modules changed; all 47 migrations and public assets are unchanged. Authority, exclusion, expiry, sharing rules, classifier settings and host permissions are unchanged. See `implementation/context-status-performance-verification.json` and the retained metadata-only evidence in `implementation/end-to-end-repair/`.

A postdeployment untraced health sample still took 4.26–5.74 seconds. Installed Mac source reading passed (12,000 characters, 10 citations), but listing took 12.383 seconds and reading 5.753 seconds. Performance is not closed by this release. A temporary loopback-only main-thread CPU profile was collected and its inspector was closed; no source text or arguments were published. Follow-up mirror scanning and shared-CPU capacity work remain separate.
