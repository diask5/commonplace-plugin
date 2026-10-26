# Zero-to-knowledge verification

The 26 October 2026 audit tests the path from an empty account to collected,
searchable context, a local folder, and rule-gated sharing. Release 0.4.21 /
runtime56 fixes a collector cursor bug found during the real Mac test. The relay
also validates large archives with bounded parallel disk reads, retaining every
integrity check instead of serially reading thousands of sections per request.

## Reproducible end-to-end journey

Run `npm run test:knowledge` in the implementation checkout. Set
`COMMONPLACE_E2E_PLUGIN` to an extracted, verified plugin to exercise packaged
native modules. Optional `ZERO_SCREENSHOTS` saves each browser stage.

The test starts with zero profiles and an empty native installation. It exercises
browser sign-in, the private setup handoff, Claude/Codex file collection, a child
chat, complete long Unicode text, hidden-reasoning/credential filtering, search,
paged MCP resources, byte-identical local files, appended messages, stale revisions,
group creation, two-person invitation acceptance, rules, actual indexed candidate
retrieval, approved excerpts, private audit, pause and exclusions.

Google identity, native host identity and classifier scores are explicit fixtures.
They do not establish real Google, operating-system app launch or classifier
accuracy. Signed HTTP, storage, indexing, browser behavior, and collection/mirror
modules are exercised directly. A separate 33 MB first-install test interrupts
file transfer, rejects partial publication, retries and reads every source to its
last message. Existing corruption, symlink, account and revision checks remain.

## Live checks and limits

The real Mac account is `diaskyle10@gmail.com` on `https://34.27.253.220`.
A real Claude CLI session created a harmless unique message; automatic collection
made that exact message searchable in the account. Its archive contained 292
documents and approximately 34.7 million characters. The initial local mirror
failed intermittently with native transport timeouts. These failures are retained
in the evidence, rather than counted as a pass.

Native 0.4.21 installation and production retesting are in progress; the machine
verification record will be updated after actual receipts. Existing chats may
still have an older MCP process loaded until their host reloads it.

“Full knowledge” means all currently supported, available visible histories and
explicit imports. It does not mean arbitrary repository files, every web-only
chat, binary attachments, or upstream MCP services. Offline devices cannot upload
new text. Excluded sources stay excluded. Sharing still evaluates bounded matching
candidates and can withhold allowed content; it is not a perfect classifier.

The original agent-centric product spec is superseded by the owner's context-only
Spaces / My context direction. Legacy messaging tests protect compatibility; they
are not a hosted-model requirement for context retrieval.

## Reproduction and release

Apply `implementation/zero-to-knowledge.patch` nineteenth, after
`sharing-walkthrough.patch`. Its manifest records exact changes. The full chain
reproduces 152 source files. Browser screenshots and detailed logs are saved under
`.context/zero-to-knowledge/`; summarized portable evidence is in
`implementation/zero-to-knowledge-verification.json`.
