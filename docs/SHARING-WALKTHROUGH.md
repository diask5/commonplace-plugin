# Guided sharing walkthrough — 26 October 2026

**Live:** https://34.27.253.220/ · release `20261026-sharing-walkthrough`.

The sharing setup now has an illustrated, animated three-step guide: choose your
app, send the setup prompt, and receive your context. Desktop uses a split dialog;
phones use a compact progress strip. The selected app's Copy setup prompt action
stays prominent until its real registration is confirmed. Host Send, approval and
reload instructions remain explicit.

Sharing rules use a two-column desktop page with three clear actions: describe
what can be shared, choose its duration, and enable requests. An illustrated
explanation shows how requests pass through every rule before approved excerpts
reach Messages. The invitation and Members screens use the same visual language.
Motion respects the system's reduced-motion preference.

Completion is based on evidence: opening an app or copying text never completes
setup; native registration and indexed-context receipts do. The sharing success
card appears only after enabled, unexpired rules have been saved and disappears
when the draft changes. This update changes no grants, accounts, native bindings,
classifier behavior or schema. Native plugin 0.4.20/runtime55 remains unchanged.

## Verification

All **70 current-context browser checks passed**, with zero skips or failures.
A separate final screenshot journey also passed. The incremental patch contains
four runtime UI modules and three browser-test
files. All 18 implementation patches replay cleanly and reproduce the complete
150-file implementation delta. Runtime bundle SHA-256:
`e0edc4be9f41f3c6cd6063c95c71268a2ae2c2c11e32cca20ae405382849267a`.

Tests cover the actual app with isolated accounts: app selection, clipboard,
registration, collection, error recovery, account changes, invitations, saved
rules, two-sided exchanges, expiry, leaving and archiving. Accessibility,
overflow and responsive controls are checked from 320 to 1920 pixels, including
reduced motion. The machine-readable verification records final counts and live
deployment separately.

A first full run exposed a test timing issue: after joining, the test attempted
to fill the background composer before closing the asynchronously opened setup
dialog. A delayed group response reproduced this with the modal open and the
composer empty. The journey now waits for that dialog before dismissing it.
No application behavior was bypassed and no readiness check was removed.

## Screens and rollout

[Desktop and phone gallery](https://kyle-cloud-w3.conductor.show/review) ·
[Production](https://34.27.253.220/)

Gallery screenshots use the real UI with labeled test accounts and synthetic
context. They do not assert a fresh real Google or native-host setup.

Apply `implementation/sharing-walkthrough.patch` after
`context-mvp-completion.patch`. See the matching manifest for exact file hashes
and `implementation/sharing-walkthrough-verification.json` for deployment state.
The server update is an additional checksummed asset on the existing 0.4.20
release; it does not replace either published plugin ZIP.

Production activation verified the exact `20261026-context-0.4.20` baseline and
allowed only the four reviewed UI modules to differ. The code-only deployment
verified unchanged migration digests, preserved the live database, and checked
web readiness and a fresh runtime worker heartbeat. All 153 deployed bundle files
match the manifest. Live Chrome at 1440px and 390px cleared loading, found the new
walkthrough markup, and reported no page errors or horizontal overflow. Served
browser modules match the tested source, and the Google helper becomes ready.
These public checks did not authenticate a Google account or exercise a native
host. Existing installed-host acceptance limits remain in the MVP rollout record.
