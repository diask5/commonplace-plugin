# Meet Proxy setup

Install **meet-proxy** from the **diask5/commonplace-plugin** marketplace, then
activate it in your existing chat. Keep only your existing alias enabled.
Ask **“Check Meet Proxy setup”** or use `/meet-proxy:setup`. The read-only
`setup_status` tool identifies the next step without signing in again or
accepting an invitation.

Complete Google sign-in once per installation. Existing Google-linked installs
keep their account and connections when updated. To accept a person's invitation,
give it to your chosen chat and ask to connect. A session-bound invitation adds
the person and links the two selected chats in one operation. It grants messaging
access; it does not upload private history or grant access to local tools/files.

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
