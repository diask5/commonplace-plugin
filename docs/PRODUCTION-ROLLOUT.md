# Production candidate: 0.4.19 / runtime 54

Prepared on 25 October 2026. The candidate follows the current Draft v3 product
contract. It does not turn an agent connection into permission to read another
person's raw context. Existing agents can read their own account archive through
MCP resources, search tools or the local context folder without a hosted model.
Authentication, storage, permissions and synchronization still use the backend.

**Production is live on `20261025-product-0.4.19`.** The public site is
https://34.27.253.220/#agents. Web and worker health checks passed; the previous
release and verified SQLite backup are retained. All 45 migrations are applied.
The deployment preserved every existing profile, device, exact agent binding and
thread mapping. Both phone and desktop public pages clear loading without JavaScript
errors; the real Google sign-in helper opens and becomes ready. The [0.4.19 native release](https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-v0.4.19)
is published with both ZIP aliases and verified checksums. The installed-host
update follows through the supported plugin manager.

For internal regression evidence only, the [Conductor walkthrough](https://kyle-cloud-w3.conductor.show/walkthrough)
runs this frozen UI with disposable demo accounts. It does not sign in to a real
Google account. The real-account staging site remains on the earlier build.

## Candidate contents

- Agents/Inbox remain the main navigation, with a contact-list layout, distinct
  active connections, a person-first invite and one Accept action. Mobile setup,
  sticky dialog controls, 44px touch targets and error recovery are improved.
- Explicit per-owner answer consent survives out-of-order invitations and expiry.
  Renewing a pair cannot resurrect work queued under an expired grant.
- Exact native legacy pairs are refused as duplicates with a useful recovery
  message. Existing narrow transcripts and private briefings are not merged.
  This is not a migration of every ambiguous historic thread into the new Inbox.
- The production wrapper now forwards MCP, OAuth protocol/metadata, restricted
  Agent Auth, account APIs and internal cloud endpoints to the current runtime.
  The actual compiled `/authorize` handler remains a live compatibility gate.
- The plugin checks verified native identity before claiming automatic delivery
  and checks current workspace scope immediately before host submission.
- Server dependencies are isolated under `account-runtime/node_modules`, retaining
  the older compiled website's dependencies. A checked archive, backup rehearsal,
  release-pointer rollback and fresh worker heartbeat protect activation.

## Artifacts and source

Artifacts are under `.context/commonplace-source/artifacts/production-0.4.19/`:

- `meet-proxy-0.4.19.zip` and `commonplace-0.4.19.zip`, each with `.sha256` and build
  inventory. Enable only the installation's existing alias.
- `server/runtime-update.json`: all 136 runtime assets and migration files.
- `runtime-dependencies.tgz`: lockfile-pinned production dependencies installed
  with `npm ci --omit=dev --ignore-scripts`; no credentials or account data.
- `server-rollout-0.4.19.tgz`: server bundle, dependencies, reviewed deployment
  helper, isolated HTTP verifier and checksums. SHA-256:
  `768fecfd8d6e3530d8c496fbc112f4b5a5bfe76faa211b73d26abb27c8048425`.

Use `implementation/build-manifest.json` and
`implementation/production-readiness-verification.json` for final artifact and
test state. The fifth ordered patch is `production-readiness.patch`; the complete
chain reproduces 95 changed files byte for byte from the recorded source base.

## Completed local verification

| Check | Result |
| --- | --- |
| Broad regression suite | 379/379 passed |
| Required browser UI suite | 57/57 passed |
| Product lifecycle scenarios | 15/15 tests passed |
| Native regressions | 131/131 passed |
| Packaged launchers and both-alias integrity | Passed |
| Actual packaged stdio and signed-HTTP smoke | Passed with synthetic host/Google fixtures |
| Deployment helper | 15/15 passed |
| Isolated candidate on production Node v22.23.2 | OAuth/MCP/resources checks passed |
| Separate agent behavior sample | 11/11 cases passed |

Browser coverage includes seven screens at four widths plus attachment and
recovery states (52 viewport checks). The model produced two synthetic invitations
and seven persisted answers/refusals; it sent nothing for an ordinary reply or
expired authorization. It answered the permitted release-date question, refused
source/personal-data disclosure, prompt injection and unauthorized uploads, and
recognized an unspecified time. The model evaluation is a sample with synthetic
identities, not a guarantee of all answers or an installed-host test. Some suites
overlap; their counts should not be summed.

## Deployment procedure

Re-read the real VM baseline before making changes. Existing authorization covers
the rollout; restoring Conductor's Mac binding is a host requirement, not a new
product approval. Use the existing authorized Mac Google Cloud account and IAP
connection to VM `commonplace`, project `vertical-web-313417`, zone
`us-central1-a`. Preserve production and staging accounts and databases.

Transfer the reviewed archive through the authorized path, verify its SHA-256,
extract into a new directory, and verify every entry against `files.json`. First
run a preparation release (paths below are relative to that extracted directory):

```sh
sudo python3 deploy-cloud-update.py \
  --baseline 20261022-context-fixes3 \
  --release 20261025-product-0.4.19-rehearsal \
  --bundle runtime-update.json \
  --bundle-sha256 b6822b77b9792a0e85299e6e08e1ea368288dd7a8bf4cc8fbd5d38f6de947cfe \
  --dependencies runtime-dependencies.tgz \
  --dependencies-sha256 a23d485dd9392c996b20838dae4b4eb2a9fbbbdfe664bb13a03289c71a4d9967 \
  --prepare-only
```

This pins and integrity-checks an online SQLite snapshot, rehearses migrations
against a disposable copy, imports the new wrapper/dependencies using the VM's
Node, and records `prepared.json`. It does not switch the live pointer or restart
services. The verified backup remains on the VM; never copy private data into
test artifacts or a release.

Run `verify-runtime-update.mjs` with `/opt/node/bin/node` and the prepared release
path. It uses a disposable database and a synthetic profile over local HTTP. It
checks discovery, PKCE/token exchange, authenticated tool/resource access, denied
writes and foreign origins. It does not exercise real Google or the compiled
authorization page. Rehearse the actual compiled app with isolated state before
activation; this remains outstanding because Mac access was lost.

When those gates pass, run the same deployment command without `--prepare-only`
and with a **new** release name `20261025-product-0.4.19`. The helper deliberately
refuses to overwrite the rehearsal release. This takes a fresh backup, rehearses
again, switches the pointer, checks web health and requires a new worker heartbeat.
On failure it restores the previous code pointer and services, preserving the live
database. Additive migrations remain in place; rollback never discards newer data.

Publish the verified native ZIPs/checksums so the matching UI links resolve, then
update the existing plugin through its supported host flow. Preserve profiles,
origins, aliases and native chat identity; a loaded old MCP process needs its host's
reload step. Do not invent native IDs or modify host permission settings.

## Live release gates

1. Verify Google sign-in and compiled `/authorize` compatibility on the candidate.
2. Check actual server origin, signed account identity and current native chat
   binding with the installed 0.4.19 runtime.
3. Exercise requester invite → Accept → permitted answer in the idle receiving
   chat → both-owner audit using real installed hosts.
4. Check offline delivery, denied host actions, expiry, either-owner sever and
   current consent on that installed path.
5. Confirm phone/desktop pages, download URLs, service health and worker heartbeat
   on the public production origin.

Fixtures, model samples, cached status and queued host messages do not satisfy
these live gates. P1 contact delivery and personal-agent support remain separately
tracked in `SPEC-COMPLIANCE.md`.
