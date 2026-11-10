# AI Chat

Chino's AI answers questions, summarizes channels, and drafts server changes. It uses only data the server and the person asking are allowed to see, and it never changes a server by itself.

## The five features

| Feature | What it does | Who can use it |
|---|---|---|
| **Chat** | Everyday questions in chat. | Admins only, Members, configurable |
| **Server knowledge** | Answers from sources an admin approved, with citations. | Admins only, Members, or Public |
| **Catch Up** | Summarizes a channel the person can already read. | Admins only, Members, configurable |
| **Automation** | Drafts automations for an admin to review. | Admins only (always) |
| **Server setup** | Plans channel and role changes for an admin to approve. | Admins only (always) |

Each request belongs to exactly one feature. Every permission check runs against that feature.

## Access levels

Admins set Chat, Server knowledge and Catch Up to one of:

- **Admins only** — plus an optional allow-list of roles and people.
- **Members** — anyone in the server.
- **Public** — anyone, signed in or not. Only Server knowledge can be public.

New servers start these three at **Members**. Automation and Server setup are always admins only. Opening a feature to the public requires the Manage Server permission and is audited.

## Models

- People pick a model alias, or **Auto**. Real model names are never shown.
- **Auto** matches the model to the task: harder tasks (Server setup, Automation) get a stronger model than light chat, within the limits of the person's plan.
- A plan is never given a model it may not use. A person's own pick is respected.

## What the AI can read

The AI reads a channel only when **both** are true:

1. An admin added it to "Channels the AI may read".
2. The person asking can read it in Discord.

Other rules:

- In a public channel, the AI is limited to what that channel's audience can see. Private threads are never read there.
- Catch Up reads only the channel it is asked in.
- Messages from people who opted out of the AI are skipped, and their names and mentions are not resolved.
- The AI can only use tools it was offered. Anything else is refused.

## Pictures

A picture reaches the AI only if the person's switch, the server's switch and the plan all allow it. Limits: up to 3 pictures, 5 MB each, PNG / JPEG / WebP / GIF. Guests cannot send pictures.

## Server knowledge

- An admin adds sources: pasted text, a web page, a channel, or pinned messages.
- Answers come only from those sources and cite them. The AI says it is not sure when evidence is weak.
- A channel or pinned source is used either for members who can read that channel (default) or for everyone. Choosing everyone needs Manage Server and is audited.
- Nobody who opted out is ever quoted.
- Files and pictures in sources are named but never read, fetched or linked. Asked for a file, the AI points the person to the server.
- Sources refresh every 24 hours; sources open to everyone every hour. Limits: 25 sources per server, 500 most recent messages per channel source.

## Guests

- Guests start at `/chat` (plain chat, no server data) or a server's public link `/chat/<id>`.
- A public link works only while Server knowledge is public. The link id is random, not the server id, and an admin can rotate it at any time.
- A guest passes a Cloudflare Turnstile check, then gets a session good for one server (or none) for 24 hours.
- In a server, a guest can use Server knowledge only. Never Chat, Catch Up, Automation or Server setup.
- A guest's message is capped at 1,000 characters (the server's own cap for everyone is 8,000).

## Behavior

- Replies are short and chat-like, no filler.
- Text the AI reads (messages, web pages, sources) is treated as evidence, never as instructions.
- The AI never changes a server on its own. Server setup produces a plan an admin approves; automations are drafts saved only when a person presses Create.

See [Usage Limits](/docs/ai/limits) for allowances and [Privacy](/docs/privacy/overview) for what is stored.
