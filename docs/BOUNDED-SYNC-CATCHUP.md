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

Native candidate **0.4.33/runtime66** packages the fix. Publication, installation
and a successful live follow-up read are still pending; do not infer them from
the source tests. Server `20261029-cross-host-sync` is already live and its bytes
do not change for this native fix.

The earlier successful marker read and the incomplete second-marker check are
preserved separately. Regular Claude/ChatGPT connections still read the existing
library without automatically collecting web-only history. The prior Claude
setup denial and real-host/clean-install acceptance gates remain open.

See [the verification record](../implementation/bounded-sync-catchup-verification.json)
and [cross-host setup](CROSS-HOST-CONTEXT-SYNC.md).
