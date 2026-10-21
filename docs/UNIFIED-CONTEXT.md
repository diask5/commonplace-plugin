# Unified personal context — 0.4.14

All connected agents can query the same owner-scoped archive using
`list_shared_context`, `search_shared_context`, and `read_shared_context`.
These tools include imported ChatGPT conversations, collected native transcripts,
agent messages, published context, and previous cloud results. They start no model.
Preserve the returned revision when paging; a changed snapshot requires restarting
the read. The cloud model uses the same projection and citation checks.

## Collection and identity

With the owner's existing sync choice enabled, each companion discovers supported
Claude, Desktop Code and Codex transcript folders, including visible child-agent
results. Conductor collectors preserve the actual host conversation identity.
Cloud capture checkpoints a host message cursor and publishes bounded increments;
collection runs independently of message delivery. No native execution identity
is synthesized or moved.

The relay stores conversations by verified owner and provider conversation ID.
Known Conductor/native identity aliases join replicas transactionally. Native
message IDs retain branches; records without IDs use a source-local position.
Unknown identities remain separate rather than merging unrelated conversations
on their wording. Equivalent bodies do not silently collapse distinct messages.

Collectors persist the exact next batch before sending it and advance the file
cursor only after acknowledgement. If a local checkpoint is lost or restored, a
device-scoped revision lookup restarts collection without exposing another
installation’s metadata. Large visible messages are split at stable
boundaries. Pending pieces survive process restarts. Files are visited fairly in
bounded batches. Append-only files use byte cursors; rewrites and periodic audits
rescan the visible records. Partial lines wait for completion. Unreadable or
oversized records are reported as partial, never as successful complete capture.

Each message has a source version. Newer edits supersede stale replicas. Different
bodies at the same version remain visible with a conflict marker. Explicit
message deletions retain a tombstone so an offline replica cannot resurrect the
old text. Missing cached files only mark a replica unavailable; absence from a
cache does not prove deletion of the original conversation.

Upgraded collectors associate their old device/path sources with the canonical
conversation. Retrieval hides those duplicate legacy copies. Other legacy
sources remain readable until their installation upgrades.

## Coverage and project views

The Working context panel and `context_sync_status` show collected conversations,
replicas, capture times, backfill, partial sources, conflicts, and connected agents
without collected history. Follow both pagination cursors to inspect the inventory.
The library reads and deletes canonical conversations alongside existing imports.

Assign a project in the coverage panel or with `configure_context_source`.
`read_project_context` exposes source-attributed `Decision:`, `Task:`, `TODO:`,
`Status:`, `Blocker:`, and `Question:` statements. Different `subject = value`
statements are returned as disagreements. These are transparent extracts, not
model-invented facts or a guarantee that the last statement is authoritative.
Follow nextOffset, then nextAfter, and read the cited conversations for context.
The cloud agent has these coverage and project tools too.

## Privacy and lifecycle

An owner-requested canonical exclusion erases its collected message text and
blocks all replicas and legacy aliases. Restoring advances an epoch and requires
a fresh collection; stale queued batches cannot silently restore excluded text.
Native-agent history exclusions also remove their canonical projection. Account
changes discard local pending upload state; different Google identities remain
separate private collections. Revoked devices and moved native bindings cannot
supply evidence. Citation validation rechecks access after a cloud model turn.

Only displayable user and assistant text is collected. Hidden reasoning, tool
payloads, credentials and neighboring settings are excluded. Secret recognition
is best-effort; it does not detect all sensitive prose.

A sleeping computer or suspended workspace cannot collect new local text.
Previously synced evidence remains readable. Conductor's exact-session wake path
still depends on its supported host delivery behavior; a queued message is not a
running chat. ChatGPT web history still requires an export import. Files,
attachments and unsupported hosts require their own explicitly authorized source
connectors. This release does not claim universal capture of every application.

## Rollout

Apply additive migration `0040_unified_context.sql` with the existing verified
backup/rehearsal deployment procedure. Upgrade the plugin to 0.4.14, runtime 47,
using its supported manager or the verified Codex bundle. Existing accounts,
chat bindings, host permissions and sync choices remain unchanged. No new
subscription or Google sign-in is required for an already connected installation.
