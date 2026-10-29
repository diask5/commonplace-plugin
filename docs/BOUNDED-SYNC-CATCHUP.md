# Bounded catch-up for long conversations

The live follow-up found a real collection bottleneck. A new visible message was
already in this Mac's staged Conductor history, but its 1,330-section conversation
was being recaptured one chunk per cycle. The collector spent its five remaining
upload slots on unchanged-source heartbeats. Atomic publication correctly retained
the earlier complete context while the new capture was incomplete, so the fresh
message was not yet searchable.

Patch 52 rotates the next chunk behind other active sources and any reserved
overdue heartbeat, before ordinary unchanged heartbeats. It keeps the existing
six-upload ceiling, byte/message limits, atomic capture, durable retry payloads,
owner fences, exclusions and malformed-source backoff. A one-slot collector also
reserves a turn for an overdue heartbeat. It does not increase the upload budget
or publish incomplete captures.

Three new regression cases fail before the fix and pass afterward: a 240-message
source finishes in six uploads in one cycle; two active sources both advance while
an overdue heartbeat retains its slot; a failed second chunk resumes with exactly
the same payload after restart. The full 631-test core suite passes, including
the five-client sync/retrieval regression. All 52 portable patches replay exactly
across 212 changed files.

Native **0.4.33/runtime66** is published and installed in both permanent
registries. The actual companion still runs runtime65: two normal activation
attempts deferred, and the same restart endpoint returned 45 active-work
responses during a bounded wait. No signals or force path were used. A bounded
retry (at most 12 attempts, 45 seconds between attempts) is scheduled on the Mac;
activation remains unverified until it reports runtime66. Server
`20261029-cross-host-sync` is live and unchanged by this native update.

The supported Claude updater initially saw 0.4.32 because it clones the default
`codex/plugin-distribution` branch, while the new catalog had first merged into
main. PR #46 promoted only the verified release pointers into that distribution
branch; a subsequent supported update passed. The repository default was not
changed. Accounts and saved permissions were preserved.

At 06:04:07 UTC the post-deployment marker was successfully read at archive
revision 6534 with five citations. Its source capture is complete. Other sources
remain partial, and this read still used runtime65; it is production sync
evidence, not proof the new scheduling behavior is active.

The earlier successful marker read and the incomplete second-marker check are
preserved separately. Regular Claude/ChatGPT connections still read the existing
library without automatically collecting web-only history. The prior Claude
setup denial and real-host/clean-install acceptance gates remain open.

See [the verification record](../implementation/bounded-sync-catchup-verification.json)
and [cross-host setup](CROSS-HOST-CONTEXT-SYNC.md).
