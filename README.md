# Commonplace

**Development candidate 0.2.6-dev.5.** Scoped workspaces, delegated reviews and in-agent invitations require the matching account server with migrations through 0015. They are tested locally and are not yet published to the production site or public marketplace. The installed/public release may behave differently.

Start with **`/commonplace:add Sam`** to get a private person-invitation URL. Sam signs in and accepts; this connects you without granting any private knowledge or project access. **`/commonplace:share Sam in Atlas`** then shares the selected project. Once Sam joins in their chat, **`/commonplace:ask Sam What are you working on?`** sends an addressed project question their agent can claim and answer from shared context. **`/commonplace:sync`** brings the latest wiki, skills, setup and context into your own local copy. Plain `/commonplace:message` text does not start autonomous work.

Share from Claude with **`/commonplace:share Kyle in Atlas`** (or just `/commonplace:share` to choose). Kyle receives an invitation in his agent and accepts with **`/commonplace:join Atlas`**. Each existing chat attaches to the shared wiki, skills, setup, tasks and conversation. **`/commonplace:message What should I review?`** sends chosen text between those chats; use it without text to read messages. Sharing can capture the relevant project brief and selected skills from this chat without exporting its transcript. **`/commonplace:join`** lists incoming invitations when needed. Each agent keeps its own local copy and personal chat; My knowledge and private history are not shared. Claude requires namespaced plugin commands. Other hosts can invoke the same share/join skills or ask in plain language. Codex checks invitations when a task starts or the owner next prompts it; idle push remains unavailable. Ordinary sharing and messaging do not require native task creation. Optional autonomous reviews use separate isolated tasks where supported.

For the new flow, each person tells their personal agent: **“Automatically review requests in this workspace using its shared context, and bring me the finished result.”** A teammate can then say **“Ask Kyle to review this commit against our shared review criteria.”** The receiving agent loads a separate scoped task, asks linked questions, and prepares evidence for its human. The host controls whether opening needs acceptance; closed hosts leave work queued. See [what syncs and stays private](docs/shared-workspace.md).

Shared workspaces inside the agents you already use. Ask a teammate's agent a question, discuss the answer, and keep working with the same project knowledge.

## Use it

1. Install **Commonplace** in your agent's plugin manager.
2. Connect your Commonplace account in the browser window it opens.
3. Say **“Create a workspace for Atlas and invite my teammate.”** Share the private invitation with them.
4. Your teammate installs the plugin, signs in to their own account, and accepts the invitation.
5. Say **“Ask Alex in Atlas what still blocks launch.”** Continue the discussion in that conversation.

The plugin includes its runtime and starts its local connection automatically. No separate app, Node installation, listener command, API key, or configuration file is required. Use the host's ordinary plugin installation and permission screens. New installations become available when the host loads the plugin into a session.

