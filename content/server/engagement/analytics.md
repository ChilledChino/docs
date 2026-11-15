# Analytics & Scheduled Reports

Track server activity and post scheduled digests in [`/configure`](/docs/reference/commands) (`analytics`), [`/analytics`](/docs/reference/commands), or **Dashboard → Analytics** (`/dashboard/<id>/analytics` & `/analytics-settings`).

<!-- TODO: Put screenshot of `/dashboard/<id>/analytics` charts here. -->
## Activity Charts

- View time-series charts for members, messages, reactions, attachments, links, peak online, voice activity, boosts, and busiest day.
- Retention window depends on your server's plan (for up to date data, see [Pricing and Limits](/docs/reference/pricing)).

## Scheduled Reports & AI Summary

Configure delivery channel, frequency (daily or weekly), day/time, and IANA timezone in **Analytics → Settings** (`/dashboard/<id>/analytics-settings`), or run [`/analytics`](/docs/reference/commands) on demand.

- **AI Conversation Summary (Off by Default):** Optionally summarizes recent messages from chosen channels into one short line per channel (plus up to 2 top-reacted message links).
- **Strict Privacy:** Messages are sent without authors, links, or mentions as untrusted data and are never stored or logged (see [Privacy](/docs/privacy/overview)). Channels whose audience differs from the report channel are skipped before reading.
- **Allowance:** Charged to the server's background AI allowance, not to any member. Plan limits control how many channels and messages are read (for up to date data, see [Pricing and Limits](/docs/reference/pricing)).
