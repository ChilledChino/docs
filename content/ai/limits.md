# Usage Limits

Limits keep the AI fair and prevent any one person or server from exhausting it.

## Plan allowances

Each person's plan sets:

- A **daily** allowance.
- A **running-at-once** limit (how many requests at the same time).
- A **per-minute** limit.

Each server also has its own allowance for background work (for example music suggestions), charged to the server, not to a person.

A request is charged before it runs and refunded if it fails.

## Misuse pauses

The AI refuses requests that are illegal, harmful, harassing, about private data, or that try to override its rules. Refusals add points to the person who sent them:

- **3 points** in 24 hours → a warning.
- **6 points** → access pauses for 24 hours, or until staff clears it.

Being asked *about* a hostile message never pauses the person who was only asked about it. Thresholds are owner settings.

## Guest caps

Guests (not signed in) are capped per day on every axis so they cannot exhaust the bot. Defaults:

| Cap | Default |
|---|---|
| Per session | 10 / day |
| Per visitor address | 30 / day |
| All guests together | 500 / day |
| Guests outside servers | 100 / day |

Caps live in the owner admin panel. Guest counters are tracked against a session id and a short hash of the visitor's address (never the address itself), so limits survive a new session.

## When the AI is not set up

If the bot's owner has configured no model, the AI replies that it is not set up and nothing is charged.
