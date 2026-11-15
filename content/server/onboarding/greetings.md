# Welcome & Farewell Greetings

Greet new members and log departures in [`/configure`](/docs/reference/commands) (`welcome`, `farewell`) or **Dashboard → Onboarding & XP → Greetings** (`/dashboard/<id>/onboarding`).

![Welcome and farewell message with Canvas card](/images/feature_greet_farewell.png)

## Options

- **Channel & Message:** Pick target channels for Welcome and Farewell independently.
- **Image Mode:** Send plain text, a custom HTTPS image URL, or a generated **[Canvas Card](/docs/server/onboarding/canvas)**.
- **Live Preview:** Preview the rendered greeting in [`/configure`](/docs/reference/commands) before saving.

## Supported Placeholders

| Placeholder | Inserts |
|---|---|
| `` `{username}` ``, `` `{user}` ``, `` `{mention}` `` | Member name / display / `@mention` |
| `` `{userId}` ``, `` `{discriminator}` `` | Discord user ID / discriminator |
| `` `{server}` `` | Server name |
| `` `{memberCount}` ``, `` `{memberCountOrdinal}` `` | Member count (`142` / `142nd`) |
| `` `{joinDate}` ``, `` `{creationDate}` `` | Join date / account creation date |
| `` `{highestRole}` `` | Member's highest role |
