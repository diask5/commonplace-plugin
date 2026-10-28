# Private native titles — 28 October 2026

Patch 46 keeps native source titles in private classifier evidence and uses
“Shared excerpt” as the recipient-facing heading. The exact message body and the
complete surrounding conversation remain unchanged. A title carrying a
confidentiality restriction remains available to the classifier. If the title
plus conversation exceeds the existing 16,000-character bound, the candidate is
withheld. Owner-only audit retains the original title.

The live 0.4.32 server withheld the current public Larkspur answer at 0.969888.
An isolated comparison reproduced that score exactly. Moving its private title
out of the proposed disclosure raised the current answer to 0.996158. The cutoff
remains 0.995; model, prompt, owner rules and authority fences are unchanged.
Five negative examples were withheld, including finance, mixed text, title-only
confidentiality, a confidential earlier turn and an injected permission claim.
The title-only sample scored 0.994216: these few samples do not establish
calibrated safety or general reliability.

The candidate changes only two account-server modules. Native 0.4.32/runtime65
and its published artifacts remain unchanged. All 606 core tests pass; 46 ordered
patches replay exactly across 206 files. The extracted server passes HTTP/OAuth,
resource, read-only write-refusal and origin checks using a synthetic profile.
The compiled authorization page in that smoke test is a placeholder.

Server `20261028-private-titles` is published and deployed. All 159 files are
verified/readable and all three services are healthy. A signed request from the
second selected account shares the current public answer at 0.996158 without
the private title. Three other requests returned `unavailable`, including two
private-content requests; their generic `request_stopped` audit does not establish
the cause or a successful privacy check. An owner-only production diagnostic
classified all 12 private-query candidates and withheld all, but that does not
replace the failing signed request path. Patch 47 was then prepared to add bounded
request diagnostics; its deployment and subsequent checks are recorded below.
[Exact evidence](../implementation/private-native-titles-verification.json).
Earlier failures, source-overlay benchmarks and recordings remain preserved.


## Bounded diagnostics and selected-account acceptance

Patch 47 is published and deployed as `20261028-sharing-diagnostics`, changing
only the request module from the private-title baseline. All 159 files are
verified/readable, three services healthy, migrations unchanged. All 607 core
tests pass and 47 patches replay exactly across 206 files. Stopped requests retain
only phase and deadline/source/authority-change booleans in owner-only audit.
These observations do not infer causes, expose error bodies or change the
recipient response, deadline, retries, classifier or authorization rules.

The first signed request on this diagnostic release completed: all 12 candidates
for the private budget/audit query were below threshold, with zero excerpts.
That closes this selected case, not the cause of the three earlier unavailable
requests. The requester reads the same approved public excerpt as the owner,
without private checks. The owner then removed the second account through the
browser confirmation; subsequent request/activity returned 404 and reuse of the
old invitation returned 403 before the link was separately revoked.

The policy is paused at revision 2, invitations revoked, and the temporary space
archived. These are the owner's two existing selected accounts, not an independent
human or clean-machine test. Native default-host invitation routing remains a
separate gate. [Exact final receipts](../implementation/space-request-diagnostics-verification.json).


The additional ordinary-prompt Claude Desktop check also passed native
`create_context_space`, `create_space_invitation`, and `archive_context_space`
without host denial or model overrides. The second selected account previewed
and accepted the native-created invitation through signed API calls. Following
native archival, a new context request was rejected (404) and the old invitation
was rejected (404). No private-sharing opt-in was invoked, and the added test
space is archived. Recipient-host model acceptance remains distinct from this
API check. [Native lifecycle receipts](../implementation/p0-native-space-lifecycle-verification.json).

[Updated narrated recording](P0-LIVE-VIDEO-UPDATE.md) preserves the original video
and its failures. The update covers actual Desktop source-read review, browser
sharing, withholding and removal; the later native invitation check has separate
receipts and is not claimed as part of that footage.
