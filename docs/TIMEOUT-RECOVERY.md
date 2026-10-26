# Context timeout recovery — 0.4.26/runtime59

The real ordinary-prompt benchmark found an SDK timeout reported as
`Commonplace Agent Auth failed (23).`. The trailing period escaped the connector's
exact error match, so Claude tried setup recovery and Codex reported an auth
problem. Both now map to a timeout message that explicitly preserves sign-in.
Other errors, host denials and attacker-appended text keep their original meaning.
This change does not increase request deadlines or fix production capacity.

The follow-up is published and live at `20261026-timeout-recovery`. All 156
server files match the bundle; all three services are active and migrations are
unchanged. Seven public UI asset checks and desktop/phone browser checks pass.
The Mac has 0.4.26 installed and runtime59 active, with account, bindings and
saved permissions preserved. The maintenance script initially missed old cached
launchers, allowing an older companion to reclaim the lock; a second guard then
refused to signal the mismatched process. Corrected exact-path detection completed
the graceful handoff and resumed all paused product runtimes. Existing host chats
may retain older loaded plugin metadata until reloaded.

527 core tests, six focused setup browser tests, both-alias packaging,
34 extracted feature/launcher tests, three extracted exact-error tests, packaged
stdio and six-profile mailbox checks passed. The focused UI run first caught an
outdated test version regex; corrected and rerun. Full unchanged UI/lifecycle
results remain recorded with 0.4.25, not relabeled as a new 0.4.26 run.

The [first native run](../implementation/seamless-native-first-attempt.json)
retains five passes, two transport failures and one unstarted Claude case.
Actual Claude and Codex used MCP search and supporting source reads without tool
names in the user prompts; successful answers cited the retrieved notes. Their
90–152 second answer times are not a seamlessness pass. The [separate follow-up](../implementation/context-timeout-native-benchmark.json)
records one pass, one partial result and one failure. Codex used search and full
source reads and ignored the injected note. Claude answered the current date
correctly but cited the prior plan from a search snippet without fully reading it.
Its remaining unknown-information case hit reconnect/timeout errors and attempted
unapproved setup diagnostics; the guard stopped it without a final answer.
The scorer now recognizes actual document-URI IDs; its original score is preserved.
 Default-host invitation routing and real production
latency remain open gates. The separate controlled space run passed five executed
cases but skipped two previously blocked cases and cannot certify normal host routing.

An unintended empty ChatGPT space, Briar Review, remains from the earlier unsafe
benchmark. No reversible cleanup capability was available. No personal context
was deliberately added to it; its emptiness has not been independently rechecked.

See [the earlier walkthrough and screenshots](SEAMLESS-CONTEXT.md), the original
[spec compliance audit](SPEC-COMPLIANCE.md), and the machine-readable
[follow-up verification](../implementation/context-timeout-recovery-verification.json).

Live health checks still take 12.5–14.7 seconds. The VM is e2-small and its data
volume is a 30 GB standard disk; sampled I/O wait was 42–57%. This does not prove
a sole hardware cause. A source-only server follow-up is being reviewed to remove
one non-authority counter commit per request and reuse verified unchanged archive
documents. It is not deployed yet. No paid infrastructure change was made.
