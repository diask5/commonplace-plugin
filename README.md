# Meet Proxy

Share context with a person, team or project through the assistants you already
use. **Spaces / My context** is the main navigation. Each space has **Messages /
My sharing rules / Members**: a shared conversation, your own prompt rules and
simple membership controls.

The [production application](https://34.27.253.220/) includes context-sharing
spaces, one-request native plugin/MCP setup, automatic private collection,
natural-language invitations, timed rules and leave/archive controls.
The **0.4.24 / runtime57** update is published. It includes bounded context sharing,
selected MCP resource ingestion and direct document reads during archive rebuilds,
plus native Codex chat attachment and background installation updates.
The update is installed and live; actual Claude Code and Codex search/read tests
passed. Real Google sign-in and both Desktop handoffs are verified, and context is
searchable while background collection continues. See
[P0 readiness](docs/P0-NATIVE-READINESS.md) for exact evidence and remaining gates. P1 email/iMessage delivery is outside this rollout.

[See the desktop and phone walkthrough](https://kyle-cloud-w3.conductor.show/review)
or [open the interactive preview](https://kyle-cloud-w3.conductor.show/preview/sample?view=conversations).
These walkthroughs use isolated test identities; they do not prove a fresh Google
sign-in or native app launch. The real Mac context-read result is documented in
[zero-to-knowledge verification](docs/ZERO-TO-KNOWLEDGE.md).
The [sharing walkthrough](docs/SHARING-WALKTHROUGH.md) explains the animated setup,
copy/paste next step and sharing rules.

Private-library sharing is opt-in per owner and space. Every request checks the
current rules through Perplexity Decisions; rejected excerpts and classifier
checks stay private. Approved excerpts become shared history. Explicit uploaded
files are shared in full. Joining a space never grants unrestricted library access.
Existing owner retrieval through MCP or local files needs no hosted answering model.

## Unified context — 0.4.15

Version 0.4.15 fixes backfill of active chats and concurrent archive searches. It provides one shared archive per verified account for native and cloud
agents: resumable transcript collection, duplicate replica merging, source
citations, exclusions, coverage, and paginated project statements. A readable
`/context` folder holds complete source files with an index and ranked keyword
search, phrase/prefix matching, and project/source/date filters. Existing
accounts, chat bindings, permissions and sync choices are preserved.

See [unified context](docs/UNIFIED-CONTEXT.md) and
[candidate verification and rollout](docs/UNIFIED-CONTEXT-VERIFICATION.md).
The hosted backend and both plugin aliases are released. Update existing
installations through their supported manager or bundled Codex helper, then
refresh the existing chat if the host requires it. Saved sync choices are preserved.

## Test locally before deployment

The [local integration environment](docs/LOCAL-DEVELOPMENT.md) runs the real UI,
signed API, collector, search index and task worker with isolated sample accounts
and simulated model/host responses. In the implementation repository, run
`npm run dev:local` or `npm run test:local`. Conductor cloud workspaces can use
`npm run dev:preview` for a protected preview. No production setup is needed.

## One private cloud workspace

[Download Meet Proxy / Commonplace 0.4.24](https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-v0.4.24)
for a cloud workspace containing supported synced chats, permitted agent-message
threads, published working context, and previous cloud results. Your cloud agent
can query the live message board, consult your connected native agents, wait for
a matching reply, and continue the same task.

See [personal agents](docs/PERSONAL-AGENTS.md),
[cloud workspace behavior](docs/CLOUD-WORKSPACE.md), and
[production verification](docs/PRODUCTION-READINESS.md).

## Install or update

Add marketplace **diask5/commonplace-plugin** in your host's plugin manager.
New installations use **meet-proxy**. Existing **commonplace** users should
update that alias to **0.4.24**. Enable only one alias. Existing accounts and
connections are preserved. Reload or resume the intended chat after updating.

Node is bundled for Windows x64, macOS arm64/x64 and Linux arm64/x64. No separate
Node installation or model API key is required. Your agent uses its normal host
login and permissions.

Codex currently skips this marketplace's archive entries. For Codex, extract the
verified release to a permanent folder and configure its MCP server:

```sh
/absolute/path/to/meet-proxy/runtime/node /absolute/path/to/meet-proxy/server/configure-codex.mjs
```

Reload the MCP connection if the running host requires it. This configures the
tools; automatic idle delivery depends on the host's existing-session support.

## Check setup

Ask **“Check Meet Proxy setup”** or use `/meet-proxy:setup`. The read-only
`setup_status` tool checks the loaded and installed versions, local Google link,
companion and inbox diagnostics. Already linked installations keep their account.

If Claude auto mode blocks accepting an invitation, the host has stopped it
before the plugin runs. Setup guidance shows the exact action and per-tool
approval. The plugin does not retry denials or change permission settings.
See [setup and host permission recovery](docs/SETUP.md).

Version 0.4.5 starts a persistent receiver for each registered cloud Conductor
chat. Incoming messages wake that exact existing chat through Conductor's
supported CLI, with durable receipts and stable IDs for retry protection. Setup
keeps the Google account and invitation binding. `setup_status` reports receiver
health separately from account connection. A host receipt is not a model reply.

Conductor has a separate known Mac-access regression: an agent message may
invalidate the receiving chat's authorized Mac binding. This release enables
message delivery but does not bypass or repair Conductor's device authority. A
new human message from that Mac restores access temporarily.

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
New web conversations need a later export import. Version 0.4.2 also filters
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

The cloud Conductor receiver has passed delivery into the original idle chat.
Other hosts depend on their existing-session delivery support; lifecycle hooks
and bounded waits alone cannot wake an idle chat. Native host permissions and
Claude's accept/hold/refuse setting remain effective. Queued, delivered and
answered are distinct states.

See [verification results](MEET-PROXY-VERIFICATION.md) and the
[two-chat guide](docs/meet-proxy-conductor.md).

## Compatibility

Commonplace account storage, protocol identifiers, marketplace address and
plugin alias remain compatible. Personal memory capture and automatic learning
are not part of this plugin. [Commonplace Files](FILES.md) is a separate plugin
and is unchanged by this release.

## Reuse a shared chat

Say “add Zane to this chat” when you already share a conversation. Choose one if
there are several. Your side moves into this chat; Zane keeps his receiving
chat and can change it independently. No new invitation or Google sign-in.

In **People → Shared chats**, read and message that same conversation, choose
your receiving chat, or end the chat connection while keeping the person in
your circle. Offline destinations stay pinned. Private transcripts stay private.
Requires 0.4.6; your host may need to refresh its loaded tools after updating.

Version 0.4.7 also recovers a companion upgrade when an older loaded plugin
wins the runtime process lock. Existing account and chat data stay in place.

## Conductor chat history

Version 0.4.8 adds visible conversations cached by Conductor on your Mac to work-chat sync, alongside local Claude and Codex transcripts. Enable sync for your connected account. The background companion keeps it running while your Mac is awake. Provider-hosted ChatGPT and Claude website histories are not downloaded by model sign-in.

Version 0.4.9 adds per-message delivery/read receipts and fixes startup listeners that remained waiting after setup. Check receipts in People → Shared chats or with read_chat_link. Update the existing plugin and reload it in your receiving host; a session heartbeat alone is not proof of delivery.

Version 0.4.10 delivers shared-chat messages through the persistent native inbox, preserving sender attribution and original wording. Lifecycle hooks and the persistent receiver share a cursor to avoid duplicates. Reload the updated plugin in the same chat, or restart the host and reopen that conversation.

For a customer walkthrough of the local context folder, see [docs/DEMO.md](docs/DEMO.md).

The [product flow and design walkthrough](docs/PRODUCT-FLOW-DESIGN.md) follows Draft v3’s Agents/Inbox and invite/accept journey. The labeled demo is separate from real-account staging; its source is preserved in the fourth incremental patch.

The latest source follow-up adds [automatic collection and live desktop setup](docs/LIVE-CONTEXT-SETUP.md), with a single app sheet, verified account handoff and installation-specific progress. It requires a new plugin release and matching deployment; published 0.4.19 is unchanged.
