# Creating & Managing Giveaways

Run giveaways in Discord and on the web with [`/giveaway`](/docs/reference/commands) or `/dashboard/<id>/giveaway`.

<!-- TODO: Put screenshot of [`/giveaway`](/docs/reference/commands) panel + `/dashboard/<id>/giveaway` creator here. -->
## Creating a Giveaway

Use [`/giveaway`](/docs/reference/commands) (`create`) or the dashboard drawer to set:

- **Prize & Winners:** Prize title, description, and number of winners.
- **Schedule:** Start time (immediate or scheduled) and end time.
- **Channel:** Target Discord channel where the giveaway card is posted.
- **Requirements & Winner Mode:** See [Entry Requirements](/docs/server/community/giveaways-requirements) and [Winner Modes & Lucky Draw](/docs/server/community/giveaways-lucky-draw).

## Managing Active Giveaways

From [`/giveaway`](/docs/reference/commands) (`list`, `logs`) or `/dashboard/<id>/giveaway`:

| Action | What it does |
|---|---|
| **Force End** | Ends the giveaway immediately and draws winners |
| **Reroll** | Picks new winner(s) after a giveaway has ended |
| **Cancel** | Cancels the giveaway without picking winners |
| **Public Page** | Every giveaway has a shareable link at `/giveaway/<guildId>/<id>` showing live status, requirements, and entry |
