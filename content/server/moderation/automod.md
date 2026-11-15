# AutoMod

Chino's AutoMod filters messages and nicknames in real time. Configure it in [`/mod`](/docs/reference/commands) (`automod`) or **Dashboard → Auto Mod** (`/dashboard/<id>/automod`).

![AutoMod rule graph and editor](/images/feature_automod.webm)

## Presets & Visual Rule Graph

- **4 Built-in Presets:** `basics`, `antispam`, `links`, `cleanchat`.
- **Visual Rule Graph:** Connect any rule node directly to one or more action nodes in `/dashboard/<id>/automod`.
- **Dry-Run Tester:** Test sample messages against your current rules in the dashboard or [`/mod`](/docs/reference/commands) before turning them on.

## All 14 Rule Types

| Rule | What it catches | Key settings |
|---|---|---|
| **Caps Lock Spam** | Excessive uppercase messages | Min `%` uppercase (`5–100`), min length (`5–1000`) |
| **Message Flood** | Rapid message bursts | `3–10` messages within `1–10s` |
| **Duplicate Message** | Repeated identical/similar messages | `3–10` messages within `1–60s`, min length (`5–50`) |
| **Excessive Mentions** | Mass-ping spam | Max mentions (`2–50`) |
| **Excessive Links** | Link spam | Max links (`2–20`), whitelisted URLs |
| **Bad Words** | Exact or fuzzy banned words | Custom word list |
| **Mass Emoji** | Emoji floods | Max emojis (`2–200`) |
| **Zalgo Text** | Corrupted/combining character spam | Zalgo density threshold |
| **Nickname Bad Words** | Banned words in member nicknames | Action: `resetnick` |
| **Ads Detection** | Unwanted promos/invites | **41 ad types** (Discord invites, YouTube, TikTok, Twitch, X, Telegram, Patreon, etc.) |
| **Anti Ghost Ping** | Mentions in deleted or edited messages | Action: `notify` |
| **Spoiler Abuse** | Excessive spoiler tags | Max spoilers (`2–20`), max spoiler length (`50–2000`) |
| **Block Text Spam** | Wall-of-text / ASCII spam | Max special char `%`, max lines, repeated chars, consecutive spaces |
| **Honeypot** | Posting in a designated trap channel | Trap channel ID |

## Actions & Custom Notices

- **7 Actions:** `delete`, `warn`, `timeout` (`1m`–`28d`), `kick`, `ban`, `resetnick`, `notify`.
- **Notice Placeholders:** `` `{user}` ``, `` `{mention}` ``, `` `{username}` ``, `` `{channel}` ``, `` `{server}` ``.
