# Product Spec: Meet Proxy

Oct 24, 2026 · @Zane Homsi

Status: Draft v3 | Sources: "Meat Proxy feature specs" voice memo (Oct 14, 2026), "Meet Proxy user flow design" transcript (Oct 24, 2026), Zane's comments in thread (Oct 24, 2026)

Note: Items marked [proposed] are not in either transcript. They are suggested details to fill gaps and should be confirmed or cut.

## 1. Summary

Meet Proxy lets people connect their AI agents (Claude Code, Codex, and others) so the agents can talk and work together on their owners' behalf. The anchor use case is a Chief of Staff: someone needs to reach me while I am unavailable or I don't want to be in the conversation, so they talk to my agent instead. A user signs in, attaches their agents, and invites someone by asking their own agent in natural language. The other person accepts with one click and the agents are connected. Every conversation lives in a single agent-to-agent thread that both owners can read in full, and every user can see and sever every connection their agents have.

## 2. Problem

- People increasingly work through coding and personal agents, but those agents are siloed. There is no simple way for my agent to collaborate with yours.
- When I am unavailable, people who need me have no good proxy. A human chief of staff is not an option for most people.
- Granting another person's agent access to mine raises trust questions. Users need to control what it can say, for how long, and to see everything it said.

## 3. Goals

- Account setup and agent attachment in minutes.
- A connection flow that is exactly three steps: invite, accept, connected. Either side can start it.
- Full auditability: both owners see both sides of every agent-to-agent conversation.
- Protect the owner's private context while still answering useful questions.
- One-action revocation and clear boundaries on time and topic.

## 4. Non-goals (v1)

- Per-agent view of which friends or colleagues have access. The Oct 24 transcript calls this "eventually."
- Integrations beyond Claude Code and Codex, except personal agents as a stretch.
- Multiple threads between the same pair of agents. This is excluded by design (see 7.8).

## 5. Users

- **Owner:** Has an agent (their Chief of Staff) that others can talk to. Wants to stay in control of what it shares.
- **Requester:** Needs something from the owner and talks to the owner's agent, usually through their own agent.
- Every user can be both, and both are owners of their own agent.

## 6. Example Scenario

10 users each create an account and attach 2 agents, giving a pool of 20 agents. Sam needs an answer from Zane, who is in meetings all day. Sam tells their agent, "Send an invitation to Zane. I need to talk to his Chief of Staff." Zane accepts. Sam's agent and Zane's agent talk in a single thread that both Sam and Zane can read. Zane's agent answers within the topics and time window Zane set, without revealing the private sources behind its answers.

## 7. UX Requirements

### 7.1 Sign up and log in

- Single "Continue with Google" button. Gmail is p0, rest are optional.
- No extra forms on first sign-in. Name and avatar come from the Google profile. [proposed]
- After first sign-in, the user goes straight to "Attach your agents." Returning users land on the agents list.

### 7.2 Attach your agents

- Dedicated onboarding screen titled "Attach your agents."
- Shows supported agents as selectable tiles: Claude Code and Codex (P0), personal agents (P1), others such as Grok shown later or as "coming soon." [proposed: "coming soon" treatment]
- User can attach any number of agents, including more than one of the same type.
- Each tile shows a clear attached state once connected. [proposed]
- A user can finish onboarding after attaching one agent and attach more later from the agents list. [proposed]
- Ends on the agents list, showing what was just attached.

### 7.3 Agents list (home)

- Shows every agent the user has attached.
- Layout follows an iMessage contacts style: one row per agent, simple and scannable.
- Each row shows the agent name and type (for example Claude Code, Codex), an avatar or icon for the agent type [proposed], and whether the agent has active connections and how many [proposed: count].
- Agents with active connections are visually distinct from those without, so the user can tell at a glance how far their access reaches. The Oct 24 transcript calls this critical.
- Tapping a row opens the agent detail view.
- An entry point to attach another agent is always visible. [proposed]
- Navigation between the agents list and the inbox (7.8) is always one tap away. [proposed]

### 7.4 Agent detail view

- Shows data about the agent. Exact fields to be defined: attached on, has # live connections.
- Lists every active connection: the other agent's name and type, the person who owns it, and the boundaries in effect (7.7).
- Each connection links to its inbox thread and has a sever action (7.10).
- Later (P2): which friends or colleagues have access to this agent.

### 7.5 Start a connection

Either side can start it, and both paths are initiated in natural language inside the user's own agent.

**Requester-initiated (request access):**

- The requester (e.g. Sam) says, for example, "Send an invitation to Zane. I need to talk to his Chief of Staff."
- The requester's agent automatically extends the invitation to the owner.
  - In this example, the assumption is that Sam's agent has access to iMessage / email on Sam's machine, generates an invitation code and sends it to Zane via one of those channels.
- The owner only has to accept.

**Owner-initiated (delegate):**

- The owner gets asked for something and wants their agent to handle it.
- The owner tells their agent, for example, "I need you to take this conversation with Sam."
- The agent returns a link or code. The owner copies it and texts it to the requester.

**Delivery:**

- Ideal: the agent finds the contact on the user's machine and sends the invite by email or iMessage.
- Fallback: the agent returns an invite URL or code the user copies and sends themselves.
- The agent confirms what it did, for example "Invite sent to Sam via iMessage" or "Here's your invite link." [proposed]
- If a contact match is ambiguous, the agent asks the user to choose before sending. [proposed]

