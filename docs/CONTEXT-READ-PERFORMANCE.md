# Context read performance

Status polling scanned source-table pages containing large text bodies. The web
process also trusted a published flag written by a worker whose archive lives in
a different directory, which could make search rebuild the web snapshot before
answering. This server update adds covering indexes and checks the actual local
snapshot before selecting the fast path. Missing or stale snapshots still use
authoritative live reads. All post-read revision, source and expiry checks remain.

**State: server release `20261026-read-performance` is deployed; live requests remain slow and the real-model benchmark is incomplete.**
Native 0.4.26/runtime59 is unchanged. Migration 0045 adds three indexes without
changing rows or authority. It was deployed with a verified database backup and migration
rehearsal; older code remains compatible with the indexes.

Archive reads also load the MCP adapter only when serving MCP, skip redundant
permission writes on unchanged read-only sections, and use the small current
pointer when releasing a snapshot. Full byte/hash checks and pin protection remain.
The worker still cleans its separate archive; eager cleanup was not disabled.

551 core checks pass, with zero failures or skips. Independent review found no
blockers and passed 53 focused checks. Deployment checks pass 54 locally, with
the real-Nginx test skipped there (it passed for the preceding asset release).
30 portable patches reproduce 196 implementation files exactly. The bundle has
158 files. Synthetic warm-cache status queries improved from 9.06 ms to 0.16 ms;
these figures do not establish production speed.

[Verification](../implementation/context-read-performance-verification.json)
records hashes and activation. [Public asset delivery](PUBLIC-ASSETS-DELIVERY.md)
remains live. Real-model, citation and default-host routing limitations remain
recorded; no failed attempt has been replaced with a passing fixture.

## Live result (26 October 2026)

- Public smoke passed: 31 public assets returned 200, protocols answered as
  expected, and desktop and phone sign-in rendered without overflow
  ([desktop](images/read-performance/signin-desktop.png),
  [phone](images/read-performance/signin-phone.png)).
- The actual production status SQL improved from 0.03–0.22 s (full scans) to
  0.007–0.009 s (covering indexes). Overall requests remain slow: health took
  2.2–4.2 s, the first smoke health request 15.3 s, and unauthenticated MCP 3.3 s.
- Real-host benchmark ([receipts](../implementation/context-read-native-benchmark.json)):
  - Claude synthesis: **not passed.** Three searches took 28–30 s each, then the
    harness stopped the run when the model selected `list_shared_context`; no answer.
  - Claude unknown: **not run.**
  - Codex trust: **passed** in 126 s with search and two source reads; each call
    took 26–44 s.
  - Codex correction: **failed before any tool ran**; the provider reported the
    selected model at capacity.
- The rollout receipt verifies all 158 deployed files, active web/runtime/Nginx services, and the database backup. Warm real-request speedup and all-done readiness remain unestablished.

[Sanitized live evidence](../implementation/context-read-performance-live-evidence.json)
