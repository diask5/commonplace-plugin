# Top-bar Invite — 31 October 2026

**Published and live as server `20261031-invite-cta`.**

Patch 55 adds an **Invite** button beside the profile avatar on every signed-in
page. The dialog shows the sender’s email, offers a new space or one of their
owned spaces, and creates a copyable invitation link. People no longer need to
find the Members tab before inviting someone.

Opening the dialog does not create a space or invitation. The sender explicitly
chooses the scope before creating the link. New spaces start with one owner and
private sharing off. Existing spaces grant access to their shared files and
message history, explained before submission. The existing 14-day invitation,
explicit signed-in acceptance and revocation behavior are unchanged.

Interrupted creation and invitation responses reuse their operation identifiers,
including after closing and reopening the dialog. Signed-out or expired sessions
hide the action and clear its private state. Member-only spaces are not offered
as invitation targets. Copy failure leaves a selectable URL.

The 13 invitation/browser checks pass, including real isolated group creation,
acceptance, removal, old-link refusal, scope selection, stable retries and account
expiry. Dialogs and the header pass overflow/accessibility checks at 320, 390 and
1440 pixels. The 55 ordered patches replay exactly across 217 changed files.
All 41 broader context/Spaces browser checks also pass. Evidence lives in
[the verification record](../implementation/invite-cta-verification.json).

The three-file server update is published and deployed. All 160 files and service
readability match the bundle; three services are healthy. Public TLS, setup,
OAuth and deployed asset checks pass. It reuses the existing deployment helper. Native 0.4.33/runtime66, authentication,
sharing permissions, classifier settings and stored context are unchanged.
