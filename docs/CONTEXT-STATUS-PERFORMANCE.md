# Context status and backup throughput

1 November 2026. Patch 70 is packaged and independently reviewed for server `20261101-context-throughput`; publication and live acceptance are pending. Native 0.4.44/runtime77 is unchanged.

Status polling previously scanned aliases separately for every legacy row. A metadata-only owner/device pass and synchronous snapshot now preserve the same counts and exact prefix semantics without that repeated scan. Coverage also selects metadata without loading source bodies. A warmed synthetic fixture matching the observed 4,385 rows and 700 aliases improved from a 1,459 ms median to 15 ms; this is not a production latency claim.

Backups resolve the real database location before choosing their private snapshot directory. This puts verification on the balanced database volume after the storage cutover. Snapshot consistency, integrity verification, upload destination, permissions, retention on failure and timeouts are unchanged. Two prior production backup timeouts remain failures.

All 853 core checks pass. Nine status/coverage and four backup regressions pass, with before-change failures retained. Exact 70-patch replay matches 267 changed files. The extracted 166-file server passes 13 focused tests and local HTTP/OAuth/MCP smoke checks. Those smoke checks used linked unchanged dependencies; they are not independent dependency packaging or real Google/native-host acceptance.

Only three runtime modules changed; all 47 migrations and public assets are unchanged. Authority, exclusion, expiry, sharing rules, classifier settings and host permissions are unchanged. See `implementation/context-status-performance-verification.json` and the retained metadata-only evidence in `implementation/end-to-end-repair/`.
