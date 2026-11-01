# Work communication and context recovery

1 November 2026. Patch 65 prepares native 0.4.41/runtime74 and server
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

The previous Mac upgrade completed: runtime73/background0.4.40, uploads and
context mirror enabled, account and saved host permissions preserved. Its mirror
was still rebuilding. This root chat's current long capture completed at record
1553 after previously stalling at94; a successful archive read returned the
assistant marker from revision216. See [handoff](../implementation/end-to-end-repair/mac-handoff.json)
and [source read](../implementation/end-to-end-repair/long-chat-readback.json).

First failures are retained. The initial native build overlapped the final mirror
race tests; it is superseded by a fresh final build before publication. No claim
of clean-machine, independent-human or all-host seamlessness is made.
