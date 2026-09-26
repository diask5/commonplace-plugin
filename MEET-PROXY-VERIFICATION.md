# Meet Proxy 0.2.8: observed results

Published September 26, 2026. [Download the release](https://github.com/diask5/commonplace-plugin/releases/tag/meet-proxy-v0.2.8).

Meet Proxy connects accepted people through their existing agent conversations. This release changes the product name, preserves existing Commonplace identities and connections, and fixes the first-tool-list race during automatic connection.

## What passed

| Check | Observed result |
| --- | --- |
| Full local source suite | 317 passed, 0 failed, 0 skipped |
| Cold-start tool discovery | The first catalog contains messaging after delayed connection, without host refresh |
| Connection failure and explicit disconnection | Recovery remains available; the test does not advertise connected tools |
| Production relay, two disposable clients | Two initial questions received matching replies |
| Same-session restart | Identity persisted and a third exchange completed |
| Explicit move to a new session | A fourth exchange completed; the former receiver could no longer reply |
| Fresh public Claude install | Claude Code 2.1.278 installed `meet-proxy@commonplace`; all 88 files matched the tested package |
| Existing Claude update | `commonplace@commonplace` updated from 0.2.7 to 0.2.8 |
| Codex installation | Codex CLI 0.158.0-alpha.2 accepted the compatible update; 87 release files matched, with only the local manifest cachebuster differing |

The relay exchanges were scripted MCP clients using the real plugin and production relay, with synthetic content and zero paid model calls. One client supplied Conductor/Claude host metadata, the other Codex metadata. This verifies protocol, routing, restart and handoff behavior; it is not a demonstration of two models operating inside their native UIs.

## Still requires the affected Mac

The actual macOS Conductor application, its loaded Claude/Codex version, and idle message delivery were not tested in this Windows environment. The reported Conductor incident is not conclusively diagnosed from the available description. The startup race is a reproduced defect, not proof that it caused that specific incident.

Follow [the Conductor demonstration](docs/meet-proxy-conductor.md) in the affected session to close that gap. Opening a browser UI alone does not demonstrate a connected receiver or an answer. A plugin update requires the host to reload it, and host hook/message permissions still apply.

The hosted Files website and Commonplace Files 0.1.0 package are unchanged by this messaging-plugin release.

## Exact artifacts

- `meet-proxy-0.2.8.zip`: SHA-256 `f7562829022a82dc67ac1953505c4cbb6df86678d51b6e8d0c14c85d4c715753`
- `commonplace-0.2.8.zip` (compatible alias): SHA-256 `1bdda4e68646d1b8cd200e3e2a3d627c94d3d24a936068fa36e657fd4936587b`
- [Machine-readable verification](https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-v0.2.8/meet-proxy-0.2.8-verification.json)
- [Fresh public installation](https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-v0.2.8/meet-proxy-0.2.8-public-install.json)
