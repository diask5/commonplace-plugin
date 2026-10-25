# End-to-end verification — 25 October 2026

Candidate **0.4.19-rc.2**, companion revision **53**. This is local verification,
not production sign-off. No live account, permissions, installation or deployment
was changed. Test identities, source documents and Google assertions are synthetic.

## Component coverage

| Component | Executed evidence | Boundary still requiring live verification |
| --- | --- | --- |
| Distribution and installation inputs | Both alias ZIPs checked against pinned baseline, source bytes, import closure, licenses and executable modes. Rejected a corrupt baseline. | Supported plugin-manager install/update and host reload. |
| Bundled launcher | Executed Linux dispatcher with a path containing spaces and literal shell metacharacters. Windows command resolves to the shipped native PE binary. | Actual Windows/macOS launch and host environment interpolation. |
| Native MCP | Packaged stdio process, inert discovery, first-use account activation, signed HTTP, hook delivery and retry deduplication. | Claude/Codex host permission UI and real idle/busy wake cycles. |
| MCP protocol | Modern and four legacy stdio versions, modern/legacy HTTP SDK negotiation, validation, structured results, prompts and rollout flags. | Full upstream conformance certification and installed-client matrix. |
| Remote authorization | OAuth PKCE, redirect/resource/replay rejection, owner and read/write checks through real HTTP. | Google browser consent and production TLS/proxy configuration. |
| Collection and merged context | Real collector, signed upload, replica merging, pagination, revision changes, exclusions, local folder and search index. | Every user's supported transcript root, awake/offline collection and real large accounts. |
| Resources/search/folder consistency | A collected source is read through remote Resources and native tools; exclusion removes Resources, search and the mirror. | Optional resource notifications and code snapshot projection. |
| Durable task lifecycle | Real HTTP task creation, nonce retry, worker clarification, whole-service restart, authorized input, cited completion, native read and browser rendering. | This integration uses an explicit simulated model function. Real subscription/container execution remains unverified for RC2. |
| Selected-agent connections | Native invitation, browser acceptance on another account, signed question/reply, both owners' audit, browser sever, blocked subsequent send and retained history after refresh. | Fixture native identities; this does not prove a host wake. |
| Mailbox recovery | Packaged companion/receiver, offline backlog, restart, exact-route fencing, uncertain delivery and receipt retries. | Host socket/CLI responses are doubles; submission is not proof a real chat turn ran. |
| UI | 50 tests including setup, account changes, activity, context, People, Circles, Agents/Inbox, mobile, keyboard and accessibility. New integration tests additionally render actual task and pair results. | Browser identities and provider sign-in are fixtures. |
| Existing database upgrade | Apply migrations through 0042, seed accounts/bindings/audit/tasks, upgrade through 0044, verify unchanged existing records, no new grants, clarification resume, integrity and repeat startup. | Canary upgrade of the deployed database and production backup/restore. |
| Deployment tooling | 12 local tests of consistent backups, schema checks, readiness, worker failure and rollback. | No service was deployed during this verification. |
| Model answer quality | Separate Conductor evaluator over synthetic collected context; results recorded separately below. | Not the deployed cloud runner; not a guarantee of arbitrary code answers or Chief of Staff disclosure safety. |

## Regression fixes and added checks

An omitted launcher test found that the release manifest selected a POSIX wrapper
on Windows. The builder now chooses a native Windows executable or the bundled
POSIX dispatcher through the host's environment interpolation. Existing runtime
files are retained, and aliases each declare exactly one server. The launcher
check and benchmark-scoring tests now run in release CI.

Added `tests/mcp-system-e2e.test.mjs` connects layers previously tested mostly in
isolation: task clarification/restart/browser, source/resource/tool/folder deletion,
and native/browser pair messaging/revocation. `tests/mcp-upgrade.test.mjs` exercises
an existing database rather than only fresh migrations. The first task browser
attempt incorrectly opened Settings; it now navigates through the visible Feed
link, with no forced click or weakened assertion.

## Results

- Backend: **368 passed**, zero failures/skips.
- UI: **50 passed**, zero failures/skips.
- Package integrity: **1 passed**, covering both aliases.
- Launcher: **2 passed** (Linux execution; Windows wiring only).
- Both packaged smoke flows passed; the Mac test kit also builds with executable
  launchers and verified archive integrity (not executed on a Mac).
- Benchmark scorer: **3 passed** (scoring logic, not answer quality).
- Deployment harness: **12 passed**.
- Runtime update: **135 files / 180 relative imports**, hashes and source parity checked.
- Production dependency audit: **0 reported vulnerabilities** at verification time.

The four new system/upgrade tests are included in the backend count. Targeted MCP
tests and separate system-test reruns must not be added again. Raw logs live in
`.context/verification-20261025/`; portable results and checksums live in
`implementation/verification.json` and the source/build manifests.

## Separate-agent benchmark

A fresh Conductor Codex session, using its default `gpt-6.1-sol` model at high
effort, answered **13/13 cases**, **29/29 facts**, with **zero invalid citations**.
It used search/read/list against **101 synthetic documents, 1,276 messages and
378,396 source characters**. The parent graded the saved first answers against
the expected values and recorded retrieval receipts; the evaluator was instructed
not to read answer keys or scores. The workspace did not enforce OS isolation.

The cases include conflicting decisions, calculation, code-string lookup,
separate projects, unknown information, pagination over 18 sources, a long
runbook, an injected instruction, account isolation, freshness and deletion.
There were 26 successful retrieval calls: median 347 ms, p95 386 ms. Summed
per-case answer time was 109 seconds; wall time including setup between cases
was about 149 seconds. These are observations from one small local run, not an SLA.

The fresh-account direct-read attempt returned “Cloud work is unavailable”; its
search and list returned no documents. Foreign direct reads are independently
denied by the system integration test. The benchmark exercised the collection and
retrieval tools with a real separate model; UI and the cloud worker are verified
separately. This was not a run through a real cloud subscription/container.

See [per-case benchmark results](../implementation/benchmark-result.json).

## Remaining release gates

1. The new pair connection grants messaging only. Legacy Chief of Staff identity
   and private mandate mapping remain separate; the full three-step delegated
   answering product is not complete.
2. Run actual supported-host installation/reload and repeated idle/busy/offline/
   restart ask/reply cycles. No local fixture can certify native wake behavior.
3. Run the broader context/code/adversarial benchmark using the deployed cloud
   subscription runner, including disclosure boundaries. A small synthetic
   retrieval benchmark is only partial evidence.
4. Rehearse deployment on a canary with existing data, validate OAuth/browser
   sign-in, and retain revocation and task-generation fencing on rollback.

See [build report](MCP-BUILD-REPORT.md) and [contracts](MCP-CONTRACTS.md) for scope.
