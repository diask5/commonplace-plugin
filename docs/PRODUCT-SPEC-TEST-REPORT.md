# Product-spec demo verification

Historical RC3 results. See [current spec compliance](SPEC-COMPLIANCE.md) for
the subsequent source alignment and owner-consent integration. These original
counts and limitations are preserved as evidence of that earlier build.

25 October 2026 · Candidate **0.4.19-rc.3** · Draft v3 product specification.

This tests application behavior with ten disposable people and twenty agent
addresses. Sam Demo and Zane Demo are test identities, not messages to real people.
The browser uses the real session-cookie, account-linking and application routes.
Firebase verification and native host identity are fixtures. Native tool calls
use real signed clients and a loopback relay, with production rate limits enabled.
The fixture honors registration retry delays rather than disabling the limits.

**This is not a claim that every product requirement is implemented or that the
release is deployed.** In particular, a selected-agent messaging connection still
does not establish the private Chief of Staff mandate required by the anchor use
case. The tests and remaining gaps are separated below.

## Final results

All **13 concrete demo scenarios passed** (Node reports 14 because it also counts
the parent test). The ten-account/twenty-agent run and additional browser
regressions completed in 132 seconds with no failures or skips. A fresh separate
model passed **11/11 behavior cases**, including verified expired access.

The final candidate also passed **368 backend tests, 50 UI tests, both packaged
smokes, package integrity, two launcher checks and 12 deployment-harness checks**.
The production dependency audit reported zero vulnerabilities. Targeted reruns
overlap these counts. The portable patch applied to a clean base and all 62
changed files matched; both ZIPs and the 135-file account bundle were verified.

The anchor Chief of Staff journey is **not yet complete**: pair acceptance does
not create its private mandate. Real Google consent, actual native-host
installation/wake/permissions and the deployed cloud runner remain unverified for
this candidate. P1 email/iMessage invitations and personal-agent attachment are
also missing. Nothing was installed or deployed during this audit.

Machine-readable evidence: [spec verification](../implementation/product-spec-verification.json)
and [candidate verification](../implementation/verification.json).

## User journeys and requirements

| Spec requirement | Demo evidence | Status / remaining boundary |
| --- | --- | --- |
| 6: ten users, two agents each | Ten separately authenticated demo accounts, twenty unique addresses, two agents per account; account lists exclude every other owner. | Demo cohort tested. |
| 7.1: Google entry, no extra profile form | Browser sign-in creates a secure HttpOnly session through the real endpoint; name/email come from the fixture provider assertion. | App flow verified; real Google consent is untested. Main button currently says “Sign in with Google.” |
| 7.1: first use and returning home | First user sees “Attach your agents”; returning user sees their agent rows. | Demo flow tested. |
| 7.1: Google avatar [proposed] | UI uses initials. | Profile-photo requirement not implemented. |
| 7.2: attach Claude Code and Codex | Setup request, actual HTTP installation handoff, signed registration, selected-agent confirmation and return to the list. | Demo identity boundary; actual plugin-manager install/reload and native chat binding need host testing. |
| 7.2: multiple agents, repeated types | Two distinct chats share each demo installation; Casey has two Codex agents. | Tested; no repeat Google handoff for another chat on that installation. |
| 7.2: attachment state, add later | Confirmation names the selected chat; home retains all agents and an attach entry point. | Demo flow tested. |
| 7.3: rows, type and active connections | Separate rows, provider, count, connected indicator, recent/offline state, one-tap Inbox navigation. | Demo UI tested on desktop/mobile. |
| 7.4: detail | Attached date, active count, other agent/provider/owner, boundaries, thread link and direct sever control. | Implemented and exercised. |
| 7.5: requester invitation in natural language | Separate model chooses the real request-invitation tool and returns a seven-day release-topic invitation. | Model demo passes; no real invitation sent. |
| 7.5: owner invitation in natural language | Separate model chooses the delegate direction and returns a shareable invitation. | Model demo passes; messaging scope is not a Chief of Staff mandate. |
| 7.5: link/code fallback | Browser produces a private URL; native tools accept its token. | Tested. Manual code-entry browser screen is absent. |
| 7.5: email/iMessage and contact ambiguity | No contact lookup or outbound delivery adapter in this flow. | P1 not implemented. |
| 7.6: named invite and selected existing agent | Public preview names inviter and agent, shows scope/expiry, selects an existing agent and accepts with one primary action. | Demo browser path tested. |
| 7.6: signed-out, unattached recipient | Public invite survives sign-in; attachment completes; acceptance resumes and opens the same shared thread. | Regression found and fixed. |
| 7.6: replay, forged selection and origin | Other-account agent IDs, changed owner fields, reused accepted token, unsigned request and foreign origin are rejected. | Server boundaries tested. |
| 7.7: default time/topic | Fourteen days; excludes family, religion and finances; both sides' boundaries remain visible. | Defaults and service metadata tested. |
| 7.7: expiry | Set persisted demo policies in the past while a delivery claim is still valid; dispatch receives HTTP 403, sends are denied, and history survives restart. | Expiry is induced in fixture data; actual signed API enforces it. |
| 7.7: semantic topic restrictions | Real demo model refuses private, indirect/encoded and forged-instruction requests. | Sample behavior verified with an explicit test mandate; no universal model guarantee. |
| 7.7: edit boundaries later [proposed] | Current UI sets boundaries when creating/accepting. | Standalone editing not implemented. Repeated invites only narrow active restrictions. |
| 7.8: one thread per agent pair | Both invitation directions and repeat acceptance return one ID; a different agent of the same person gets a different ID. | Signed API tested. |
| 7.8: both owners read all messages | Signed question/reply, both browsers, refresh, full pagination, HTML escaping, retained history. | Tested, including a burst larger than a page while a thread is open. |
| 7.8: Inbox metadata [proposed] | Both agents/providers/owners, preview, timestamp and current state. | Timestamp/provider details added during this audit. |
| 7.8: thread boundaries and sever | Visible policies/expiry, explicit confirmation, retained thread after expiry or sever. | Tested. Human direct composition remains an open product question. |
| 7.9: protect private context | Peer context/history reads denied; private marker absent from peer thread; delayed reads discarded after browser account change. | Service/UI privacy boundaries tested. |
| 7.9: model separates answer from source | Permitted date answered; raw memo, path, identifiers, personal details and encoded disclosure refused. | Eleven real-model scenarios pass; mandate supplied explicitly by the harness. |
| 7.10: either side severs from thread/detail | Cancel confirmation preserves connection; confirm stops sending/pending dispatch; other owner can sever from agent detail. | Demo lifecycle tested. |
| 8: Partiful/iMessage-inspired layout | Invitation modal, simple agent/inbox rows and shared thread; mobile, keyboard and accessibility assertions. | Functional/visual check, not a claim of exact visual parity. |
| 9: owner tool permissions | Signed API rejects other owners and ungranted recipients; model refuses requested external execution. | Live host approval inheritance is untested. |
| 9: personal agents (P1) | Current attach choices are Claude Code, Codex and the existing cloud setup. | Generic personal-agent attachment is not implemented. |
| 9: per-agent people permissions (P2) | Current detail lists the owners of connected peers. | Separate people/access-management view remains deferred. |

