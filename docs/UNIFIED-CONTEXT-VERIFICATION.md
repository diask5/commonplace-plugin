# Unified context candidate — 21 October 2026

Implementation: [source PR #9](https://github.com/diask5/commonplace-session-tests/pull/9),
commit `2181c53`, plugin 0.4.14, runtime revision 47.

## Validated behavior

- 303 application tests pass, including source convergence, durable retry,
  checkpoint recovery, edits/deletion, Unicode, child agents, native identity
  aliases, account isolation, exclusions/restore, and damaged-source isolation.
  Search checks cover ranked keywords across turns, quoted phrases, prefixes,
  literal punctuation, filters, exact read offsets and excerpt-only receipts.
  Complete file parity, old-layout upgrades and damaged-index recovery pass.
- 49 UI/API checks pass, including mobile accessibility, source reading, project
  pagination, account changes and exclusion controls.
- Ten deployment regression checks pass; the dependency audit reports zero
  known production vulnerabilities.
- Local integration checks exercise the real signed HTTP collector, search, cited
  answers, sync pause, edits, exclusions, offline consultations, cancellation,
  sign-in failure, model limits, persistence and origin rejection. Browser checks
  cover search pagination, setup, account-switch races, mobile layout and accessibility.
  Google, models and native hosts are isolated fixtures; see [local development](LOCAL-DEVELOPMENT.md).
- Both archives passed package integrity checks. The packaged signed transport
  smoke passed with six fresh profiles, exact-chat receipts, restart recovery,
  offline backlog and deduplication. Google identity and native hosts were
  synthetic fixtures; this is separate from live deployment verification.

The candidate includes the latest released backup and nonblocking Conductor
receiver fixes. The previous production health check returned ready. That does
not prove this candidate is deployed.

The updated [GitHub verification run](https://github.com/diask5/commonplace-session-tests/actions/runs/39691242304)
checks this source commit, including application/UI suites, deployment regressions,
package integrity, signed transport smoke and runtime bundle build.

## Rollout state

Deployment is intentionally deferred at the owner’s request. The local lab runs
independently and does not change production accounts, sync choices or installs.
Prior Mac deployment attempts timed out waiting for the client; rollout still
requires an authenticated deployment environment. No credentials were copied.

The backend bundle contains additive migration `0040_unified_context.sql` and
124 runtime/migration assets. Before activation, inspect the actual current
release, retain a full verified database backup and rehearse migrations using
`deploy-cloud-update.py`. Do not use `--code-only` for this migration. Verify both
services, a fresh worker heartbeat, all manifest hashes, and synthetic collection,
query, exclusion and restore on the deployed service before promotion.

After backend verification, publish the verified plugin archives, merge the
marketplace update, and update each existing installation through its supported
manager or bundled Codex helper. Verify accounts, sync preferences and native
bindings are preserved. These installation steps have not been performed for
0.4.14. Existing production stays on the released 0.4.13 code.

## Limits

Collection requires an enabled sync choice and an awake, supported source.
ChatGPT web history still requires export import; attachments and unsupported
apps require explicit connectors. Different verified accounts retain separate
archives. Unknown conversation/message identities remain separate. Project
statements are attributed extracts, not automatic semantic truth resolution.
Conductor's sleeping-chat wake remains an independent host limitation.

## Artifacts

Both plugin archives passed source, SHA-256, dependency, bundled import and
executable-mode checks. The candidate remains a draft until backend and
existing-installation verification complete.

| Artifact | SHA-256 |
| --- | --- |
| `meet-proxy-0.4.14.zip` | `370206d4789bcdba08c19a91335c3b1873f5bd6db593cff03b589c722916695f` |
| `commonplace-0.4.14.zip` | `888bbdef9c3dd8922cc8c7a28224742b12a210ab97d6b3a7ae4ab2bae08c4b4b` |
| `runtime-update.json` | `18877cafca5d6f7a73a61bb3451703b22cb7f8e83d1e4ae5094d75923d4eaf33` |
