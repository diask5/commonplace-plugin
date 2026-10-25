# Customer demo: your context as files

Fifteen minutes. One Mac with Claude Code and the Meet Proxy plugin connected to
a Google account whose work-chat sync is on. Open these before you start:
the Meet Proxy web app signed in as that account, a terminal, and one Claude Code
chat in a project folder.

## 1. The problem (1 minute)

"Every agent you use starts from zero. Your decisions live in last week's
Claude chat, a Codex session, and a ChatGPT export. We make all of it one folder
that any agent can read."

## 2. Show the folder (3 minutes)

In the terminal:

```sh
ls ~/.commonplace/context/current/
head -40 ~/.commonplace/context/current/INDEX.md
```

Point out: one text file per conversation, newest first, with source and
project. Then search without any model. In the Claude chat ask for
`context_folder_status` once; it returns the exact `searchCommand` for this
machine. Paste it into the terminal as a variable and run it:

```sh
SEARCH='<searchCommand from context_folder_status>'
eval "$SEARCH" '"release date"' --limit 3
```

Show a hit, then open the cited file at the offset with `sed -n`. "Plain files,
hashed against the server copy, swapped atomically."

## 3. Ask an agent (4 minutes)

In the Claude Code chat:

```
/meet-proxy:context What did we decide about the release date, and who owns rollback?
```

The agent runs the search command, reads the files, and answers with the file
paths it used. Follow up with something that needs two conversations combined,
for example a budget minus committed spend. Then ask something the archive does
not contain and show it says so instead of inventing an answer.

## 4. Show it staying current (3 minutes)

In a second Claude Code chat, state a new decision in plain words, for example
"Decision: the demo environment moves to Friday." Wait about twenty seconds, then
in the terminal:

```sh
eval "$SEARCH" --phrase "moves to Friday"
```

Back in the first chat, ask again; the answer now reflects the new decision.
"Collector on the Mac, merge on the server, mirror back down. No model in that
loop."

## 5. Control (2 minutes)

In the web app, open **Your agents → Setup status**: the "Local context folder"
row names the computer and the conversation count. Open **Collection coverage**,
exclude one conversation, and run the phrase search again: it is gone from the
folder within a refresh. Restore it. "Exclusion follows every copy."

## 6. Close (2 minutes)

"Same folder on every computer you connect, including cloud workspaces. The
server only collects and merges. There is no agent in the middle deciding what
to tell you, and nothing to wake up."

## If something is off

- Folder missing: the chat's `context_folder_status` reports why. Usually the
  account is not connected or the first sync has not finished.
- Search returns nothing: use two or three key words, not a sentence. `--phrase`
  for exact strings.
- A new message does not appear: the collector runs while the Mac is awake and
  the chat's transcript is in a supported location; check **Collection
  coverage** for the chat's state.
- Keep the cloud agent out of the demo unless asked. It still works, but the
  story is the folder.
