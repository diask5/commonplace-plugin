Independent review disposition (root, 26 October 2026)

The reviewer confirmed both instruction deltas and their hashes, and raised four concerns.

1. Legacy learn_wiki/share_wiki descriptions still exist. No change is made to these capabilities: the tested library path is archive retrieval, the fixture model credential is read-only, and legacy writes remain out of scope. Their continued presence is a catalog/discovery limitation, not evidence that a write occurred. The candidate still exposes all 85 tools, so a model selecting an unauthorized legacy route fails the benchmark.
2. The remote catalog differs from the native filtered catalog. This is recorded as a limit: remote cloud results cannot certify installed-native behavior. The observation alone does not prove the catalog difference is the sole cause. No capabilities are removed merely to force a test pass.
3. The two native skills retained an ambiguous phrase after the new owner-selected-space paragraph. Fixed to say owner-selected group/space consistently. Patch38 was regenerated before publication; its remote module and the tested three substitutions are unchanged. Patch39 was replayed after the updated38.
4. Existing 8 routing/sharing and 26 archive/remote tests are regression checks, not model-behavior evidence. Reports already separate them. The three scope model cases passed; retrieval candidate model evidence remains separate and pending.

An additional argument-error reporting issue is preserved separately: some invalid archive calls return JSON-RPC -32603 rather than result.isError. The worker's characterization has 2 passing assertions and 3 TODO desired-behavior cases. This is not a pass on the desired behavior and does not diagnose the earlier Mac connection-unavailable failure. No error-handling implementation changed in these guidance patches.
