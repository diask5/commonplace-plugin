# MCP adoption source delivery

**Current published native release: 0.4.24 / runtime57.** Its P0 native
fix is preserved in `p0-native-readiness.patch`. Apply all 24 patches
in `p0-native-readiness-manifest.json` order (`applyAfter`, then `patch`).
The clean replay reproduces 178 implementation files. See
[P0 live readiness](../docs/P0-NATIVE-READINESS.md) for release evidence;
installation and production activation are distinct from packaging.

The latest web UI update is [the guided sharing walkthrough](../docs/SHARING-WALKTHROUGH.md).
Its [verification record](sharing-walkthrough-verification.json) distinguishes
browser fixtures from live deployment checks.

This repository distributes the plugin. Its implementation checkout
([commonplace-session-tests](https://github.com/diask5/commonplace-session-tests)) is separate,
at `.context/commonplace-source` in this workspace. Because `.context` is ignored,
the complete implementation delta is also preserved here as a portable Git patch.

- Release: **0.4.19**, companion runtime **54**.
- Source base: **5479e529c85dda95b4ab6107fe3c7db7af569d13**.
- Ordered patches: `mcp-adoption-0.4.19-rc.3.patch`,
  `agent-launch-and-server-check.patch`, `spec-alignment.patch`,
  `product-flow-design.patch`, then `production-readiness.patch`.
- `source-manifest.json`: patch digest and SHA-256 of every changed/new source file.
- Architecture: [contracts](../docs/MCP-CONTRACTS.md).
- Validation and live rollout state: [production rollout](../docs/PRODUCTION-ROLLOUT.md).
- Current spec audit: [demo journeys and gaps](../docs/PRODUCT-SPEC-TEST-REPORT.md).
- Machine-readable spec results and blockers: [verification](product-spec-verification.json).
- Current verification and separate-model behavior sample:
  [production verification](production-readiness-verification.json).
- Historical RC2 component audit: [end-to-end verification](../docs/MCP-E2E-VERIFICATION.md).
- Historical RC2 retrieval benchmark: [13-case result](benchmark-result.json).

The stable source is the complete five-patch chain. RC1/RC2 and the RC3-only build
are historical artifacts. The current chain reproduces 95 changed files exactly;
see `source-manifest.json` and each follow-up manifest for digests and order.

## Unreleased context UI follow-up

Apply `context-product-ui.patch` after the five production patches above to
reproduce the minimal Connections / Context / Shared access top navigation,
sharing-first home, per-connection picker, account profile, conversation board, context list, sharing sheet and recipient
invitation preview. Its 19-file
inventory and baseline hashes are in `context-product-ui-manifest.json`; exact
verification scope is in `context-product-ui-verification.json`.
This follow-up is source-only and available as an interactive design preview;
it does not change the published 0.4.19 ZIPs or production. The original five
patches still reproduce the production release.

Run `npm run preview:context` for an isolated, labeled sample-data preview of the
actual app. Run `npm run test:context-ui` for retrieval, responsive accessibility,
account reset and recovery checks. Sharing uses a document picker and one review sheet with optional expiry
(default two weeks); link creation and the preview Accept action are disabled.
Selected-document recipient grants are not implemented or implied.

## Unreleased automatic collection follow-up

Apply `automatic-context-ingestion.patch` **after** `context-product-ui.patch`.
It repairs large JSON history backfill, includes enabled custom transcript
folders, groups the unified catalog by source project, reports canonical
collection status, and adds direct sync setup and live refresh to Context.
The manifest and verification JSON with the same prefix record its source
digests, full chain replay and exact checks. No schema migration is required.
This seventh patch is source-only; published packages and live accounts remain
unchanged. See [automatic collection](../docs/AUTOMATIC-CONTEXT-COLLECTION.md).

## Unreleased prompt-based sharing experiment

Apply `prompt-based-sharing.patch` after `automatic-context-ingestion.patch`.
It adds a Perplexity Decisions adapter, a recipient-bound filtering primitive,
an isolated MCP adapter, a synthetic rule-testing page and a 28-case live-model
benchmark. Run `npm run test:policy` or `npm run benchmark:policy` in the
implementation checkout. Configuration and boundaries are documented in
[prompt-based sharing](../docs/PROMPT-BASED-CONTEXT-SHARING.md).
This eighth patch changes no live grants or production endpoints. Model accuracy
must be measured separately from passing fixture tests. Its manifest and
verification JSON record exactly what was checked.

Apply `sharing-rules-design.patch` next for the invitation-style rule tester:
illustrated sharing card, compose/recipient-preview steps, mobile spacing and
disclosed technical details. The four-file manifest and verification with the
same prefix preserve the UI changes, responsive accessibility checks and a live
synthetic preview. This ninth patch does not change classifier or grant behavior.

Apply `sharing-desktop-layout.patch` tenth for the full desktop sharing workspace.
The rule editor and recipient preview stay visible side by side above 960px;
mobile keeps the compact two-step flow. Its three-file manifest and verification
record seven-width accessibility checks, breakpoint preservation, long-result
scrolling and the live synthetic preview. No production permissions change.

Apply `sharing-interactions.patch` eleventh for SVG checking/approval animation,
reduced-motion states, cancel/Escape, keyboard preview, undo, setup retry and
request timeouts. Cancellation stops the active provider request and prevents
later candidate calls. Its seven-file manifest preserves the source changes.

Apply `shared-spaces.patch` twelfth for the latest Spaces / My context navigation.
It merges Connections and Shared access; adds prompt drafts per space, group
creation, membership controls, a message composer, explicit text/Markdown file
uploads and exact-space assistant setup. The real group/document APIs back these
controls. Uploaded files are shared with group members; private archive rules
remain drafts and upstream MCP ingestion is not implemented. See the manifest
and verification JSON for tested scopes, file hashes and full replay evidence.

Apply `message-first-spaces.patch` thirteenth. It adds the compact message-first
header, per-owner server rules, bounded parallel Decisions checks, owner-private
audits, shared exchange history, signed MCP/native request tools, invitation links
and observed native setup/collection state. Its manifest lists every changed file;
its verification records the full replay and test evidence. It adds four SQLite
tables on first use. It does not update published ZIPs or production. See
[message-first spaces](../docs/MESSAGE-FIRST-SPACES.md) for rollout limits and the
live synthetic provider result, including the first false withholding.

Apply this to a clean checkout of the **implementation repository at the source
base**, not to this distribution repository. For example, create a detached
worktree from an existing implementation checkout, then apply the patch there:

```sh
git -C /path/to/implementation worktree add --detach /path/to/candidate 5479e529c85dda95b4ab6107fe3c7db7af569d13
for patch in mcp-adoption-0.4.19-rc.3.patch agent-launch-and-server-check.patch spec-alignment.patch product-flow-design.patch production-readiness.patch; do
  git -C /path/to/candidate apply --whitespace=nowarn --check "/path/to/commonplace-plugin/implementation/$patch" || exit 1
  git -C /path/to/candidate apply --whitespace=nowarn "/path/to/commonplace-plugin/implementation/$patch" || exit 1
done
cd /path/to/candidate
npm ci --ignore-scripts
npm run build:mcp
npm test
npm run test:ui
npm run test:spec
```

Node 22.13+ and Python 3 are required; the local validation used Node 24 and
installed Google Chrome. Worker ownership tests need a Linux environment capable
of the existing container UID operations. No model login is required for these
fixture tests. Browser and native identities in tests are disposable fixtures.

To build and exercise the actual plugin:

```sh
python3 scripts/build-plugin.py --output artifacts/candidate
COMMONPLACE_TEST_PACKAGE_DIR=artifacts/candidate npm run test:package
unzip -q artifacts/candidate/meet-proxy-0.4.19.zip -d artifacts/verify-plugin
COMMONPLACE_TEST_PLUGIN="$PWD/artifacts/verify-plugin" node --test apps/commonplace/tests/runtime-mcp.test.mjs
node scripts/smoke-plugin.mjs "$PWD/artifacts/verify-plugin"
node scripts/smoke-mailbox.mjs "$PWD/artifacts/verify-plugin"
python3 scripts/build-runtime-update.py --output artifacts/runtime-update
```

The builder checks the pinned baseline SHA-256 and preserves runtime executable
modes. Both plugin aliases are produced; only one alias should ever be enabled
in an installation. These commands build and test locally. They do not install,
publish, change host permissions, or deploy anything.

New migrations 0043 and 0044 are additive. A future deployment must back up the
database, verify existing account/binding preservation and keep the new revocation
and task-fencing rules on rollback. See the contracts before promoting a release.

## Unreleased automatic desktop setup

Apply `live-context-setup.patch` after `message-first-spaces.patch` (14th patch).
It replaces the optional sync toggle and manual chat picker with an authenticated,
single-use native setup handoff, automatic private collection, installation-specific
progress, and a live setup sheet. It also fixes browser asset inclusion in the
production overlay. The manifest and verification files with this prefix record
replay hashes and tests. This is source/preview only; release 0.4.19 is unchanged.
See [flow and live gates](../docs/LIVE-CONTEXT-SETUP.md).

## Unreleased direct plugin setup

Apply `seamless-plugin-setup.patch` after `live-context-setup.patch` (15th patch).
Three direct app-launch cards replace selecting an app and then opening it. A
provider-specific request installs or reuses the plugin and configures MCP, with
browser identity carried by the existing private handoff. The progress sheet has
three rows and troubleshooting is secondary. Account changes, stale responses,
preparation failures and expiry have verified recovery. The matching manifest
and verification file record exact source hashes and checks. Published 0.4.19
does not include the handoff tool; this remains source/preview work.

Apply `copy-setup-prompt.patch` after `seamless-plugin-setup.patch` (16th patch).
After choosing an app, Copy setup prompt appears above live status with clear
paste-and-send instructions. It returns to troubleshooting after connection.
The same-prefix manifest and verification record the four-file source change,
browser/clipboard checks and full chain replay. Release state is unchanged.

## Context MVP completion

Apply `context-mvp-completion.patch` after `copy-setup-prompt.patch` (17th).
It adds native/remote space management, per-owner expiry with a two-week default,
member Leave and owner Archive controls, legacy navigation recovery, full current
journey captures, and 0.4.20/runtime55 packaging. The manifest records 29 incremental
files; the verification record distinguishes packaged, deployed and installed state.
No existing migrations are rewritten. `cp_space_policy_limits` is additive on first
use. Existing profiles, exact native bindings, private scope and pair histories stay
intact.

## Guided sharing walkthrough

Apply `sharing-walkthrough.patch` after `context-mvp-completion.patch` (18th).
It adds the animated three-stage native setup, prominent next action, responsive
sharing-rule explanation and clearer invitation screens. Four runtime UI modules
and three browser-test files change; no backend, schema or native package changes.
The full chain still reproduces 150 files. Published plugin ZIPs are unchanged.

## Zero-to-knowledge verification

Apply `zero-to-knowledge.patch` nineteenth, after `sharing-walkthrough.patch`.
It fixes bounded collector cursor ordering, parallelizes complete archive integrity
validation, adds an empty-account browser/native/context/sharing journey and a
33 MB interrupted mirror regression, and packages 0.4.21/runtime56. See
[the audit](../docs/ZERO-TO-KNOWLEDGE.md) and its verification JSON for actual live
receipts and the distinction between fixture and installed-host evidence.

Apply `archive-read-performance.patch` twentieth. The live large-account test
showed that each file page revalidated the complete archive. Read requests now
reuse a current authorized snapshot, verify accessed file/index digests, repair
corruption and still fence new source revisions and expiry. Full reconciliation
retains whole-archive validation. This is a server-only follow-up to native 0.4.21.

## Local native discovery

Apply `native-discovery.patch` twenty-first. Native resource discovery advertises
the static context index and document template without fetching the account or
archive. Explicit reads retain authorization, scope and revision checks. Remote
and pinned archive resource enumeration is unchanged. The patch adds real stdio
discovery/closure regressions, packages native 0.4.22, and updates the legacy setup
release link. The companion remains runtime56; no daemon behavior or schema changes.

Apply `archive-revision-fence.patch` twenty-second. Stale paged reads return a
revision restart before joining an archive rebuild. The post-preparation revision
check remains. This server-only update preserves native 0.4.22 ZIPs and schema.


## Context completion candidate

Apply `context-completion.patch` twenty-third, after `archive-revision-fence.patch`.
It adds bounded Unicode-safe sharing chunks and approved-only continuation,
explicit native MCP resource ingestion, contact invitation adapters, compatible
MCP assistant setup, direct canonical document reads and drained archive shutdown.
The candidate is native 0.4.23/runtime57; current public marketplace remains 0.4.22.
All 23 patches reproduce 174 files exactly; this patch changes 50 files. Its
manifest records input/output hashes and order; `context-completion-verification.json`
records test logs and native/runtime artifact digests. Read [the candidate and
activation gates](../docs/CONTEXT-COMPLETION.md) before release. Packaged checks are
not evidence of installed or deployed readiness.

## Seamless context retrieval and setup

Apply `seamless-context.patch` twenty-fifth, after `p0-native-readiness.patch`.
It adds MCP-first routing, generated request IDs and bounded safe retries,
authoritative live archive search with post-read fences, prioritized private
collection and installation-specific canonical readiness. The 31-file incremental
patch reproduces all 185 changed implementation files with the preceding chain.
The candidate is 0.4.25/runtime58. See `seamless-context-verification.json` and
[the rollout record](../docs/SEAMLESS-CONTEXT.md) for the distinction between
packaged, deployed, installed and real-model-tested state.
