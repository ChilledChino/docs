# Privacy & Data Rules

What Chino processes, what is stored, for how long, and the controls you have.

## What Reaches the AI Provider

Prompts go to the AI provider configured by the bot's operator. Sent: system rules, your message and recent chat turns, tool results the AI requested (such as allowed channel messages or knowledge passages), and pictures if allowed. **Never sent:** tokens, passwords, or other servers' data. The provider's own terms apply to what it receives.

## What Is Stored

| Data | Stored? | Retention |
|---|---|---|
| **Saved AI Chats** | Only when **both** you and (for server chats) server admins enable saving | **30 days** without activity |
| **Unsaved AI Context** | In memory only | **~30 minutes** |
| **Docs Assistant Questions** | Never saved (even if chat saving is on) | - |
| **Raw Channel History, Images, Model Reasoning** | Never written to storage | - |
| **AI Usage Records** | Counts, timings, model alias, tokens only (no text); servers can set data use to `none` | - |
| **Guest Counters** | Session ID + short hash of visitor address (never raw IP) | **40 days** |
| **[Support Desk](/docs/server/support/desks) Transcripts** | Stored for closed tickets | **30 days** default (configurable per server) |
| **Analytics Digest Messages** | Read in memory, summarized without authors/links, and dropped | Never stored |

Turning off chat saving (personally or per server) immediately deletes the saved chats it covered. Guests' chats are never saved.

## Opting Out

Anyone can switch the AI off for themselves in [`/account`](/docs/reference/commands) (`privacy`) or `/me/settings`:

- The AI stops running for you immediately (including [`/ask-server`](/docs/reference/commands) and [Support Desk](/docs/server/support/desks) AI).
- Your messages and forum posts are skipped by AI reading tools and never quoted from [Server Knowledge](/docs/ai/knowledge).

## Admin Controls

Admins can disable AI, restrict features, disable image inputs, disable chat saving, restrict readable channels, and audit all changes.

## Known Limitations

- **Delete lag:** A deleted or edited message can still be quoted from a knowledge source until the next re-read (up to 1 hour for public sources, 24 hours otherwise).
- **Opt-out and past calls:** Opting out stops future reads; it cannot remove text already sent to the upstream provider.
- **Provider retention:** Retention by the upstream AI provider is governed by that provider's policy.
