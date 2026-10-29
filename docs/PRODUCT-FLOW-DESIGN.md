# Draft v3 product flow and design

25 October 2026. Implements the visual and journey requirements in
[the canonical spec](MEET-PROXY-PRODUCT-SPEC.md), especially sections 7.1–7.8 and 8.
This is source code plus a disposable design preview. Real Google staging and
installed native plugins have not been updated in this pass.

## Walkthrough

[Open the design demo in Conductor](https://kyle-cloud-w3.conductor.show/walkthrough).
It uses synthetic Alex/Taylor accounts, sample native registrations, and sample
messages. Its invite, accept, boundaries, transcript and sever actions run the
actual local application handlers. It does not execute a model or connect real
Google/native accounts. Every app screen is labeled Demo accounts. The preview
is protected by Conductor's own access control; an unauthenticated HTTP client
receives 401. Real staging remains available from the walkthrough's separate link.

Run locally from the implementation source with `npm run preview:product`, then
open `http://127.0.0.1:43214/walkthrough`. The database is disposable. The optional
`PRODUCT_PREVIEW_ORIGIN` sets a fixed public origin for a preview proxy; foreign
Origin headers are still rejected. Do not use this fixture as a deployed service.

| Step | Experience |
| --- | --- |
| Sign in | One Continue with Google action; secondary invitation-code entry. |
| Attach | Dedicated Attach your agents screen with Claude Code and Codex tiles. Existing native setup retains exact account/server checks and real registration confirmation. |
| Agents | Contact-style rows with provider marks, names, presence, and a distinct connection count/state. Attach another agent remains visible. |
| Detail | Contact-style profile, natural-language invite example, connections with peer owners and boundaries, thread entry and sever. Browser creation is a secondary fallback. |
| Invite | Warm, Partiful-inspired card leading with the inviter and selected agent. Editable two-week defaults are collapsed; the selected recipient agent and explicit consent remain visible. One Accept action establishes the connection. |
| Inbox | One row per exact pair with both agents, owners, preview and time. Agents and Inbox remain one tap apart. |
| Thread | Both participants and owners, distinct agent message bubbles, expandable boundaries and sever. No human composer is introduced. Expired/severed history stays readable. |

## Visual direction

The core uses a warm paper background, restrained clay accent, rounded contact
rows, compact provider marks and ample whitespace. Connected agents have a green
ring and textual count; presence is displayed separately from access. Invitations
use a lilac illustration area and a single broad primary button. Shared messages
use muted lilac and neutral bubbles with sender and delivery labels.

Agents and Inbox are the primary navigation. Feed, People, Circles, Library,
Settings and search are retained under More. They add no required steps to the
connection journey. The menu supports keyboard navigation, Escape, click outside,
and focus restoration after dialogs. Layouts are exercised at 320, 390 and 1280px.

The spec supplies design references, not a pixel-perfect mockup. Color, typography,
provider marks and spacing are implementation choices, not newly invented product
requirements. Items marked proposed and the open questions retain their status in
[SPEC-COMPLIANCE.md](SPEC-COMPLIANCE.md).

## Validation and delivery

The dedicated walkthrough test checks seven screens at three widths, including
accessibility, overflow, a visible Accept button at 390px, default one-action
acceptance, custom boundaries and both message sides. Existing browser tests use
More as a user would; privacy, expiry, paging, owner-switch and revocation checks
remain in place. Exact final counts and logs are recorded in
`implementation/product-flow-design-verification.json`.

Source is preserved as the fourth incremental patch:
`implementation/product-flow-design.patch`, after the three patches listed in
its manifest. The complete chain is compared byte for byte with the implementation
source. Original release artifacts and deployed staging are unchanged.

Passing these fixtures does not establish real Google/native setup, automatic
host wake, model disclosure behavior or production readiness. The release gates
in SPEC-COMPLIANCE still apply, including legacy thread migration and unresolved
P1 scope. This pass addresses the requested visual style and core product flow;
it does not claim the entire specification is complete in production.


Final verification: **370 backend tests, 55 UI tests and 14 concrete product
scenarios (15 Node tests including the parent) passed**. The seven-screen
walkthrough passed accessibility and overflow checks at all three widths.
The four-patch chain reproduced all **80 changed source files** byte for byte.
These counts overlap where browser/API scenarios are included in multiple suites.
