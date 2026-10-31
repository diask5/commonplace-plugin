# Invite into the current space — 31 October 2026

Patch 57 is **published, not deployed**, as `20261031-current-space-invite`.
Conductor rejected `RunLocalCommand` with “Local execution is not enabled for
this session” before executing the deployment command. The public asset still
matches live server `20261031-setup-activation`; no alternate deployment route
or automatic retry was attempted. Native 0.4.33/runtime66 is unchanged.

The top-bar Invite action previously defaulted to a new space even when a space
was open. If the signed-in account was a member, its current space disappeared
from the picker because only owned spaces were included. The UI gave no reason.

Invite now selects the visible space. Owners can immediately create its link.
Members see the same space selected, its owner's display name, and an explanation
that only the owner can invite. Creation is disabled, and **View space members**
opens the existing Members tab. No ownership, membership or sharing permissions
are changed. A new space remains an explicit choice.

Changing the visible space discards an unrelated invitation result. Loading
retries preserve the intended target, and an inaccessible target cannot silently
become a new space. On My context and other pages, a hidden board selection is
not treated as the destination. Existing retry nonces, clipboard handling,
account resets, 14-day expiry and removed-member protections are retained.

All 17 invitation/browser checks pass, including owned/member contexts, failed
loading and retry, exact invitation scope, no accidental space creation,
signed-in acceptance, removal, and phone/desktop accessibility. The 57-patch
replay matches 217 changed files. The server bundle changes only two modules
within the same 160 files. See
[verification](../implementation/current-space-invite-verification.json).

This update does not address incomplete collection on another work machine.
Setup claims and collector counts must remain separate from proof that every
expected conversation was uploaded.
