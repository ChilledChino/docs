# Privacy

What Chino's AI stores, for how long, and the controls you have.

## What reaches the AI provider

Prompts go to the AI provider the bot's operator configured. Sent: the system rules, your message and recent turns of that chat, tool results the AI asked for (such as channel messages or knowledge text), and pictures if allowed. Not sent: tokens, passwords, or other servers' data. The operator names the provider in their privacy policy, and the provider's own terms apply to what it receives.

## What is stored

| Data | Stored? | How long |
|---|---|---|
| Chats | Only with consent (see below) | 30 days without activity |
| Unsaved chat context | In memory only | ~30 minutes |
| Raw channel history, picture data, model reasoning | Never written to storage | — |
| Usage records (counts, timings) | Yes, unless a server turns it off | — |
| Guest counters (session id + address hash) | Yes | 40 days |

### Chats are saved only with consent

A chat is saved only when the person turned saving on **and**, for a server chat, the server's admins turned "save history" on (off by default). Turning a switch off deletes the chats it covered. Guests' chats are never saved.

### Logs never hold content

Prompts, answers and retrieved text are never logged. Usage records hold counts and timings only — who or which server, feature, model alias, tokens, status — never the text. A server can switch usage records off ("data use: none").

## Opting out

Anyone can switch the AI off for themselves, from the account panel in Discord or the dashboard. The AI then does not run for them, anything in progress is stopped, and their messages are left out of what the AI reads and are never quoted from a knowledge source.

## Admin controls

Admins can:

- Turn the AI off for the server.
- Restrict it to chosen features.
- Switch pictures off.
- Turn chat saving on or off.
- Choose who can use each feature.
- Choose which channels the AI may read.

All of these changes are audited.

## Known limitations

- **Delete lag.** A deleted or edited message can still be quoted from a knowledge source until the next re-read (up to an hour for sources open to everyone, 24 hours otherwise).
- **Opt-out and old messages.** Opting out stops the AI reading your messages from then on; it does not remove text the provider already received.
- **Provider retention.** What the configured provider keeps, and for how long, is decided by that provider.
