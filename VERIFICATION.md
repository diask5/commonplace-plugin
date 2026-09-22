# Commonplace 0.2.7 verification

This release adds invitations connecting two selected existing native chats, plus visible `/commonplace:invite` and `/commonplace:session` commands. The local Desktop and hosted SSH launchers are byte-for-byte unchanged from 0.2.6. Memory automation remains removed.

Verified on Windows on September 22, 2026 (UTC):

- The new packaged regression failed against 0.2.6, confirming that its invitation schema and session binding were missing.
- **20 packaged tests passed, zero failures or skips**, covering the invitation flow, verified native identity, runtime startup, native messaging, refusal controls and removal of memory tools.
- **20 backend tests passed**, including separate links for already connected teammates, offline destination preservation, acceptance retries, stale responders and rejection of unrelated sessions.
- Two fresh packaged MCP profiles used signed Agent Auth against the live GCP service, accepted a session-bound invitation, verified the selected receivers, and completed two question/reply rounds.
- The exact packaged local launcher created a genuine named Claude session in an isolated profile with **zero inference requests**. This verifies session creation; it does not by itself verify a Desktop GUI opening.
- The matching built server passed isolated real HTTP / signed Agent Auth testing with two fresh accounts and three replies. Its additive migration was deployed with a verified database backup and existing record counts preserved.
- Claude Code's native plugin validator accepted the package.

Native messaging tests use a synthetic loopback inference provider. Live GCP checks use disposable identities. No real teammate receives test messages. The Mac collaborator separately reported an existing successful automatic **local** Desktop Code session; that is reported Mac evidence, not a fresh Mac GUI installation test performed by these checks.

Hosted SSH still opens a prepared composer requiring Desktop confirmation/submission. This release does not claim automatic executing cloud sessions, ordinary Desktop Chat/Cowork support, or a fresh physical Mac/Linux installation test.

Archive SHA-256: `95090c1322686e5d271a56d46c6ae035bea070a0658f26dce45f9733cec12dc8`.

The `v0.2.7` tag is pinned to the commit containing its matching marketplace catalog. Older 0.2.6/dev.19 tags pointed at earlier distribution metadata; immutable old tags and archives are retained. Install 0.2.7 from the current marketplace rather than an old tag.

Refresh the marketplace, update Commonplace and reload the plugin in the intended chat. Installation does not hot-reload tools already cached by an open host.
