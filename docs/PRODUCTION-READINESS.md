# Production verification

Verified October 20, 2026. The hosted relay and cloud worker are active on the
0.4.13 runtime. Marketplace publication awaits the final native consultation.

## Deployed service

Release `20261020-cloud-workspace3` is active at
[the hosted service](https://34.27.253.220). The public `/healthz` endpoint is
ready, both services are active, and the worker reports a fresh heartbeat.
All 117 installed runtime file hashes match the release manifest. Migrations
0037–0039 are applied.

The initial migration rollout retained a complete SQLite backup, passed integrity
checks, and rehearsed the migrations on a disposable copy before activation.
Subsequent code-only rollouts verified the complete migration file set and bytes
against the current release and the applied database digests. Failed activation
restores the previous code and services without replacing the live database.
The previous releases, deployment audits, and verified backup remain available.

The data disk was expanded online from 10 GB to 30 GB after it reached 99% usage.
Existing cloud workspaces were retained; approximately 20 GB is now free.

## Checks completed

- 274 application tests passed before the final argument-feedback change; all
  13 targeted cloud-workspace tests passed after that change.
- 45 browser/API checks passed, including setup recovery, mobile layouts,
  accessibility, account changes, and stale-response handling.
- Ten deployment regression tests passed, including worker readiness, rollback,
  complete bundles, and strict code-only migration verification.
- Both plugin archives passed source, dependency, SHA-256, and executable-mode
  checks. The dependency audit reported no known vulnerabilities.
- Packaged signed onboarding and native-delivery smoke passed, covering retry
  deduplication, ordered offline catch-up, and a persistent receiver. These
  fixtures use synthetic Google and native-host assertions.
- The pinned production container started and called both MCP servers as UID
  1000 with a read-only root and no subscription credentials in the test.
- A real subscription task read the disposable archive source, cited it, computed
  73,411 minus 22,508 as 50,903, and sent one consultation to the authorized native
  peer. The task entered durable waiting while that peer's workspace was asleep.
  A queued message does not establish a completed round trip.

## Installation and scope

The existing Codex chat loaded the verified 0.4.13 package and runtime revision
45. Its receiver upgrade retained the account, original linked conversation,
native binding, and delivery cursor. Status reports automatic delivery and a
ready receiver. The host's already running MCP process may require refresh to
expose the new tool catalog. The Mac plugin-manager update follows publication.

The owner explicitly approved only the cloud runtime's
`network.send_agent_message` tool for task-scoped consultations with their own
agents. Recipient ownership, active leases, cancellation, and the eight-message
budget remain enforced. Native host permissions and existing transcript-sync
choices were preserved.

The known Conductor Mac execution-binding regression remains a host limitation.
A sleeping workspace cannot run its receiver; queued messages wait for that
workspace to resume. Unsupported or unsynced sources do not supply live context.
This verification does not establish support for every native host.

## Artifacts

| Artifact | SHA-256 |
| --- | --- |
| `meet-proxy-0.4.13.zip` | `c4c1feefb2c07e638dd5df11f72e959c6e8ac939173ba2f4d559d4fee8351b9a` |
| `commonplace-0.4.13.zip` | `3431eec65f48eeb24fc59f2a77a850a47cdf6daa9c165687cc34e2a30dda059f` |
| `runtime-update.json` | `553ea72a0088a0e882c263925741bb52fb87c55e07d77b46b36c55f6ecb39061` |

Implementation: [cloud workspace](https://github.com/diask5/commonplace-session-tests/pull/6),
[rollout hardening](https://github.com/diask5/commonplace-session-tests/pull/7), and
[receiver upgrades and consultations](https://github.com/diask5/commonplace-session-tests/pull/8).
