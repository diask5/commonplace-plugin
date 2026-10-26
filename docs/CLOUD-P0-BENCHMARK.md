# Conductor cloud P0 benchmark — 26 October 2026

The owner authorized the prepared benchmark in new Conductor cloud sessions after
the latest Mac command was denied. No Mac retry, production mutation, real-person
invitation, paid model fallback or saved global permission change was made.
[Machine-readable evidence](../implementation/cloud-p0-benchmark-verification.json)
and [portable fixture sources](../implementation/cloud-p0-benchmark/README.md)
record the original attempts and subsequent source candidates separately.

## Baseline findings

The published 0.4.28/runtime61 account service ran on loopback with synthetic
profiles, real OAuth/DCR/PKCE, disposable SQLite and the full 85-tool remote MCP
catalog. Space rules used a deterministic classifier. Actual Conductor sessions
used host defaults, ordinary prompts alone and no tool names or expected answers.
Standalone nested CLIs had failed model authentication before any product call;
those failures are preserved and do not count as product cases.

| Track | Result |
| --- | --- |
| Invitation, context, leave | Five clean passes: preview/accept, create/invite, approved context, unknown time, leave. |
| Post-leave | No context leaked and membership stayed revoked, but the model posted its query into another space with the same contributor. Scope routing failed. |
| Old invitation after leave | Separate non-model control returned 403; membership unchanged. |
| Claude retrieval | Correct facts, but called the legacy wiki outside the benchmark route and cited one planning note seen only in search. Failed. |
| Codex retrieval | Correct facts and both citations backed by reads, but also called the legacy wiki outside the benchmark route. Failed. |
| Remaining retrieval cases | Six unstarted after both host tracks stopped; no retry or permission widening. |

Both retrieval attempts completed before the observer's stop/cancel reached them.
No host denial or API error occurred in these scored baseline cases. The earlier
provider-refused private-finance prompt remains skipped. Candidate withholding
inside ordinary context requests is separate evidence.

## Source changes and candidate checks

Patch 38 adds consistent owner-selected-space guidance to native/remote MCP
instructions, tool descriptions and native skills. Missing, inaccessible, expired
or left spaces cannot be replaced merely because another space contains the same
person or topic. Ambiguous requests ask the owner which space. Three new model
cases pass: the correct space is used, a missing named space stops without a
shared write, and ambiguity causes a question with no shared write. The alternate
space in the missing-space test had an enabled policy that would allow the public
candidate, so the result does not depend on that policy withholding it.

Patch 39 clarifies archive discovery and reads: every supporting document and
final citation needs its own successful source read; snippets and failed/changed
reads do not count. Legacy wiki descriptions direct ordinary work-context
questions to the archive tools. All 85 tools, schemas, annotations and authority
checks remain. The distinct retrieval candidate passed **8/8** fresh-session cases: correction,
synthesis, source trust and unknown facts on both Claude and Codex. All 27 actual
content calls used archive tools; 16 successful source reads supported every final
citation. Root independently fetched all eight visible session traces and checked
read receipts and final citation IDs. These cases read short dated notes; the
non-model long-document/pagination checks remain separate.

Eight existing routing/sharing and 26 archive/remote tests pass. They check
regressions, not whether a model follows text instructions. The citation grader's
four self-tests accept read-backed citations and reject snippet-only, changed and
error-backed citations. The ordered 39-patch replay reproduces all 203 changed
source files. The review disposition records the native-skill wording correction
and the limits of the remote catalog.

## Release and evidence boundaries

The guidance changes are **source-only**, absent from the locally packaged
0.4.30/runtime63 diagnostics candidate, the uploaded 0.4.29 drafts and live
0.4.28. No guidance fix is claimed as installed or deployed.

The remote catalog differs from the filtered native plugin catalog. Synthetic
profiles, warmed local archives and loopback invitations cannot prove clean
Google/Desktop setup, real cross-person delivery or production latency. The
Mac connection-unavailable cause remains unknown. A separately observed invalid
archive-argument reporting issue returns JSON-RPC -32603 instead of a recoverable
tool reply; its desired behavior remains unimplemented (three TODO assertions),
and it does not establish the Mac failure cause.

Temporary project configuration restricts these disposable sessions. Claude
reported a host-selected bypass mode; no bypass flag or mode change was requested.
Project denies removed built-in file/shell routes, but SDK-injected Conductor
terminal/diff tools remained advertised. No scored file access was observed.
Allow entries are not an exclusive deny list, which is why actual tool receipts
are graded and the legacy wiki calls count as failures. All temporary project files (`.codex/config.toml`, `.mcp.json`, and
`.claude/settings.local.json`) were restored to their prior absence. All six
scored-fixture servers were stopped and listeners closed. The preparation worker
also stopped its separate fixture.

Candidate SQLite/archive roots, origin and credentials were new, with no shared
mutable paths. The deterministic synthetic owner ID repeated because the owner
tag was omitted; the fresh profile row/state was accepted as sufficient for this
isolated check, and no distinct-owner-ID claim is made. The fixture was warmed
before scoring; preflight reads were excluded.

[P0 closeout](P0-CLOSEOUT.md) continues to track live acceptance separately.
