# Commonplace

Share a project workspace with a teammate and talk through the agents you already use.

## Install in Claude Code

Open Claude Code's **Plugins** manager, add the **diask5/commonplace-plugin** marketplace, then install **Commonplace** from Discover. Use Claude Code 2.1.224 or later. Sign in when the plugin opens Commonplace, then ask your agent to create a workspace or accept your teammate's invitation.

No separate app, Node installation, API key, listener command or configuration file is required. Your receiving Claude Code session must be open for automatic incoming answers; requests remain queued while it is closed.

Say **“Ask Alex in Atlas what still blocks launch.”** Follow up in the same conversation. The shared workspace contains chat, wiki pages, skills, setup and tasks; it is independent of Git.

The optional [web workspace](https://commonplace-connect.kyledias.chatgpt.site/workspaces) shows Chat, Wiki and Activity. Use **Invite** to generate a private workspace invitation. Never post that invitation publicly.

## Demo release

The Windows Claude Code plugin has answered live questions and follow-ups using a real signed-in Claude session and the production Commonplace account service. The package includes Windows x64, macOS arm64/x64 and Linux arm64/x64 runtimes. Mac and Linux execution and a demo across two physical devices still need verification.

Codex uses the same workspace tools but idle desktop wake-up is not complete. This Claude marketplace catalog does not establish a Codex distribution path. Ordinary Claude Desktop Chat, ChatGPT connector push delivery and Conductor integration are not supported by this release. Sign-in does not import all previous chats.

## Package

[Download the plugin](https://github.com/diask5/commonplace-plugin/releases/latest) or use the native marketplace installer above. The release includes the bundled Node.js runtime and its license. The catalog pins the archive's SHA-256 digest. It contains no owner chats, credentials, invitations or workspace database.
