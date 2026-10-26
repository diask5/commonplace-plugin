# Automatic collection and one context library

Source follow-up, 25 October 2026. This change is implemented and available in the
interactive preview. It has not been released, installed or deployed. The
existing account connection and production 0.4.19 packages are unchanged.

## User flow

Open **Context → Add context**, connect Claude Code or Codex on each computer,
and enable **Automatic chat sync** once for the account. The same saved choice
controls Settings. It applies to supported chat transcripts on connected
installations, including supported Desktop Code and Conductor histories.
The companion continues collection while online; collection starts no model.

Enabled, locally configured Claude/Codex transcript folders now join automatic
discovery alongside standard locations. Disabled sources, remote-device source
records, symlinked folders, repositories and document folders are not implicitly
added to chat uploads. An inaccessible source is a coverage gap; accessible
sources can continue. Existing conversation exclusions remain enforced.

The companion checks approximately every five seconds and works through bounded
batches. Backfill duration depends on the archive size and source availability.
The Context screen refreshes visible collection status and changed library
snapshots every fifteen seconds. These intervals are not completion guarantees.

## Combining the context

All supported sources feed the same private account archive and keyword index.
Real conversation identities reconcile known replicas across devices. Separate
conversations keep their IDs, source text, timestamps and citations; conflicting
source versions stay visible. Similar wording or matching person names does not
merge conversations.

Native session metadata supplies project labels where available, including
Windows paths. The relay and local mirror generate a project-grouped `INDEX.md`;
the relay's `WORKSPACE.md` has the same catalog. Project labels organize links to
the original documents across providers. A matching project label is not proof
that two conversations or claims are equivalent. Search and project filters
continue to retrieve original evidence. No model, embeddings or generated
summary is required for collection or indexing.

## Reliability changes

- Large JSON histories keep one capture ID across batches and process every
  message. Restarts resume the same capture; changed exports restart from the
  first turn. Incomplete replacements do not replace previously complete text.
- Collector format 2 performs a repair scan for older checkpoints, preserving
  exact pending retries, revisions, exclusions and account boundaries.
- Metadata-only records no longer create a file identity before the native
  session ID arrives. JSON wrappers retain their session and project metadata.
- Hidden analysis phases and hidden envelope fields are excluded in addition to
  existing reasoning/channel/tool filters. Recognized-secret filtering remains
  best effort; it cannot identify every sensitive statement.
- Collection status includes canonical uploads, rather than counting only the
  older upload table and manual imports. It filters excluded sources, revoked
  devices and installations that have changed account bindings.
- New context appears in an open library without reloading the page. Opening a
  source can retry a changed snapshot; continued document pages retain their
  own revision and cannot mix old and new source text.
- Local catalog upgrades rebuild the index without downloading unchanged files.

## Boundaries and remaining connectors

Automatic sync is private ingestion, not sharing with another person. The
selected-document sharing backend is still pending. No existing account's sync
choice is silently enabled by installing this source change.

ChatGPT web history still requires an export import. Web-only Claude history,
arbitrary repositories, Drive, PDFs and other attachments are not automatically
collected by this change. They need supported source connectors and appropriate
access. No browser-session scraping or whole-home-directory scan was added.

The loaded plugin in this development chat reported a cached
`kyledias@vurbox.com` connection and version 0.4.14. The owner previously selected
`diaskyle10@gmail.com` for the combined archive. No live account switch or sync
mutation was attempted. Live collection into that chosen account needs the
correct installation/account and release activation; fixture tests cannot prove
its current upload coverage.

## Reproduction and evidence

Apply `implementation/automatic-context-ingestion.patch` after the existing
six-patch chain ending in `context-product-ui.patch`. The manifest records the
base and every before/after digest. A separate checkout replays all seven
patches and matches the changed source files exactly.

Tests exercise actual local collector, signed relay, SQLite storage, archive,
MCP retrieval and local mirror components with disposable accounts. Browser
tests exercise the real UI and HTTP handlers with fixture accounts, including
sync failures, background updates, account isolation and four viewport widths.
See `implementation/automatic-context-ingestion-verification.json` for exact
results and limitations. Logs and screenshots are in `.context/auto-ingest/`.

Final verification: **385/385 main-suite tests and 81/81 UI tests passed**, with
no skips. The MCP build passed. All 17 changed files match the seven-patch replay.
