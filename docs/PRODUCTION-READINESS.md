# Production verification — 20 October 2026

The production backend includes migrations 0037–0039, the persistent private
workspace, and task-bound cloud messaging. Both web and cloud-worker health were
checked, including a fresh worker heartbeat and every deployed runtime file hash.

A real connected ChatGPT subscription read a disposable archive source, calculated
73,411 − 22,508 = 50,903, and sent one connection-check message to an existing Mac
agent. The task entered durable waiting, received that agent's correlated reply,
resumed automatically, and completed with the correct result and source citation.
This verifies the actual cloud → native Mac → cloud path, beyond a queue receipt.

Automated checks cover account isolation, exclusions and revocation, fresh
onboarding, browser and mobile UI, retries, offline backlog, duplicate prevention,
task cancellation, restart recovery, package contents, and deployment rollback.
The package smoke uses real signed HTTP, companion processes and sockets, with
synthetic Google identity and native hosts. It is not fresh human Google consent.
The release workflow repeats these checks on pull requests and main.

The production backup implementation uses a dedicated SQLite read transaction
so continuous sync writes cannot restart a backup indefinitely. Backup tests
restore a snapshot while the live database changes and verify timeout cleanup.
The service retains a verified local copy if cloud upload fails and has a bounded
systemd runtime. See PRODUCTION-ROLLOUT.md for installation and recovery.

## Host and source limits

- The Mac round trip was verified. Delivery into the earlier Conductor test chat
  was accepted by its transport but did not produce a reply turn. It remains a
  separate unresolved host delivery check; receipt does not mean execution.
- Conductor agent-origin messages can invalidate the host's Mac execution binding.
  The plugin does not bypass or repair host authorization.
- Each existing chat must load the updated plugin. Installation alone does not
  prove a live MCP process reloaded, and offline devices cannot be verified.
- Sync covers supported visible local transcripts and owner-authorized imports.
  Ordinary ChatGPT/Claude website history is not available through model sign-in.
  Missing or offline sources remain missing until a supported import or sync runs.
- OAuth consent and native-host approvals are completed by their owners. Existing
  sync preferences, agent bindings and account connections survive an upgrade.

The Pulumi Cloud Run/Postgres topology remains an optional, undeployed migration.
Production uses the existing GCP VM, durable SQLite, cloud storage backups, and
isolated subscription runtime containers.

## Release record

Production release `20261020-cloud-workspace4` contains 118 verified runtime
assets. The web service and worker are healthy. The repaired daily backup
completed; a 282,689,536-byte cloud object passed its checksum and a real restore
integrity check, with 107 tables and 40 recorded migrations. The temporary
restore copy was deleted. Previous releases and migration backups are retained.

Validation: 277 application tests, 45 browser/UI checks, 10 deployment tests,
both archive integrity checks, and packaged transport smoke passed. The production
dependency audit reported zero known vulnerabilities.

## Package checksums

- `meet-proxy-0.4.13.zip`: `e00213777682a39fd9ba7accd4cacdee56f846ad041513c0913c2d01775cb634`
- `commonplace-0.4.13.zip`: `cb481fbf9e3df784027316ab33d68e47f602068a6eeb8425b4452996cabf430b`
