# Unified context candidate — 21 October 2026

Implementation: [source PR #9](https://github.com/diask5/commonplace-session-tests/pull/9),
commit `4449406`, plugin 0.4.14, runtime revision 47.

## Validated behavior

- 293 application tests pass, including source convergence, durable retry,
  checkpoint recovery, edits/deletion, Unicode, child agents, native identity
  aliases, account isolation, exclusions/restore, and damaged-source isolation.
- 46 UI/API checks pass, including mobile accessibility, source reading, project
  pagination, account changes and exclusion controls.
- Ten deployment regression checks pass; the dependency audit reports zero
  known production vulnerabilities.
- Both archives passed package integrity checks. The packaged signed transport
  smoke passed with six fresh profiles, exact-chat receipts, restart recovery,
  offline backlog and deduplication. Google identity and native hosts were
  synthetic fixtures; this is separate from live deployment verification.

The candidate includes the latest released backup and nonblocking Conductor
receiver fixes. The public production health endpoint returned ready during this
verification. That does not prove this candidate is deployed.

The complete [GitHub verification run](https://github.com/diask5/commonplace-session-tests/actions/runs/39542882981)
also passed on the final source commit, including application/UI suites, deployment
regressions, package integrity, signed transport smoke and runtime bundle build.

## Rollout state

Deployment is blocked: two `RunLocalCommand` calls returned
`Error running local command: Timed out waiting for client`. There was no new
Google authentication error or permission denial. The deployment uses the Mac's
existing authenticated gcloud installation; no credentials were copied.

The backend bundle contains additive migration `0040_unified_context.sql` and
122 runtime/migration assets. Before activation, inspect the actual current
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
| `meet-proxy-0.4.14.zip` | `a1e476c46b447b0eec21431ef57f83f9ba42a290a58b6e072b6f44b0a3eef57d` |
| `commonplace-0.4.14.zip` | `7b2d5c979086febd7df8dc07aa4037c025f579ccbd8150fcb777ec05d2d6a2e4` |
| `runtime-update.json` | `04b2bc910503ee89d47ae9a8a7f9aedf41217275fc6810b7ca67de1edad02988` |
