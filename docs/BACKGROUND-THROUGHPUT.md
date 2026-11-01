# Background sync throughput

1 November 2026. Patch 67 reduces avoidable production work during context collection. It is a server-only follow-up to native 0.4.42/runtime75 and changes three account modules. Publication and live rollout are tracked separately in [verification](../implementation/background-throughput-verification.json).

Status polling and live search/list requests now coalesce filesystem/FTS warming. A background build waits for 30 seconds without an observed revision change, with one active build and at most eight admitted owners/directories per database. Same-revision polls do not postpone the deadline. Explicit awaited warming and cloud-job preparation remain immediate; source-backed reads and mirrors retain their authority and revision checks. Pending timers are cancelled on shutdown, active builds drain, and errors settle queued callers without an automatic retry loop.

Inbox presence, route leases, poll timestamps and bounded delivery receipts now commit together using synchronous savepoints. Receipt retries skip already-recorded timestamps. Owner, session, generation and expiry checks remain intact. No transaction spans an await. Durable replay records, quota accounting and SQLite FULL durability are unchanged.

Six inbox regressions fail before the repair and pass after. Identical synthetic calls reduce registration commits from 2 to 1, empty poll commits from 3 to 1, and a 100-receipt flush from 202 to 1. The complete authenticated idle cycle improves only from 16 to 15 commits; this change alone does not establish a major live throughput gain.

All 801 core tests pass. The scheduler suite passes 16 checks, related archive/setup/disclosure checks pass 193, inbox-related checks pass 128, and independent review passes 130. Counts overlap. Exact replay of all 67 patches matches 263 changed files. The server artifact retains 166 files and all 47 migration digests; native artifacts, policies, classifier settings and host permissions are unchanged.

The original live slowdown was measured at 5.5–9.5 seconds for local server health requests, with disk commit waits and a 641 MB WAL on the existing 30 GB standard persistent disk. The exact share attributable to each workload is unconfirmed. Live latency, large Mac mirror completion and communication acceptance must be recorded after rollout before claiming readiness.

The release is now published and live as **20261101-background-throughput**, with all 166 files/readability, 47 unchanged migration digests, three services and public browser/OAuth checks verified. The retained previous release is 20261101-context-recovery. Rollout took 28.48 seconds. Three post-rollout local health samples were 2.548, 2.058 and 4.406 seconds; the Mac status call took 3.476 seconds. These observations show improvement, but are not a controlled throughput benchmark. The first large Mac mirror and native/Work reply acceptance remain open.
