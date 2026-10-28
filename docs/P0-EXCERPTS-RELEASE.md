# Visible context and exact message excerpts — 28 October 2026

Meet Proxy **0.4.32/runtime65** is published. Server
**20261028-native-excerpts** is live, with all 159 files verified and readable by
the service account. The three services are healthy; migrations are unchanged.
Runtime65 is active on the owner's Mac from the checksum-verified package.
Permanent plugin registry updates and production sharing acceptance are in progress.
This release does not close every P0 gate.

## Fix

Patch 43 rejects Claude API-request/debug envelopes before inspecting nested
roles. Both collectors migrate to format 3 and recapture existing sources. A
pending upload from the old parser is reconciled without replaying its old text.

Patch 44 uses structured native-message boundaries for complete conversations up
to 16,000 characters. Each candidate is an exact stored message body, at most
8,000 characters. The entire conversation remains private classifier evidence,
including confidentiality instructions in other turns. The serialized projection,
title and source revision must match the pinned archive. Conflicts withhold;
larger sources retain the existing bounded handling. Source offsets stay private.

Patch 45 packages these changes as 0.4.32/runtime65. There are no changes to the
0.995 threshold, classifier prompt/model, owner rules, permission settings,
membership checks, tool schemas or database migrations.

## Verification

- 604 core tests and 45 focused excerpt/policy tests pass, with no failures.
- Both native aliases pass package integrity checks. Packaged stdio/signed-HTTP
  onboarding smoke passes; Google identity and host sockets there are test doubles.
- Extracted-server HTTP, PKCE, resource reads, read-only write refusal and foreign
  origin checks pass with a disposable profile and placeholder compiled page.
- All 45 ordered portable patches replay exactly across 206 changed files.
- A real Perplexity diagnostic on synthetic state allows the latest public answer
  at 0.995085 and withholds finance and confidential-context examples. This one
  near-threshold sample does not establish robust calibration or live acceptance.
- The Mac handoff respects the active-work restart guard, preserves account and
  saved permissions, and resumes all temporarily paused plugin processes.
- A runtime65 source read returns all four visible Larkspur turns, four citations,
  the corrected date, and no host envelope, at revision 6356.

The initial production sharing request returned `unavailable`, with zero excerpts
and owner-only reason `request_stopped`, during ongoing collector migration. That
reason does not identify the cause or establish whether classification began.
The attempt remains evidence; it is not a successful sharing result.

## Artifacts and remaining acceptance

[Native release](https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-v0.4.32)
and [server release](https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-server-20261028-native-excerpts)
preserve earlier release assets. Exact hashes, test receipts and activation state
are in [candidate verification](../implementation/p0-excerpts-candidate-verification.json).

Live public sharing, private withholding, both-sided audit, removal/leave and old
invitation acceptance are being checked with the owner's two selected accounts.
This is distinct from independent-human acceptance and clean-machine Google/native
onboarding. Existing open native chats can retain older loaded plugin versions.
The [recorded walkthrough](CLAUDE-DESKTOP-DEMO.md) retains its original failure and
has not been relabeled as a successful classifier-sharing demonstration.
