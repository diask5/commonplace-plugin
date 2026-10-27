# Live acceptance handoff — 27 October 2026

Release 0.4.31/runtime64 is published and server `20261027-context-guidance-r2`
is live. Runtime64 is active on the Mac; permanent native registry installation
is being verified. [PR #37](https://github.com/diask5/commonplace-plugin/pull/37)
contains the source and evidence. P0 acceptance remains open.
[Current receipts](../implementation/p0-live-release-verification.json).

The owner reopened Mac access and completed existing-account GCP sign-in.
The first native candidate attempts failed because runtime61 could not complete
its update. Old loaded plugin launchers then raced a graceful restart; a controlled
handoff recovered runtime64 with account/settings preserved. Two distinct native
CLI synthesis checks pass, and a stricter independent receipt check verifies all
final citations against successful current source reads. These remain isolated
process tests, not a new Desktop GUI or default-host full-catalog walkthrough.

The first server activation failed with EACCES and rolled back. The separately
reviewed [deployment-mode correction](DEPLOYMENT-SOURCE-MODES.md) is now live;
all 159 source files are verified/readable and all services/worker health pass.
The historical connection-unavailable read cause remains unconfirmed.

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

- Mac execution was explicitly reopened and GCP access restored. The prepared
  [status script](../implementation/p0-ready-staging/mac-readonly-status.py)
  prints selected nonsecret fields only. Token-aware process inspection corrected
  the first check's self-matching login heuristic; current access is verified.
- The owner must select the real second participant and the intended native
  chats. That person must sign in and explicitly accept their invitation.
- Clean setup needs a separate authorized Mac or macOS user profile. Do not
  reset the working installation or present cached sign-in as new onboarding.

No answer to a pending question is approval. Existing-account GCP reauthentication
was completed; the Meet Proxy account was not switched or relinked. No saved
permission change, production test space or real-person invitation was made.

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
