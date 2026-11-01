# Context sync and communication closeout

1 November 2026. Native **0.4.44/runtime 77** is published, installed and active on the Mac and cloud. Server **20261101-context-throughput** (patch 70) is live. Distribution PRs 70 and 71 are merged; source PR 68 tracks the repairs and evidence. Setup remains https://34.27.253.220/.

## Verified live

- All **166 deployed files** and service readability, **47 unchanged migration digests**, four active services and the fresh worker heartbeat pass. Public TLS, browser, OAuth, MCP authentication and seven public-asset checks pass.
- The database moved to a balanced disk while preserving the original disk, backups and three workspace mounts. A normal backup completed at **04:39:40 UTC** with a verified snapshot and successful cloud upload. Both earlier timeouts and all guarded cutover attempts remain retained.
- The large Mac mirror passed **823 document digests / 41,196,479 characters** and later reached **899 documents / 42,219,841 characters**. The latter count is a status observation, not a second full hash audit. Installed source reading returned 12,000 characters with 10 citations. Account identity and permissions stayed unchanged.
- Local capture showed **203 complete of 204 eligible records**, no per-source errors and no queued messages; one capture remained incomplete. This is not complete coverage of every historical chat or unsupported web-only history.
- Fresh native 0.4.44 published and read back Personal progress; root independently read the exact revision-1 entry. Its Personal `progress.updated` event was observed. The same-owner message/reply roundtrip completed with both deliveries accepted and the exact expected answer. This is an actual native exchange, not a queued-message claim.

## Remaining gates

Health requests still took **4.26–5.74 seconds** in the untraced post-patch-70 sample. A Mac source listing took 12.383 seconds and its read 5.753 seconds. Status scans and backup placement are repaired, but end-to-end performance is not closed.

Patch **71** removes the remaining correlated alias scan from archive projection. It is packaged and independently reviewed, not deployed. Synthetic request medians improved from 1,864 ms to 65 ms with exact output parity. The 853 existing core checks and six new checks pass in separate runs; the permanent test command includes all six. Independent review passed 42 checks, the extracted bundle passed 34 checks, and all 71 patches replay exactly across 268 changed files. Native 0.4.44 is unchanged.

The planned upgrade from an e2-small shared-CPU VM to e2-standard-2 completed read-only preflight only. **No VM stop, machine-type change or start operation was issued.** Conductor dropped this chat’s authorized Mac binding after an incoming agent update. The next local-command call returned: “No authorized Mac is bound to this chat. Send a message from the Mac you want to use.” No retry or alternate Mac route was attempted. This blocks the remaining production rollout and capacity activation, not the already deployed patch 70.

The targeted Work question is saved in the existing space. Its selected receiver on the owner’s Bland account remains offline, and no answer or delivery receipt has been observed. Its receiving side was not moved. A generic `read_workspace` diagnostic on this group ID returned 404; group-board history is available through `read_chat_link`, and that error is retained separately.

The first fresh-44 attempt during maintenance remains failed. The later broad archive search encountered two revision changes; it is not a successful discovery check. A scoped follow-up search and successful source read at revision 459 confirmed the actual Willow Creek assistant final; prompt copies were distinguished. Earlier fresh-43 actual-assistant archive verification remains valid. There is no all-host, clean-machine, independent-human, full-history or all-P0 readiness claim.

See [status performance](CONTEXT-STATUS-PERFORMANCE.md), [archive visibility](ARCHIVE-VISIBILITY-PERFORMANCE.md), [storage](PRODUCTION-STORAGE.md), and the metadata-only records under `implementation/end-to-end-repair/`.
