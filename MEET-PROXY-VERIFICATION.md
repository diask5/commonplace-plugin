# Meet Proxy 0.4.0 verification

- 130 application tests passed, including callback owner/device/state isolation,
  durable native handoff, account failover, and interrupted source upload replay.
- Both archives preserve the pinned 0.3.0 baseline outside the reviewed overlay,
  including bundled runtimes, hooks and executable modes.
- The packaged companion starts and initializes MCP as 0.4.0.
- Production health is ready. The isolated official Codex runtime generates a
  real browser OAuth URL with PKCE and the expected loopback callback.
- Real subscription inference and installation on the target MacBook await the
  user's browser consent and that session's local installation approval.

The following records describe earlier releases and do not establish 0.4.0's
remaining live checks.

# Meet Proxy 0.3.0 verification

Verified October 18, 2026. Backend migration 0025 and browser linking routes are
live. Both stable plugin aliases use the verified mailbox implementation.

- 115 source tests and six packaging/reproducibility checks passed. The added
  regression covers identity linking while the ordinary API quota is exhausted.
- Packaged mailbox checks passed: exact recipient among three same-account
  chats, idempotent retry, receiver restart, and queued catch-up.
- The stable plugin passed signed messaging, both delegation flows, shared
  history, private briefing separation, expiry and revocation against production.
- Stable promotion preserved 93 files and every executable mode from the tested
  candidate. Only two manifests, advertised version and README changed.
- The full production web app and browser routes passed on a database copy.
  Live migration preserved all 63 existing application table counts; backup and
  previous release are retained on the VM.

Google sign-in is enabled with its OAuth client and authorized origin, verified
through the Firebase Admin API and a successful Google authorization URL response.
The cloud and Mac installations subsequently completed real Google sign-in to
the same human account. The actual Claude and Codex cloud chats independently
discovered and messaged the Mac, which replied on both conversations and
confirmed 0.3.0 loaded in its existing native chat. Claude received its reply
through native push. Codex used the published stdio entrypoint with its actual
host identity and read the reply directly; idle wake in that Codex host remains
unverified. These observations do not establish universal host wake.

The production service reserves a bounded quota for account checks and Google
linking, so heavy ordinary API traffic cannot consume the sign-in allowance.
The previous deployment is retained and the public service is healthy.

Codex's marketplace loader skips the archive sources in this catalog. The
verified Codex connection uses direct MCP configuration of the extracted stable
release; a Codex marketplace installation has not passed.

---

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
| Fresh public installation | Both aliases installed on the Mac; all 92 files matched and executable bits were intact |
| Freshly installed production plugin | Both delegation flows and boundary checks passed using the public 0.2.9 installation |

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

The release assets include archive checksums, file manifests, a promotion report
and machine-readable verification. Claude normalized two public source files
from permission mode 0600 to 0644 during installation; their bytes and executable
bits were unchanged. The fresh installations used isolated Claude configuration
directories and did not change the user's existing plugin setup.
