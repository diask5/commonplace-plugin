# Context-sharing MVP rollout — 26 October 2026

Production is running **0.4.20 / runtime 55**, release directory
`20261026-context-0.4.20`. Open https://34.27.253.220/ for the real application.
The main navigation is Spaces / My context; every space has Messages, My sharing
rules and Members. The original agent-pair surface remains at `/work-agent#agents`.

The [published release](https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-v0.4.20)
contains both plugin aliases, their checksums/build manifests, and the server overlay.
Enable only the installation's existing alias. Native app reload is a separate step.

## Verification

- 428 core tests passed; 127 full browser tests passed, including 70 current-context
  tests; the original ten-owner/twenty-agent lifecycle passed 15/15. These suites
  overlap and should not be added as distinct scenarios.
- Both ZIP aliases passed packaging checks, two extracted launcher tests, actual
  packaged stdio/API smoke, and the six-profile mailbox smoke. Google identities
  and native hosts in those checks are controlled fixtures.
- The exact 17-patch chain replays all 150 changed implementation files. The final
  completion patch changes 29 files relative to its predecessor.
- The VM's Node v22.23.2 verified the extracted MCP runtime through PKCE exchange,
  authenticated resources/tools, and denial of unauthenticated, foreign-origin
  and read-only writes using an isolated account/database.
- The actual compiled candidate served the new UI and sign-in script, discovery
  endpoints and retained `/authorize` handler (303 unauthenticated redirect).
  This check did not assert a real signed-in Google identity.
- Live Chrome at 1440px and 390px clears loading and reaches Google sign-in
  without JavaScript errors or horizontal overflow. The real Google helper becomes
  ready; four public app modules match the tested source byte for byte. No Google
  account was authenticated by these headless checks.
- All 153 deployed bundle files match their hashes. Web and runtime services are
  active with a fresh worker heartbeat.
- Stable hashes preserve all 71 profile IDs, 548 device ownership mappings,
  152 agent ownership mappings, 151 exact native bindings, seven mail-thread pair
  mappings and five installation/account mappings. No identity was relinked.

## Deployment and recovery

The exact previous release was `20261025-product-0.4.19`. An online SQLite snapshot
was pinned, copied and integrity checked, then the candidate rehearsed on a
disposable copy. The VM disk made the integrity scan take several minutes; the
first Mac command timed out while the remote check continued. Its final
`prepared.json` confirmed success before activation. No failed check was skipped.

The verified backup is retained at
`/var/lib/commonplace/rollouts/20261026-context-0.4.20-rehearsal/before.sqlite`.
After rehearsal, activation used `--code-only` and verified the exact existing
45 migration digests. The existing database and incoming writes were preserved;
no redundant second database rehearsal was needed. New policy/space tables are
additive on first use. The helper checked both services and supports restoring
the previous code pointer without restoring stale data.

The owner's supplied Perplexity key was read on the Mac and passed over SSH stdin,
never included in command arguments, source, release archives or logs. Existing
environment variables were preserved with a protected backup. The service is
confirmed to have loaded the key.

## Limits and remaining acceptance checks

A fresh 28-case real `pplx-decider-v1.2` benchmark at 0.995 yielded 23 correct,
zero false allows and five false withholds. A separate VM provider probe reached
the API and withheld both its allowed and disallowed examples. The threshold was
not lowered. These are small synthetic samples, not calibrated privacy guarantees;
useful-context recall needs further work.

Sharing currently evaluates up to six complete matching documents and withholds
documents over 8,000 characters. Upstream MCP ingestion, safe long-document
chunking, recipient-safe pagination, automatic email/iMessage delivery and P1
personal agents remain unimplemented. Explicit text/Markdown uploads work.

The fresh real Google → native app launch/host approval or reload → exact-chat
setup → automatic context ingestion → cross-person exchange walkthrough still
requires installed-host acceptance. Public sign-in readiness and fixtures cannot
replace it. This Conductor chat's old loaded MCP process reported 0.4.14/runtime48;
updating the website does not reload every native host.

See [the current spec comparison](CONTEXT-MVP-READINESS.md) and
[machine-readable evidence](../implementation/context-mvp-verification.json).
[All 14 desktop and phone screens](https://kyle-cloud-w3.conductor.show/review)
use the actual UI with clearly labeled test identities and controlled providers.
