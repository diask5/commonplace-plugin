# Conductor collection after a background restart

1 November 2026. Patch 64; published native 0.4.40/runtime73.

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

## Installed and live result

Both native aliases are published and all six uploaded asset hashes match. Source
PR #63 and distribution PR #64 are merged; the default distribution branch is
unchanged. Cloud activation reached runtime73 with identity and saved permissions
preserved. Mac 0.4.40 installation passed both registry/config checks, but the
last observed active companion was runtime66: older loaded hosts had restarted
legacy companions during the guarded handoff.

A fresh default Codex chat loaded 0.4.40, found the same verified owner, published
its progress to Personal, and sent exactly one synthetic message. The parent
received it natively and the service receipt became accepted after 101 seconds.
The ordinary assistant transcript was independently searched and read from the
native archive, including its final marker. The source read covered the relevant
page, not the entire document. All 699 core tests, 48 extracted-runtime checks,
both-alias packaging and exact replay pass. The first extracted harness lacked a
relay fixture; that pre-test failure is retained alongside the corrected pass.

The original long chat advanced from record 94 to 577 but remains incomplete.
A fresh short-chat success is not complete history coverage, clean onboarding,
independent-human acceptance, or evidence that every host is seamless.

## Mac verification interruption

A bounded maintenance script used the normal sync control to pause uploads while
the legacy companion completed its supported restart guard. It was configured to
restore the previous setting in finally after at most 150 seconds of waiting.
The incoming Conductor message then removed this chat's Mac execution binding.
RunLocalCommand returned: “No authorized Mac is bound to this chat. Send a message
from the Mac you want to use.” No retry or alternate execution route was used.
The last observed activation was still waiting; final runtime and sync restoration
remain unverified. No forced process signal or host permission change was used.
