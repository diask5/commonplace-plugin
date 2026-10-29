# Automatic context setup — 25 October 2026

This describes the original setup implementation. It shipped in 0.4.20 and is
included in the current **0.4.27 / runtime60** plugin; [registration recovery](REGISTRATION-RECOVERY.md) records the live server, installation and benchmark state.
The [current P0 readiness record](P0-NATIVE-READINESS.md) records installation, deployment and
actual read receipts. Earlier validation and release prerequisites below are
historical; fresh Google consent and every native app launch remain separate
live acceptance checks.

The flow replaces optional collection and manual chat selection with one app
setup sheet.

## User flow

1. Sign in with Google. New users without an attached chat are offered setup;
   accepting a space invitation retains that destination.
2. Click **Open in Claude**, **Open in Codex** or **Open in Conductor**. Each card
   directly opens the app with a complete installation request; there is no
   separate select-then-open step. “Add context” opens this sheet directly.
   The next view prominently shows **Copy setup prompt**, with instructions to
   paste into that app and send. If the app already contains the request, just
   send it. Manual prompt review and download links live under troubleshooting.
3. Send the setup request in the desktop app. It authorizes plugin setup,
   automatic private collection and the exact selected space receiver. Existing
   source exclusions remain in force. The host can still require approval or a
   reload, and a different account/server must be preserved and reported.
4. The plugin calls `finish_context_setup` with the private browser handoff.
   Browser sign-in carries across, so there is no second Google ceremony. The
   service binds the actual host-supplied chat; no chat picker or synthetic native
   identity is involved. A later receiver change invalidates an older setup.
5. The browser checks every 2.5 seconds and shows **Set up plugin & MCP → Sync
   your context → Ready**. Account binding is included in the plugin confirmation,
   not a separate user step. Checks resume when the page becomes visible or
   reconnects. Opening an app never completes a step.
6. The companion scans supported visible histories every 5 seconds while online;
   the context library refreshes every 5 seconds while open. New data is indexed
   as complete captures arrive. These are polling intervals, not a latency SLA.

Collection is private to the account. Space membership and setup do not enable
personal-context sharing rules or publish any private transcripts to members.
Per-member sharing rules still govern context requests. Existing advanced pause
and source-exclusion APIs remain; the primary flow has no sync checkbox. An
idempotent setup retry cannot undo a pause performed after the first claim.

## Real progress, not an installation animation

The authenticated browser creates a 30-minute, single-use handoff. Only its hash
is stored by the service. The native adapter supplies the real session and
loaded plugin version; the browser cannot nominate a fabricated session.
The token is carried privately in the desktop setup prompt, never a public web
URL or a status response, and both collector/import sanitizers remove it.

Registration confirms installation and account binding. Collector reports contain
only an allowlisted state, timestamp and count. Actual canonical upload receipts
from that installation confirm incoming context. A ready archive plus eligible
published messages confirms searchability. Separate Agent Auth scope credentials
are recognized as the same installation without mixing another computer’s data.
Progress never includes transcript bodies or private file paths.

Offline, partial, interrupted, paused, empty and expired states are explicit.
Previously indexed context remains usable while a computer is offline; this does
not imply all sources are current. The timeline says when it is waiting for a
collector or indexing, and provides recovery for expired setup. Delayed responses
are fenced when the app/account changes or the dialog closes.

New lazy-created tables: `cp_context_setups` and `cp_context_collectors`.
Existing conversation identities and sharing-policy tables are unchanged.
The deployment overlay now includes all browser assets, fonts and licenses,
as well as the new backend module. No published package was overwritten.

## Validation and remaining live gates

The handoff/backend changes are recorded in
`implementation/live-context-setup-verification.json` and its manifest. The
direct app-launch refinement is preserved as the 15th patch,
`implementation/seamless-plugin-setup.patch`, with its own verification and
source manifest. The two records distinguish their test runs.
The 16th patch, `copy-setup-prompt.patch`, promotes the copy action above live
progress after app selection. Its own manifest and verification record this
small follow-up; the action recedes once native registration is confirmed.

The native integration test uses a real signed installation and MCP tool call,
then a real filesystem transcript collector, authenticated upload, canonical
archive and search/read handlers. It appends another visible message and verifies
that the next collection cycle exposes it. Test identities and data are synthetic;
this is not evidence of a real Google or operating-system app launch.

Browser tests cover live step transitions, no false completion from other chats
or older account data, empty/error/offline collection, expiry, owner changes,
resuming a private handoff, accessibility and 320/390/768/1440/1920 layouts.
The remaining UI suite covers sharing, invitations and the message board.

## Plugin and MCP installation in one request

Each app gets a prepared private handoff before the click, preserving the browser
gesture required for an app launch. Preparation has a visible waiting state and
retry. Clipboard copying is attempted on the click, and a prominent **Copy setup
prompt** button remains available above progress until connected. An unavailable clipboard
leaves a selectable request in troubleshooting. Reopening uses the same handoff
until it expires. Switching apps cannot inherit a delayed confirmation from the
previous app, and account changes invalidate links even before the first launch.

The request checks existing setup first and skips installation when the required
tool is loaded for the correct account/server. Claude's plugin includes its MCP
server; the prompt uses the supported plugin manager and prevents a duplicate MCP
entry. Codex's bundled helper configures MCP while preserving settings. Conductor
uses the path for its actual Claude or Codex provider. The user still sends the
prepared request and completes any host-required approval or reload.

Official documentation checked on 25 October 2026:

- [Claude plugin installation](https://code.claude.com/docs/en/discover-plugins):
  marketplace/install commands, included MCP servers and host reload behavior.
- [Claude Desktop Code](https://code.claude.com/docs/en/desktop):
  `claude://code/new?q=…` fills the prompt; it does not prove submission.
- [Conductor MCP](https://conductor.build/docs/reference/mcp): uses the provider's
  MCP configuration rather than another Conductor-specific configuration.

Official Codex app/MCP pages returned redirect errors during this check. The
existing Codex and Conductor app links remain best-effort and have a copy fallback;
their OS handlers have not been verified on a Mac in this change.

Original release prerequisites (publication and deployment are now complete):

- Publish a new plugin version exposing `finish_context_setup`; release 0.4.19
  does not contain it. The generated request reports this missing capability
  rather than claiming an old installation completed the new flow.
- Deploy matching account runtime and browser modules; configure real Google.
- Verify app URL handlers and the host install/reload flow on an actual Mac for
  Claude Desktop Code, Codex and Conductor. Links remain best-effort with a copy
  fallback; browser tests verify their construction, not OS acceptance.
- Exercise fresh sign-in → native registration → actual history collection →
  group context request with the release. Native message wake/reply is separate
  from context availability and is not certified by this setup timeline.

Supported visible work histories only: web-only chats, arbitrary repositories,
attachments and upstream MCP sources are not automatically collected. Existing
large-document sharing limits and classifier calibration work remain unchanged.
