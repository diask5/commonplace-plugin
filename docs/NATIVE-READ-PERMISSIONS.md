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

The real 26 October answer test loaded the MCP tool but was denied by Claude's
noninteractive policy. No permission file was edited, no allowed-tools override
was applied, and that answer remains unverified until the owner grants access.
Independent collection, cloud retrieval and local-file integrity checks passed.
