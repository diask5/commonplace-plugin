# MCP adoption source delivery

This repository distributes the plugin. Its implementation checkout
([commonplace-session-tests](https://github.com/diask5/commonplace-session-tests)) is separate,
at `.context/commonplace-source` in this workspace. Because `.context` is ignored,
the complete implementation delta is also preserved here as a portable Git patch.

- Candidate: **0.4.19-rc.3**, companion runtime **53**.
- Source base: **5479e529c85dda95b4ab6107fe3c7db7af569d13**.
- Patch: `mcp-adoption-0.4.19-rc.3.patch` (including new files, bundled code and licenses).
- `source-manifest.json`: patch digest and SHA-256 of every changed/new source file.
- Architecture: [contracts](../docs/MCP-CONTRACTS.md).
- Validation and limitations: [build report](../docs/MCP-BUILD-REPORT.md).
- Current spec audit: [demo journeys and gaps](../docs/PRODUCT-SPEC-TEST-REPORT.md).
- Machine-readable spec results and blockers: [verification](product-spec-verification.json).
- Current separate-model behavior benchmark: [11-case result](product-spec-model-result.json).
- Historical RC2 component audit: [end-to-end verification](../docs/MCP-E2E-VERIFICATION.md).
- Historical RC2 retrieval benchmark: [13-case result](benchmark-result.json).

RC3 supersedes RC2 and RC1. The earlier patch and ZIPs remain historical artifacts;
the current source/build/verification manifests identify RC3.

Apply this to a clean checkout of the **implementation repository at the source
base**, not to this distribution repository. For example, create a detached
worktree from an existing implementation checkout, then apply the patch there:

```sh
git -C /path/to/implementation worktree add --detach /path/to/candidate 5479e529c85dda95b4ab6107fe3c7db7af569d13
git -C /path/to/candidate apply --whitespace=nowarn --check /path/to/commonplace-plugin/implementation/mcp-adoption-0.4.19-rc.3.patch
git -C /path/to/candidate apply --whitespace=nowarn /path/to/commonplace-plugin/implementation/mcp-adoption-0.4.19-rc.3.patch
cd /path/to/candidate
npm ci
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
unzip -q artifacts/candidate/meet-proxy-0.4.19-rc.3.zip -d artifacts/verify-plugin
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
