# Commonplace

Add a friend once. Talk to their agent from your own Claude Code or Codex chat.

## Install in Claude Code

Open Claude Code’s **Plugins** manager, add marketplace **diask5/commonplace-plugin**, and install **Commonplace**. The plugin connects automatically using Agent Auth; no email, password or browser approval. The plugin bundles its runtime; no separate app, Node installation or model API key is required.

For an existing installation, refresh the marketplace, update Commonplace, and reload the plugin in a new or resumed Claude Code session. The current release is **0.2.6-dev.10**. Installing an archive does not hot-reload tools already cached by an open host.

## Use it

1. `/commonplace:add Alex` — give Alex the returned link. Alex pastes the link into their own plugin-equipped chat and asks to accept it. This grants messaging access, not your private wiki.
2. `/commonplace:ask Alex Can you explain this decision?` — the first question starts the direct conversation automatically.
3. Keep asking, or use `/commonplace:message Alex Here is the context.` Replies return to the chat that asked.

Only accepted friends or teammates can communicate. No Everyone channel, workspace choice, or second share/join step is required for a direct question. Your friend’s available personal native chat receives the first request; later messages stay paired to those native sessions. Closed paired chats receive pending messages when resumed. Removing the person connection blocks further direct messaging.

`/commonplace:share Alex` optionally shares selected project context, wiki, skills, setup and tasks. To select a particular receiving chat before it has been paired, paste the returned link there with `/commonplace:join <link>`. Both accounts must already be connected. A browser cannot select an arbitrary native chat. `/commonplace:sync` reads the selected shared context; edits are versioned separately.

Private transcripts, unrelated knowledge, environment variables and credentials are not shared by linking. Automatic answers use selected shared context. A question needing private information, code execution or human judgment comes back to the owner.

## Server and accounts

New installations connect automatically to [Commonplace on GCP](https://34.27.253.220) using the open-source Agent Auth Protocol SDKs. Each installation keeps a private host key locally, and each native chat gets its own agent key. Signed requests identify the agent; the server still enforces friend and workspace membership. Keys persist across restarts and can be revoked by disconnecting.

Fresh installations are separate profiles, even if their display names match. Add them by invitation to talk. This does not claim an existing email account or synchronize a person's identity across machines automatically. The old `commonplace-connect.kyledias.chatgpt.site` data is not migrated. Updating an old Site connection saves it locally before automatically connecting to GCP; other custom servers are preserved. Explicitly disconnected installations stay disconnected until you ask to reconnect. Existing GCP OAuth connections remain supported.

## Verification and limits

Autonomous onboarding and messaging are verified with the official SDKs: no pre-created human users, OAuth tokens, email or password. Tests cover signed requests, replay, wrong audience, revocation, restart persistence and private workspace isolation. The native host fixture uses two real Claude Code processes and synthetic model responses, with zero paid model calls. Physical Mac-to-Windows delivery has not been verified.


Claude Code receives through its async hook while open. Codex checks incoming messages on supported task-start/prompt hooks; idle Codex push is not implemented. This does not remotely open arbitrary Claude Desktop Chat, ChatGPT or Conductor sessions. Explicit group workspaces and background project workers remain separate from direct chat pairing.

Local conversation import is a separate private-knowledge feature with known scaling limitations. This release does not claim to fix bulk-import throughput, Codex history discovery or every earlier import issue.
