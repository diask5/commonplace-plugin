# Meet Proxy in two Conductor chats

Install **meet-proxy@commonplace** from marketplace **diask5/commonplace-plugin**
in the agent environment Conductor uses. Existing **commonplace@commonplace**
users should update that alias to 0.2.9. Keep only one alias enabled and reload
the two chats after updating. Use Claude Code for the owner when checking
unsolicited native delivery; normal project, MCP, hook and tool permissions apply.

## Requester asks for access

1. Connect the two test people using an ordinary teammate invitation if needed.
2. In the requester chat: “Ask the other person's Chief of Staff about the Atlas
   pilot's budget ceiling and start date for the next 15 minutes.”
3. In the owner chat: “Accept that request. You may share a ceiling of $125,000
   and a November 12 start. Keep source names, documents and negotiation details
   private. Answer ordinary questions about those facts without asking me again.”
4. Finish the owner turn and leave the session open. In the requester chat ask:
   “Does a $110,000 pilot on November 12 fit?” Read the actual answer.

## Owner issues an invitation

1. In the owner chat: “Take a conversation about the Atlas pilot's budget and
   start date for the next 15 minutes. You may disclose a $125,000 ceiling and
   November 12 start, but no source information or negotiation details. Give me
   a private invitation code. Answer in-scope questions without further approval.”
2. Copy the code to the requester chat. Ask that agent to preview the scope,
   accept the invitation and ask a budget/timing question.
3. Leave the owner session open and verify that the requester receives an answer.

## Check the boundaries

Ask for the private source or an unrelated filesystem action. The owner agent
should refuse. Read the full delegation transcript from both sides: questions,
answers and lifecycle events should match, while the private briefing remains
owner-only. Revoke the grant, or let its deadline pass, and verify that another
message is rejected while the audit remains readable.

The relay fixes the topic, expiry and native chat bindings at acceptance.
Changing those requires a new grant. The requester cannot grant permissions for
the owner. Model instructions enforce source removal and topic relevance; the
service enforces consent, time, revocation and native routing.

## What has been verified

Two real Claude Code CLI sessions on a Mac passed these flows using actual
models and native session IDs. The packaged plugin separately passed both flows
against the production relay. The actual Conductor desktop UI remains untested.
Codex lifecycle hooks and explicit bounded waits do not start an idle or closed
session. A queued message is not proof that the recipient answered.

See [the release verification](../MEET-PROXY-VERIFICATION.md). Conductor's
[MCP documentation](https://conductor.build/docs/reference/mcp) describes host
configuration.
