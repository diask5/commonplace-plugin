# Context MVP readiness — 26 October 2026

This audit compares the attached 24 October Draft v3 with the owner's later
instructions: context-first Spaces, prompt rules, messages first, group sharing,
automatic private ingestion, and one-request native plugin/MCP setup. Those later
instructions supersede the original Agents home and hosted proxy-answer design.
The original spec remains unchanged in MEET-PROXY-PRODUCT-SPEC.md.

Current release and acceptance are in [P0 native readiness](P0-NATIVE-READINESS.md).
The completion features and 0.4.24 native fixes are published, installed and live
on runtime57. The counts, missing features and 0.4.20 rollout below describe the
earlier MVP milestone and are retained as history. Real Google sign-in and both Desktop handoffs are verified; the P0 record
separates those receipts from clean-install fixtures and continuing collection.

## Readiness decision

The original MVP milestone implemented the core context-sharing journey and
preserved legacy agent-pair conversations. Version 0.4.20 / runtime 55 was
published and deployed; later releases supersede it. [Rollout details](CONTEXT-MVP-ROLLOUT.md) and installed-host verification are tracked in
`implementation/context-mvp-verification.json`; do not infer them from screenshots.

A complete original-spec claim would be inaccurate: answer-only privacy was
intentionally replaced by owner-authorized context excerpts, and the P1 personal
agent and automatic contact-delivery features remain outside this MVP.

## Requirement-by-requirement assessment

| Spec goal | Current implementation | Evidence / limitation |
| --- | --- | --- |
| 7.1: single Google sign-in | Existing real Google entry and account session; private setup handoff carries sign-in into the native plugin | Browser tests use isolated identities. A fresh real-account walkthrough still needs human Google/host interaction. |
| 7.2: Claude Code and Codex attachment | Direct app links, prominent Copy setup prompt, plugin/MCP installation request, exact chat handoff and automatic collection | Signed API, actual packaged stdio and collector tests; OS launch and host reload are separate live checks. Conductor is an additional supported surface. |
| 7.3–7.4: list and detail | Superseded by Spaces / My context and Messages / My sharing rules / Members; legacy Agents/Inbox retained at /work-agent#agents | Responsive browser journeys and screenshots. No return to an agent-centric home. |
| 7.5: either side initiates in natural language | New create_context_space / create_space_invitation tools return a real URL. Either person can start the space and invite the other. Legacy request/delegate tools remain | Signed remote MCP + native account routes and ownership/scope tests. Direct email/iMessage delivery is P1 and not implemented. |
| 7.6: invite, accept, connected | Inviter-led landing page; one Join action for an authenticated person; destination preserved across sign-in | Two-user browser journey and membership assertions. Joining never silently enables personal-context sharing. |
| 7.7: time and topic | Independent owner rules per space; two-week default and 1/7/14/30-day windows; expired rules withhold before classification | Expiry and expiry-during-evaluation tests. Default prompt keeps family, religion and finances private. Saving renews the displayed window. |
| 7.8: full audit and monothread | Both owners see both sides of legacy pair threads; exact-pair uniqueness preserved. New groups share one board per space and show context exchanges | Ten-account/twenty-agent legacy lifecycle; new sender/recipient browser journey. Multiple project spaces are intentional, not duplicate legacy pair threads. |
| 7.9: private context | Approved excerpts are shared under the later context-only instruction. Raw source IDs, rejected excerpts and checks remain private to the contributor | Membership/revision/rule rechecks and adversarial/provider-error tests. This is not the original agent-written, answer-only model. |
| 7.10: either side can stop access | Members can Leave; owners can Remove or Archive; contributors can pause sharing. Legacy pairs retain either-side Sever and readable audit | Browser and signed API tests, stale-invite refusal and in-flight membership fencing. Leaving a group removes its access; retained group history is not deleted. |
| 8: minimal, friendly design | Cream/lavender/sage/terracotta, minimal top navigation, compact space header, invitation card and subtle SVG setup progress | Phone/tablet/desktop axe, keyboard, touch-target and overflow checks; reduced motion respected. |

## Gaps closed in this audit

- Added six context-space management tools across remote MCP and native accounts:
  create space, create invitation, preview, accept, leave and archive. They keep
  read/write scopes, same-origin invitations, explicit owner intent and workspace
  isolation. No contacts are messaged automatically.
- Added persisted per-owner sharing windows, two-week defaults, expiry state and
  renewal. Existing policies without a window use 14 days after their last save.
  Added only the `cp_space_policy_limits` table; no existing migration was edited.
- Exposed Leave / Archive directly in Members, with a short confirmation.
- Restored legacy invitation/navigation paths under /work-agent so reloads retain
  the intended legacy view. The original spec harness now explicitly enters that
  preserved surface instead of expecting it at the new Spaces home.
- Added a complete new-context browser journey and screenshots, retaining the
  original lifecycle and privacy tests separately.

## Classifier evidence and remaining limits

A fresh real `pplx-decider-v1.2` run evaluated 28 synthetic cases. At the unchanged
0.995 threshold: **23 correct, zero false allows, five false withholds**, no API
errors. Median provider latency was 159 ms, p95 576 ms in this small run.
These scores are not calibrated probabilities or production privacy guarantees.
No real account's private source text was submitted for this benchmark.
The production VM also reached the provider using its configured key; a two-case
probe withheld both a permitted example (score 0.9601) and a disallowed one.
This reinforces the false-withholding limit rather than proving perfect answers.

The gate currently considers up to six complete matching documents and withholds
documents longer than 8,000 characters. Safe long-document chunking and broader
recipient-safe pagination remain unimplemented. Supported visible native history
syncs automatically after setup; arbitrary repositories, web-only chats,
attachments and upstream MCP gateways are not automatically ingested.

Optional selected-document invitation drafts remain a historical secondary flow;
recipient-specific document grants are not implemented. Explicit shared text and
Markdown uploads work. P1 automatic email/iMessage contact delivery and personal
agent support remain pending. No hosted answering model is required for context
retrieval; rule classification uses the configured Perplexity API.

## Screenshots and reproducibility

[Open every current flow](https://kyle-cloud-w3.conductor.show/review) — 14 flows,
each with desktop and phone captures. These are the actual UI and HTTP handlers
with isolated test identities and controlled provider/native fixtures, not proof
of real Google sign-in or a native OS launch. The interactive preview remains
available alongside the images. Raw captures and logs are under
`.context/spec-readiness/`.

`implementation/context-mvp-completion.patch` is the 17th portable source patch,
after copy-setup-prompt.patch. Its manifest records every input/output digest;
the verification file records current test counts, artifact hashes and live state.