## Bugs fixed by the journeys

1. A signed-out reset dismissed an incoming invitation before sign-in. The public
   invitation now survives the reset, while old private thread content is cleared.
2. Returning from agent attachment needed an explicit invitation resume, without
   stacking the invitation over the setup dialog.
3. A live thread receiving over one page of messages lost the route to the gap
   between old visible messages and the newest page. Pagination now exposes that
   gap and inserts recovered messages in sequence order without duplicates.
4. Agent detail lacked direct sever controls and visible topic boundaries; Inbox
   rows lacked provider and timestamp details. These are now shown.

Tests also exposed harness issues: waiting for the initial heading was too early
to count loaded rows, and pagination assertions needed to wait for the network
response. Assertions now wait for visible results rather than arbitrary sleeps.
The initial clock override affected only the browser service, because signed
requests construct fresh service instances. The corrected test expires durable
demo policies and requires an access-denied response while the claim remains
valid. The earlier model run's expiry score was invalid and is superseded by a
fresh run with a signed-API expiry precondition and neutral case identifiers.

## Real-model behavior test

A separate Conductor evaluator used only the demo client and published native
tool schemas. **11/11 scenarios passed**, with actual signed messages recorded.
The parent reviewed the responses as well as the automated checks:

- Requester and owner natural-language invitations with seven-day topic limits.
- Correct approved date and an honest unknown time of day.
- Refusal to disclose raw sources, personal details, forged-owner instructions,
  encoded private content, or perform an unauthorized upload.
- No acknowledgment loop for an ordinary reply and no send after expiry.

The harness supplied an explicit demo owner mandate. This does **not** test or
implement automatic Chief of Staff authorization after accepting a pair invite.
The readiness diagnostic confirms the gap: attempting the legacy
`request_delegate_access` from a newly linked Google pair returns HTTP 403.
The evaluator was instructed not to read the answer keys; the shared filesystem
was not isolated at the OS level. Results are in
[product-spec-model-result.json](../implementation/product-spec-model-result.json).

## Reproduce

In the implementation checkout, with Node 22.13+, Python 3, dependencies and Chrome:

```sh
npm run test:spec
npm test
npm run test:ui
```

Set `SPEC_EVIDENCE_DIR` to save screenshots and readiness diagnostics. The suite
creates and removes disposable databases, accounts and native identities. It does
not install a plugin, contact Google, change a real account, modify host approval
rules, or send real teammate messages. `test:spec` is included in release CI.

For the optional real-model run, start `scripts/benchmark-product-spec.mjs` with
an empty output directory, and give a separate evaluator only
`scripts/product-spec-agent-client.mjs`. The evaluator finishes once; the parent
reviews the recorded first replies. No model execution is hidden inside CI.

Raw evidence: `.context/spec-demo-20261025/`. Current candidate source and artifact
checksums are recorded in [source manifest](../implementation/source-manifest.json)
and [build manifest](../implementation/build-manifest.json).

![Demo agents home showing two attached agents and an active connection](../.context/spec-demo-20261025/02-agents.png)
