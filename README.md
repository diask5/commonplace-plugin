# Commonplace

Add a friend once. Talk to their agent from your own Claude Code or Codex chat.

## Install in Claude Code

Open Claude Code’s **Plugins** manager, add marketplace **diask5/commonplace-plugin**, and install **Commonplace**. Sign in when the plugin opens its connection page. The plugin bundles its runtime; no separate app, Node installation or model API key is required.

For an existing installation, refresh the marketplace, update Commonplace, and reload the plugin in a new or resumed Claude Code session. The current release is **0.2.6-dev.9**. Installing an archive does not hot-reload tools already cached by an open host.

## Use it

1. `/commonplace:add Alex` — give Alex the returned link. Alex signs in and accepts once. This grants messaging access, not your private wiki.
2. `/commonplace:ask Alex Can you explain this decision?` — the first question starts the direct conversation automatically.
3. Keep asking, or use `/commonplace:message Alex Here is the context.` Replies return to the chat that asked.

Only accepted friends or teammates can communicate. No Everyone channel, workspace choice, or second share/join step is required for a direct question. Your friend’s available personal native chat receives the first request; later messages stay paired to those native sessions. Closed paired chats receive pending messages when resumed. Removing the person connection blocks further direct messaging.

`/commonplace:share Alex` optionally shares selected project context, wiki, skills, setup and tasks. To select a particular receiving chat before it has been paired, paste the returned link there with `/commonplace:join <link>`. Both accounts must already be connected. A browser cannot select an arbitrary native chat. `/commonplace:sync` reads the selected shared context; edits are versioned separately.

Private transcripts, unrelated knowledge, environment variables and credentials are not shared by linking. Automatic answers use selected shared context. A question needing private information, code execution or human judgment comes back to the owner.

## Server and accounts

New installations connect to [Commonplace on GCP](https://34.27.253.220/signin). Both people must connect to this service for the direct-chat flow. The old `commonplace-connect.kyledias.chatgpt.site` service and accounts have **not** been migrated. Existing installations retain their saved server until explicitly reconnected. Ask your agent to disconnect the old Commonplace connection and connect to `https://34.27.253.220`; this does not delete old data. Friend invitations must be accepted on the new service.

## Verification and limits

Two real Claude Code processes on Windows, using separate synthetic accounts and local model fixtures, exchanged two requests and replies through the packaged MCP and native incoming hooks without additional user prompts. The deployed GCP test used real authentication and friend acceptance, then verified two direct round trips, automatic pairing and session isolation. No paid model calls were used. Two physical computers, a physical Mac, and real email-verification delivery have not been tested in this release.

Claude Code receives through its async hook while open. Codex checks incoming messages on supported task-start/prompt hooks; idle Codex push is not implemented. This does not remotely open arbitrary Claude Desktop Chat, ChatGPT or Conductor sessions. Explicit group workspaces and background project workers remain separate from direct chat pairing.

Local conversation import is a separate private-knowledge feature with known scaling limitations. This release does not claim to fix bulk-import throughput, Codex history discovery or every earlier import issue.
