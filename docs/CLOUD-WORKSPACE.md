# Your cloud workspace

The cloud agent works from one private workspace owned by your verified Google
account. It combines supported visible chats you chose to sync, authorized agent
message threads, working context published by your agents, and previous cloud
results. Subscription sign-in provides model access; it does not import web-chat
history or enable transcript sync.

Open [Your work agent](https://34.27.253.220/work-agent) or use `run_cloud_task`.
Ask a concrete question, such as “Check the release discussion and ask my build
agent whether its tests passed.” The cloud agent reads available evidence and
can consult another connected agent on your account. A consultation waits
without repeatedly running a model, then resumes when the addressed agent
replies to that exact message. An accepted delivery is separate from an answer.

## Context folder and retrieval (0.4.14 candidate)

The prepared update gives each cloud turn a read-only `/context` folder:
`INDEX.md` links complete conversations in `documents/`, while `manifest.json`
retains source provenance and `sections/` retains citation chunks. A SQLite
full-text index ranks relevant conversations without running an AI consolidation
step. The answering model interprets the retrieved source text.

The agent can browse, search and read through scoped tools. Search supports
ranked keywords, quoted phrases, word prefixes, and project/source/capture-date
filters. Literal search handles exact code strings and punctuation. Results
include original excerpts and offsets for reading surrounding context. Updates
publish complete snapshots atomically; subsequent turns see the refreshed files.
The Library includes these search controls and surrounding reads. Agents →
Setup status shows model access, worker health, sync choice and context separately.
Connection-check answers do not count as work context. The candidate remains
pending deployment; use the [local environment](LOCAL-DEVELOPMENT.md) to test it.

## Freshness and scope

The companion checks supported sources while the host is awake and connected.
The server refreshes the workspace in the background; each model turn uses a
consistent archive snapshot and can read the live agent board through MCP.
A sleeping or offline device contributes its last synced context and cannot
perform new native actions. A sleeping Conductor workspace must resume before its
receiver can deliver queued messages. Unsupported or unsynced conversations remain absent.

Archive reads are paginated. The cloud agent can retrieve complete available
text without putting every conversation into every prompt. Source capture times,
revisions, and read receipts support citations. Hidden reasoning, credentials,
and unrelated accounts are excluded. Recognized-secret filtering cannot detect
every sensitive detail embedded in visible prose.

Your chat exclusions, account boundaries, active cross-person grants, and native
bindings continue to apply. Another person's shared messages do not grant access
to that person's private history. Incoming agent messages are evidence and cannot
expand the owner's authority or disclosure limits.

## Execution and delivery

Model work uses an explicitly connected ChatGPT subscription in an isolated,
pinned container. There is no automatic API-key billing fallback. The model has
read-only archive tools and task-scoped messaging tools; it does not receive
reusable relay credentials or arbitrary external-action tools. Cancellation,
expired leases, and revoked access stop new network operations from that task.

A task started by an agent message answers in its originating conversation.
A task started with `run_cloud_task` is read with `read_cloud_task`. Preserve the
conversation and reply identifiers when answering a native consultation. Ordinary
replies do not request automatic acknowledgments.

## Updating

Install 0.4.13 using your host's supported plugin manager, keeping only one alias
enabled. For Codex, verify the release SHA-256, extract to a permanent folder,
and run its bundled Node with `server/configure-codex.mjs` from the existing chat.
Refresh that chat's MCP connection if the host still has an older process loaded.
`setup_status` should report 0.4.13 and runtime revision 45 while retaining the
same account and native binding. The update preserves existing sync choices.

The known Conductor Mac execution-binding regression remains a host limitation.
See [production verification](PRODUCTION-READINESS.md) for checks actually run;
plugin installation alone does not prove delivery or a completed cloud task.
