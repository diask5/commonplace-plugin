# Commonplace 0.2.6 verification

Verified on Windows with Claude Code 2.1.278 on September 22, 2026 (UTC).

- **312/312 source tests passed**, with no skipped tests.
- **19/19 packaged integration tests passed**, including bundled-runtime startup, paths containing spaces, inbox renewal, refusal controls and the shared reader sandbox.
- **Fresh public GitHub installation passed** in an empty Claude profile. Two new profiles registered automatically, accepted an invitation, exchanged two question/reply rounds through the GCP service, and disconnected.
- **Two real Claude Code sessions installed from the public marketplace**, received the actual teammate text through their native inboxes, and completed two question/reply rounds. A separate fresh-install run verified that Claude's refusal setting blocks delivery without a fallback.
- Removed memory/import tools were absent and rejected even with old learning/capture flags enabled. No learning hook is shipped.
- The current shared-context Codex reader disables autonomous goals, shell, images and delegation. Its read-only sandbox rejected a file write.

Native host tests use a synthetic loopback inference provider, with zero paid model calls. The live GCP check uses disposable test identities. No real teammate was messaged. These runs verify Windows execution; they do not establish fresh physical Mac/Linux host execution.

The public marketplace selects stable **0.2.6**, and GitHub marks it as the latest non-prerelease. Installed runtime, skills and hooks on the local Claude and Codex copies were compared against the release archive.

[Machine-readable verification](https://github.com/diask5/commonplace-plugin/releases/download/v0.2.6/commonplace-0.2.6-verification.json)

Archive SHA-256: `1e4cbfdbd78ce3a0c909f8e551a6a91eb52890d466a5fba99ebc9bda607eeae8`

Already-installed users should refresh the marketplace, update Commonplace and reload their plugin or start a new session. An open host can retain instructions loaded before the update.
