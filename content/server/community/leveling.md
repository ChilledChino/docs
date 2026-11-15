# Leveling & XP

Reward active members with XP, ranks, and automatic role rewards.

![Leveling and rank card](/images/feature_level_rank.webm)

## Member Commands

| Command | What it does |
|---|---|
| [`/rank`](/docs/reference/commands) `[user]` | Shows your (or another member's) XP, current level, server rank, and Canvas rank card |
| [`/leaderboard`](/docs/reference/commands) | Paginated server XP leaderboard |

## Configuration

Set up in [`/configure`](/docs/reference/commands) (`leveling`, `rewards`) or **Dashboard → Leveling** (`/dashboard/<id>/leveling` or `/xp`):

- **General:** Enable/disable leveling, set XP gain rates, choose the level-up announcement channel and custom message.
- **Multipliers:** Boost XP for specific roles or channels.
- **Ignored Lists:** Exclude specific roles or channels (e.g. bot-spam) from earning XP.
- **Role Rewards:** Automatically grant roles when a member reaches a target level (for up to date limits, see [Pricing and Limits](/docs/reference/pricing)).
- **Web Leaderboard:** Browse and search the full server leaderboard in the dashboard.
