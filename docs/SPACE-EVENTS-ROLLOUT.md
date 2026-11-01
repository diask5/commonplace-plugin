# Space events and continuous sync production rollout

1 November 2026: server **20261101-space-events** is live at
[Meet Proxy](https://34.27.253.220/). Native **0.4.37/runtime70** is published in
both plugin aliases, and the default distribution branch points to the verified
archives. This includes patches 57–61: contextual invitations, multiple-account
profiles, compressed uploads, common Space events and continuous catch-up.

The earlier Mac execution rejection remains in the historical reports. On the
owner's new explicit deployment request, the Mac execution tool succeeded and
the existing Google Cloud login reached the production VM. No new login, account
link, host permission or classifier setting was needed.

## Server verification

The rollout pinned and verified all 160 files of `20261031-setup-activation`,
then verified the new 165-file bundle. Existing migration digests are unchanged;
`0046_personal_space.sql` is the only addition. The full deployment path took a
verified SQLite backup and rehearsed migration plus integrity checks on a copy
before switching production. The backup and prior release remain on the VM.

Activation succeeded in 484.58 seconds. All 165 live file hashes and service-user
readability checks pass. All 47 migrations have the expected digests. The web,
worker and nginx services are active, and the worker wrote a fresh heartbeat
after startup. HTTPS certificate verification, public health, OAuth discovery,
unauthenticated MCP rejection and seven deployed browser assets pass. Desktop
and phone login pages show no JavaScript errors or horizontal overflow.

## Native distribution and activation

Source PR [#56](https://github.com/diask5/commonplace-plugin/pull/56) merged into
`main`. Distribution PR [#57](https://github.com/diask5/commonplace-plugin/pull/57)
merged into `codex/plugin-distribution`; the repository default remains unchanged.
Both published ZIP digests match the reviewed packages. The unrelated
`commonplace-files` entry remains unchanged.

Mac installation passed: Claude's supported plugin manager reports 0.4.37,
Codex points to the verified 0.4.37 package, and its configuration changed only
the plugin paths. Account and saved permissions were preserved.

Runtime activation remains incomplete. All 12 bounded calls through the supported
upgrade path deferred. A direct authenticated check confirmed HTTP 409:
“Commonplace is finishing active work before updating.” A bounded maintenance
pause through the existing collection control did not clear that guard. The prior
enabled setting was restored and verified; no forced process signals were used.
Runtime66 remains responsive, and its persistent launcher remains 0.4.33. The
retry process has finished; no further retry is claimed to be queued.

After restoration, the collector reported 197 discovered files, no partial
coverage, no collection error, and a new successful sync timestamp. Conductor
reported 49 conversations across four discovered transcript roots. These are
observations of the configured Mac on runtime66, not evidence that runtime70 is
active or that another work machine's full library was collected.
Open native chats can retain an older loaded plugin even after the companion
updates; a new chat or the host's supported activation controls load new tools.

## Scope and retained limits

The candidate evidence remains unchanged: 685 core tests, 41 browser/probe
checks, 19 focused recovery/cross-host checks, 17 extracted-native checks,
both-alias integrity, and exact 61-patch replay across 242 changed files.
The synthetic 6,722-file benchmark demonstrates reduced scanning and scheduling
overhead, not live network throughput.

Events are authorized references with durable cursor recovery. Notifications do
not guarantee that a host starts a model. Shared Spaces still apply the existing
classifier rules; Personal is account-private. No live notification wake,
universal transcript coverage, clean-machine onboarding or all-P0 readiness is
claimed. Unsupported web-only history is not collected automatically, and prior
false withholding and sharing acceptance limits remain open.

The first signed production smoke command exceeded its 60-second host timeout
without a final receipt. The continuation first reconciled existing spaces and saved completed actions.
Signed production event reads, pinned cursor replay, duplicate-free resumption,
activity reads, Personal invitation refusal, unknown-space refusal and archived-
space refusal all passed. The disposable space was archived. The initial timeout
is retained. No private transcript or classifier input was used by this smoke check.

See [rollout verification](../implementation/space-events-rollout-verification.json),
[Space events](PERSONAL-SPACE-EVENTS.md), and
[continuous sync](CONTINUOUS-CHAT-SYNC.md).
