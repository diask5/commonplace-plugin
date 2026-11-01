# Multiple native accounts

1 November rollout update: this work is included in published native **0.4.37/runtime70** and live server **20261101-space-events**. The earlier candidate and access-block records below are historical. See [current rollout evidence](SPACE-EVENTS-ROLLOUT.md) for publication, installation and activation separately.

31 October 2026 — patch 58, native **0.4.34/runtime67 is published**:
https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-v0.4.34

657 core tests, nine isolation regressions, five extracted-package checks,
both-alias integrity checks and exact 58-patch replay across 223 files pass.
Installation and activation on the Mac remain blocked.

One native installation can keep up to eight independently verified Google
accounts. `link_account` takes the requested email, keeps a separate credential
and companion directory, and reuses that email's pending sign-in. Google and
host approvals remain explicit. The original account is never disconnected.
The additional profile keeps the original server origin.

`list_linked_accounts` shows the linked emails and active profile.
`use_account` selects an account for the actual host-supplied Claude or Codex
chat identity. Conductor's native identity mapping is preserved. Each chat is
pinned when context or messaging starts: another account uses a new chat,
which prevents existing threads and queued replies from changing identity.
Workspace-scoped and managed shared conversations cannot select accounts.
Native hooks follow the same routing; stale companion requests are rejected.

Selecting an account pauses this chat's capture by default. The owner can
explicitly choose `syncHistory: true` or `set_chat_account_sync(enabled: true)`
to capture this whole chat, including earlier visible turns, to that account.
This is not implied by adding an account or by joining a space. Account-wide
sync and source exclusions still apply. Existing archives remain where they
were uploaded; nothing is migrated or merged. Other chats keep their existing
account. The original profile retains collection of unassigned supported native
chats; secondary profiles upload only explicitly assigned chats. Sources without
an unambiguous native identity are withheld in multiple-account installations.
Regular Claude and ChatGPT web histories are not collected by these tools.

Canonical uploads, durable pending retries, and Conductor/native transcript
aliases use the same account ownership check. Selection waits for an already
started upload; subsequent uploads from its old account are blocked. Paused
history cannot complete a new on-demand snapshot. Already saved private history
is retained, so pause is not deletion. Linking is blocked if the primary companion
cannot complete its supported upgrade to runtime67; an older collector must not
continue alongside a new account profile without these protections.

Validation includes separate credential files, mismatching Google identities,
revoked/unverified accounts, pending-upload races, subagent aliases, scoped-chat
restrictions, actual signed-account stdio routing, cross-account history denial,
and legacy/modern discovery with no setup side effects. Tests use synthetic
identities on an isolated relay; they do not prove a real Google or installed
Mac walkthrough. See `implementation/multiple-accounts-verification.json`.

The live server remains `20261031-setup-activation`; patch 57's server invitation
change remains published but undeployed. This native feature requires its new
package and host activation. Current Mac activation cannot be attempted because
Conductor previously rejected `RunLocalCommand`: “Local execution is not enabled
for this session.” No alternate route, permission change, or denial retry was used.
The separate work-machine missing-history investigation remains unresolved.
