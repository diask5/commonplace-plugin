# Live acceptance handoff — 27 October 2026

Release preparation is complete through verified GitHub drafts and draft
[PR #37](https://github.com/diask5/commonplace-plugin/pull/37). P0 acceptance is
still open. The candidate is 0.4.31/runtime64; current live evidence remains
0.4.28/runtime61 and server `20261026-current-read`.

## Prepared artifacts

Both aliases and the server update were downloaded from the new drafts. All ten
download hashes and sizes match local bytes and GitHub's asset digests.
[Staging receipts](../implementation/p0-ready-staging-verification.json) record
the exact target commit and artifact hashes. All ten older 0.4.29 asset digests
and sizes remain unchanged. No marketplace pointer has been promoted.

An independent Conductor source/evidence review found no material new blocker in
patches 40–41. The earlier 594/594 core result and synthetic model regressions
remain qualified as recorded in [candidate evidence](P0-READY-CANDIDATE.md).
The public health endpoint returned HTTP 200 and `ready: true` on 27 October;
this is not an authenticated retrieval or worker-health check.

## Inputs required before live work

- The owner must explicitly reopen Mac execution after the prior denial. A
  read-only request is pending for current runtime/account metadata, the existing
  GCP sign-in, and relevant server error metadata. The prepared
  [status script](../implementation/p0-ready-staging/mac-readonly-status.py)
  prints selected nonsecret fields only. It has not run on the Mac.
- The owner must select the real second participant and the intended native
  chats. That person must sign in and explicitly accept their invitation.
- Clean setup needs a separate authorized Mac or macOS user profile. Do not
  reset the working installation or present cached sign-in as new onboarding.

No answer to a pending question is approval. No new login, account switch,
permission change, production space, invitation or local execution occurred in
this staging step.

## Execute once access is available

1. Read current Mac runtime and cached account metadata. Confirm the intended
   Meet Proxy account is `diaskyle10@gmail.com`; do not relink on mismatch.
   Check the existing GCP sign-in without starting a duplicate. Cached account
   listings are not live authentication evidence. Respect any new host denial.
2. Through the existing authenticated GCP path, inspect bounded server metadata
   around the retained synthesis failure. Use project `vertical-web-313417`,
   zone `us-central1-a`, VM `commonplace`. Record timestamps and error categories;
   keep credentials, request bodies and private source text out of reports.
   Use [the prior diagnosis](../implementation/current-read-connection-diagnosis.json)
   and [retained failed test](../implementation/current-read-synthesis-retest.json).
3. If original logs cannot establish the cause, install the reviewed diagnostic
   candidate for the authorized test and capture its bounded stderr category.
   Preserve both accounts and saved permissions. Host Send, approval and reload
   remain explicit. Do not force past an active-work update guard or restart
   unrelated applications. A diagnostic category is evidence, not proof of repair.
4. Implement a behavioral fix only if the observed cause requires one. Give any
   changed build a new version and new hashes; never replace these draft bytes
   under their recorded checksums. Run the affected regression before rollout.
5. Roll out the reviewed server through `deploy-cloud-update.py`, pinning the
   freshly observed baseline and exact bundle SHA-256. The current candidate
   bundle is `255688ceb2220b0adb035fe2e4f4f31ed20f0494fac5cc8530c64e3bce64dfa1`.
   Use a new release directory; code-only mode must confirm all migration bytes
   and applied digests. Verify manifest hashes, web readiness, fresh worker
   heartbeat and retained rollback. Then promote the matching native artifacts
   through the release flow and verify active runtime64 in the selected chats.
6. In each actual installed Claude/Codex chat, use fresh uniquely named synthetic
   notes for an ordinary correction/synthesis question. Record collection and
   archive readiness first. Require the correct current facts and a successful
   read of every final cited source in the same session. Observe default routing;
   do not coach the prompt with tool names or silently filter the catalog.
7. In the owner-selected production test space, verify invitation preview and
   explicit signed-in acceptance; membership alone must leave private sharing
   disabled. Enable only the owner's chosen synthetic-content rules, exercise
   approved and withheld requests, and check both participants' shared history
   while keeping rejected content/checks owner-only. Test leave/removal,
   follow-up withholding and failure of the old invitation to restore access.
8. In the separate clean environment, verify Google → prepared request → actual
   Send/approval/reload → exact native identity → installation-specific collection
   receipts → searchable and readable new synthetic text → browser Ready. Run
   both hosts, record unsupported/partial coverage, and confirm Copy setup prompt
   recedes after registration. Existing-owner evidence does not close this gate.

For each gate record the active build, exact host/chat, observation time,
successful and failed tool receipts, persisted effects and remaining limits.
Stop the affected path on a denial; never reroute or retry around it. The deferred
private-finance benchmark stays skipped. The unintended empty ChatGPT space
remains owner cleanup. Direct Mail/iMessage remains P1.
