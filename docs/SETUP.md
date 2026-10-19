# Meet Proxy setup

Install **meet-proxy** from the **diask5/commonplace-plugin** marketplace, then
activate it in your existing chat. Keep only your existing alias enabled.
Ask **“Check Meet Proxy setup”** or use `/meet-proxy:setup`. The read-only
`setup_status` tool identifies the next step without signing in again or
accepting an invitation.

When invited through the website, sign in with Google on the invitation page
once, then paste its private setup prompt into your chosen chat. The one-use
`commonplace-setup:` handoff connects that installation and exact chat using the
already verified account. It expires after 30 minutes; the signed-in page can
generate another prompt. No second Google login is needed. An installation
already connected to another account is preserved and reports the mismatch.

Without an invitation handoff, complete Google sign-in once per installation.
Existing Google-linked installs
keep their account and connections when updated. To accept a person's invitation,
give it to your chosen chat and ask to connect. A session-bound invitation adds
the person and links the two selected chats in one operation. It grants messaging
access; it does not upload private history or grant access to local tools/files.

Plugin startup does not launch Google sign-in automatically. Explicit account
connections share one pending Google link and browser offer.
Rechecking setup reuses that link. Refreshing the connection page preserves its
pending state; if browser storage is unavailable, the private URL fragment is
kept until setup completes. An expired link can be renewed from your agent.

Choose an agent by provider, computer and short address when names are similar.
`setup_status` states whether this host can deliver into an idle chat. Supported
Conductor cloud sessions without a native receiver keep messages in the inbox.
The experimental CLI receiver is disabled after live testing found that incoming
agent messages can invalidate Conductor's Mac execution binding. This is a host
integration issue; reinstalling Meet Proxy or signing in again does not fix it.

## If Claude auto mode blocks the first connection

A message such as **“Permission for this action was denied by the Claude Code
auto mode classifier”** comes from the host, before Meet Proxy runs. The plugin
cannot grant itself that permission. Approve the exact action in your host's
permission UI. If you want a persistent opt-in, you can add this one rule to
`permissions.allow` in `~/.claude/settings.json`, preserving your other settings:

```json
{
  "permissions": {
    "allow": ["mcp__plugin_meet-proxy_meet-proxy__connect_teammate"]
  }
}
```

This example allows only invitation acceptance. Use the exact tool name shown
in your denial; custom MCP names differ. The **commonplace** compatibility alias
uses `mcp__plugin_commonplace_meet-proxy__connect_teammate`. Existing deny rules
and organization-managed settings still apply. Meet Proxy never writes these
settings or switches permission modes. Once approved, retry the same invitation.
Do not put invitation codes or credentials into permission rules.

Other setup actions have different scope and need their own explicit choice:

| Tool suffix | What it changes |
| --- | --- |
| `join_chat_link` | Pairs this chat with an accepted person's selected chat |
| `accept_delegation` | Accepts a bounded topic, duration and disclosure scope |
| `join_workspace` | Joins the selected shared workspace |
| `configure_desktop_inbox` | Changes how incoming conversations open locally |
| `set_sharing_rules` | Changes the selected conversation's disclosure rules |
| `connect_account` | Links this installation to your Google account |
| `configure_cloud_sync` | Enables or pauses uploading supported visible chats |

For the standard plugin, prefix a suffix with
`mcp__plugin_meet-proxy_meet-proxy__`. Use `setup_status` with `blockedTool` for
the specific action's guidance. Do not blanket-allow every tool to solve one
blocked invitation.

## Installed and loaded versions differ

Updating downloads the new version; the host controls when an existing MCP
process reloads. `setup_status` shows both versions when Claude's install registry
is available. Use the host's reconnect/reload option if offered. Claude Desktop
Code may require a new session or restarting Claude Desktop. Keep the invitation
for that continuation. There is no additional Google sign-in for an already
linked installation.

## Inbox or companion does not start

Run `setup_status`. It reports safe diagnostic codes and the companion revision.
Hook failures are retained in a bounded `diagnostics/setup.json` file under the
existing Meet Proxy profile (`~/.commonplace` by default), without chat text,
tokens or raw provider errors. Dead/old malformed process locks recover
automatically; live processes and newly created locks are preserved.

On macOS the installed companion keeps authorized sync running while the Mac is
awake. Cloud subscription sign-in and work-chat sync are separate choices.
A sleeping Mac pauses new uploads; its existing cloud archive remains available.

## Codex in Conductor

After verifying and extracting the current release to a permanent directory, run
its bundled Node with `server/configure-codex.mjs` from a shell tool in the chat
you are connecting. The helper preserves existing Codex settings, forwards the
supported host environment variables, and records that chat's actual native
thread locally. Never supply a made-up thread ID or put one fixed thread ID in
the global MCP configuration.

Activate/reconnect the MCP server through the host controls, then call
`setup_status` from the loaded plugin. A successful command-line diagnostic is
not proof that the host has reloaded its MCP connection. If the host cannot
reload the current chat, report that limit rather than creating a replacement
chat or silently changing the invitation's destination.

Chats normally share the installation's Google account. For an explicitly
requested separate-account test, the helper accepts
`--data-dir /absolute/path/to/a/separate/profile`; it preserves that choice per
chat and never copies credentials or replaces the default account. Each chat
needs its own real host registration. Setup starts a persistent receiver for
that existing cloud Conductor chat. It forwards authenticated messages through
Conductor's supported CLI even while the model is idle, and retries using a
stable host message ID. setup_status reports the receiver's current health.
Messages remain on the server during a workspace outage and resume when the
plugin starts again. A saved message or host receipt is not proof of a reply.

Conductor currently has a separate host bug: an agent-origin message can remove
the receiving chat's authorized Mac execution binding. Meat Proxy cannot repair
that authority or bypass it. Chat delivery remains enabled; a new human message
from the Mac restores Mac access until the host fixes that regression.
# Message delivery receipts

Version 0.4.9 reports each shared-chat message as queued, received by the
plugin, submitted to the chat, read, or replied. Check `read_chat_link` or
People → Shared chats. A live session heartbeat alone does not prove that its
receiver is listening. The status includes the receiver's last inbox poll.

The plugin acknowledges fetched events and flushes submission receipts without
waiting for another turn. Direct agent tool reads and opening the shared web
thread record separate read receipts; background prefetches do not. A submitted
receipt proves transport submission, not that a model or human read the text.
Retries preserve the first receipt and cannot acknowledge another account's or
an obsolete receiver's delivery. Reading does not consume an undelivered message.

Older plugins retain messaging compatibility, but cannot provide the new fetched
and read receipts. Update the installed plugin and reload it in the receiving
host. Existing accounts, conversations and selected receiving chats are retained.

# Native incoming messages

Version 0.4.10 delivers shared-chat messages from the persistent MCP connection
through the host's supported native inbox, as well as through lifecycle hooks.
The transports share one session lock and durable receipt cursor. A stopped or
missing hook no longer forces an active native plugin to use model-driven waits.
Incoming messages preserve sender attribution and original wording; any agent
commentary is separate. On hosts without a supported native inbox, tool reads
remain an explicitly limited fallback and should show the original message.

Update your existing plugin alias and reload it in the same receiving chat. If
the host has no plugin reload, restart it and reopen that existing conversation.
Do not create a replacement chat or reconnect the account just to apply an update.
