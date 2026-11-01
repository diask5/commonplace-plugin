# Automatic startup and guarded update activation

1 November 2026. Patch 62; candidate native 0.4.38/runtime71.

## Problems reproduced

The selected cloud chat was signed into a different account from the Mac and was
not a member of Work. Installing on the Mac did not update the cloud runtime.
Recurring collection and mirroring kept the old companion's restart guard busy.
A newer client then tried to launch competing daemons instead of keeping the
working connection usable. Conductor's persistent receiver did not emit the
Personal startup observation when the host omitted CLI hooks. Setup instructions
still recommended a second computer for a different account.

## Changes

- The supported companion restart now drains recurring work for up to two minutes.
  Running foreground jobs retain their guard. A deadline resumes scheduling.
  Mirroring stops between pages and retains the last complete generation.
  Collection consent, saved sync choices, pending uploads, and exclusions stay intact.
- Clients keep a busy older connection usable and retry activation in the background.
  LaunchAgent replacement waits until the companion has safely upgraded; periodic
  plugin checks finish the launcher update afterward.
- Conductor's existing receiver reports a fixed startup observation to Personal,
  with account, capture and scope fences. It does not send transcript text as a
  progress observation or infer task completion.
- Setup uses the supported linked-account tools when available. Existing used chats
  retain their account; server mismatches stop setup. GUI guidance uses browser
  activation rather than an unavailable terminal reload command.

## Verification

Five new regressions fail on the previous source and pass with the changes.
The core suite passes 695 tests, setup/browser/account checks pass 53, focused
checks pass 46, mirror checks pass eight, and the final drain/resource checks pass
21. Counts overlap; do not add them. Exact ordered replay of all 62 patches matches
246 changed files. Package, installation and deployment results are tracked in
`implementation/oob-activation-verification.json`.

The owner-authorized Work repair accepted membership and selected this actual
cloud chat as its receiving side. A synthetic message was saved and read through
the other selected account's signed space-activity API. This proves shared history
between those accounts, not independent-human acceptance or execution by the
currently running Bland chat. The other participant's receiving side was not moved.
No private sharing was enabled.

## Limits retained

The already-running older Mac companion initially continued to return HTTP 409
from its supported restart. No process signal, host permission change, or account
replacement was used to defeat it. Old loaded plugins and active runtimes are
reported separately from package installation. Remote MCP retrieves existing
context; it cannot collect web-only Claude or ChatGPT history. Shared-space
membership does not publish everyone's private transcript or relax the classifier.
Do not claim all-host out-of-box readiness from these tests.
