# Unified context production verification — 22 October 2026

Release: Meet Proxy 0.4.14, companion runtime 48. Implementation: [source PR #9](https://github.com/diask5/commonplace-session-tests/pull/9), commit `74d7a24`. The final bundle includes additive migrations `0040_unified_context.sql` and `0041_atomic_context_captures.sql`.

Production is active on `20261022-unified-context3`. Both services are healthy,
all 125 installed assets match the manifest, and all 36 deployed integration
checks pass. Existing account settings and native routing match the pre-rollout
fingerprints. Verified backups and previous releases are retained.

## Validation

- 312 application tests and 49 UI checks pass, covering signed collection, full source files, ranked search, filters, citations, source exclusions, replica convergence, deletion, and account isolation.
- Incomplete captures preserve the previous complete version. Replacement scans, interrupted long messages, staged deletions, revocation and exclusion are covered by the new atomic-capture tests.
- All 12 deployment checks pass. Rollout backups now pin one read-only SQLite snapshot, so ongoing worker writes cannot restart the copy indefinitely. A two-minute copy deadline removes incomplete backups before activation.
- All 25 focused companion upgrade, receiver and setup checks pass. Runtime 48 ensures existing candidate installations load the atomic collector.
- Both plugin aliases pass package integrity, bundled dependency and executable-mode checks. The final archive hashes are below.
- A separate real-agent diagnostic benchmark passed 13 cases and 29 factual checks. The UI-to-worker-to-real-agent round trip completed in 32.935 seconds with six valid citations. This was a synthetic corpus and a local model adapter; see [the benchmark report](LOCAL-AGENT-BENCHMARK.md).

The [GitHub verification run](https://github.com/diask5/commonplace-session-tests/actions/runs/39714216694) passed for the final source commit, including application/UI tests, deployment regressions, package integrity, signed transport smoke and runtime bundle creation.

## Production rollout

The hosted relay is updated through authenticated Google Cloud IAP access. Each schema change retains a verified SQLite backup, rehearses migration on a disposable copy, preserves the prior release and requires a fresh worker heartbeat after activation. The final release is `20261022-unified-context3`.

Preservation checks compare installation/account links, model-account state, sync choices and exact native routing with the backup. A display-name-only change observed during the first rollout did not change identity, routing or generation. All installed files are checked against the bundle manifest.

Public desktop and mobile checks verify delivered UI assets against their hashes, reject unauthenticated context search, check JavaScript errors and check horizontal overflow. Authenticated UI behavior is exercised with isolated local fixtures.

All 36 deployed integration checks passed in 176.493 seconds. The suite uses the installed account-runtime modules with disposable databases and a loopback signed-auth fixture. Its SDK dependencies are bundled for the fixture; no synthetic records enter the production database. This verifies module behavior, not a fresh production Google/model sign-in or a universal native-host wake test.

This existing Codex chat was updated through the verified bundled helper. A fresh MCP process confirmed version 0.4.14, runtime 48, the same account, a verified native identity and a ready receiver; the existing linked conversation still permits replies. A settings fingerprint confirms that only the plugin executable paths changed.

Other existing installations use their supported plugin manager or bundled Codex setup helper. Verify the current account, native binding, runtime 48 and receiver status after updating. A running host may require an MCP refresh in the same chat. No repeat Google link or transcript-sync change is required.

## Limits

Collection requires the owner's saved sync choice and an awake, supported source. ChatGPT web history requires an export import; attachments and unsupported applications need explicit connectors. Unknown conversation identities remain separate, and extracted project statements retain attribution rather than becoming automatic semantic truth.

Answer citations still display as IDs. Conductor's sleeping-chat wake and Mac-binding limitations remain host-specific. The real-agent benchmark did not evaluate all private owner context or every supported host.

## Verified artifacts

| Artifact | SHA-256 |
| --- | --- |
| `meet-proxy-0.4.14.zip` | `676a0e296c3f86a37e7b66cf1a949e80456bc297503d719e259c96a33cb99bbd` |
| `commonplace-0.4.14.zip` | `a73fd6cb8d0b71d67acb83003ae85b2914df8a11708e9672d1780749f1b93919` |
| `runtime-update.json` | `1f331efa0ef28a2ed2c134dc0d3161ac8f6dac93beaa1a8a4d64880bcf9b68af` |
