# Events are the common Spaces contract

1 November rollout update: this work is included in published native **0.4.37/runtime70** and live server **20261101-space-events**. The earlier candidate and access-block records below are historical. See [current rollout evidence](SPACE-EVENTS-ROLLOUT.md) for publication, installation and activation separately.

The owner clarified that events are fundamental to every Space. Personal is the
private default space for a verified account, using the same group, membership,
message and change-log infrastructure. There is no separate work-board service.

A mutation creates a durable event in `cp_workspace_changes`. An explicitly
subscribed MCP client receives a URI notification, resumes `read_space_events`
from its saved cursor, and reads the referenced message, approved exchange,
document or completed transcript through the existing authorized reader. Events
and source text are data; neither grants permission to run another task.

## Delivery and recovery

- All Spaces use `meetproxy://spaces/{groupId}/events`.
- Personal additionally supports `meetproxy://spaces/{groupId}/agents/{agentId}/events`.
- `read_space_events` returns `cursor`, `through` and `hasMore`. Keep `through`
  while paging, even across an empty filtered page; omit it for the next catch-up.
- Legacy stdio uses `resources/subscribe` and `resources/unsubscribe`. Modern
  stdio and authenticated HTTP use `subscriptions/listen`, with SDK-owned framing
  and subscription IDs. Legacy HTTP can read the same durable cursor with tools.
- Notifications contain the resource URI only. The current implementation checks
  authorized change cursors every 15 seconds. It is not instantaneous database
  push. HTTP streams last at most 15 minutes; reconnect and resume the saved cursor.
- Watches stop on account/access errors and on cancellation or connection close.
  Overlapping native listeners share one watch. Capacity is bounded at eight
  resource URIs per listen and two modern listens per connection/installation.
- A notification does not prove the host started a model. Existing addressed
  messaging and its delivery receipts remain the route for an explicit request.

## Personal and shared context

Registration attaches an agent by its actual verified account binding. Automatic
native hooks post fixed connected/activity/turn-ended observations; they never
copy raw hook input. `publish_agent_context` commits useful progress to Personal
in the same transaction as its revisioned resource. A turn ending is not evidence
that its task succeeded. Supported visible transcripts stay in the existing
private canonical archive; only completed captures create transcript references.

Personal cannot invite another person. Its agents read their own account context
without the cross-person classifier. Shared Spaces emit approved-context
references; the contributor's existing rule gate still controls disclosure.
Private checks and private raw transcripts never become shared event payloads.
Membership, account selection, current generation, source exclusions and token
expiry are rechecked on the read path. Excluding agent history erases copied
Personal progress from both message storage and historical change-log bodies.

The browser retains **Spaces / My context** and the existing space header. Personal
shows agent attribution and a paginated agent roster, uses account-only audience
copy, and offers no foreign-member or private-library-sharing controls.

## Candidate evidence and release state

Patch 60 packages native **0.4.36/runtime69** and a 165-file server bundle locally.
679 core checks, 41 browser/probe checks, 16 extracted native/server checks and
12 extracted HTTP/OAuth smoke checks pass. The exact 60-patch replay matches all
239 changed files. Test accounts and data are synthetic; extracted tests reuse
the source dependency installation. The original pagination-fixture failure is
retained separately from the corrected passing run.

This candidate is not published, installed, activated or deployed. Production
remains the previously verified `20261031-setup-activation`. Rollout must include
migration `0046_personal_space.sql`; `--code-only` is invalid for this change.
The previous Mac execution block remains: `mcp__conductor__RunLocalCommand`
reported “Local execution is not enabled for this session.” It was not retried
or bypassed. No live host-notification, universal transcript coverage or all-P0
readiness claim follows from these local checks.

Machine-readable details: [verification](../implementation/personal-space-events-verification.json).
