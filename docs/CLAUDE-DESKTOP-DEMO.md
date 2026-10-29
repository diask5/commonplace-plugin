# Claude Desktop demo — 28 October 2026

The owner requested actual Claude Desktop footage, automatic information sync,
sharing rules, real messages, private withholding and revocation, with natural
Bland narration. The native video uses the recovered real window recordings, with close-ups,
anchored callouts, captions and seven chapters of Bland River narration.
The 2:47 export passed full-stream decode, audio-level checks, chapter seeking,
HTTP range playback and desktop/mobile layout checks.

[Watch the native walkthrough](https://kyle-cloud-w3.conductor.show/walkthrough/?v=3)
(requires Conductor access), or
[download the MP4](https://kyle-cloud-w3.conductor.show/walkthrough/meet-proxy-p0-walkthrough.mp4?v=3).
The 1080p master is `.context/claude-desktop-demo/public/meet-proxy-p0-walkthrough.mp4`.
The earlier browser-only video remains separately preserved.

## Observed native results

These are production account/native-host operations with fictional project data,
using the owner's two selected accounts. They are not a clean-install or an
independent real-person onboarding test.

- Claude Desktop 4.29.0, installed Meet Proxy 0.4.31/runtime64.
- A new native source chat recorded the fictional Larkspur Beacon plan and its
  correction from November 5 to November 12, 2026. Eden Hart remained owner;
  keyboard accessibility review caused the delay; time/timezone stayed undecided.
- A separate fresh Desktop chat retrieved the automatically collected source
  through `search_shared_context` and a successful `read_shared_context` at
  revision 6304. It returned the updated facts with citations from that read.
- The new accepted connection received a real question from the selected second
  account. The native Claude read the source and sent a correct concise answer,
  without source titles, IDs or private text. The reply reached the requester.
- A follow-up stayed on the same link and correctly reported the missing time
  and timezone. It identified only the documented remaining work.
- A question asking for the fictional private budget and audit marker received
  a refusal. Neither private value appeared in the answer.
- The requester disconnected this demo link. Both a subsequent read and a new
  question failed with HTTP 404, `Inbox conversation unavailable`. This is the
  observed immediate revocation result, not proof of a retained post-revocation
  audit view.

The first setup had two host-denied attempts before the denial was observed,
followed by the owner's explicit one-time approval and successful acceptance.
There was no saved permission edit or Auto-mode change. The native agent also
created a scoped memory while confirming the demo mandate; this was not requested
by the recording agent. Do not describe setup as a single clean first attempt.

## Sharing-rule result and repair

A separate two-member space, `Larkspur Beacon · Desktop demo`, was created in the
real browser. The owner saved a narrow public-launch policy, explicitly enabled
for 14 days. The browser's request checked the owner's library and **withheld the
public sample too**. Owner-only checks recorded failure to reach the unchanged
99.5% threshold. This did not become a successful library-sharing demonstration.

Investigation found that Claude's `api-request-blob` records were accepted as
visible user messages because their nested message had role `user`. These host
records contain reminders and duplicates of visible user text. The source-only
43rd portable patch now rejects nonconversation record envelopes, including
wrapped message arrays. Both collector formats reparse existing sources; an old
pending upload is reconciled without replaying its old text. Account identity,
permissions, classifier thresholds and disclosure rules are unchanged.

The cleaned-text classifier diagnostic still scored the public example below the
threshold (0.993939 vs 0.995), and withheld the private example (0.000766).
A separate short public answer excerpt passed a diagnostic at 0.996813,
which supports investigating narrower excerpts. This was not a production request.
The parser repair therefore does **not** establish that useful library sharing is
fixed. It is not installed, packaged, published or deployed. The final core suite passes
598/598, with no skipped tests; patch replay reproduces all seven changed files.

The separate sharing space was subsequently cleaned up through its real browser
UI. Saving the paused policy returned “Saved. New requests are off. Previously
shared excerpts stay in the space.” Removing the selected second member returned
“Removed from the space.” Only the space owner remains. These actions were
recorded in the fifth take; the revoked direct link and this space are distinct
scopes.

## Recording recovery and edit

Conductor temporarily lost the Mac execution binding after an incoming native
reply. No alternate execution route was used; a later owner message restored
access. The earlier long-running transfer hit the tool's 300-second timeout.

The original Swift recorder's background timer also failed to stop reliably.
One native take continued for approximately 8.7 hours. Its window-only MP4 was
finalized with macOS's visible “Stop Recording This Window” control before the
process was terminated. Only the initial 420 seconds were exported for editing;
the long original remains private on the Mac. The browser take was readable at
126 seconds. The source, retrieval, rules and messaging exports were recovered,
transferred in bounded chunks, and hash-checked. No full-display take is used.

A revised recorder uses a main run loop, a wall timer and graceful SIGUSR1 stop.
Its eight-second probe and 65-second cleanup capture both finalized successfully.
A final Mac process check found no active demo recorders.

The edit uses real recorded frames at normal speed, with ordinary cuts to shorten
waits and close-ups to make text legible. It does not recreate the assistant UI,
replace failed results, use slide scenes, or extend takes with frozen frames.
Unrelated browser sidebars are cropped out. Narration explicitly distinguishes
native conversation answers from the still-failing automatic library gate.

Source footage and audio remain under `.context/claude-desktop-demo/`; the five
Mac takes are under `~/Movies/Meet Proxy Desktop Demo/`. The original full-display
captures and overlong native original remain private, outside the served files.
The supplied Bland credential is never included in the player or media.

See `implementation/claude-desktop-demo-verification.json` for media, playback,
cleanup and release-state evidence, and
`implementation/visible-transcript-envelopes-verification.json` for the separate
source-only parser repair. This is not evidence that every P0 gate passes.
