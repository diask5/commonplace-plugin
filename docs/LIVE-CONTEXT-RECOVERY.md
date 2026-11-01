# Live context and receiver recovery

1 November 2026. Patch 66 publishes native **0.4.42/runtime75** and server
**20261101-context-recovery**. Publication, installation, activation and live
checks are recorded separately in
[verification](../implementation/live-context-recovery-verification.json).

The live Mac had 684 conversations, 13,694 sections and approximately 39.4 million
characters. Uploads advanced the archive while the local folder waited for a full
filesystem and search-index build. A signed manifest request timed out after
30 seconds before any file download. The original failure is retained.

Mirror manifests and file pages now read the current authorized source projection
in bounded workers. They avoid building filesystem files or a search index.
Metadata is cached by owner, revision and expiry; source bodies are not cached in
that metadata. File slices, response sizes, worker concurrency, queue limits and
final revision/authority checks remain bounded. A projection digest lets the new
native client establish exact equality after metadata eviction, including grant
expiry that does not change the database revision. The 64 MB document limit is
checked during reading; observation timestamps reflect included source metadata.

A second live failure involved old loaded plugins overwriting a current native
receiver's capability and verified chat name. Expiring registration metadata now
protects the exact device, session, provider and binding generation from older
writers. An old heartbeat cannot renew that protection. Tool arguments cannot
supply its provenance. Launcher startup is serialized and confirms the actual
receiver revision, with bounded retries if an old launcher wins the lock.

These changes do not grant access, move agents, merge accounts, change sharing
rules or classifier settings, or bypass host approval. There is no migration.
The previous native and server releases remain preserved.

Independent review reproduced and closed a cache-eviction retry loop, an expiry
case involving two installations, late size validation, and an epoch-zero source
timestamp. Runtime75 passes 150 mirror/archive checks; registration/receiver
repairs pass 108 related checks, with five regressions failing before and passing
after. Independent reviews pass 57 projection and 72 transport checks. These
counts overlap and must not be added. The full core, artifact and deployment
checks are recorded in the verification file.

The final synthetic scale run uses the same document/section/character counts as
the observed Mac archive. It measured approximately 1.49 seconds and 73 MiB peak
RSS for manifest projection, and 0.25 seconds for a selected 57,600-character file.
Those are source-test measurements, not production throughput.

The projection handshake requires the new companion for reliable progress under
metadata eviction. An unchanged 0.4.41 client still fails closed in that case.
Continuous uploads can still require revision restarts. Remote MCP cannot collect
web-only chat history. Source tests and service health do not establish completed
Work replies or all-host, clean-machine, independent-human readiness.

Both native aliases are published; distribution PR #69 is merged. Both the Mac and cloud now run companion75 with accounts and permissions preserved. The server rollout verifies 166 readable files and unchanged 47 migration digests. Public health, OAuth, asset and desktop/phone browser checks pass. These live results are distinct from the source tests above.

The Mac mirror cache progresses, but its first full publication remains pending. A fresh 0.4.42 native chat read another same-account agent’s published Personal progress and published its own; the earlier chat’s actual final assistant sentence has not yet appeared in saved archive reads. Incoming native roundtrip and Work reply tests are deliberately deferred until Mac-dependent deployment work finishes, because earlier incoming messages invalidated this chat’s Mac execution binding.

Production throughput remains under repair: repeated localhost health requests took 5.5–9.5 seconds while the main process waited on filesystem commits. Synthetic investigation found 16 WAL commits per empty receiver cycle; this does not conclusively attribute the live delay. Original evidence and published artifacts are retained.
