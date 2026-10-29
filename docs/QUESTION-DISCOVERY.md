# Full-question context discovery

The recorded request “What is the Juniper Lantern private budget and audit marker?”
matched no sources; the shorter topic query found four candidates. That first
result was not a privacy pass. Patch 49 adds one bounded discovery fallback after
an empty search: remove common question words while preserving meaningful terms.
The fallback stays in the existing four-search budget and pins the first archive
revision. Explicit phrase/prefix queries and queries with no remaining meaningful
terms do not broaden. The original question remains in shared history.

Classification, whole-message excerpts, the 0.995 threshold, provider model and
prompt, deadlines, candidate cap and all authority/source fences are unchanged.
All 611 core tests pass. All 49 ordered patches replay exactly across 206 files.
The 159-file server bundle changes only space-context.mjs and passes isolated
HTTP/OAuth smoke checks, with synthetic identity and placeholder-page limits.
Server `20261029-question-discovery` is published and live. All 159 files match the
release and are readable by the service user; all three services are active.
Native 0.4.32/runtime65 is unchanged. The prior bounded-classification release is retained.

A separate verbatim-paragraph/list-item experiment passed 52 focused tests but
its bounded real-model diagnostic still withheld all four tested inputs. It used
the selected synthetic source and a simplified audience label, and disclosed
nothing to a recipient. It is preserved under implementation/experiments and is
not included in patch 49 or this release. No live sharing success is claimed from it.

Live browser acceptance: the formerly empty full-sentence private question now
finds four candidates, all withheld, with no provider errors or recipient checks.
A fresh public-brief question finds two candidates but still shares nothing:
scores 0.9920847781 and 0.9262219195 remain below 0.995. This closes the observed
question-discovery bug, not useful sharing or all P0 readiness. The selected demo
member was removed; group and activity reads return 404. See the verification JSON
for the exact request IDs and production evidence.
