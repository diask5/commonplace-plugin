# Cloud workspace rollout

The 0.4.13 source integrates the personal agent board, published working context,
and supported visible chat sync into one private cloud workspace. The hosted
relay must be updated before publishing the corresponding marketplace update.
Installing the plugin alone does not activate these server capabilities.

## Prepare the release

Use Node 22.13 or newer and Python 3.9 or newer. From this repository:

```sh
npm ci --ignore-scripts
npm test
npm run test:ui
npm run test:deployment
python3 scripts/build-plugin.py --output artifacts/public-0.4.13
COMMONPLACE_TEST_BASELINE="$PWD/artifacts/.cache/meet-proxy-0.3.0.zip" npm run test:package
python3 scripts/build-runtime-update.py --output artifacts/runtime-0.4.13
```

The runtime bundle includes every account-runtime module, nested browser asset,
and SQL migration, with a SHA-256 manifest. This avoids dropping a dependency
when a deployment spans multiple plugin versions. Keep the existing compiled
website, authentication integration, dependencies, runtime image, and secrets
on the server. Do not copy credentials into release files or a synced workspace.

## Inspect and activate the existing relay

Deployment access uses the owner's authenticated Google Cloud CLI and IAP SSH
to `commonplace` in project `vertical-web-313417`, zone `us-central1-a`.
Authentication must succeed before deployment; reauthentication is a Google
browser step, not a new Meet Proxy account connection.

Before activation, record the current `/opt/commonplace/current` target, applied
migrations, both systemd service states, free space on the database volume,
and the pinned Codex image. Confirm the previous service is healthy. Transfer
the reviewed bundle, manifest, checksum, and `scripts/deploy-cloud-update.py`
through that authenticated SSH connection. Verify the checksum on the VM.

Run as root with the exact observed baseline and a new release name:

```sh
python3 deploy-cloud-update.py \
  --bundle runtime-update.json \
  --baseline OBSERVED_CURRENT_RELEASE \
  --release 20261020-cloud-workspace1
```

The script keeps a verified SQLite backup, rehearses all unapplied migrations on
a disposable copy, preserves the previous release, switches the release, and
checks web readiness. It then requires an active cloud-worker service and a
heartbeat written after that worker started. A web response or an old heartbeat
cannot establish worker readiness. A failed activation restores the previous
release and restarts both services. It does not overwrite the live database or
discard writes; migrations must therefore remain additive and backward compatible.

The rollout record includes the exact installed file hashes and retained backup.
Check these against `runtime-update-manifest.json`, confirm migrations
`0037_agent_history.sql`, `0038_agent_context.sql`, and `0039_cloud_workspace.sql`,
and confirm both services remain healthy. Do not edit already applied migrations.

For a later code-only update, `--code-only` verifies that the complete migration
file set and bytes match the current release, and that the live database already
records every expected migration digest. Any difference stops the deployment.
This mode leaves the database untouched and retains previous backups; activation
still requires web readiness, a fresh worker heartbeat, and rollback on failure.

The cloud runtime explicitly approves only `network.send_agent_message` for
owner-authorized task-scoped consultations. Other tool approval defaults and all
native-host permission settings remain unchanged. Account checks, active task
leases, cancellation, recipient checks, and the eight-message budget still apply.

## Verify before publishing

Use disposable signed test profiles for transport checks and existing owner
authorization for any real model or chat test. Verify:

- A private workspace snapshot includes supported synced text, an agent message
  thread, and published working context, with source timestamps and revisions.
- Owner exclusions, revocation, and unrelated accounts remain isolated.
- The actual pinned container can start both archive and network MCP servers.
- A cloud task uses workspace evidence, consults an authorized native agent,
  waits without repeated model polling, and resumes on the matching reply.
- Its final reply returns to the originating conversation. Record the model
  reply separately from queue, transport, and read receipts.
- A cancelled task or expired lease cannot use the communication socket.

Only after those checks, publish both verified plugin aliases and update the
marketplace hashes. The Conductor receiver records its runtime revision. Updating
a legacy receiver verifies its live process, account profile, native thread,
host/workspace identity, and process lock before graceful retirement. A receiver
that cannot be verified or has not released its lock is not replaced; its durable
delivery cursor remains intact. Reload the intended existing chats and confirm runtime
revision 45, account identity, native binding, and receiver status. Preserve
existing sync choices; enabling transcript upload remains a separate owner choice.

Keep the deployment record, previous release, and database backup. Report any
untested host explicitly. The known Conductor Mac-binding regression is a host
limitation and is not fixed by this rollout.

## Daily backup and restore

The account runtime includes `backup.mjs`. It uses a separate read-only SQLite
connection and an explicit read transaction to pin one consistent snapshot while
sync and worker heartbeats continue. An unpinned incremental SQLite backup can
restart indefinitely under those writes. Only an integrity-checked snapshot is
renamed to the final filename. Upload failure keeps that verified local copy.

After deploying the runtime, install `infra/production/backup.conf` as
`/etc/systemd/system/commonplace-backup.service.d/reliability.conf`, reload systemd,
and restart `commonplace-backup.service`. Keep its existing identity, restricted
filesystem access, environment file, bucket and daily timer. The override changes
the entrypoint and bounds execution to five minutes. Check successful exit and
the next timer deadline; a timer waiting on an indefinitely running job is not a
successful backup. Download the new object to a disposable path, verify SQLite
integrity, and compare its schema/table inventory before deleting that test copy.
Never restore a test backup over the live database.

If rolling back to a release without `backup.mjs`, remove the entrypoint override
before reloading systemd. Retain the finite timeout and verified backup objects.