The optional [web workspace](https://commonplace-connect.kyledias.chatgpt.site/workspaces) shows the shared chat, wiki and activity. Its **Invite** button creates the same workspace invitation as the agent tool. Workspace invitations grant access to that workspace's shared context; they do not import anyone's entire private history.

## One shared context

A workspace contains conversations, wiki pages, skills, setup and tasks. It is independent of Git. Both teammates' agents read the same shared records and can contribute updates. Local repositories and private notes stay local until their owner deliberately contributes information.

Opening a workspace in an agent attaches that installation. The plugin maintains a private local SQLite replica and synchronizes it with the authenticated cloud account service. Outgoing edits survive restarts and temporary network failures. Stable operation IDs prevent duplicate delivery; conflicting page edits preserve the draft for resolution instead of overwriting a teammate's change.

Incoming requests are saved in the cloud. An eligible receiving agent claims a request before answering, and an expired worker cannot post a late duplicate reply. With Claude Code open, the native plugin wakes its receiving conversation. With the receiving session closed, work stays queued until a session reconnects. Installing a plugin does not run a model while every receiving host is closed.

Teammates can delegate routine project knowledge answers or discuss a draft and choose to send it. Incoming messages never authorize arbitrary local commands or disclosure of unrelated information. Skills and wiki pages provide context; the owner's permissions still apply.

## Verified demo and current limits

On September 14, 2026, the installed Windows Claude Code plugin connected to the public Commonplace sign-in service using normal OAuth. A real Claude session read a synthetic project's cloud wiki and answered an initial question and its follow-up in that same session. No API key or custom MCP launcher was used. This verifies the production account connection and native receive/reply path on this machine; two physical teammate devices have not yet been verified together.

The downloadable Claude marketplace package requires Claude Code 2.1.224 or later. The package includes Windows x64, macOS arm64/x64 and Linux arm64/x64 runtimes. Windows execution is verified; macOS and Linux execution still needs native testing.

Codex can use the same workspace tools and checks its inbox at task start and on new owner prompts. Automatic delivery into an idle Codex desktop session is not complete. Ordinary Claude Desktop Chat, ChatGPT connector push delivery and Conductor integration are not supported by this release. Claude Desktop's Code task-card flow is still under verification.

Connecting starts an import of local Claude Code conversations and saved project notes from `~/.claude/projects`. The plugin uses the signed-in local Claude or Codex to build topic pages, then uploads sanitized conversation evidence and the wiki to an owner-only **My knowledge** workspace. Open its **Wiki** tab to read the pages and **Chat** to ask about them. Your local companion answers these private questions using the generated pages; teammate requests still use the receiving native agent session.

Ask your agent **“Show my Commonplace import status”** for progress and the workspace link, **“Pause my Commonplace chat import”** to stop it, or **“Import my Claude chats with Codex”** to resume using that provider. New and changed files are checked while the plugin companion runs. Completed processing is cached across restarts. Existing sources are retained separately from topic pages; the wiki may omit details, and an answer must say when evidence is missing.

This imports local Claude Code conversation text, not claude.ai or ChatGPT cloud history. It excludes tool arguments and hidden reasoning and redacts recognized credential patterns, emails and personal machine paths before upload; this is not a general guarantee of removing every sensitive fact. Different accounts stay separate. Every device keeps distinct source archives and uses revision checks when merging topic pages. Import stops if its private workspace gains another member. The existing service has a 128-document workspace limit; an oversized import reports the limit and retains local work. Simultaneous first-time connections on multiple machines can create duplicate private workspaces; automatic consolidation is not implemented.

For an existing installation, update Commonplace in Claude Code's Plugins manager and start a new Claude session. The plugin replaces its own legacy companion automatically; no separate app or runtime setup is needed.

## Development

The following commands are for maintainers, not teammate setup:

```text
npm test
npm run package:plugin
python scripts/package-release.py
```

Private runtime state lives in `~/.commonplace`, outside the installed plugin. Never distribute that folder. The release builder includes only plugin files, rejects private state, preserves executable permissions, and records a SHA-256 digest. The cloud account service is in the sibling `commonplace-account` project.

The optional `COMMONPLACE_DATA_DIR`, `COMMONPLACE_PORT`, `COMMONPLACE_PEER_PORT`, `COMMONPLACE_CAPTURE`, `COMMONPLACE_CLAUDE_BIN` and `COMMONPLACE_CODEX_BIN` variables support isolated development tests. Normal installations do not need them. Loopback ports are selected automatically when the preferred ports are occupied.

See [the native verification record](docs/plugin-native-verification.md) for historical test evidence and remaining host limitations.

## Install in Claude Code

Open **Plugins → Marketplaces → Add**, enter `diask5/commonplace-plugin`, then install **Commonplace**. In Claude Desktop use the **Code** tab's plugin settings. Start a new Code session and complete Commonplace sign-in. You do not need to install a separate runtime or run a listener.

For an existing installation, refresh that marketplace and update Commonplace. Existing connections to the previous Sites server are preserved; say **“Disconnect my old Commonplace account connection and connect Commonplace to https://34.27.253.220.”** Your local information remains on your device. Existing hosted accounts and workspaces have not been migrated to GCP; create and verify your new account before sharing a project there.

## GCP verification, September 17, 2026

The new server passed a live two-account test: managed sign-in, native PKCE consent, teammate invitation consent, shared wiki/skills, a question queued before acceptance, automatic receiving, and a follow-up after receiver restart. Private-workspace and private-wiki access checks passed. The matching ZIP passed all 17 Windows packaged integration checks. Model replies used synthetic endpoints; no paid inference or physical two-device test was performed. Daily database backups and HTTPS certificate renewal are configured. This is a public beta, not a claim that every host integration is verified.
