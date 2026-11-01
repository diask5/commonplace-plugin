# Archive visibility performance

1 November 2026. Patch 71 is packaged and independently reviewed for server `20261101-archive-visibility`; it is not deployed. Production remains `20261101-context-throughput`, with native 0.4.44/runtime77 unchanged.

Archive projection still evaluated every alias for every legacy row after patch 70 repaired status polling. The same owner/device metadata lookup now filters hidden rows before fetching their bodies. It runs within the existing pinned snapshot and is discarded after each request. Document IDs, ordering, source authority and revision/expiry/exclusion checks are unchanged.

A warmed synthetic 4,385-row/700-alias/24-file request fell from a 1,864 ms median to 65 ms; a 13,694-section/224-alias projection fell from 1,894 ms to 294 ms. These are synthetic measurements, not production throughput claims. Two regressions fail before the change. All six new tests and 853 existing core tests pass in separate runs; the permanent npm test command includes the new tests. Independent review passed 42 focused checks. Exact 71-patch replay matches 268 changed files.

The 166-file extracted bundle passes 34 focused tests and HTTP/OAuth/MCP smoke checks. Dependencies are linked from the unchanged source installation, so the smoke output’s generic “isolated dependencies” label is not an independent dependency packaging claim. An initial extracted-test invocation used the wrong working directory; that harness failure is retained separately. Only `archive-source.mjs` differs from the live bundle; all 47 migrations and public assets are unchanged.

Conductor removed this chat’s authorized Mac binding after an incoming agent update. Its local-command tool returned: “No authorized Mac is bound to this chat. Send a message from the Mac you want to use.” No retry or alternate Mac route was attempted. The planned capacity upgrade completed read-only preflight only; no stop, resize or start operation was issued. Final deployment and performance acceptance remain open. See `implementation/archive-visibility-performance-verification.json`.
