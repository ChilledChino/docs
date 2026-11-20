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

Lucky Draw happens **after** the giveaway ends, in three steps.

1. **Entrants pick a number.** A **Lucky Draw** button appears on the giveaway card, linking to `/giveaway/<guildId>/<id>/games/lucky-draw`. You must have entered the giveaway. Pick **one** number from **1 to (entries + 10)**. Numbers are first come, first served, and you cannot change yours. This step runs for **6 hours**.
2. **The host picks the winning numbers.** When the 6 hours are up, Chino posts that entries are closed. On the same page, the **giveaway host or an Administrator** chooses as many different numbers as there are winners. Only numbers someone picked can be chosen. The people who picked them win, and Chino announces them in Discord.
3. **Done.** Winners are shown on `/giveaway/<guildId>/<id>`.

### For Hosts

- **End picking early:** close step 1 before the 6 hours are up.
- **Extend:** add between **5 minutes** and **6 hours**.
- **If you do nothing:** 12 hours after step 1 closes, Chino picks the winners at random.
- **Reroll:** the host or an admin can reroll at any time ([`/giveaway`](/docs/reference/commands)).

### When There Are Not Enough Players

- **Fewer entries than winners** when the giveaway ends: it ends without winners. Reroll once enough people have entered.
- **Fewer picked numbers than winners** when step 1 closes: it ends without winners. Extend step 1 to give people more time.
