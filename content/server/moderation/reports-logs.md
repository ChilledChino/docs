# Member Reports & Mod Logs

## Member Reports

Members can report rule-breaking messages or users directly to staff without pinging moderators in public:

- **In Discord:** Right-click a message → **Apps → Report message**, or right-click a member → **Apps → Report member**, and enter a reason. (Users cannot report themselves, bots, or webhooks.)
- **Reviewing Reports:** Staff triage open reports, add resolution notes, and mark them as resolved or dismissed in [`/mod`](/docs/reference/commands) (`reports`) or **Dashboard → Reports** (`/dashboard/<id>/reports`).

## Mod Logs & Event Logs

Configure log channels and toggle individual event types in [`/mod`](/docs/reference/commands) (`adminlogs`, `eventlogs`) or **Dashboard → Modlogs** (`/dashboard/<id>/modlogs`):

- **Moderator Actions:** Bans, unbans, kicks, purges, slowmodes, timeouts, warnings, and [AutoMod](/docs/server/moderation/automod) triggers.
- **Server Events:** Message edits/deletes, member joins/leaves, role/channel updates, and voice state changes.
- **Dashboard Audit Log:** Configuration changes made on the dashboard are recorded separately (viewable by `Manage Server` and above).

![Reports and moderation logs](/images/feature_report_modlog.webm)
