# Live search index reuse

**Published and live: server `20261026-live-index`, with all 159 files verified.** Native 0.4.27/runtime60 is unchanged.

Ordinary questions still timed out after registration recovery: an archive change
made each search reconstruct the full text index. The runtime60 benchmark passed
three cases, fell short on three and left two unstarted. Those results remain in
[the original evidence](../implementation/registration-recovery-native-benchmark.json).

The server now copies a verified prior index and updates its changed documents.
It still captures the complete current authorized projection. Search ranking,
pagination and snippets match a fresh index, and source/authority/revision/expiry
changes still withhold results. A damaged or retired base falls back to a fresh
build. Derived indexing happens after the database read transaction commits.

Private scratch indexes live outside published generations and are removed when
the query finishes. Archive cleanup reclaims a crashed process's scratch, using
Linux process start ticks to distinguish reused PIDs. Published files and primary
database durability are unchanged.

One isolated probe on the production machine compared identical results across
the 35 MB archive: full indexing took 8.242 seconds; index reuse took 4.500 seconds,
reusing 372 documents and updating one. This sequential sample does not establish
end-to-end performance under concurrent collection. The earlier model failures
remain open until a fresh installed-host benchmark succeeds.

[Verification and hashes](../implementation/live-index-reuse-verification.json)
track source, packaging, deployment and behavioral evidence separately. Patch32
follows registration-recovery.patch; no prior release artifact is overwritten.

All 580 core tests pass with no failures or skips. The complete 32-patch replay
reproduces the source exactly. The code-only deployment preserved the migration
set; web, runtime worker and nginx are active. The eight-case installed-host
benchmark finished with four rubric passes and four failures requiring review. Three
Claude answers cited a source seen only in search because supporting reads restarted;
one Codex case could not retrieve an answer. No permission denial occurred and saved
configuration stayed unchanged. The 69.79–192.24 second cases still had tool timeouts.
Correct facts alone do not clear grounding or performance gates.

[Sanitized model evidence](../implementation/live-index-reuse-native-benchmark.json)
preserves all eight results. Browser acceptance and default-host routing remain
distinct gates. The next server candidate removes unnecessary idle cloud indexing.
