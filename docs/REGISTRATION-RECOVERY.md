# Context registration recovery — 0.4.27

**Published and live: server `20261026-registration-recovery`, installed native 0.4.27 and active runtime60. The fresh real-host benchmark remains incomplete.**

Existing native chats used to wait behind unrelated new-chat registration. The
updated connector reads an existing session immediately and keeps serialized,
deduplicated registration for new sessions. Identity, account scope and host
permissions are unchanged.

The server closes its archive read transaction after capturing source content,
metadata and expiry, before building derived files. This shortens the period
in which it prevents database checkpointing. Optional legacy cloud runs also
check their archive revision and expiry before inference and inside the final
result-publication transaction. Changed or excluded context withholds even an
uncited answer. Refreshed model credentials are retained independently. If a
consultation was already sent, the task retains its durable waiting state without
publishing withheld text or sending an acknowledgment.

Whole-archive changes can cause those optional cloud jobs to retry even when the
changed source is unrelated. The existing five-attempt limit remains. Existing
owner retrieval through MCP still requires no hosted model.

[Verification](../implementation/registration-recovery-verification.json) records
source, package and deployment states separately. [Diagnostics](../implementation/registration-recovery-diagnostics.json)
preserve the installed runtime59 timeout alongside faster direct transport
measurements; the regression fix alone does not establish a live speedup.

The cache relocation proposal was rejected after review and was never applied.
Native host approvals, prior default-host invitation failures, and external model
capacity errors remain visible in the readiness evidence.

The Mac update preserved the account and saved permissions. The initial handoff
attempts failed: the helper missed old cached launchers, and waiting for a PID
to disappear did not establish release of the runtime lock. The supported
background installer updated the LaunchAgent to 0.4.27. A subsequent guarded
handoff observed the old lock release and activated runtime60 while eight exact
old plugin processes briefly waited; all were resumed. Claude and Codex remained
open. [Installation receipts](../implementation/registration-recovery-native-install.json)
preserve the failures and the successful activation separately.

Installed MCP search and full supporting reads confirmed both fictional benchmark
notes in 9.19 seconds. This is one readiness observation, not an ingestion-latency
or general search-speed guarantee. Eight held-out ordinary-language questions were scheduled
in parallel host tracks with the previously approved per-process retrieval
tools. This controlled catalog does not close the default-host routing gate.

Live public checks verified 31 assets and sign-in at 1440px and 390px, with no
script errors or horizontal overflow. [Public evidence](../implementation/registration-recovery/public-smoke.json)
and the [desktop](../implementation/registration-recovery/production-desktop.png) /
[phone](../implementation/registration-recovery/production-phone.png) screenshots
are separate from authenticated setup and invitation acceptance.

The final [runtime60 benchmark](../implementation/registration-recovery-native-benchmark.json)
passed three cases. Claude's correction gave the right facts but did not read one
of its cited sources; both synthesis cases failed to retrieve sufficient context.
Claude's sequence stopped on an unapproved `list_shared_context` selection, so its
last two cases did not run. No host denial was recorded and saved configuration
was unchanged. Completed cases took 108–175 seconds, with repeated timeouts and
revision restarts. This is not a seamlessness pass. A separately reviewed server
index-reuse candidate is being measured; it is not part of this live release.
