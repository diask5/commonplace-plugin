# Try Meet Proxy

Open **https://34.27.253.220/** and choose **Continue with Google**. Use your own
Google account throughout. The production application and native 0.4.33 package
are available. This is an early-use handoff with the limits below.

1. Open **My context** and connect the app you use. For Claude Code, Claude
   Desktop Code, Codex or Conductor, copy the prepared setup request into the
   intended chat and send it. Complete any approval or reload required by that
   host. Wait for the installation's collection receipts and successful source
   read; copying the prompt alone does not complete setup.
2. Ask that assistant a question about a recent supported conversation and check
   the cited source. Private collection runs on the connected computer while
   it is awake. A regular Claude/ChatGPT MCP connection can read existing context,
   but it does not automatically upload web-only conversations.
3. Create a **Space**, generate its invitation and send it to the other person.
   They sign in with their own account and accept. Membership alone does not
   enable either person's private-library sharing.
4. In **My sharing rules**, choose the allowed topics and exclusions, select a
   duration, and enable sharing. The default is 14 days. Each contributor controls
   their own rules. Approved excerpts become history readable by all current
   and future members; rejected material and classifier checks stay owner-only.
5. In **Messages**, request context from the contributor. Test a permitted
   question, then an excluded topic. Review the shared result from both accounts
   and the checks from the contributing account.
6. Pause sharing or remove the member to stop future requests. Removing a member
   also prevents their old invitation from restoring access. Previously shared
   content cannot be recalled.

The classifier can still withhold permitted information. The first signed check
after the classifier release did exactly that. After the imported-excerpt
correction, a fresh signed check shared the exact public answer, withheld private
content, preserved both sides of history and passed revocation. Both runs used
synthetic notes and the owner’s two selected accounts; neither is clean-user
onboarding proof. Do not promise that every ordinary question will produce an
answer. Explicit file uploads share the whole file and are separate from private
library classification.

The current Spaces product shares approved excerpts. It does not automatically
copy an assistant's final private-chat answer into shared history, nor does a
Space by itself establish an exact agent-pair thread. Those distinctions and
clean-machine/independent-human acceptance remain in the
[P0 mapping](P0-SPEC-MAPPING.md). Current production evidence is in the
[classifier release record](CLASSIFIER-RELIABILITY.md).
