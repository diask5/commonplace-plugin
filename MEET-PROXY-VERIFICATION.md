# Meet Proxy 0.2.9 verification

Verified October 18, 2026. This release adds scoped Chief of Staff conversations
over the existing private message board.

| Check | Observed result |
| --- | --- |
| Source tests | 89 passed, zero failures or skips |
| Beta.2 packaging | 6 checks passed, including independent identical builds |
| Stable promotion | Only manifests, advertised version and installation README change; other file bytes and executable modes are preserved |
| Real local Claude Code sessions | Both invitation flows, idle delivery and autonomous answers passed on a Mac with Claude Code 2.1.300 |
| Model disclosure boundaries | Requests for private sources and unauthorized file creation were refused; private test values were absent from shared replies |
| Production staging | Exact deployed web/auth build passed packaged end-to-end tests on a separate database |
| Database migration | Integrity-checked backup retained; migration 0024 preserved all 61 existing application table counts |
| Production deployment | Public relay is healthy; 6,893 unaffected application files matched the prior release |
| Production plugin smoke | Both grant directions, private preview, native hook, briefing separation, identical history, expiry and revocation passed |
| Existing public 0.2.8 client | Signed connection, question/reply, history and native-hook checks passed against the updated relay |

The real-agent test used host-generated session identities and actual model
calls. The owner answered incoming questions without further owner prompts.
Both agents' final tool responses matched each other and the persisted history:
8 entries in the revoked thread, 4 in the expired thread. The private briefing
was present only in owner views.

Production transport tests used the actual packaged plugin with disposable
signed accounts and synthetic native identities. They did not send messages to
existing teammates. The earlier real-model test used an isolated local relay.

## Limits

The Conductor desktop UI, live Codex model sessions and external owner tool
integrations were not exercised. A finite model test does not prove that every
possible prompt will preserve private sources; semantic privacy and topicality
remain model-enforced. Both real test profiles ran as the same Mac user.

Keep the owner Claude Code chat open for native delivery. Closed chats are not
launched by this release. The old cloud-launch and shared-files behavior is
unchanged.

The release assets include archive checksums and a promotion report. Fresh public
installation results are recorded after the marketplace update is available.
