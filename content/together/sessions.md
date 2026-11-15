# Voting, Sessions & Voice Handoff

## Ranked-Choice Voting

Inside any plan ([`/together`](/docs/reference/commands) `schedule` or `/together/<id>`):

- Propose options (games, movies, times) and rank them in order of preference.
- Chino calculates the winner using **ranked-choice voting** (requires `>50%` majority across elimination rounds) and displays the round-by-round breakdown.

## Sessions, RSVPs & Voice Handoff

- **Sessions:** Plan owners can create, start, complete, or cancel sessions. Members RSVP with `going`, `maybe`, or `no`.
- **Voice Handoff:** Launch a voice room directly in a shared Discord server (with an optional music playlist/query) from the plan.
- **Share Cards:** Generate an SVG share card for any plan from `/together`.

<!-- TODO: Put screenshot of ranked-choice voting results + voice handoff modal here. -->