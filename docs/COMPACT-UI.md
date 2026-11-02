# Compact UI

2 November 2026. Server-only patch 72 redesigns Meet Proxy around the compact workspace in [AgentMake](https://github.com/diask5/agentMake/tree/2a900202e799cc60658f848d418696168a6f9eea). Reference components were `project-shell.tsx`, `project-tabs.tsx`, `app-sidebar.tsx` and `globals.css`. The reference checkout was read without edits.

The current candidate is packaged and running in a disposable browser preview. It is not deployed. Last verified production remains `20261101-context-throughput` (patch 70); native 0.4.44/runtime77 is unchanged. Patch 71 remains an earlier published, undeployed dependency. The prior Mac binding block has not been retried or bypassed.

## What changed

Spaces, messages, My context, readers, sharing rules, members, invitations, profile, settings and setup now use one compact scale. Warm neutral surfaces, Arial/system typography, charcoal actions, thin borders and small corner radii follow AgentMake's workspace. The main top bar shrank from 80 to 60 pixels; page headings use 22–24 pixels instead of 30–34. Desktop controls generally use 36 pixels; top navigation, setup completion/close controls and phone controls retain larger targets.

The 920-pixel illustrated setup dialog became a single 560-pixel panel. App selection, the primary Copy setup prompt action and receipt-driven progress remain in their original order. The large sharing illustration is gone; its explanation of classification and explicit sharing consent remains. The profile banner is 64 pixels instead of 148. Secondary connection and account pages use the same compact scale.

The main product stylesheet was consolidated from 93,479 to 62,858 bytes. It no longer layers successive redesigns over one another. Existing asset URLs remain compatible. No new UI dependency or external font request is required. A secondary setup check also exposed an existing hardcoded 0.4.31 installation prompt; it now points to the already-published 0.4.44 release.

Global navigation remains **Spaces / My context**, with **Messages / My sharing rules / Members** in the space header and **Invite** in the top bar. The change does not alter account identity, invitation scope, opt-in, expiry, classifier decisions, collection or revocation behavior.

## Review

Open the [interactive preview](https://kyle-cloud-w3.conductor.show/preview/sample) from Conductor. This is a sample account with disposable context, not production. The local preview serves real UI/HTTP handlers at port 43319; the Conductor preview edge requires its own sign-in (an unauthenticated external request returns 401, not an app success receipt).

| View | Screenshot |
| --- | --- |
| Spaces and messages | [Desktop](../implementation/compact-ui/screenshots/spaces.png) · [Phone](../implementation/compact-ui/screenshots/mobile-messages.png) |
| Sharing rules | [Before](../implementation/compact-ui/screenshots/before-rules.png) · [After](../implementation/compact-ui/screenshots/rules.png) |
| My context | [Library](../implementation/compact-ui/screenshots/context.png) |
| Setup | [Before](../implementation/compact-ui/screenshots/before-setup.png) · [After](../implementation/compact-ui/screenshots/setup.png) · [Phone](../implementation/compact-ui/screenshots/mobile-setup.png) |
| Invitations and profile | [Invite](../implementation/compact-ui/screenshots/invite.png) · [Profile](../implementation/compact-ui/screenshots/profile.png) |

## Verification and packaging

See [verification](../implementation/compact-ui-verification.json), [ordered manifest](../implementation/compact-ui-manifest.json) and [replay result](../implementation/compact-ui/replay72.json). All 72 patches reproduce the current implementation across 268 changed files with zero mismatches. The 166-file server bundle preserves all 47 migration digests. Its six changed runtime files since patch 71 are view/CSS modules, generated `ui.css`, and the secondary setup prompt.

All 110 UI/browser checks pass, as do five runtime asset checks and 12 extracted HTTP/OAuth/MCP smoke checks. Browser checks exercise source reading, live updates, message retries, file disclosure, rules, invitations, account changes, setup receipt states, keyboard/focus behavior and accessibility at phone/tablet/desktop widths. Reduced-motion checks were moved from removed decorative SVGs to the actual controls and progress indicators. The original failed assertions and corrected runs are retained. Extracted HTTP/OAuth/MCP checks use linked unchanged dependencies and a disposable profile; they do not prove Google, native-host or production acceptance.
