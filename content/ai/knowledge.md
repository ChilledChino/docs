# Server Knowledge & /ask-server

Server Knowledge lets admins index approved info so Chino can answer member (or public) questions with citations, and say it is not sure when evidence is weak.

<!-- TODO: Put screenshot of `/dashboard/<id>/knowledge` sources list + [`/ask-server`](/docs/reference/commands) reply here. -->
## Supported Sources

Configure sources in [`/configure`](/docs/reference/commands) (`knowledge`) or **Dashboard → Knowledge Base** (`/dashboard/<id>/knowledge`):

| Source type | What it indexes | Default audience |
|---|---|---|
| **Pasted Text** | Custom text or FAQ entries | Anyone who can ask |
| **Web Page (URL)** | Public web page content | Anyone who can ask |
| **Channel** | Up to the **500 most recent messages** | Members who can read that channel |
| **Pinned Messages** | Pinned messages in a channel | Members who can read that channel |
| **Forum Channel** | Up to **300 open** + **200 recent archived** public posts (title, tags, first message, first **20 replies** per post) | Members who can read that forum |

## Audience & Privacy Rules

- **Members vs. Everyone:** Channel, forum, and pinned sources default to **Members who can read that channel**. Opening a source to **Everyone (including guests)** requires `Manage Server` and is written to the audit log.
- **Ephemeral Replies:** [`/ask-server`](/docs/reference/commands) replies are always ephemeral so channel-restricted answers never leak into public channels.
- **Opt-Out Respect:** Messages or forum posts authored by users who opted out of AI are never indexed or quoted.
- **Attachments:** Files and images in indexed messages are named as `(attached file: name)` but are never downloaded, read, or linked.

## Limits & Freshness

| Rule | Limit |
|---|---|
| Max sources per server | **25** |
| Question length ([`/ask-server`](/docs/reference/commands)) | **3 to 300** characters |
| Standard source cap | **500,000** characters / **200** passages (~1,000 chars each) |
| Forum source cap | **1,500,000** characters / **2,000** passages (post-level citations) |
| Auto refresh | Every **24 hours** (every **1 hour** for sources open to everyone) |
| Forum live post refresh | Single post refreshes ~1 minute after creation, edit, or early reply |
| Manual re-sync cooldown | **1 minute** (**10 minutes** for forums; none for pasted text) |
