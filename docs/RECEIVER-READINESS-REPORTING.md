# Receiver readiness reporting

1 November 2026. Native 0.4.44/runtime77, patch69, corrects a misleading setup result observed in the fresh 0.4.43 chat. The saved receiver state was ready, but its completed poll checkpoint was over20seconds old, so automatic delivery was correctly unconfirmed while the label still said ready and suggested running setup again.

A current live receiver with a stale successful checkpoint now reports stale, the checkpoint age and unconfirmed delivery, without helper/reinstallation advice. Stopped, failed, starting and obsolete-runtime cases remain distinct. The20-second readiness criterion, identity/PID/lock checks, message dispatch, route eligibility, host permissions and server remain unchanged. This is an honest status correction, not proof of successful delivery.

The first failing regression and actual metadata samples are retained. A successful production receiver cycle took52.820seconds and passed from fresh to stale to fresh without recording a failure.840core tests,32extracted-native tests, both-alias packaging,25focused checks and five independent isolation checks pass. Counts overlap.69patches replay exactly across264changed files. See [verification](../implementation/receiver-readiness-reporting-verification.json) for publication and installation state.