### 7.6 Accept an invite

- The recipient opens the link (or enters the code) and lands on a page modeled on a Partiful invite.
- The page clearly states who is inviting them (the inviter's name), and the recipient can define which agent they want to connect with (the agent's name), and the boundaries of the access if the owner set them [proposed].
- One primary action: accept. Pressing it establishes the connection.
- The full flow must be as simple as: invite sent, invite accepted, connection established. No extra steps for a user who is already signed in with an agent attached.
- Recipients without an account sign in with Google and attach an agent, then return to the invite to accept. [proposed, not covered in either transcript]
- A clear success state confirms the connection and opens the new inbox thread. [proposed: opens thread]

### 7.7 Set boundaries

- When an owner accepts or extends a connection, they can set two kinds of boundaries. **Time:** access lasts for a set period, then expires. **Topic:** what the agent is allowed to comment on.
- Sensible defaults so setting boundaries never blocks the three-step flow.
  - Time default: 2 weeks
  - Topic Default: Avoid personal details about family, religion or finances.
- Boundaries are editable later from the agent detail view or the thread. [proposed]
- Enforcement relies on the model following strict instructions, backed by auditability between both parties (7.8).

### 7.8 Inbox and auditability

- A messaging inbox lists every agent-to-agent conversation the user's agents are part of.
- **Monothread by design:** each pair of connected agents has exactly one thread. There cannot be multiple threads between the same two agents. Every new request between them continues in that same thread.
- Example: when Zane's Claude and Kyle's Codex communicate, they share one thread. There cannot be a second thread between Zane's Claude and Kyle's Codex.
- Threads are per agent pair, not per person pair. If Zane's Codex later connects with Kyle's Codex, that is a separate thread. [proposed]
- Inbox layout follows iMessage: one row per thread, showing both agents, both owners, the latest message preview, and the time. [proposed: row contents]
- **Full two-sided visibility:** both owners see the entire thread, including both agents' messages. Neither side has a private view.
- This visibility is the social proof that keeps both parties in check. Each person knows the other can see everything.
- Each thread header shows the connection's boundaries (time remaining, allowed topics) and a sever action. [proposed]
- Owners can read threads at any time. Whether owners can type into a thread directly is an open question.
- When a connection is severed or expires, the thread stays readable as a record but no new messages can be sent. [proposed]

### 7.9 Context guarding

- The owner's agent separates the answer from the sources behind it.
- A requester can see the owner's response but not the ground-truth sources used to produce it (documents, emails, notes, and so on).
- This applies in the thread view too: the requester never sees sources. [proposed: whether the owner sees their own agent's sources in the thread is an open question]

### 7.10 Manage and sever connections

- After a connection is established, both users see it on their agents list, in the agent detail view, and in the inbox.
- Either user can sever a connection at any time from the agent detail view or the thread.
- Severing takes effect immediately for both sides. [proposed: immediacy]
- A short confirmation before severing to prevent accidental taps. [proposed]

## 8. Design Inspiration

### 8.1 Partiful (invite and accept)

Why: Partiful makes accepting an invite feel instant and low-commitment. That is the feeling we want for connecting agents.

- **Link-first:** The invite is just a URL sent by text or email. No app install required to open it.
- **Host is front and center:** The page leads with who invited you and what you are invited to. For us: inviter name and agent name.
- **One big button:** RSVP is the single obvious action. For us: Accept.
- **Instant confirmation:** You know right away you are in. For us: "Connection established."
- **Personality:** Partiful pages feel friendly and playful rather than corporate. Worth borrowing for a product that could otherwise feel like a permissions screen.

### 8.2 iMessage (agents list, inbox, and detail)

Why: Everyone already knows how to read an iMessage list. The agents list and inbox should feel just as familiar.

- **Simple rows:** One row per agent (agents list) or per thread (inbox), with an icon, name, and a short status or preview line.
- **One thread per contact:** iMessage keeps one running thread per person. Our monothread rule is the same idea applied to agent pairs.
- **Glanceable state:** Like unread indicators, a row should show at a glance whether an agent has active connections or a thread has new activity.
- **Tap to go deeper:** Tapping a row opens the thread or a detail view, like a contact's info page.
- **Minimal chrome:** No dashboards or tables on the home screen. Just the list.

## 9. Requirements

- **P0:** Google sign-in.
- **P0:** Attach Claude Code and Codex.
- **P0:** Agents list showing active connections per agent.
- **P0:** Requester-initiated and owner-initiated invites in natural language, returning a shareable link or code.
- **P0:** Invite landing page naming the inviter and their agent, with one-click accept.
- **P0:** Inbox with exactly one thread per agent pair.
- **P0:** Both owners can read both sides of every thread.
- **P0:** Responses never expose the owner's underlying sources to the requester.
- **P0:** Agents inherit their owner's tool access and cannot exceed it.
- **P0:** Sever a connection from either side.
- **P1:** Time and topic boundaries on a connection.
- **P1:** Agent sends invites directly via email or iMessage using local contacts.
- **P1:** Attach personal agents.
- **P1:** Agent detail view with data about the agent.
- **P2:** Per-agent view of which people have access.
