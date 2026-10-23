# Native code verification — candidate 0.4.17

Candidate 0.4.17 fixes failures found while exercising real cloud questions
against a separate, owner-authorized native Claude Code session. It is prepared
for further live verification; the results below do not establish universal
automatic wake or production repeatability.

## Changes

- If the relay commits a dispatch receipt but its response is lost before host
  submission, the adapter releases only the still-valid claim for retry.
  Ambiguous host submissions continue to require reconciliation.
- Bounded per-chat diagnostics identify the failed delivery stage. Empty polls
  preserve failure evidence; stored diagnostics omit text, tokens and raw errors.
- Native reply calls validate their documented arguments before network traffic.
  A body passed as `message` instead of `text` now produces an actionable error.
- History readers accept filesystem aliases above a root, including macOS
  `/var`, while rejecting linked roots and escaping files.
- Portable fixtures preserve production container ownership rules. Additional
  regressions keep cancelled cloud tasks final when late replies arrive.

## Verified

The source is in [implementation PR #11](https://github.com/diask5/commonplace-session-tests/pull/11).
[CI](https://github.com/diask5/commonplace-session-tests/actions/runs/39743051945)
passed 334 application tests, 49 browser/UI tests, 12 deployment checks,
dependency audit, package integrity, packaged transport and runtime packaging.
The packaged transport uses synthetic identity and host sockets; it does not
prove a real native GUI wake.

A real production cloud task previously woke an idle native chat, received
fresh repository inspection and test results, resumed automatically and cited
that evidence. A subsequent delivery became uncertain and remains preserved.

The isolated 0.4.16 candidate also woke automatically and ran 78 selected Mac
tests successfully, but its reply failed because the agent supplied the wrong
argument name. After the validation fix, a supported reload and coordinator
correction, the same native agent sent its evidence and the original cloud task
resumed. This is assisted recovery, not an unattended pass. Loaded 0.4.17,
companion revision 51, the original stable agent and existing account were
verified. Another fresh unattended consultation was then queued to inspect
delivery recovery and run the complete Mac application suite.

## Still to verify

- Completion and repeatability of fresh unattended consultations on 0.4.17.
- Final results of the full Mac suite through the native consultation.
- Installation of the published package through the normal plugin manager.
- Conductor's separate queued-turn wake behavior: a queued or accepted host
  message has not consistently started its intended chat.

The Mac control tool stopped returning during the latest observation, even for
a simple clock command. This prevents a current final-state claim; it does not
prove the Mac or native task is offline. Existing accounts, permissions,
bindings and uncertain messages remain unchanged. No new sign-in or automatic
uncertain-delivery replay was used.
