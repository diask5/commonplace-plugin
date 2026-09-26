# Commonplace Files 0.1.0

Versioned cloud folders for people and their agents. Each agent gets a private working copy. Edits stay private until an authorized task publishes them; teammates receive shared changes at the next clean task or explicit sync.

## Install

In Claude Code's Plugins manager, add marketplace **diask5/commonplace-plugin**, refresh it, and install **commonplace-files**. Start a fresh session after installation. **Node.js 22.13 or newer must be on PATH.** This Files package does not bundle Node.

The [release archive](https://github.com/diask5/commonplace-plugin/releases/download/files-v0.1.0/commonplace-files-0.1.0.zip) also contains Codex and Claude plugin manifests, a standard MCP entry point, and host setup instructions in its README. Extract it to a permanent location for direct MCP configuration. Existing Commonplace identity is reused; account setup is needed on a new machine.

Then ask your agent:

> Open Project in Commonplace Files, update status.txt, and share the change.

The agent opens its own copy, refreshes and pins the task, verifies edits, runs the folder's configured checks, and publishes. For a private edit, say “Keep this private.” Reading the latest shared version preserves existing drafts. On Windows, “Open Project as a drive” uses the built-in WebDAV client; chat-only hosts can use the Files tools.

## Verification and limits

The full suite passed 365 tests. Actual Claude Desktop Code tests on Windows covered mounting, shorter-file save and checked publication, private drafts, reading shared contents without overwriting drafts, and releasing tasks before answering. An independent installed client verified exact bytes, unchanged unrelated files, cloud-save state, and draft recovery after restart.

The plugin guides Windows saves up to 512 KiB through Files write/read tools. Native editors that replace a file by renaming a temporary file can still report stale WebDAV metadata; this release does not fix arbitrary editor compatibility. Larger-file native behavior and macOS/Linux native mounting are not established by these tests. Notifications do not wake idle agents. Shared folder checks establish only the checks actually configured.

The archive contains 113 client files, including runtime dependencies and skills. It excludes backend source, tests, credentials, and account data. See the [release](https://github.com/diask5/commonplace-plugin/releases/tag/files-v0.1.0) for the SHA-256 checksum and verification summary.
