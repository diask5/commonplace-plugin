# Context sync across native and regular chats

29 October 2026: the five-host setup update is published and live on server
`20261029-cross-host-sync`. All 159 deployed files match and are service-readable;
all three services are active. Public OAuth, MCP authentication, exact asset bytes
and desktop/phone sign-in checks pass. The prior server release remains retained.
Native 0.4.32/runtime65 was unchanged at this rollout; the later
[bounded catch-up fix](BOUNDED-SYNC-CATCHUP.md) addresses an observed long-chat delay.

The setup chooser now offers Claude Code, Claude chat, ChatGPT, Codex and
Conductor directly. Native setup still prepares one plugin/MCP request and carries
the browser account into the exact chat. Copy, Send, required approval/reload,
registration and collection receipts remain separate steps. Claude Code users
can paste the same request in Desktop Code or a terminal session.

| App | Collects supported visible native history | Reads the same private library | Connection |
| --- | --- | --- | --- |
| Claude Code, including Desktop Code | Yes, after authorized native setup | Yes | Bundled plugin and MCP |
| Codex | Yes, after authorized native setup | Yes | Native MCP installation |
| Conductor | Yes, from supported local/cached native history | Yes | Actual provider's native installation |
| Regular Claude chat | This connection does not upload its chat history | Yes | Remote MCP connector with OAuth |
| Regular ChatGPT | This connection does not upload its chat history | Yes | Custom MCP plugin with OAuth, when allowed by the host account/workspace |

Regular-chat setup shows the expected Meet Proxy account, current official host
instructions and a copyable connection check. That check requires successful
source reads, follows search cursors even through empty pages, and reports source
capture time when available. Copying a URL, successful discovery and OAuth sign-in
alone are not retrieval or collection proof. Native history remains private until
explicit sharing rules allow an excerpt.

The native progress view now distinguishes saved context from current collection.
Offline, paused, interrupted and partial collection each have their own message;
previously received context can remain usable without implying that new messages
are currently syncing. Exclusions and installation-specific readiness are preserved.

## Live sync evidence

A fresh harmless marker posted visibly in this Conductor chat reached the Mac's
staged history, canonical capture and live account archive. At 05:42:57 UTC, a
successful signed source read returned the exact marker with two source citations
at archive revision 6530. No unrelated source text or credentials were retained.

The first empty phrase-search result was a bounded page, not missing ingestion:
this long conversation has 1,330 sections. Pages through 500 and 1,000 had no
match and returned cursors; the final page found it. The verification request now
makes this continuation requirement explicit. No sync latency guarantee is inferred
from this diagnostic. The Mac retained its existing account and runtime65.

## Validation and release limits

628 core tests, 27 setup/browser checks and 23 tests against the extracted server
bundle pass. Deployment checks pass 57 with one skipped. All 51 ordered patches
replay exactly across 212 changed files. The bundle contains 159 files, changing
six server modules and no migrations. It also includes patch 50's tested fix:
rejoining a space invalidates old sharing consent even with equal or backwards
timestamps.

The new integration test collects Claude/Codex/Conductor-format files and reads
the result through three native clients and two separate OAuth clients. It checks
edits, failed-upload recovery, exclusion propagation, hidden-content filtering,
account isolation and truthful installation receipts. These use synthetic protocol
identities; they do not prove actual host-model or clean-machine onboarding.

The prior Claude `finish_context_setup` approval remains pending. No denied setup
action was retried, no permission changed and no account relinked. Actual fresh
host acceptance remains open. The [sharing stress failures](SHARING-STRESS.md)
also remain: retrieval recall, useful admission and concurrent provider capacity
are not fixed by this update. This is not an all-P0 readiness claim.

Exact artifacts, tests, live diagnostics and release state are in
[the verification record](../implementation/cross-host-context-sync-verification.json).

Host setup references checked on 29 October:

- [Claude custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [ChatGPT custom MCP plugins](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Codex MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Conductor MCP](https://www.conductor.build/docs/reference/mcp)
