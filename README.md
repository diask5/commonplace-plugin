# Commonplace

Share a project workspace with a teammate and talk through the agents you already use.

## Install in Claude Code

Open Claude Code's **Plugins** manager, add the **diask5/commonplace-plugin** marketplace, then install **Commonplace** from Discover. Use Claude Code 2.1.224 or later. Sign in when the plugin opens Commonplace. Your local history is captured automatically. Ask your agent to import it; it can build the wiki in the current signed-in session. For a shared project, ask your agent to create a workspace or accept your teammate's invitation.

No separate app, Node installation, API key, listener command or configuration file is required. Your receiving Claude Code session must be open for automatic incoming answers; requests remain queued while it is closed.

Say **“Ask Alex in Atlas what still blocks launch.”** Follow up in the same conversation. The shared workspace contains chat, wiki pages, skills, setup and tasks; it is independent of Git.

The optional [web workspace](https://commonplace-connect.kyledias.chatgpt.site/workspaces) shows Chat, Wiki and Activity. Use **Invite** to generate a private workspace invitation. Never post that invitation publicly.

## Demo release

The Windows Claude Code plugin has answered live questions and follow-ups using a real signed-in Claude session and the production Commonplace account service. The package includes Windows x64, macOS arm64/x64 and Linux arm64/x64 runtimes. Mac and Linux execution and a demo across two physical devices still need verification.

Codex uses the same workspace tools but idle desktop wake-up is not complete. This Claude marketplace catalog does not establish a Codex distribution path. Ordinary Claude Desktop Chat, ChatGPT connector push delivery and Conductor integration are not supported by this release. 

## Your private wiki

Connecting imports local Claude Code conversation text and saved project notes into a private **My knowledge** workspace using your local Claude or Codex login. Open Wiki to browse topic pages and source evidence, and Chat to ask about them. Ask your agent to show Commonplace import status for progress and the link, or pause chat import. This does not import claude.ai or ChatGPT cloud history. Your companion must be running to process and answer. 

Already installed? Update Commonplace in Claude Code's Plugins manager and start a new Claude session. No separate app or command is required.

The existing 128-document workspace limit is reported without truncating local work; simultaneous first installs on different machines can create duplicate private workspaces.

## Package

[Download the plugin](https://github.com/diask5/commonplace-plugin/releases) or use the native marketplace installer above. The release includes the bundled Node.js runtime and its license. The catalog pins the archive's SHA-256 digest. It contains no owner chats, credentials, invitations or workspace database.

## If Claude says chat uploads are disabled

Update Commonplace in Claude Code's Plugins manager and start a new Claude Code chat. Say **“Import my local Claude Code chats into my Commonplace wiki and show the import status.”** The current plugin exposes `chat_import_status` and `import_chat_history`. If those tools are absent, the session has not loaded the current importer.

An older raw-upload capability is disabled; local chat import uses the workspace API instead. The cloud can show pages from another connected device even while this device has not imported anything. Check the device name on its import-status page. Hosted claude.ai and ChatGPT history are not imported.

## Install in Claude Desktop (Code tab)

Open **Customize → Plugins → Add → Add marketplace → Add from a repository**, select `diask5/commonplace-plugin`, and click **Sync**. Add **Commonplace** from that marketplace and start a new local Code conversation. If an old `commonplace-local` copy is installed, disable that duplicate. This installation path was exercised through the Windows Desktop UI.

Version 0.2.1 also discovers local Desktop agent transcripts on Windows and macOS, including Windows Store installations, and respects `CLAUDE_CONFIG_DIR`. It imports transcript folders, not neighboring app configuration. A real Windows scan found 46 conversation files including 25 previously missed Desktop transcripts. Mac fixtures pass, but a physical Mac upload has not been verified. The native Desktop test confirmed capture but exposed a separately unauthenticated CLI. Version 0.2.2 adds resumable processing in the current signed-in agent through next_import_batch and complete_import_batch, with no terminal login. Full native generation is still being verified; installation success alone does not prove wiki generation.

## Import recovery in 0.2.3

A malformed wiki outline or topic response can be corrected without losing completed batches. Resume also recovers interrupted checkpoint writes, and an unchanged or empty scan does not prevent later chats being discovered. Account changes stop the pending resume. The full local suite passes 210 checks; physical Mac upload is still unverified. The plugin uses the model selected in your agent: choose your preferred model before a large import.
