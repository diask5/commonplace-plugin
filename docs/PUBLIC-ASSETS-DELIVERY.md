# Public UI asset delivery

The public page could time out while its JavaScript, CSS and font requests queued
behind server work. This server-only update serves 31 exact public asset paths
through Nginx, including CSS generated from the current source. Private pages and
APIs retain their existing application handlers and authentication.

**State: published and live at `20261026-public-assets`.**
Native 0.4.26/runtime59 and its ZIPs are unchanged. No database migrations, account
changes, saved permission changes or paid infrastructure changes are included.

The installer requires the exact site-config hash, verifies all asset hashes, and
backs up the site/include privately. It validates Nginx before reload and restores
both files on failure. Missing assets fall back to the exact existing proxy body,
so older-release rollback keeps dynamic CSS working. The current four response
headers are preserved. Only exact allowlisted GET/HEAD paths receive static files.

54 Python checks passed locally with the real-Nginx fixture skipped there. All
29 deployment checks, including that fixture, passed using an isolated loopback
Nginx process on the VM; the production config was untouched by that test. Nine
context regression checks passed. The first real fixture failed because its
temporary directory was not readable by the Nginx worker; the corrected fixture
passed. Independent review found two issues, both corrected before activation:
missing-file rollback and rechecking the include under the install lock.

29 ordered patches reproduce 192 implementation files exactly. The runtime bundle
contains 157 files. [Verification](../implementation/public-assets-delivery-verification.json)
tracks the exact hashes and activation. [I/O follow-up](SERVER-IO-RECOVERY.md)
retains the prior browser timeout and real-model failures. This change does not
claim to resolve HTML/API latency or default-host invitation routing.

Live checks verify all 31 asset bodies, MIME types and headers. OAuth discovery,
compiled authorization, MCP authentication rejection, HEAD, denied POST and
private-source rejection pass. Public desktop/phone pages render without overflow
or JavaScript errors in 5.078 / 8.298 seconds; assets return in 0.028–0.192 seconds.
These are public sign-in checks, not a new authenticated onboarding walkthrough.

Production screenshots: [desktop](images/public-assets/production-desktop.png) /
[phone](images/public-assets/production-phone.png).
