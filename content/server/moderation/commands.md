# Moderation Commands & Cases

Moderators can act via slash commands or the ephemeral [`/mod`](/docs/reference/commands) panel. Every action checks Discord role hierarchy (bot vs. target, moderator vs. target, server owner).

![Moderation panel and warnings](/images/feature_mod.webm)

## Slash Commands

| Command | What it does | Key limits |
|---|---|---|
| [`/ban`](/docs/reference/commands) | Permanent or timed ban (auto-unbans when `duration` expires) | Message delete: `0–7` days |
| [`/unban`](/docs/reference/commands) | Unban a user by ID | Logs to admin log |
| [`/kick`](/docs/reference/commands) | Kick a member | Logs to admin log |
| [`/purge`](/docs/reference/commands) | Bulk delete messages (optionally by user or time range) | Max `1000` messages; Discord 14-day age limit |
| [`/slowmode`](/docs/reference/commands) | Set channel slowmode in seconds (`0` to disable) | Text, Announcement, and Stage channels |
| [`/warn`](/docs/reference/commands) | Issue a warning with an 8-character ID | Stored in server warning history |

## The `/mod` Panel

Run [`/mod`](/docs/reference/commands) (requires `Kick Members`, `Ban Members`, `Moderate Members`, `Manage Messages`, or a delegated [module](/docs/reference/permissions)):

| Section | What it manages |
|---|---|
| **Warnings** (`warnings`) | Browse all or per-member warnings, edit reasons, delete, or clear |
| **Timeouts** (`timeouts`) | View active timeouts, apply (`1m`–`1d` presets or custom up to `28d`), or remove |
| **Member Reports** (`reports`) | Triage open member reports and resolve/dismiss with notes |
| **AutoMod** (`automod`) | Toggle [AutoMod](/docs/server/moderation/automod), pick preset, run dry-run tests, edit rules |
| **Admin Logs** (`adminlogs`) | Browse moderator actions and set the admin log channel |
| **Event Logs** (`eventlogs`) | Configure server event audit logging |
| **AFKs** (`afks`) | View or clear members' AFK statuses |
