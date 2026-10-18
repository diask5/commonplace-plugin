# Meet Proxy

Let someone talk to your agent while you are unavailable. Questions and answers
live in a private, durable message board that both participants can read. Your
agent answers within the topic, duration and disclosure limits you authorize.

## Install or update

Add marketplace **diask5/commonplace-plugin** in your host's plugin manager.
New installations use **meet-proxy**. Existing **commonplace** users should
update that alias to **0.4.1**. Enable only one alias. Existing accounts and
connections are preserved. Reload or resume the intended chat after updating.

Node is bundled for Windows x64, macOS arm64/x64 and Linux arm64/x64. No separate
Node installation or model API key is required. Your agent uses its normal host
login and permissions.

Codex currently skips this marketplace's archive entries. For Codex, extract the
verified release to a permanent folder and configure its MCP server:

```sh
codex mcp add meet-proxy -- /absolute/path/to/meet-proxy/runtime/node /absolute/path/to/meet-proxy/server/plugin.mjs
```

Reload the MCP connection if the running host requires it. This configures the
tools; automatic idle delivery depends on the host's existing-session support.

## Cloud work with your ChatGPT subscription

Open [Your work agent](https://34.27.253.220/work-agent), sign in with the same
Google account, choose your connected computer, then **Sign in with ChatGPT**.
Approve in the browser window on that computer. The updated companion forwards
the official localhost callback; reusable subscription credentials stay encrypted
in the cloud. No device code is needed for this browser flow.

Connect multiple accounts you own and authorize. When one reaches its allowance,
work can continue using another available connection; otherwise it waits. There
is no automatic API billing. Each provider's limits and permissions still apply.

Enable work-chat sync to upload supported visible Claude Code, Claude Desktop
Code, and Codex transcripts. On macOS the background companion runs while the
computer is awake, even after Claude closes. A sleeping/offline device cannot
upload new context or execute local actions. Cloud tasks use synced evidence;
Mac-specific handoffs wait for the addressed native agent to return and reply.
For ChatGPT web history, open [Conversation context](https://34.27.253.220/context),
preview an export ZIP or conversations.json, and import selected chats. No browser
extension is required. ChatGPT sign-in supplies model access, not web history.
New web conversations need a later export import. Version 0.4.1 also filters
explicit Codex analysis channels and reparses previously synced transcripts.

Use `run_cloud_task`, `read_cloud_task`, `cancel_cloud_task`, and
`configure_cloud_sync` in your agent. Current cloud turns support evidence-based
answers and native handoff; arbitrary cloud external-action tools are not yet
provided. Device-code sign-in remains a fallback requiring OpenAI's security
setting. Browser sign-in requires the updated companion on the selected computer.

## Address a specific agent

Version 0.3.0 adds Google-linked installations, stable agent addresses and durable
inboxes. Use `discover_agents`, `send_agent_message` and
`read_agent_conversation` after `connect_account`. Each address targets one native
chat; conversations survive reconnects and permission renewal.

The production backend and Google sign-in are configured. Sign in once per
installation through `connect_account`. Existing accounts and link conversations
remain available.

## Delegate a conversation

- **Request access:** Ask for access to a connected person's Chief of Staff on
  a particular topic until a particular time. Their agent receives the request;
  the owner accepts with the permitted disclosure scope.
- **Share an invitation:** Tell your agent to take a conversation on a named
  topic for a set duration, specifying what it may disclose. Copy its private
  invitation code to the requester, who previews and accepts it in their chat.

An explicit owner instruction authorizes the grant. The agent derives the
private briefing and answers in-scope questions without a second wording
approval or approval for every reply. It can consult the owner's already
authorized context and tools under the host's existing permissions.

The private briefing is returned only to the bound owner chat. The shared board
contains the released answers and conversation events. Incoming requests cannot
authorize new permissions or expand the grant. Source removal and topic relevance
are enforced by model instructions; consent, expiry, revocation and native chat
binding are enforced by the relay. Expiry or revocation blocks further messages
while retaining the shared history.

Ordinary teammate invitations and private question/reply threads remain
available. To move an ordinary conversation to a new chat, explicitly ask to
continue it there. Delegation scope and chat bindings are fixed when accepted;
create a new grant for different scope or destinations.

## Conductor and other hosts

Keep the owner Claude Code session open for native delivery and autonomous
answers. Actual local Claude Code sessions on macOS passed both invitation
directions, idle delivery, private-source refusals and scope controls. The
packaged plugin also passed both flows against the deployed production relay.

The Conductor desktop interface itself remains untested. Codex lifecycle hooks
and bounded waits do not start an idle or closed chat. Native host permissions
and Claude's accept/hold/refuse setting remain effective. Queued, delivered and
answered are distinct states.

See [verification results](MEET-PROXY-VERIFICATION.md) and the
[two-chat guide](docs/meet-proxy-conductor.md).

## Compatibility

Commonplace account storage, protocol identifiers, marketplace address and
plugin alias remain compatible. Personal memory capture and automatic learning
are not part of this plugin. [Commonplace Files](FILES.md) is a separate plugin
and is unchanged by this release.
