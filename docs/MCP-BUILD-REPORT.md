# MCP adoption build — 0.4.19-rc.3

25 October 2026. **Production rollout pending.** After the local audit, the account
UI/API was deployed to [real-account staging](REAL-ACCOUNT-STAGING.md). The plugin
candidate has not been installed or published; production is on its prior release.
Companion runtime revision: **53**. Source base:
`5479e529c85dda95b4ab6107fe3c7db7af569d13` in
[`diask5/commonplace-session-tests`](https://github.com/diask5/commonplace-session-tests).

The [RC3 product-spec demo audit](PRODUCT-SPEC-TEST-REPORT.md) covers ten users
and twenty agents, signed-out invitation recovery, direct sever controls, full
audit recovery, and eleven separate-model behavior scenarios. The earlier
[RC2 component audit](MCP-E2E-VERIFICATION.md) is retained as historical evidence.

## Delivered

- One bundled SDK adapter for native stdio, cloud archive/network tools and
  authenticated remote MCP, with modern and legacy protocol paths, structured
  results, bounded validation and inert initialization/catalog probes.
- Context Resources over the existing authorized archive. Tools, Resources and
  the local folder return the same snapshot text and citation receipts. Search
  results carry revision-pinned resource links; existing search remains available.
- Durable Tasks integration and revision-keyed clarification, preserving the
  existing cloud queue, target, cancellation fencing and ordinary status tools.
- Agents home, agent detail, invitation/acceptance, pair Inbox, shared audit and
  sever controls. Both invitation directions select existing agents and reuse one
  thread per pair. Both owners can read the thread after it ends. Repeat invites
  cannot widen existing boundaries; unavailable agents can still be severed.
- Additive migrations 0043/0044, protocol feature flags, bundled dependency
  notices, package integrity checks and CI regeneration checks.

The [contracts](MCP-CONTRACTS.md) describe authorization, cursors, identity,
idempotency, policy, rollback and the deliberately separate legacy flows.

## Validation

All tests use local services and disposable identities. Counts overlap between
the full backend suite and targeted suites; they must not be summed.

| Check | Result / scope |
| --- | --- |
| `npm test` | 368 passed: backend, archive, delivery, task, protocol and pair tests. |
| `npm run test:ui` | 50 passed, including mobile/keyboard/accessibility, existing onboarding/settings, invitation acceptance and audit/sever. |
| `npm run test:spec` | 13 concrete scenarios passed (14 Node tests including parent): ten demo users, twenty agents, signed-out acceptance, privacy, full audit, either-side sever, expiry and restart. |
| RC3 model behavior | 11/11 with a separate real model, an explicit demo mandate and neutral case IDs; signed-API expiry precondition verified. This does not prove the missing pair-to-mandate integration. |
| MCP tests within `npm test` | 22 passed; five stdio versions, HTTP, Resources, Tasks, prompts, flags, authorization and official SDK 2.4.0 client negotiation. |
| Fresh plugin discovery subprocess | Legacy and modern probes leave the disposable data directory empty; spoofed client metadata creates no binding. |
| Package integrity | Both alias archives match source overlays, baseline assets, licenses and executable modes; corrupt baseline rejected. |
| Bundled-runtime plugin smoke | Passed: real stdio/companion/signed HTTP, duplicate retry, hook delivery, context-folder search, retained legacy delegations, new human-linked pair replies and sever. |
| Bundled-runtime mailbox smoke | Passed: six fresh profiles, invitation as the first tool, one-sign-in handoff, exact simulated receiver, ordered offline backlog, restart, deduplication and persistent simulated Conductor transport after MCP exits. Google assertions and host sockets/CLI remain test doubles. |
| Runtime update closure | 135 files and all 180 relative imports verified. |
| Deployment harness | 12 local Python tests passed; no deployment occurred. |
| Benchmark scorer | 3 tests passed; these validate scoring, not model answer quality. |
| Prior RC2 retrieval benchmark | 13/13 cases, 29/29 facts, zero invalid citations over 101 synthetic documents. A real Conductor evaluator uses local retrieval tools; the production model runner is not exercised. |
| Packaged launcher | 2 passed: Linux execution and Windows PE wiring; not actual Windows/macOS execution. |
| Existing database upgrade | Records preserved through 0042 → 0044; queued/clarification work survives, no new access granted, repeated startup and integrity checks pass. |
| Dependency audit | `npm audit --omit=dev --audit-level=high`: zero reported vulnerabilities at verification time. |
| Portable source patch | Applied to a fresh worktree of the base commit; all changed files matched the manifest. Generated SDK template/license whitespace retained byte-for-byte. |

The [fresh end-to-end audit](MCP-E2E-VERIFICATION.md) adds service-restart task
clarification, browser/native pair acceptance and revocation, source exclusion
across access paths, and a populated 0042-to-0044 migration test. It also found and
fixed the Windows manifest launcher selection; Windows execution remains a live
host gate. Launcher and benchmark-scorer checks now run in release CI.

The final first-use activation fix was checked again with real plugin discovery
subprocesses and the rebuilt ZIP. Initialization remains inert; a valid first
invitation tool call now prepares the anonymous installation before routing the
single-use handoff, without opening another Google sign-in.

These are integration/compatibility tests, not a certification against an entire
upstream conformance suite. A localhost fixture cannot establish production
OAuth consent, native GUI wake or a general model nondisclosure guarantee.

## Scope against the roadmap

| Stage | Local implementation status | Remaining evidence/work |
| --- | --- | --- |
| M0 contracts | Source/base versions, contracts, pinned SDK and local harness delivered. | Installed/deployed host capability inventory. |
| M1 adapter | Native, worker and remote paths implemented; legacy fallback tested. | Actual client/version matrix and upstream conformance coverage. |
| M2 Resources | Read projection, revision checks, scope checks and file/tool parity delivered. | Optional notifications and permitted code-snapshot projection. |
| M3 product flow | New selected-agent pair service and browser/native flow delivered. | Safe legacy ID/mandate migration; standalone boundary editing. |
| M4 Tasks | Durable work/clarification bridge implemented. | Real-host repeated wake/reconnect cycles and real-model runs. |
| M5 auth/UX | Existing OAuth path adapted and negative tests added; workflow prompts delivered. | Optional Apps, Skills, Registry/Server Cards and broader host validation. |
| M6 rollout | RC artifacts, additive migrations and protocol rollback controls prepared. | Backup/migration canary, installation/deployment and production evidence. |

## Release gates and known limits

1. **Legacy identities and Chief of Staff mandates remain a separate flow.**
   New pair connections grant messaging only. They do not silently attach a
   private delegation briefing or permit autonomous access to private sources.
   Historical person/session threads cannot safely be merged by person name.
   Existing legacy grants remain readable after installation linking.

   The initial mixed-identity smoke exposed the remaining compatibility boundary:
   a newly created Google-person chat connection does not itself establish the
   older autonomous-account friendship expected by legacy `request_delegate_access`.
   This candidate does not claim that path is unified. The corrected smoke
   separately verifies retained legacy delegation and new Google-linked pairs;
   it does not count one as evidence for the other. Resolve this identity/mandate
   mapping before claiming the full three-step Chief of Staff product is complete.
2. **Real native wake remains a release gate.** Run the planned 20 sequential
   ask/reply cycles per supported host pairing, including busy, restart, offline
   and uncertain delivery. A simulated socket or Conductor CLI receipt does not
   prove a model turn ran in Claude Code, Codex or Conductor.
3. **Real-model quality and disclosure remain a release gate.** The prior 13-case synthetic
   retrieval benchmark and current 11-case product behavior sample pass with separate real agents; the broader planned
   40-question context/code/adversarial benchmark and real cloud runner have not
   been exercised for this build.
   Deterministic isolation tests do not prove semantic topic compliance or that
   an agent can answer every question.
4. **Deploy and migrate deliberately.** Back up before applying migrations; test
   existing accounts, native bindings, queued work and revocation on a canary.
   Protocol flags preserve the new authorization rules. Rolling back to a binary
   that ignores pair revocations or task generations is not a safe rollback.
5. Resource/task push notifications, in-chat Apps, Skills extension publication,
   direct email/iMessage delivery and filesystem writes are not included. Native
   setup still uses each host's existing approval and reload process.

## Review and reproduce

The implementation lives at
[`../.context/commonplace-source`](../.context/commonplace-source).
The distribution branch also contains the complete
[portable source delivery](../implementation/README.md), so the code changes are
not stranded inside a gitignored checkout. No source branch was renamed.

The [source manifest](../implementation/source-manifest.json) identifies the
base, patch checksum and every changed source file. The
[build manifest](../implementation/build-manifest.json) records the release ZIP
and runtime-update hashes. The [verification record](../implementation/verification.json)
records test counts, scope and local evidence paths. Reproduction and local smoke commands are in the
source-delivery README.

Built artifacts in this workspace:

- [Meet Proxy ZIP](../.context/commonplace-source/artifacts/product-spec-rc3/meet-proxy-0.4.19-rc.3.zip)
- [Commonplace alias ZIP](../.context/commonplace-source/artifacts/product-spec-rc3/commonplace-0.4.19-rc.3.zip)
- [Runtime update](../.context/commonplace-source/artifacts/product-spec-runtime-rc3/runtime-update.json)

The ZIPs are local build outputs; the checksum is an integrity record, not proof
that a public release was published. No account reconnection, transcript upload,
host-permission change or live teammate message was part of this build.

![Mobile shared thread after severing; the script-like message is an escaping test fixture](../.context/build-evidence/agent-pair-thread.png)
