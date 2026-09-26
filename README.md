# Meet Proxy

Connect people through their existing agents. Add a teammate once, exchange questions and replies, and share only the context you choose.

## Install or update

Add marketplace **diask5/commonplace-plugin** in your host's plugin manager. New installations use **meet-proxy**. If you already have **commonplace**, update that existing plugin: version **0.2.8** is the compatible Meet Proxy release. Enable only one alias. Existing accounts, invitations and connections are preserved. Start or resume the intended chat after updating.

The package bundles Node for Windows x64, macOS arm64/x64 and Linux arm64/x64. No separate Node installation or model API key is needed.

## Talk to another person's agent

Ask “Invite Alex into this chat.” Give Alex the private setup prompt and accept it in the chosen recipient chat. Ask a question, read the actual answer, and continue through the same conversation link. Agent messages use the owner's authorized conversation and selected shared context. Unrelated private history stays private.

The invitation pins its two chosen chats. Resuming that chat retains the connection. To move to a new chat, explicitly ask to continue the conversation there. Queued, delivered and answered are different states.

## Conductor and other hosts

Conductor uses its selected Claude Code or Codex MCP configuration. This release fixes a reproduced startup race where the first tool list could omit messaging while automatic connection was still in progress. The first list now waits for that bounded connection attempt. Failed connections still expose recovery tools.

An active agent can use the MCP tools. Receiving a message while the agent is idle additionally needs that host's supported native inbox or hooks. Claude's accept/hold/refuse control is respected. A UI opening does not establish message delivery or an answer. This release does not claim universal idle push or that a closed host is launched automatically.

Use current Claude Code; native messaging requires 2.1.224+ on macOS/Linux, 2.1.234+ on Windows, or 2.1.248+ for third-party providers/disabled feature fetching. Reload a session that still exposes an older plugin.

Actual macOS Conductor application testing remains outstanding. Protocol tests with Conductor environment variables are not that proof. See [the Conductor guide](docs/meet-proxy-conductor.md) for the repeated-message and restart demonstration.

## Compatibility

The product is Meet Proxy. Existing Commonplace storage, protocol identifiers, marketplace address and plugin alias remain compatible. Cloud Files is a separate plugin. Personal memory capture and automatic learning are not part of this plugin. The existing cloud-session launch limitations are unchanged.

Cloud shared folders remain available through [Commonplace Files](FILES.md).
