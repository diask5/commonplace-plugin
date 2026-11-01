# Context upload progress under slow requests

1 November 2026. Patch 63; native candidate 0.4.39/runtime72.

## Reproduced problem and change

The live cloud collector staged this chat but left it at record 94 while new
sources kept taking the first upload slot. Each relay upload exceeded the
cooperative time slice. Interleaving fresh and continuing work only inside a
single pass therefore did not prevent starvation across passes. The heartbeat
reservation in the third slot could also go unused indefinitely.

The collector now persists the next service class with its durable pending
upload. Fresh captures, continuing captures and due retries take turns across
passes and process restarts. Fresh selection alternates newest and oldest;
overdue heartbeats receive the first slot. Exact retries, complete-capture
publication, account routing, exclusions, gzip payload bounds and server
backpressure are unchanged. No fixed six-upload cap is reintroduced.

## Evidence

Two regressions fail on patch 62 and pass with patch 63: a slow network with
constant fresh arrivals and restarts, and an upload whose acknowledgement is
lost before restarting. All 697 core tests, 34 focused collector checks and 34 checks against the
extracted native runtime pass. Counts overlap; do not add them. Exact replay of
63 patches matches all 246 changed source files. Full suite, package, install
and live collection results are recorded in
`implementation/upload-fairness-verification.json` as they complete.

The prior 0.4.38/runtime71 release, server rollout and Work connection evidence
remain in [guarded activation](OOB-ACTIVATION.md). This is a native scheduler
change; no production server update, schema change or classifier change is needed.
A first complete capture must finish before it is available in the shared context
archive. Private account collection does not opt into sharing in Work.
