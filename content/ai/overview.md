# AI Chat & Modes

Chino's AI answers questions, summarizes channels, drafts automations, and plans server changes. It uses only data the server and the person asking are allowed to see, and **never modifies a server by itself**.

<!-- TODO: Put screenshot/video of `/chat` mode switcher or [`/ask`](/docs/reference/commands) in Discord here. -->
## The Six AI Features

| Feature | What it does | Where to use | Who can use it |
|---|---|---|---|
| **Chat** | Everyday questions with server-aware read tools | [`/ask`](/docs/reference/commands), `/chat`, `/dashboard/<id>/chat` | Configurable (*Admins*, *Members*) |
| **Server Knowledge** | Answers strictly from approved sources with citations | [`/ask-server`](/docs/reference/commands), `/chat/<slug>` | Configurable (*Admins*, *Members*, *Public*) ([details](/docs/ai/knowledge)) |
| **Catch Up** | Summarizes recent messages in one channel (max 15 citations) | [`/catchup`](/docs/reference/commands), `/dashboard/<id>/chat` | Configurable (*Admins*, *Members*) |
| **Automation** | Drafts event-condition-action rules for review | [`/automate`](/docs/reference/commands) (`draft`), `/dashboard/<id>/chat` | Admins only ([workflows](/docs/server/engagement/automation)) |
| **Server Setup** | Plans channel and role changes for approval | [`/setup`](/docs/reference/commands), `/dashboard/<id>/chat` | Admins only (always) |
| **Docs Help** | Answers questions about Chino and highlights dashboard UI | `/docs` assistant | Everyone (guests included) |

## Models

Pick a model from the menu or leave it on **Auto**. **Auto** picks a stronger model for harder tasks like *Server Setup* and *Automation* and a lighter model for quick chat, within your plan's limits (for up to date data, see [Pricing and Limits](/docs/reference/pricing)).

## What the AI Can Read

- **Channels:** Readable only when **both** an admin added the channel in **Channels & Memory** (`/dashboard/<id>/ai-chats`) **and** the asker has Discord permission to read it.
- **Forum Channels:** Forum posts are listed, searched by title/tags, and read under the same two conditions.
- **Public Replies:** In a public Discord channel, Chino only reads what that channel's audience can see; private threads are never read there.
- **Opt-Outs:** Messages from anyone who [opted out of AI](/docs/privacy/overview) are skipped, and their names/mentions are never resolved.
- **Personal Tools:** Signed-in users in interactive Personal or Server chat can ask Chino to list, create, snooze, or cancel their own [DM reminders](/docs/personal/reminders) and list or create their own [Chino Together plans](/docs/together/plans).

## Pictures

An image reaches the AI only when **your personal switch**, **the server's switch**, and **your plan** all allow it.

- **Limits:** Up to **3 images**, **5 MB** each (`PNG`, `JPEG`, `WebP`, `GIF`).
- **Guests:** Cannot send images.

## Safe Server Changes

- **Server Setup ([`/setup`](/docs/reference/commands)):** Starts by asking *"What may Chino change?"*, inspects the server, and outputs an approval card. Requires `Manage Server` (and bot `Manage Channels` + `Manage Roles`). Nothing runs until you press **Approve**.
- **Automation Drafts:** Outputs a validated rule card with **Create (turned off)**, **Create and turn on**, or **Discard**.
