# Agent launch links and server verification

Staging update `20261025-agent-launch-v2` adds app launch actions to **Add an
agent → Connect Claude or Codex**. The page shows its server origin and builds
the request for its signed-in account. Existing chats use **Copy setup request**.

| App | Link | What the user does next |
| --- | --- | --- |
| Claude Desktop Code | `claude://code/new?q=…` | Choose a folder, review the request and send. Copy it if this app version does not fill it in. |
| Claude Code terminal | `claude-cli://open?q=…` | Review and press Enter. Requires a registered Claude Code URL handler. |
| Codex | `codex://threads/new?prompt=…` | Review the prepared composer and send. |
| Conductor | `conductor://prompt=…` | Choose a repository and create the workspace. |
| Claude Code in VS Code | `vscode://anthropic.claude-code/open?prompt=…` | Review the extension's draft and send. |
| Codex selection, VS Code | `vscode://agents/new?prompt=…` | Select Codex in the Agents draft before sending. |

The links use a direct click without asynchronous clipboard work, which keeps
browser activation intact. No directory, SSH target, thread ID or host permission
is fabricated. Launching does not establish a connection. Confirmation requires
selection of an agent returned by this server for the current signed-in owner.

The user-reported agent was absent from staging on 25 October 2026. The Mac's
default active profile pointed to `https://34.27.253.220`, with the same Google
account used in staging. This explains why its prior setup answer could not
confirm a staging connection. No existing profile was moved or reset.

The revised prompt checks both server and account before registration, preserves
mismatches and reports unavailable origin information as unverified. The source
also adds `account.serverOrigin` to `setup_status`, from the active profile only.
It rejects URLs with credentials, paths, queries or fragments. This native plugin
change is tested source only; it is not installed on the user's Mac or published.
An already connected production plugin still needs a supported separate staging
profile before this staging walkthrough can complete.

Verification: 20 focused browser/setup tests passed, including exact URL encoding,
unusual account characters, account switching, clipboard denial, keyboard
activation, mobile overflow, accessibility, reload recovery and server-origin
redaction. The two deployed UI files were checked against their previous hashes;
the public script matches source and the staging page has no browser errors.
The first deployment restored its previous files after a short health-check
timeout. The second allowed staging's normal startup time and passed.

Native app launch and full real-account staging attachment remain unverified.
Browser tests intercept protocol navigation and do not start actual host chats.
Production's release and the installed plugin remain unchanged.

The original RC3 artifacts are preserved. Apply
`implementation/agent-launch-and-server-check.patch` after the original source
patch; its manifest records all five changed source/test files. The patch was
applied to the before snapshots and compared byte for byte with the result.

Official protocol references checked on 25 October 2026:

- https://code.claude.com/docs/en/deep-links
- https://code.claude.com/docs/en/desktop#open-an-ssh-session-from-a-link
- https://code.claude.com/docs/en/vs-code#launch-a-vs-code-tab-from-other-tools
- https://learn.chatgpt.com/docs/reference/commands#deep-links
- https://conductor.build/docs/reference/deep-links
- https://code.visualstudio.com/docs/configure/command-line

Claude Desktop's documentation describes the new-session route and its `q`
parameter in the SSH section. Local prefill has not been exercised on the user's
installed version; the UI provides an explicit copy fallback.
