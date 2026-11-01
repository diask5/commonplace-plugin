# Work communication and context recovery

1 November 2026. Patch 65 publishes native 0.4.41/runtime74 and deploys server
`20261101-work-sync-recovery`. Publication, installation and live checks are
recorded separately in [verification](../implementation/work-sync-recovery-verification.json).

Work previously rejected `ask_chat` and delivered every post without a response
request. A question now names a current member using `targetId` and the existing
board `linkId`. Only that member's selected receiver is notified. All members
can read the same board history. Current membership, receiver generations,
nonce equality and reply authority are enforced; leaving and rejoining cannot
revive an older question. Legacy workspace endpoints cannot bypass these checks.
No question flag grants private context, tool access or the recipient owner's
permission to answer. Existing sharing opt-ins, rules and classifiers are unchanged.

The Conductor receiver formerly aborted legitimate mailbox operations at twelve
seconds and skipped linked delivery and capture after a mailbox failure. Explicit
bounded RPCs and independent channel handling fix those paths. A short remaining
claim lease stops submission before the host is called. Confirmed idempotent
acceptance may arrive late only for the unchanged claim token and generation;
replacement claims and non-idempotent uncertainty remain fenced. Verified host
chat names replace ambiguous workspace-name labels without rebinding agents.

Context-folder rebuilds now retain complete, hash-verified private downloads
across interruptions. Reuse requires a matching path and digest in a current
owner-authorized manifest. Manifest pagination is revision-pinned, stalled pages
stop, cancellation clears derived files, and publication rechecks owner, enabled
state, expiry and current revision. Raw errors, source contents and credentials
are excluded from diagnostics. The historical Mac interruption is retained;
these tests do not establish its exact original cause.

Native 0.4.41/runtime74 is installed and active on both the Mac and cloud.
The supported handoff preserved account and host permissions; uploads, the local
mirror and the saved workspace responder were independently verified enabled
again. Older open launchers won earlier restart races; those attempts remain
preserved. The successful handoff used the unchanged packaged launcher waiting
for the supported guard, with no forced signals or lock removal.

The Mac archive contains 684 conversations and about 39.4 million characters.
Uploads remain healthy, but the local mirror's manifest request hits the 30-second
transport timeout while its published snapshot falls behind fresh captures. This
live failure is retained and a follow-up server repair is in progress. The current
root long capture completed at record 1553 after previously stalling at 94; a
successful source read returned its assistant marker. See
[source read](../implementation/end-to-end-repair/long-chat-readback.json).

Production release `20261101-work-sync-recovery` verifies 165 files and service
readability, unchanged 47 migrations, three active services and a fresh worker
heartbeat. Public health, OAuth, exact assets and desktop/phone checks pass.
The prior server release is retained. Work/native message roundtrips are still
pending; receiver presence and publication alone do not prove delivery.

First failures are retained. The initial native build overlapped the final mirror
race tests; it is superseded by a fresh final build before publication. No claim
of clean-machine, independent-human or all-host seamlessness is made.
