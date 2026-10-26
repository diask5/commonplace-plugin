# Context timeout recovery — 0.4.26/runtime59

The real ordinary-prompt benchmark found an SDK timeout reported as
`Commonplace Agent Auth failed (23).`. The trailing period escaped the connector's
exact error match, so Claude tried setup recovery and Codex reported an auth
problem. Both now map to a timeout message that explicitly preserves sign-in.
Other errors, host denials and attacker-appended text keep their original meaning.
This change does not increase request deadlines or fix production capacity.

The follow-up is packaged and verified, pending publication and activation.
527 core tests, six focused setup browser tests, both-alias packaging,
34 extracted feature/launcher tests, three extracted exact-error tests, packaged
stdio and six-profile mailbox checks passed. The focused UI run first caught an
outdated test version regex; corrected and rerun. Full unchanged UI/lifecycle
results remain recorded with 0.4.25, not relabeled as a new 0.4.26 run.

The [first native run](../implementation/seamless-native-first-attempt.json)
retains five passes, two transport failures and one unstarted Claude case.
Actual Claude and Codex used MCP search and supporting source reads without tool
names in the user prompts; successful answers cited the retrieved notes. Their
90–152 second answer times are not a seamlessness pass. Follow-up attempts will
be recorded separately. Default-host invitation routing and real production
latency remain open gates. The separate controlled space run passed five executed
cases but skipped two previously blocked cases and cannot certify normal host routing.

An unintended empty ChatGPT space, Briar Review, remains from the earlier unsafe
benchmark. No reversible cleanup capability was available. No personal context
was deliberately added to it; its emptiness has not been independently rechecked.

See [the earlier walkthrough and screenshots](SEAMLESS-CONTEXT.md), the original
[spec compliance audit](SPEC-COMPLIANCE.md), and the machine-readable
[follow-up verification](../implementation/context-timeout-recovery-verification.json).
