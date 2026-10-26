# Context registration recovery — 0.4.27

**Packaged; activation and live benchmark pending.**

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
