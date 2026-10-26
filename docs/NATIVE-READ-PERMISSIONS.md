# One-time permission for context reads

MCP describes what a tool does; the receiving application decides whether it may
run. Meet Proxy already marks `search_shared_context` and `read_shared_context`
with `readOnlyHint: true` and `destructiveHint: false`. These annotations do not
grant permission or override a Claude, Codex or Conductor host decision.

For a seamless setup, use the host's remembered permission for those two exact
tools when the owner chooses it. Claude Code's actual tool names for the default
plugin in the tested installation are:

```
mcp__plugin_meet-proxy_meet-proxy__search_shared_context
mcp__plugin_meet-proxy_meet-proxy__read_shared_context
```

Use the names the current host exposes; a legacy alias may have a different
namespace. A server-wide wildcard would also cover sharing and account mutations,
so it is not equivalent to allowing these two reads. The installer's existing
rule to preserve host permissions remains in force.

For an owner-approved automated test, Claude Code also supports a per-invocation
allowlist. The installed CLI's `--help` confirms `--allowedTools`. For example,
the owner can launch their existing session with:

```sh
claude --resume <existing-session-id> \
  --allowedTools 'mcp__plugin_meet-proxy_meet-proxy__search_shared_context,mcp__plugin_meet-proxy_meet-proxy__read_shared_context'
```

This is an exact read-tool allowlist, not a request to disable the host's permission
system. Host or organization denial rules can still take precedence. The agent
must not silently add permission settings after a denial.

The initial 26 October answer test was denied by Claude's noninteractive policy.
After the owner explicitly approved these two tools for this test, a fresh run
used this exact per-invocation allowlist. Successful search and read receipts were
verified, and Claude returned the complete known probe marker without being given
its numeric suffix. There were no permission denials; before/after permission
checks matched. No saved permission rule was added.

This resolved the permission gate for that test. It does not preapprove future
sessions. The answer took 87.95 seconds, with an initial resource-list timeout and
a transient read timeout before success. The harness also hit its process/pipe
cleanup deadline after Claude emitted its successful final result. These are
separate startup/transport/lifecycle issues, not a reason to broaden permissions.
See [the live verification record](ZERO-TO-KNOWLEDGE.md).
