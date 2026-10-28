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
replace the failing signed request path. Bounded request diagnostics are being
prepared as patch 47.
[Exact evidence](../implementation/private-native-titles-verification.json).
Earlier failures, source-overlay benchmarks and recordings remain preserved.
