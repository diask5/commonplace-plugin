# Conductor collection after a background restart

1 November 2026. Patch 64; native candidate 0.4.40/runtime73.

Live follow-through after the upload-fairness release exposed a separate gap:
the background daemon no longer inherited the original Conductor session
environment after activation. Its receiver kept staging visible messages, but
the uploader discovered only ordinary transcript directories. This cloud chat
stayed at record 94 and eventually appeared absent from the discovered roots.

The daemon now discovers already-staged Conductor cloud captures under its exact
account data directory without calling the host CLI for other sessions. Native
receivers continue to authorize and stage their own conversations. The collector
checks directory and file types, rejects linked roots and uses only the current
owner’s staging folder. Existing account selection, exclusions, consent and
complete-capture upload behavior remain enforced. Export checkpoints explicitly
record whether more host pages remain; an older or missing checkpoint reports
partial coverage rather than complete history.

Two regressions fail on the preceding source and pass after this change. All 699 core tests and the 29
focused history/upload/account checks pass, and exact replay of all 64 patches
matches 247 changed files. Full test, package, install and live read results are
tracked in `implementation/staged-collection-verification.json`.

This is a native-only change. Server `20261101-oob-activation` stays live. The
[upload fairness release](UPLOAD-FAIRNESS.md) and its initial activation results
remain preserved. Neither published packages nor a receiver reporting ready
prove complete context coverage. Web-only history remains outside native collection.
