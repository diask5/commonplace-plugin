# Meet Proxy in Conductor

Meet Proxy is the new name for Commonplace. It connects accepted people through their existing agent conversations. Each host runs the same plugin and uses the same relay for invitations, shared messages, and selected context. Existing account storage and connection identifiers are retained.

## Setup

Conductor loads the MCP configuration of its selected agent. Install the plugin in the Claude Code or Codex environment that Conductor actually runs. For new Claude Code installations, add marketplace `diask5/commonplace-plugin` and install `meet-proxy`. Existing `commonplace` installations receive the same compatible update under their existing ID. Keep only one alias enabled.

After an update, refresh MCP status and reload or resume the intended session. The first tools/list result must contain `ask_chat`, `read_chat_link`, and `reply_chat`. A browser page opening or an installation record alone does not prove this activation. Check `connect_account`, then `list_chat_sessions` to identify the actual receiver.

Use the host's supported installer and normal permission controls. Claude's native message accept/hold/refuse setting remains effective. MCP tools work while the agent is active; unsolicited arrival into an idle agent also requires a supported native inbox or host hook. These are separate capabilities.

## Repeatable demonstration

1. In the selected sender chat, invite a test teammate. Accept its private invitation in the receiver chat.
2. Send a synthetic question and read the actual reply in the original chat.
3. Send a different follow-up through the same link and verify a second reply.
4. Restart and resume that same receiver session; verify a third exchange and unchanged account identity.
5. If choosing a new chat or another host, explicitly continue the conversation there. Verify the previous receiver can no longer reply, then exchange another question and reply.

Session-bound invitations intentionally remain attached to their selected chat while it is offline. A new Conductor workspace is a different chat. Moving the responder is an explicit operation so unrelated sessions cannot silently take over private conversations.

## Verification boundary

The startup discovery regression is reproduced using the real stdio plugin and a delayed local companion. Before the fix, an immediate catalog omitted messaging; after the fix, it includes messaging without requiring tools/list_changed handling. Failed onboarding retains connection recovery, and an explicit disconnection is preserved.

This Windows development environment cannot run the macOS Conductor application. A process with Conductor environment variables tests host classification and protocol behavior, not the actual Conductor UI or idle delivery. Actual Mac Conductor testing remains required before claiming full Conductor support.

References: [Conductor MCP configuration](https://www.conductor.build/docs/reference/mcp), [setup and refresh](https://www.conductor.build/docs/guides/configure-mcp-servers), [supported platforms](https://www.conductor.build/docs/installation).
