# Auto-Response, Starboard & Counters

## Auto-Response

Reply automatically when messages match a trigger string. Configure in [`/configure`](/docs/reference/commands) (`autoresponse`) or **Dashboard → Auto Response** (`/dashboard/<id>/auto-response`):

- Set trigger text, case sensitivity, plain text or embed reply, and channel/role blacklists.

## Starboard

Highlight popular messages in a dedicated channel. Configure in [`/configure`](/docs/reference/commands) (`starboard`) or **Dashboard → Starboard** (`/dashboard/<id>/engagement`):

- Tracks reaction counts in real time, updates the starboard embed as stars change, forwards attachments, and cleans up if the original message is deleted.

## Announcements

Schedule future messages to any server channel in [`/configure`](/docs/reference/commands) (`announcements`) or **Dashboard → Announcements** (`/dashboard/<id>/announcements`).

## Live Channel Counters

Display live server stats as voice channel names. Configure in [`/configure`](/docs/reference/commands) (`channelstats`) or **Dashboard → Counters** (`/dashboard/<id>/counters`):

- **14 Built-in Kinds:** Members, Humans, Bots, Boosts, Channels, Roles, Online, Idle, Do Not Disturb, Offline, Text channels, Voice channels, Members in voice, Listening to music, plus per-role counters.
- **Template:** Use `` `{count}` `` and optional `` `{kind}` `` (max 100 chars, e.g. `` `Members: {count}` ``).
- Update frequency and channel caps follow your server's plan (for up to date data, see [Pricing and Limits](/docs/reference/pricing)).

<!-- TODO: Put screenshot of `/dashboard/<id>/counters` or Starboard embed here. -->