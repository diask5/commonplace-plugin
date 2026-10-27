# Disposable Conductor cloud benchmark

See [the verification record](../cloud-p0-benchmark-verification.json). These
are synthetic fixtures and preserved visible outcomes, not live readiness proof.
The original failed model attempts remain failures; later source-guidance checks
are separate candidate runs with new names and databases.

The harness loads the public server bundle from release
`meet-proxy-server-20261026-current-read`:
`https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-server-20261026-current-read/runtime-update.json`.
SHA-256: `429bed64cdb57f2bbcd58ba5f3b273bbd4739ed6cb1e8c72c1c891182097dbe5`.
`extract-bundle.mjs` verifies that digest before extraction. Use a fresh disposable
root with Node supporting `node:sqlite`; the observed environment was Node 24.
The fixtures generate their own local OAuth credentials. Never commit those
credential files, copy production tokens, or connect this fixture to an account.

The retrieval server seeds three canonical streams through the real ingest API,
then exposes the complete published remote MCP catalog. Its model credential is
read-only. The space server uses synthetic identities and a deterministic rule
classifier. Its `space-private` natural-prompt case is retained as historical
source only: it was provider-refused and must remain skipped.

Run models as fresh supported Conductor sessions, using natural prompts alone.
Standalone nested CLIs lacked model authentication in this environment. Project
configuration belongs only in the disposable workspace and must be restored
when finished; do not change global settings or host approval mode. Tool allow
entries are not an exclusive deny list. Check actual visible tool calls, source
read receipts and persisted state; do not infer completion from correct text.

The archived grader accepts supporting citations only from successful reads,
never search snippets, error replies or changed/restart replies. Do not include
its plan, expected answers or fixture source in scored model context. Record
all first attempts, host/tool blocks and unstarted cases. No denied route may be
retried through another tool. Loopback links cannot establish external delivery.
