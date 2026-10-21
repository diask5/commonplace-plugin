# Local integration environment

Run the UI, signed relay API, SQLite database, collector, context snapshots,
search tools, task worker and durable agent messaging without a deployment.

```sh
npm ci --ignore-scripts
npm run dev:local
```

Open `http://127.0.0.1:43210/__local` for test controls, `/` for the application,
`/context` for search, and `/work-agent#work` for setup. Node 24.14.1 is the CI
version. No Docker, Google credentials, ChatGPT subscription or production access
is needed for this environment.

The Conductor run configuration starts the same environment. In a cloud
workspace, `npm run dev:preview` explicitly shares the port through that
workspace's authenticated Conductor preview. This is a development preview,
not a production deployment. Outside Conductor use `dev:local`.

## Real components and simulated boundaries

The lab uses production application routes, schema migrations, installation
signatures, account isolation, file collection, versioning, exclusions, FTS
search, task leases, citation validation, consultation queues and reply handling.
Two fixture agents register only against the local relay. Sample transcript files
live inside the lab directory; the collector never scans your actual chats.

Google identity, subscription sign-in, model execution and native host delivery
are simulated. The model fixture reads the real index and returns quoted source
text with checked citations. It supports release questions, `search: <keywords>`,
and `Ask the reviewer about the release`. It does not measure model reasoning,
real OAuth, subscription limits, Docker isolation or Conductor wake behavior.
Those boundaries have separate unit/package coverage and still require a live
acceptance test after deployment. Do not use lab setup prompts to connect real
native chats; local fixture agents are already registered.

## Walk through the complete flow

1. Open the library. Search `release`, filter to project `release`, and read the
   surrounding source. Change to exact text to search `release date = Thursday`.
2. Create `What is the release plan?` in the application. The real worker finishes
   a task using the simulated model's retrieved text and citations.
3. In test controls, move the release to Friday. Verify the next search and answer
   show Friday. Pause sync in the application, edit again, and resume to catch up.
4. Take the devices offline and create `Ask the reviewer about the release`.
   The task waits. Bring the devices online; the same task completes after a
   signed reply, without creating acknowledgment loops.
5. Exclude and restore a conversation in Agents → Collection coverage. It
   disappears from search until recollected. Deleting fixture messages exercises
   actual deletion tombstones.
6. Switch to the empty sample account. Connect the simulated model with the
   device-code option, run the connection check and see that personal context is
   still empty. Test sign-in failure, worker outage, account limits and cancellation.

The dashboard exposes status and recent events. A visible banner identifies every
application screen as a local simulation. The empty and populated sample accounts
are separate, so account-switch and disclosure tests exercise real boundaries.

## Tests

```sh
npm run test:local
npm test
npm run test:ui
npm run test:deployment
```

`test:local` creates fresh disposable environments and tests collection → search
→ cited answer, edits, sync pause, exclusions/restore, offline consultations,
sign-in failure, model limits, cancellation, persistence and origin rejection.
Browser tests cover search filters/pagination, surrounding reads, setup, actual
task completion, account-switch races, mobile layout and accessibility. They use
the installed Google Chrome; set `CHROME_BIN` if it is at a different path.
Screenshots go to `artifacts/local-lab/`, or `LOCAL_LAB_SCREENSHOT_DIR` when set.
These tests are also part of the application/UI CI suites.

## State and cleanup

Normal development keeps synthetic state under `.data/local-lab/` so restarting
preserves fixture identities, uploaded context and tasks. The directory contains
its own `LOCAL-LAB.json` marker, local signing material, SQLite database, sample
transcripts and generated context snapshots. These files are gitignored. The
server refuses to open a nonempty directory without its own marker.

Stop with Ctrl+C. To start a fresh lab, choose a new empty directory:

```sh
LOCAL_LAB_DIR=.data/local-lab-fresh npm run dev:local
```

`LOCAL_LAB_PORT` changes the port. Reuse the same port when restarting persisted
state, because the fixture installations are bound to that relay origin.
`LOCAL_LAB_HOST` defaults to loopback; explicit shared previews use `0.0.0.0` and
an exact HTTPS `LOCAL_LAB_PUBLIC_ORIGIN`. Browser mutations retain origin checks.
Production database and credential environment variables are ignored.
