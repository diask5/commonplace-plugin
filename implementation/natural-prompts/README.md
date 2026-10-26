# Natural-prompt benchmark harness

Evidence tooling for the published 0.4.24/runtime57 release. This does not modify
the implementation or add another implementation patch. The 24-patch production
chain remains unchanged.

The original harness is archived byte-for-byte in `baseline/`; its digests remain
in the baseline verification record. The parent scripts additionally support the
owner-approved retest and per-case durable-state snapshots.

`plan.json` freezes the eight retrieval questions, synthetic note facts and rubric.
The scored prompt contains only the ordinary user question. The answer key is
held outside each fresh working directory. The harness is not OS-isolated from
those files; inspect actual model tool receipts for contamination.

Run only on an owner-authorized Mac with the existing installed plugin, enabled
private collection and authenticated Claude/Codex hosts. `runner.py seed` creates
two explicitly synthetic native work-note chats, which remain in the private
archive. It sends no messages to other people. The owner must authorize any
per-process tool allowances; never automatically widen them after a denial.

Copy the harness files to a fresh private directory. Set
`MEET_PROXY_BENCHMARK_DIR` to that directory (the default is the original
`$HOME/.commonplace-code-verification/natural-prompts-0.4.24/`). Existing case
streams and fixture databases are not overwritten. From that directory, run:

```sh
python3 runner.py seed
python3 start-when-ready.py
python3 collect.py
```

The watcher waits for both seed documents to appear in the real local mirror,
records the observation time/revision, then starts one fresh Claude and one fresh
Codex case at a time. Inputs/outputs use separate paths; subprocess stdin is
closed. Raw transcripts can contain private context and must remain private.
The Claude profile uses only the earlier owner-selected search/read allowlist;
the first context-folder denial stops that track. The driver was hardened after
the baseline to stop immediately after a denial and tolerate non-message events.
The completed baseline responses were recovered from their original streams;
no scored prompt was replayed.

`run-spaces.py` verifies and extracts the public runtime bundle, starts a
disposable service with synthetic identities and real OAuth, and exposes the
published remote tools through `space-bridge.py`. It disables configured personal
MCP servers for that process; host-provided app/browser tools may still be
available. It never uses production account credentials. Its classifier and
source candidates are deterministic fixtures. The default host permission policy
still applies, including write approval. The driver stops on an approval block.

The baseline orchestration was stopped after host denials; only three of the
seven planned space cases were attempted. Do not count a tool selection as a
successful mutation. A returned result, persisted state and shared audit are
needed to grade a completed flow.

Reruns need a new directory, separately named results and explicit permission
for any previously denied tool. Preserve first attempts. Do not place golden
answers or retrieval instructions in the scored model prompt. No permission
flags, model choices or release pointers should be changed silently.

For the owner's approved retest only, copy the current scripts and plan to a new
directory and set `MEET_PROXY_BENCHMARK_DIR`. Run `python3 runner.py approved-claude`
to add only `context_folder_status` to the existing two-tool process allowlist.
Run `python3 run-spaces.py --owner-approved-tools` to approve exactly the five
named fixture tools through `mcp_servers.spec.tools.<tool>.approval_mode` process
overrides. Other host restrictions still apply. These switches are not permission
to add filesystem roots, approve browser access, relink an account or retry a
newly denied action. The approved run stopped remaining Claude cases when new
denials occurred. See the separate approved verification record for outcomes.
