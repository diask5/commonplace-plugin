# Production database storage — 1 November 2026

The **r5 production storage cutover passed** at **04:16:48 UTC**. Performance remains unresolved: post-storage health requests took approximately **4.0–9.5 seconds**, and main-process CPU remained high. Both live scheduled-backup attempts timed out; normal backup reliability and final readiness remain open.

The [live result](../implementation/end-to-end-repair/storage69-attempt5.json) records all four services active: `commonplace`, `commonplace-runtime`, `commonplace-files` and `nginx`. Startup required main health, a fresh worker heartbeat, Files `/files/config` availability and an actual Files mount-namespace read of the selected auth database. All **47 migration digests** matched. The backup timer's prior active state was restored, with its enabled state unchanged, before `passed` was recorded.

## Storage and recovery retained

The stable database path `/var/lib/commonplace/account.sqlite` now resolves to `/var/lib/commonplace/database-storage/account.sqlite` on the balanced disk `/dev/sdc`, UUID `4b9a5959-5eed-4a88-a902-b4f30c7993cd`. R5 reused the existing nested mount; it did not remount or format the disk, or change service sandboxes or permissions.

The original `/dev/sdb` mount at `/var/lib/commonplace` and all **3 SSH workspace mounts** remain. The verified pre-cutover database copy is retained at `/var/lib/commonplace/storage-before-balanced-20261101-r5/account.sqlite`; the populated earlier target remains `database-storage/account.before-r4.sqlite`. Prior attempt evidence and backups are retained. Closed checkpoint, hash/schema/quick-check validation, atomic path publication and recovery by copying the latest committed data were preserved.

The independently reviewed and executed r5 helper has SHA256:

```text
84bf47d080ed1aa0fac230035000d7451f705b756b8a98656964f7e361cd0aab
```

## Four earlier guarded attempts

All four recorded results are `rolled-back`; their failures remain evidence.

| Attempt | Start, UTC | Recorded failure |
| --- | --- | --- |
| [1](../implementation/end-to-end-repair/storage69-attempt1.json) | 03:41:18 | Assertion with no explanatory message; the result does not identify its failing condition. |
| [2](../implementation/end-to-end-repair/storage69-attempt2.json) | 03:44:14 | Remaining database holder, PID 253145. |
| [3](../implementation/end-to-end-repair/storage69-attempt3.json) | 03:47:20 | Main health did not become ready after the sibling-mount cutover. The subsequent target used the existing writable subtree. |
| [4](../implementation/end-to-end-repair/storage69-attempt4.json) | 04:05:52 | A scheduled backup acquired the database during preflight, PID 883648. The main namespace probe passed; recovery also passed the Files auth namespace proof against the original regular database. |

R5 paused only `commonplace-backup.timer`, checked expected application-holder cgroups before pausing the apps, and retained the strict no-holder check after stopping them. It never stopped or signaled the active backup service and restored the timer in `finally` after application checks or recovery.

## Backup status remains separate

The scheduled backup that started at **04:03:23 UTC** hit its **existing 5-minute systemd timeout** at **04:08:23 UTC**. Its result remains `failed` / `timeout`, exit status **15**, with no successful snapshot observed. The repair did not signal it or reset its failure. R5 accepted only the exact recorded **12-field historical fingerprint**, with MainPID **0** and no unexpected holder; a changed or newly occurring failure still aborted. This exception did not replace r5's fresh, verified migration backup. See the [retained timeout](../implementation/end-to-end-repair/storage69-backup-timeout.json).

The follow-up backup started at **04:22:55 UTC**, PID **886126**, invocation `5dfe709008d341b8a9bacc3b43bd8d9c`. The owner confirmed that it also hit the existing systemd timeout at **04:27:55 UTC**, with MainPID **0**, `failed` / `timeout` and exit status **15**. No agent signal or `reset-failed` occurred. No snapshot-verified message or successful upload was established; this is a second failed live attempt.

At **04:27:15 UTC**, live inspection found a roughly **365 MB partial snapshot** on the old disk (device **2064**), while the actual database was on device **2080**. The backup was reading the partial file, with `folio_wait_bit_common` and approximately **335 MB of disk reads**. The backup entrypoint selected `backups` from the logical database pathname, so the symlink relocation left snapshot verification on the old disk.

A minimal **source-only correction**, intended for patch 70, resolves the database with `realpath` before choosing its backup directory. For the current layout this selects `/var/lib/commonplace/database-storage/backups`. Its two symlink regressions failed before the change, while both regular-path cases passed. All **6 focused synthetic checks** now pass, including successful upload cleanup, retention of a verified backup after upload failure, the existing pinned snapshot under concurrent writes and existing timeout behavior. Permissions, verification, upload protocol and timeouts are unchanged. The source and new test are frozen for independent review; this record establishes no deployment or successful live backup after the correction.

## Performance and validation limits

The [before](../implementation/end-to-end-repair/capacity69-before.json) and [after](../implementation/end-to-end-repair/capacity69-after.json) production samples show:

| Measurement | Before | After |
| --- | --- | --- |
| Sample duration | 44.68 seconds | 44.50 seconds |
| Health request range | 2.7–6.8 seconds | 4.0–9.5 seconds |
| Host iowait | 40.4% | 12.4% |
| Main-process CPU | 90.0% | 133.4% |
| Disk await | 8.46 ms | 2.75 ms |

Every sampled health response reported ready, but latency remained high. These short, instrumented live samples show reduced iowait; they do not establish a sustained throughput improvement or a solved performance problem. Root and agents 92 and 66 are implementing and reviewing **patch 70** for reproduced `sourceStatus` alias scans, alongside the backup-directory correction. Its deployment and live performance acceptance are not established by this storage record.

Separately, **43 local synthetic checks** passed and an independent reviewer reran the same 43 checks, plus **36 changed-fingerprint rejection checks**. These disposable SQLite/filesystem and simulated systemd/process fixtures are distinct from the live cutover. See the [independent review](../implementation/end-to-end-repair/review-storage69-r5-verification.json) and [machine-readable storage record](../implementation/production-storage-verification.json). This documentation update made no new production or Mac calls and establishes no final readiness claim.
