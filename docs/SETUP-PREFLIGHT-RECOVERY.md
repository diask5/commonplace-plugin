# Native setup without a GUI reload command — 31 October 2026

Patch 56 is packaged for server `20261031-setup-activation`. Publication and
production verification are pending. Native 0.4.33/runtime66 is unchanged.

The supplied setup transcript exposed three separate problems: an obsolete
PATH executable interpreted plugin commands as model prompts, the current
Conductor conversation did not acquire newly installed tools, and browser
sign-in differed from the machine’s existing Meet Proxy account. A cached
conversation count was then incorrectly treated as evidence that setup worked.
The private setup code in that transcript is not reproduced or reused.

The setup request now checks existing account/server identity before installing
or claiming the handoff. It resolves the host’s actual Claude executable,
including `CLAUDE_CODE_EXECPATH` and paths with spaces, checks version and plugin
support, then reuses the installed alias and marketplace. A different account
stops setup and preserves the existing connection; this is not an account
migration feature.

When newly installed tools are unavailable, the browser offers **Plugin
installed? Finish in a new chat**. This prepares a shorter activation prompt
with the same account, space and unclaimed private handoff. The **Copy activation
prompt** and app-opening actions sit above live progress. Claude Desktop uses
the existing new-Code-chat deep link. Conductor opens the app and explicitly
asks for a new chat in the same workspace; its link does not promise to create
that chat automatically. The user still sends the prepared request and handles
any host-required approval. This flow does not prescribe `/reload-plugins` in
Conductor or Claude Desktop or treat MCP status refresh as a tool-context reload.

Choosing activation does not claim the request, enable collection or move a
receiver. The existing server claim binds only the actual native chat. Claimed,
disconnected and expired requests cannot offer another activation; expiry uses
the existing renewal flow without a second Google sign-in. Account changes
clear the prepared prompt and links. Clipboard refusal leaves selectable text.
Only installation-specific receipts and searchable content count toward setup
readiness; the activation prompt additionally asks for a fresh source read.
Opening or copying is not a completion receipt.

Verification and hashes are in
[the verification record](../implementation/setup-preflight-recovery-verification.json).
All 34 browser and 11 setup/protocol contract checks pass; the 56-patch replay
matches all 217 changed files. Browser checks use isolated synthetic identities and a simulated native claim
against the real handoff service. They cover all three native app choices,
scope/token preservation, no pre-claim mutations, cross-chat claim refusal,
disconnection, expiry, account changes and responsive accessibility. Existing
signed-native collection/retrieval and cross-host protocol checks are retained.
These do not prove a clean installation in the actual GUI hosts.

The work-machine companion failure in the supplied transcript remains separate:
the available Mac is a different installation, so its health cannot diagnose
that machine. No account migration, credential deletion, host-policy change or
permission bypass is included.

Host references inspected on 31 October:

- [Conductor MCP setup](https://conductor.build/docs/guides/configure-mcp-servers):
  configuration changes require a new session to load tools into model context.
- [Conductor MCP reference](https://conductor.build/docs/reference/mcp): status
  refresh is distinct from a new agent session.
- [Claude Desktop Code](https://code.claude.com/docs/en/desktop): native Code
  sessions and plugin management; no GUI `/reload-plugins` assumption.
