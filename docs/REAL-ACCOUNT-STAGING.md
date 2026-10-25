# Real-account staging

The 0.4.19-rc.3 Agents/Inbox build is available at:

https://meet-proxy-staging.34.27.253.220.nip.io/

Deployed on 25 October 2026 after the local product-spec audit. This environment
uses real Google/Firebase authentication and an empty, separate database.
Production chats, credentials, agent bindings and synced context were not copied.

Choose **Sign in with Google**, then **Continue with Google** in the sign-in
window and select your account. First use leads to agent attachment. Staging
will initially have no agents; existing production installations are not
automatically attached here. Native attachment and a successful human sign-in
remain walkthrough steps, not claims established by the signed-out checks.

The staging service uses the verified account runtime bundle
`ec952f39e75ebb2dbe0bfb1b2b1abec343c53de1539cc4e61b0e9c55e06ada60`, its own
locked dependency installation, separate OS user and SQLite database. It does
not run the local demo identity adapter or simulated model worker. Production
continues to use release `20261022-context-fixes3`.

A dedicated Firebase Hosting sign-in page returns only to the exact staging
origin, using the existing popup/window/nonce checks. All seven preexisting
Hosting files were preserved by hash. Production's sign-in page is unchanged.

Verified after deployment:

- Trusted HTTPS certificate and automatic staging renewal timer.
- Candidate health and the new UI render successfully.
- The Google helper loads and its Continue button becomes enabled.
- Invalid Google tokens, demo cookies, spoofed identity headers and foreign
  origins do not authenticate.
- Production web/worker and the staging service remain active.

Local evidence and deployment helpers are under `.context/real-staging/`.
The [product-spec report](PRODUCT-SPEC-TEST-REPORT.md) still describes the known
feature gaps; staging does not complete the Chief of Staff mandate integration
or provide a configured cloud inference account.

The staging UI now includes [app launch links and server verification](AGENT-LAUNCH-LINKS.md).
This is a two-file overlay on the original runtime bundle. Its verification is
recorded in `implementation/agent-launch-verification.json`. The new native
`setup_status` origin diagnostic is source-only, not an installed plugin update.
The user's reported production agent was not present on staging; real-account
native attachment remains incomplete.
