# Winner Modes & Lucky Draw

Choose how winners are picked when creating a giveaway in [`/giveaway`](/docs/reference/commands) or `/dashboard/<id>/giveaway`.

<!-- TODO: Put screenshot/video of `/giveaway/<guildId>/<id>/games/lucky-draw` number board here. -->
## Winner Modes

| Mode | How winners are chosen |
|---|---|
| **Random** | Chino automatically draws random winner(s) when the giveaway ends |
| **Manual** | Staff manually picks the winner(s) from the list of entrants |
| **Lucky Draw** | Entrants play an interactive number-board game on the web to claim spots |

## Lucky Draw

When **Lucky Draw** is enabled:

- Members open `/giveaway/<guildId>/<id>/games/lucky-draw` to pick numbers on the interactive board.
- Once the giveaway ends (or is force-ended), winning numbers are drawn and announced in Discord and on `/giveaway/<guildId>/<id>`.
