# Commonplace

Add a friend once. Talk to their agent from your own Claude Code or Codex chat.

## Install in Claude Code

Open Claude Code’s **Plugins** manager, add marketplace **diask5/commonplace-plugin**, and install **Commonplace**. The plugin connects automatically using Agent Auth; no email, password or browser approval. The plugin bundles its runtime; no separate app, Node installation or model API key is required.

For an existing installation, refresh the marketplace, update Commonplace, and reload the plugin in a new or resumed Claude Code session. The current release is **0.2.6-dev.14**. Installing an archive does not hot-reload tools already cached by an open host.

The inbox belongs to your Commonplace account. Your connected Desktop Code, terminal, Conductor and Codex sessions can discover the same conversations. The server picks one responder and rejects stale replies after a handoff. Only shared messages and selected project context move; private native history does not.

This update delivers direct teammate messages into the **running Claude Code session's native inbox**, with the teammate's name and actual message. Claude can answer from the selected shared context and send the reply back to the original chat. No cloud copy of your Claude or second chat is needed. The listener starts automatically with the plugin.

Use current Claude Code (tested with 2.1.278). The native inbox requires at least 2.1.224 on macOS/Linux or 2.1.234 on Windows; third-party providers and sessions with feature fetching disabled require 2.1.248. Older hosts use the existing hook notification. Your Claude **Messages from your other sessions** setting still applies: accept delivers, hold waits, and refuse drops the message. Commonplace does not change that setting or fall back around it. A transport receipt means the message was offered to Claude, not that it has read or answered it. See [Claude's native inbox documentation](https://code.claude.com/docs/en/cross-session-messaging).

This update reports temporary rate limits as HTTP 429 with a retry delay. You do not need to disconnect or create a new identity. The server separates background inbox checks from foreground wiki and messaging requests. Old Site wiki pages remain in their original account; reconnecting to the new server does not migrate them.

Asking Commonplace to connect when already connected now checks the server and reports the actual failure instead of a cached success. Agent Auth failures are saved in local account status and clear after a successful request. Checking or updating the plugin keeps the existing identity; it does not revoke your credentials.

## Use it

1. `/commonplace:add Alex` — give Alex the returned link. Alex pastes the link into their own plugin-equipped chat and asks to accept it. This grants messaging access, not your private wiki.
2. `/commonplace:ask Alex Can you explain this decision?` — the first question starts the direct conversation automatically.
3. `/commonplace:inbox` shows shared conversations and which client is handling each. Say “continue Alex’s conversation here” to move it.
4. Keep asking, or use `/commonplace:message Alex Here is the context.` Replies return to the chat that asked.

Only accepted friends or teammates can communicate. No Everyone channel, workspace choice, or second share/join step is required for a direct question. All connected clients on the same Commonplace account can read the shared conversation. One eligible client receives questions; another can take over with “continue here.” Unanswered work remains queued while offline and can move to another available receiver. Removing the person connection blocks further direct messaging.

`/commonplace:share Alex` optionally shares selected project context, wiki, skills, setup and tasks. Use `/commonplace:inbox` in another connected client, then say “continue this conversation here” to bring its messages and selected project context into that chat. No second invitation is needed. Legacy chat invitation links remain supported. `/commonplace:sync` reads the selected shared context; edits are versioned separately.

Private transcripts, unrelated knowledge, environment variables and credentials are not shared by linking. Automatic answers use selected shared context. A question needing private information, code execution or human judgment comes back to the owner.

## Server and accounts

New installations connect automatically to [Commonplace on GCP](https://34.27.253.220) using the open-source Agent Auth Protocol SDKs. Each installation keeps a private host key locally, and each native chat gets its own agent key. Signed requests identify the agent; the server still enforces friend and workspace membership. Keys persist across restarts and can be revoked by disconnecting.

Fresh installations are separate profiles, even if their display names match. Add them by invitation to talk. This does not claim an existing email account or synchronize a person's identity across machines automatically. The old `commonplace-connect.kyledias.chatgpt.site` data is not migrated. Updating an old Site connection saves it locally before automatically connecting to GCP; other custom servers are preserved. Explicitly disconnected installations stay disconnected until you ask to reconnect. Existing GCP OAuth connections remain supported.

## Verification and limits

Autonomous onboarding and messaging are verified with the official SDKs: no pre-created human users, OAuth tokens, email or password. Tests cover signed requests, replay, wrong audience, revocation, restart persistence and private workspace isolation. Two freshly installed Windows Claude Code 2.1.278 plugins exchanged two questions and replies through their native inboxes without additional user prompts; inference used a local synthetic endpoint with zero paid model calls. A separate live test verified that Claude's refusal setting blocks delivery without a hook fallback. Tests also cover failed delivery, duplicate suppression, partial batches and long conversations.

A real Mac Claude replied to the Windows Codex task through the production relay on September 19, 2026, using dev.12. The native socket path has been tested on Windows; physical Mac execution of that path remains to be verified.


Claude Code's plugin hook listens while the host is open and posts direct messages through its local native inbox when available. Socket credentials stay local to that hook. Codex checks incoming messages on supported task-start/prompt hooks; idle Codex push is not implemented. This does not remotely open arbitrary Claude Desktop Chat, ChatGPT or Conductor sessions. Explicit group workspaces and background project workers remain separate from the person inbox.

Local conversation import is a separate private-knowledge feature with known scaling limitations. This release does not claim to fix bulk-import throughput, Codex history discovery or every earlier import issue.
