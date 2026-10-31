# Imported conversation excerpts — 31 October 2026

Patch 54 extends the native message-body boundary to imported ChatGPT
conversations. It reconstructs the complete indexed conversation from stored
message rows and compares it byte-for-byte with the pinned archive read before
selecting exact message bodies. Source titles, generated role headers, message
IDs and reply IDs remain private classifier evidence. The complete conversation
and actual source title still govern confidentiality. Embedded role headers are
ordinary message text, never new message boundaries.

The provider, prompt v5, 0.995 cutoff, owner rules, expiry, membership, source
revision checks and large-source bounds remain unchanged. The 160-file server
bundle changes only `space-context.mjs`; no native package or migration changes
are needed. All 645 core tests and 14 extracted-bundle tests pass; the 54 ordered
patches replay exactly across 217 changed files. Four of five new regressions fail
on the prior source. The first final-suite run exposed a fixture that compared
untrimmed input with stored text; that failure is retained, and the corrected
fixture uses an explicit end marker to test exact Unicode bytes across chunks.

The first production check on patch 53 withheld a permitted imported launch
answer at 0.9921505. A four-call synthetic format comparison admitted the exact
body while withholding the old generated projection. However, a realistic
imported-archive fixture still withheld the public sample. Format alone is not a
complete reliability fix.

Two further prompt experiments were rejected. Version 7 improved the additional
corpus from 12/20 to 15/20 allowed, but regressed native public admission and still
withheld the imported public sample. Version 8 also withheld the imported sample.
No forbidden fixture was released. These 125 additional provider calls are
synthetic, development-selected evidence, not an independent final holdout.
Neither prompt is shipped; the already evaluated version 5 remains selected.

The original live failure, rejected experiments and cleanup receipts are retained.
The candidate is packaged for `20261031-imported-excerpts`; its deployment state
and any later live acceptance are recorded in the
[verification record](../implementation/imported-context-excerpts-verification.json).
Do not equate this metadata/privacy correction with complete admission reliability
or all-P0 readiness.
