# Prompt-based context sharing experiment

The owner requested natural-language sharing rules on 25 October 2026: search
across available context and classify each candidate before a recipient can read
it, using Perplexity's Decisions model first. This supersedes mandatory manual
document selection as the intended primary flow. An existing connection does not
thereby become a grant to the owner's entire archive.

**State:** the original isolated experiment is retained. The thirteenth source
patch adds an opt-in, persisted per-space gate on browser, remote MCP and native
account routes; see [message-first spaces](MESSAGE-FIRST-SPACES.md). It has not
been deployed or packaged. Existing accounts, source exclusions,
published packages and live permissions are unchanged. Only synthetic examples
are used here; no real archive is sent to Perplexity.

## Experience

Choose a person, describe what they can know, and preview the result:

> Share Project Lumen product decisions, progress and release dates with Zane.
> Never share customer identities, credentials, finances or confidential material.

The rule-testing page follows the existing invitation sheet: a lavender SVG arch,
tilted context/person tiles, warm cream surface and terracotta pill action. On
desktop, rules and the recipient view remain side by side in a full workspace.
Use **Preview for Zane** to update the reading pane; editing clears stale results.
On mobile, the same content uses the compact two-step card. **Refine your rules**
returns to the preserved prompt. Resizing preserves the draft and results without
new model calls. Technical
details are tucked into **About this preview**; failures remain visible. The global navigation now follows the owner’s latest Spaces / My context direction. Editing a prompt clears the old result. Testing
does not activate access. The older document picker remains available during
evaluation.

The eventual sharing action needs a persistent, recipient-bound, expiring grant.
This original experiment does not implement grant persistence or invitation
redemption. The newer space flow persists owner rules and group membership
separately; it does not implement selected-document or expiring person grants. Redaction and synthetic summaries are also deferred: the
binary gate releases exact excerpts or withholds them whole.

## Implemented boundary

1. Resolve the authenticated principal and owner-controlled grant on the server.
   Client names, tool arguments, emails in text and model output create no rights.
   Owner preview and recipient reads have distinct principal checks.
2. Retrieve eligible candidates privately. Excluded and foreign-owner sources
   never reach the classifier. Trusted callbacks must validate current source
   revisions, exclusions and any revoked device/source access.
3. Evaluate the exact proposed **title and text**, using private surrounding
   context for confidentiality labels and references. One candidate per request;
   candidate text is untrusted evidence, never instructions or consent.
4. Require a numeric `answers.share.noul` at or above **0.995**. This is an initial
   cutoff, not a measured 99.5% safety guarantee. Errors and uncertainty withhold.
5. Recheck grant content/revision, identity, expiry and every approved source
   after the whole batch. Mid-request changes discard the response. No streaming
   or positive cache bypass exists.
6. Return only `{excerpts: [{title, text}]}` to recipients. No raw paths, document
   IDs, offsets, candidate counts, rejected titles, scores or denial reasons.
   The owner preview separately provides a minimal audit. No source/key logging.

`createPolicyContextMcp` exposes only `search_permitted_context`. Its trusted
transport callback supplies principal/grant; tool arguments cannot override them.
It offers no raw archive tools or resources. Actual stdio tests cover discovery,
filtered reads, spoofed arguments, raw-read refusal and revocation. This adapter
is deliberately not registered on the live relay yet.

Bounds: 32 candidates/read, 8,000 characters/excerpt, 300/title, 16,000/surrounding
context, 4,000/rules. Oversize candidates are withheld, not truncated. Production
needs conservative chunking with inherited source restrictions and opaque
pagination. Splitting storage sections blindly can lose confidentiality labels.

## Perplexity research

Official documentation retrieved 25 October 2026:

