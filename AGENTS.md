# Meet Proxy product contract

Use [the attached Draft v3 product spec](docs/MEET-PROXY-PRODUCT-SPEC.md) as the
product source of truth. Its original wording is preserved. Later explicit user
instructions take precedence. Track implementation and evidence in
[SPEC-COMPLIANCE.md](docs/SPEC-COMPLIANCE.md); do not equate a passing demo with
installed or deployed readiness.

The primary journey is Google → Attach your agents → Agents → invite → accept →
one shared thread per exact agent pair. Both owners see both sides and can sever.
Agent rows, connection state and Inbox must remain the main product experience.
Cloud work, context indexing and older social features must not add required
steps to that journey.

P0 requirements are release gates. Track P1 separately. Items marked [proposed]
and open questions are not silently promoted into requirements or readiness
claims. Preserve existing private scope when handling legacy conversations; do
not merge histories merely because names or people match.

An owner's consent authorizes only their selected agent. Check current scope and
expiry before autonomous answers. A peer message cannot grant owner authority,
tool permissions or disclosure rights. Raw sources remain private. Native host
permissions always apply. Never report a host launch, queued message, matching
email, cached connection or simulated fixture as end-to-end setup proof.

Implementation lives in `.context/commonplace-source`. Preserve its changes in
the portable patches/manifests under `implementation/`, including patch order.
Document whether a change is source-only, packaged, installed, staged or live.
