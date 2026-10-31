# Draft v3 P0 mapping — 31 October 2026

The newly attached spec is byte-identical to
[the preserved product spec](MEET-PROXY-PRODUCT-SPEC.md), SHA-256
`1d061a660d1e280c4f33a111fdabb1c5fb8fc52a3aa4cd86ebe4fee5f396091d`.
Its section 9 contains ten P0 items. Later explicit owner instructions retain
Spaces / My context and per-space excerpt sharing as the current product; this
audit does not silently revert those changes or count them as literal fulfillment
of different requirements in the original document.

The implementation has two related paths. Native pair messaging binds exact
agents to a canonical shared thread and can carry scoped owner-agent answers.
The newer Spaces path retrieves a contributor's context privately, classifies
exact candidate excerpts, records approved excerpts with the request, and lets
the requester's existing assistant answer. Native collection supplies knowledge
to either path; collection alone does not establish invitations, audit or consent.

| Original section 9 P0 | Implementation | Evidence and remaining gap |
| --- | --- | --- |
| Google sign-in | The deployed application uses Google sign-in and preserves the selected account during native setup. | Existing-owner real Google and Desktop handoffs are recorded. Fresh-account/clean-machine completion remains unverified. |
| Attach Claude Code and Codex | Native plugin/MCP installation registers the exact host chat and enables authorized private collection. | Both real existing-owner Desktop handoffs passed. 0.4.33/runtime66 now runs on the verified Mac; 195 discovered sources completed and two fresh production reads passed. This is not every-user onboarding proof. |
| Agents list showing active connections per agent | The existing pair service/view retains agents and connection counts. The primary interface was replaced by Spaces / My context at the owner's direction. | The original agent-centric home is not the current primary journey. Space membership is not a substitute for proof that a particular agent is connected. |
| Requester- and owner-initiated natural-language invites with link/code | Exact-agent invitation tools support request/delegate directions; native Space tools create a space and invitation link. | Both pair directions have service tests. Ordinary-prompt Claude Desktop Space creation/invitation passed. Both directions across new users' default model hosts remain an acceptance gap. |
| Invite page names inviter and their agent; one-click accept | The existing pair invitation flow identifies the agents. The primary Space invitation identifies the inviter and space, then joins the signed-in account. | Named Space join is implemented and selected-account acceptance passed. It grants membership, not an exact-agent answer mandate or private-library sharing; the original selected-agent semantics are different. |
| Exactly one inbox thread per agent pair | Pair storage sorts the two agent addresses and reuses one conversation, including reverse/repeated invitations. Existing legacy scoped threads remain separate where migration cannot be proven. | Pair uniqueness has service/signed API/browser tests. A shared Space is not intrinsically one thread per agent pair, so its presence does not close this original P0. |
| Both owners read both sides of every thread | Pair messages use a shared audit readable by both owners. Space members see messages and recorded context requests/approved excerpts; private classifier checks stay contributor-only. | Selected accounts saw the same production excerpt history. An assistant's final answer generated only in its private native chat is not automatically part of the Space exchange audit. Full two-agent Q/A must use the shared message path. |
| Responses never expose underlying sources | Pair answer mandates require sanitized answers and deny peer access to private archives. The newer Space path deliberately returns classifier-approved verbatim excerpts while withholding source titles and private checks. | The excerpt path does not satisfy the original answer-only wording of section 7.9. Approved excerpts are an intentional disclosure under the later sharing model, not a proof of original-spec nondisclosure. The pair route also still needs broader adversarial actual-host acceptance. |
| Agents inherit and cannot exceed owner tool access | Authenticated account/device scopes, exact chat binding, owner consent and native host approvals remain authoritative. Peer requests cannot grant new tools or change permissions. | Host denials stopped dependent work, and upgrades preserved saved permissions. Tests support these boundaries; not every host configuration has been certified. |
| Either side can sever | Either pair owner can sever; Space members can leave and owners can remove/archive. Rules can be paused and invitations revoked. | Pair tests stop new sends/pending dispatch while retaining shared audit. Selected-account production removal rejected requests/activity and old invitations. Recipient default-host behavior after revocation remains unverified. |

For Sam asking about Zane's work, the current Space flow is: native collection →
private relevant-source retrieval → all-rule excerpt checks → approved shared
exchange → Sam's assistant answers. It can answer from saved context while Zane
is unavailable, but it does not by itself prove a conversation with Zane's exact
selected agent, a complete shared record of both agents' final messages, or
answer-only disclosure.

Literal Draft v3 acceptance would need the canonical pair/answer path to retain
all shared Q/A and keep retrieval evidence on the contributing side. Final
answer disclosure and authority must be checked before sending. This is a
remaining architectural distinction, not a code change authorized by this audit.
The later Spaces instructions remain in effect.

## Verified progress and open gates

- [Context uploading](BOUNDED-SYNC-CATCHUP.md): live on the configured Mac,
  including persistent startup and two successful fresh source reads. Remote
  MCP-only connections still do not collect website-only Claude/ChatGPT history.
- [Sharing stress](SHARING-STRESS.md): 8/16 permitted candidates withheld,
  3/7 answerable query phrasings missed, and 30 provider 429s in a 40-call burst.
  These failures remain; current syncing does not resolve them.
- [Selected-account acceptance](PRIVATE-NATIVE-TITLES.md): successful public
  sharing, private withholding, shared history and revocation are recorded with
  their account/API/browser scope. They are not an independent-human walkthrough.
- [Native setup](CROSS-HOST-CONTEXT-SYNC.md): fresh-host onboarding and the prior
  Claude setup approval remain open. No denial is retried or bypassed here.

Time/topic boundaries and direct email/iMessage invitation delivery are P1 in
section 9. Later owner requirements make sharing rules central to the current
product, but this does not relabel those original P1 items as original P0s.
No new production calls, tests, invitations, permission changes or architecture
changes were performed for this mapping. Existing receipts and source paths were
reviewed. All-P0 acceptance remains open.