- [Quickstart](https://docs.perplexity.ai/docs/decisions/quickstart):
  `POST https://api.perplexity.ai/v1/decisions`, bearer key, named `noul` question.
- [API reference](https://docs.perplexity.ai/api-reference/decisions-post):
  `{model, state, questions}` request; probabilities in `answers`.
- [Pricing](https://docs.perplexity.ai/docs/getting-started/pricing):
  `pplx-decider-v1.2` $0.02/million input tokens; Flash $0.01; free output tokens.
- [Decider for Mac](https://docs.perplexity.ai/docs/decisions/decider-for-mac):
  Apple silicon, macOS 13+, 16 GB memory, roughly 6 GB download. Local Flash uses
  the same API at `http://127.0.0.1:8080/v1/decisions` without a key.

Default: `pplx-decider-v1.2`, with no fallback to Sonar or other providers. The
docs recommend this larger model for nuanced/costly decisions and one candidate
per request. Explicit version names can still route to successors when retired;
responses echo the requested name. Revalidate on provider changes. Local
quantized Flash and hosted models need separate benchmarks.

Hosted classification sends even rejected candidates to Perplexity. Before
private archive activation, make this provider disclosure explicit and confirm
appropriate processing/retention terms. Local Decider is an alternative; it was
not installed or started here. Hosted classification does not keep data on-device.

## Run

Set `PERPLEXITY_API_KEY` securely in the process environment or in the gitignored
distribution-workspace file `.context/perplexity.env` (prefer mode 0600). Optional
`PERPLEXITY_ENV_FILE` selects a different private file. Values are parsed as data,
never executed or printed. The preview reloads configuration before each test.

```sh
cd .context/commonplace-source
npm run test:policy
npm run benchmark:policy -- ../policy-sharing/live-benchmark.json
npm run benchmark:policy -- ../policy-sharing/live-rule-probes.json --rule-probes
npm run preview:context
```

The preview prints a private `/preview/rules/open?token=...` URL. This sets an
HttpOnly cookie and redirects to the clean URL. Paid calls require that cookie
and same-origin JSON. Only owner rule text and eight fixed synthetic candidates
are accepted: no uploaded context, account IDs or arbitrary endpoints. One active
run, twelve runs/process. The API key never reaches the browser.

For an already-running Decider, execute on the same Mac:

```sh
PERPLEXITY_DECISIONS_URL=http://127.0.0.1:8080/v1/decisions npm run benchmark:policy
```

Only the exact hosted endpoint or literal loopback HTTP endpoints are accepted.
Redirects are refused; the hosted key is never sent to loopback. No automatic
retry/fallback. The cloud VM's loopback cannot reach an app on the Mac.

The live benchmark uses **28 hand-labelled synthetic cases**: allowed updates,
private facts, mixed content, confidential titles and neighbors, French,
obfuscation and prompt injection. Expected labels never enter model requests.
Reports include false approvals, false withholds, errors, latency and token cost.
Threshold sweeps are exploratory, not held-out validation. Missing configuration
produces `blocked` with no accuracy score. Canned provider responses in unit/UI
tests are never reported as live-model evidence.

## Measured results

Actual hosted `pplx-decider-v1.2` calls, 25 October 2026, cutoff 0.995:

| Run | Matched labels | Forbidden examples approved | Allowed examples withheld |
| --- | --- | --- | --- |
| Initial 28 cases | 25/28 | 0/20 | 3/8 |
| Eight later rule-change probes | 8/8 | 0/4 | 0/4 |

The initial false withholds were implementation details, a failing regression
test update, and French engineering progress. The later probes explicitly
permitted implementation details and failed tests; both then passed. The same
budget excerpt changed from approved to withheld when its rule changed. These
probes were added after the initial run and are diagnostic, not a large independent
safety assessment. The prompt, model and default cutoff were not tuned afterward.

Initial latency: median 130 ms, p95 234 ms; 10,807 input tokens, estimated
$0.00021614. Rule probes: median 165 ms, p95 243 ms, estimated $0.00005172.
The actual browser submitted eight samples, displayed two approved excerpts and
reported zero provider errors. Its screenshots show real provider output.

Main suite: 407 passed. Policy/unit/MCP/browser suite: 33 passed, including four
responsive widths and axe checks. Existing context UI regression: 24 passed.
These counts overlap. Eight-patch replay reproduced all 12 changed/new files.
See [raw benchmark](../implementation/prompt-based-sharing-benchmark.json) and
[verification](../implementation/prompt-based-sharing-verification.json).

## Before real sharing

Evaluate the actual model on a larger held-out corpus and then shadow-evaluate
owner-authorized content without recipient disclosure. Test long-context
boundaries, adversarial prompts and disclosures that become sensitive only when
combined across requests. A small passing benchmark cannot certify privacy.

Connect persistent grants, authenticated MCP sessions, invite/revocation UI,
source revision fencing, bounded pagination, budgets, audit retention and
provider configuration. Retain deterministic exclusions for sources that must
never leave the account/device. Recipients must not receive the owner archive
mount or raw resource access. Revocation stops future reads, not past copies.
Verify a real two-account flow before production activation.

Source delivery: eighth patch `implementation/prompt-based-sharing.patch`, after
`automatic-context-ingestion.patch`. Its manifest/verification separate fixture
tests, browser evidence and real provider evaluation.

The subsequent visual refinement is preserved in the ninth patch,
`implementation/sharing-rules-design.patch`. It changes the rule-testing UI and
its browser checks only. Both steps pass axe and overflow checks at 320, 390, 768
and 1280 pixels; reduced-motion preferences are respected. The new layout also
completed a real eight-excerpt Perplexity preview with two approvals and no errors.

The tenth patch, `implementation/sharing-desktop-layout.patch`, adds the complete
desktop workspace at widths of 960px and above. It uses a wide illustrated header,
a larger rule editor and a separate scrollable reading pane, while retaining the
mobile card below that breakpoint. All 38 policy/browser checks pass, including
both states at 320, 390, 768, 1024, 1280, 1440 and 1920 pixels, breakpoint changes
without data loss, and keyboard scrolling through long results. This is still
source and preview work; production authorization and classifier rules are unchanged.


The eleventh patch, `implementation/sharing-interactions.patch`, adds state-driven
SVG checks/approval motion, reduced-motion equivalents, cancellation through the
browser and provider, retryable setup/timeouts, keyboard submission and example
undo. Its final policy run passed 45 checks. One live eight-sample Perplexity run
returned two approved excerpts and no provider errors; no real archive was used.

The twelfth patch, `implementation/shared-spaces.patch`, integrates prompt drafts
into the new Spaces UI and merges Connections with Shared access. Drafts belong
to an exact space and current owner, survive reload in the browser tab, and are
cleared on owner reset/sign-out. They do not activate classifier access. Real group
membership, messages and explicitly uploaded shared files use existing service
contracts. Uploaded files are shared whole; they are not silently governed by an
inactive prompt draft. Upstream MCP gateway ingestion remains pending.
