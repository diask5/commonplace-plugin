# 0.4.31/runtime64 candidate — 26 October 2026

**Locally packaged for native acceptance; P0 remains open.** Neither alias nor
the server update has been uploaded, published, installed or deployed. Current
production remains 0.4.28/runtime61 with server `20261026-current-read`. Existing
0.4.29 draft assets and local 0.4.30 artifacts are unchanged.

## Changes in this candidate

- Includes patches 38–39: resolve the owner's selected space without substituting
  another audience, and require a successful source read for every final citation.
  Their separate Conductor model checks passed 3/3 space and 8/8 retrieval cases.
- Adds patch 40: three exact archive validation/lookup failures now return
  `result.isError` with fixed correction guidance, rather than JSON-RPC -32603.
  Unknown documents, offsets past the end and whitespace-only search phrases are
  covered. No input IDs or source text enter those correction messages. All other
  exceptions retain their existing error path. This change is remote MCP only.
- Includes the earlier page-size guidance and bounded stderr diagnostics. The
  diagnostics still do not identify or fix the Mac connection-unavailable failure.
- Patch 41 assigns 0.4.31/runtime64 and includes the new regression in `npm test`.

No tool, schema, permission, account, scope, retry, authority or source-fence
relaxation is part of this candidate. The original failed benchmark results,
unstarted cases and previous release records remain intact.

## Evidence

[Machine-readable verification](../implementation/p0-ready-candidate-verification.json)
records exact package/server hashes and a 41-patch replay reproducing all 204
changed source files. The full core suite passes **594/594**, with zero skips or
TODOs. The new integration tests reproduce the three failures before the fix,
then exercise corrected calls through real local OAuth and archive workers.
Separate checks preserve stale-revision restarts, read-only write refusals and
unrelated internal failures. These use disposable synthetic profiles.

Both native aliases pass package integrity checks for overlay bytes, dependency
preservation and executable modes. Both launcher checks and both native identity
tests pass. The packaged stdio/signed-HTTP smoke test passes with synthetic
identities and host metadata. The extracted server passes OAuth/resource and
scope/origin checks using the installed dependency tree and a placeholder for the
compiled authorization page; it does not exercise Google or a native host.
All five error regressions also pass against the extracted server artifact.

The earlier 3/3 and 8/8 model checks used source overlays in fresh Conductor cloud
sessions. They are not a new model run against the 0.4.31 package, a cold-start or
multi-page model benchmark, or installed-native/production proof.

## Remaining live gates

Follow [P0-CLOSEOUT.md](P0-CLOSEOUT.md): diagnose the real failed reads, verify the
candidate in both installed hosts, complete a real owner-selected second-person
invitation/sharing/revocation walkthrough, and prove clean Google/Desktop setup.
Host-required Send, approval and reload remain explicit.

The latest Mac execution request was denied. This work did not retry it, use an
alternate local route, change permissions, or start another login. Existing-account
GCP reauthentication remains unverified. Further live diagnosis requires the owner
to explicitly reopen that execution path and complete the existing sign-in.
No real-person invitation or cleanup of the unintended empty space was performed.
