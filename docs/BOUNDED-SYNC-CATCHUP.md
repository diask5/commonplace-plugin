# Bounded catch-up for long conversations

31 October 2026: **0.4.33/runtime66 is now active on the owner's Mac**, and
the persistent background launcher points to 0.4.33. The supported upgrade guard
accepted the transition without forced companion signals; account and saved
permissions were preserved. No new source, package or server release was needed.

The initial check found an older loaded 0.4.15 process running runtime49,
background startup still pointing to 0.4.32, and all 12 earlier upgrade retries
exhausted. Why the previously observed runtime65 stopped is not established.
At that check, 194 of 195 recorded sources were complete and one long Conductor
conversation was continuing without a source error. After activation, runtime66
used six slots for continuing chunks; all 195 discovered sources became complete,
discovery and collection reported no partial coverage, and the sync error cleared.

Two fresh visible texts were successfully read from production at archive
revisions 6603 and 6604. Both searches followed empty phrase-search pages through
cursors 500 and 1000. The second text was posted after activation. Only marker
checks, counts and citation metadata were retained; no private transcript or
credentials are in the evidence. These observations prove current collection on
this configured Mac, not every-host onboarding, a latency guarantee or reboot
acceptance. Cross-person sharing reliability and the prior Claude setup approval
remain open. See [activation evidence](../implementation/context-upload-activation-verification.json).

The 29 October implementation and deferred-activation record below is retained
as history; the 31 October observation above supersedes its active-runtime status.

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

On 29 October, native **0.4.33/runtime66** was published and installed in both permanent
registries. The actual companion still ran runtime65: two normal activation
attempts deferred, and the same restart endpoint returned 45 active-work
responses during a bounded wait. No signals or force path were used. A bounded
retry (at most 12 attempts, 45 seconds between attempts) was scheduled on the Mac;
activation was then unverified. Server
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
