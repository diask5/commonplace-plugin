# P0 closeout — 26 October 2026

**P0 remains open.** This is the execution order for the outstanding gates in
[SPEC-COMPLIANCE.md](SPEC-COMPLIANCE.md), not a release or acceptance claim.
The original Draft v3 and the owner's later Spaces amendments remain the contract.

## Release state

| Build | State |
| --- | --- |
| 0.4.28/runtime61; server `20261026-current-read` | Published, installed and active; current production baseline. |
| 0.4.29/runtime62 page-size guidance | Packaged; native/server GitHub draft assets uploaded. Not published, installed or deployed. |
| 0.4.30/runtime63, patches 36–37 | Locally packaged and verified; includes page-size guidance and bounded transport diagnostics. Not uploaded, published, installed or deployed. 0.4.29 draft assets unchanged. |
| Scope and retrieval guidance, patches 38–39 | Distinct cloud model regressions pass 3/3 spaces and 8/8 retrieval. Now included in local 0.4.31; absent from live releases. |
| 0.4.31/runtime64, patches 40–41 | Locally packaged with patches 38–39, page-size guidance, diagnostics and recoverable remote archive input errors. Not uploaded, published, installed or deployed. [Evidence](P0-READY-CANDIDATE.md). |

The diagnostic delta preserves one bounded, allowlisted exception category and
any valid status supplied by the original exception on local stderr. It excludes
messages, stacks, URLs, paths, identities, credentials, bodies and source text.
It adds no retries, relinking, permission changes or public-error changes. The
generic failed-read message still does not prove an HTTP 503 or expired sign-in.
See [the delta verification](../implementation/transport-diagnostics-verification.json)
and [the prior diagnosis](../implementation/current-read-connection-diagnosis.json).

## 1. Establish the failed-read cause

1. Finish the existing same-account GCP browser reauthentication on the Mac;
   do not start a duplicate login or replace the connected account. Obtain host
   approval for the concrete Mac command before executing it.
2. Inspect production logs around the retained synthesis failure. Correlate
   timestamps and outcomes without copying private source content into reports.
   The two failed reads took about 5.2 and 5.7 seconds; timing does not identify
   the cause. Preserve any uncertainty.
3. If those logs are insufficient, package the reviewed diagnostic delta under a
   distinct version with new hashes, verify the package, then install it for an
   authorized native test. Do not overwrite the reviewed 0.4.29 assets under their
   existing hashes. Capture only the bounded stderr diagnostic.
   The later 0.4.31/runtime64 candidate already combines this delta with the tested
   routing/read guidance and remote archive error fix; prefer its reviewed artifacts
   to the older local 0.4.30 package for subsequent authorized acceptance.
4. Choose a behavioral fix from the observed failure and verify its regression.
   Do not infer an authentication repair or add retries from the generic wrapper
   error. Reconcile uncertain writes before any write retry.
5. Repeat an ordinary-language synthesis question with unique synthetic names on
   both installed native hosts. Record actual host identity, active collection,
   tool receipts and successful reads for every final citation. A search hit or
   correct answer alone does not pass. Include the page-size guidance candidate
   in the reviewed rollout and record whether it changes model behavior.

The earlier Mac request timed out without execution. The latest resumed request
returned “The user denied local command execution.” No retry or alternate local
path was used. The owner directed this benchmark to new Conductor cloud sessions.

The diagnostic candidate is now packaged as 0.4.30/runtime63, with 37 ordered
patches reproducing 203 files. Both aliases, extracted launchers, actual packaged
stdio/signed-HTTP smoke and extracted-server OAuth/resource checks pass. The
server check uses a compiled `/authorize` stub. Independent source review found
no blocker. These checks do not establish the failed-read cause.
[Exact hashes and limits](../implementation/cloud-closeout-runtime-verification.json).

## 2. Finish native invitation and access acceptance

1. The authorized disposable Conductor cloud MCP acceptance retest passed, with
   actual preview/accept calls and persisted membership. The broader baseline
   found cross-space fallback and legacy-wiki/search-only-citation failures.
   Source guidance candidates pass 3/3 space and 8/8 retrieval cases; original
   failures remain. [Evidence and limits](CLOUD-P0-BENCHMARK.md). Temporary
   settings were restored; no saved global permissions changed. This completes
   the cloud benchmark, not installed-native default routing or real-person
   production acceptance. A denied route must not be bypassed.
2. With an owner-selected real second person, create a scoped production space
   invitation, preview it and obtain their signed-in explicit acceptance. Record
   the intended receiving native chat on each side. A queued message, launch or
   matching email is insufficient.
3. Verify both people see the shared message/request and approved excerpt audit.
   Joining grants membership only; private-library sharing requires the owner's
   explicit rules and opt-in. Exercise approved and withheld requests within the
   authorized synthetic test scope, preserving owner-only checks and rejections.
4. Verify leave/removal through the model, then ask a relevant follow-up through
   that same path and verify access is withheld. Verify an old invitation cannot
   restore removed membership. Record actual results, including any tool-choice
   failures. Do not retry around a provider refusal.

## 3. Prove fresh setup separately

Use an owner-authorized clean Mac/account test environment for Claude Desktop
and Codex Desktop; do not reset the working installation to manufacture one.
For each host, record real Google consent, the prepared plugin/MCP request,
actual Send, host approvals/reload, exact native identity, installation-specific
collection receipts, newly searchable and readable synthetic text, and the UI's
Ready state. Confirm browser sign-in carries over and Copy setup prompt recedes
after registration. Identify partial collection and any unsupported sources.
Existing-owner handoffs, cached identity and fixture onboarding do not replace
this coverage. If no clean environment is available, leave this gate open.

## 4. Release and accept against receipts

After the cause is understood and a candidate is verified, publish/install/deploy
the reviewed artifacts through the authorized release flow, preserve accounts
and permissions, reload older host sessions where required, and verify exact
artifact hashes and service health. Re-run only the affected acceptance paths
against that active build. Update the compliance table with source, package,
installation, production and model evidence as separate states. A diagnostic
patch or a passing local demo does not close a live gate.

Direct Mail/iMessage delivery and personal agents remain separate P1 work.
The unintended empty ChatGPT space remains owner cleanup; this checklist does
not authorize deleting it or merging any existing histories.
