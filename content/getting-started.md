# Getting Started

## 1. Choose How to Add Chino

| Install type | Where it works | How to add |
|---|---|---|
| **Server Install** | Inside a Discord server | Invite Chino from the dashboard and grant the requested permissions. Missing permissions disable only the features that need them. |
| **User Install (Personal)** | Any server, DMs, and group DMs | Authorize Chino on your Discord account to use [`/account`](/docs/reference/commands), [`/remind`](/docs/reference/commands), [`/ask`](/docs/reference/commands), [`/together`](/docs/reference/commands), and right-click message actions anywhere. |

<!-- TODO: Put screenshot of Discord invite / User Install prompt here. -->
## 2. Configure a Server

Everything can be managed from **Discord panels** or the **web dashboard** (`/dashboard`):

- **In Discord:** Run [`/configure`](/docs/reference/commands), [`/mod`](/docs/reference/commands), [`/music`](/docs/reference/commands), [`/automate`](/docs/reference/commands), [`/economy`](/docs/reference/commands), or [`/giveaway`](/docs/reference/commands).
- **On the Web:** Open `/dashboard`, pick your server, and edit any [module](/docs/reference/permissions).
- **Who can manage what:** Server owners, `Administrator`, and `Manage Server` have full access. Other roles or members can be granted **Read** or **Write** access per [module](/docs/reference/permissions) in **Permissions** (see [Dashboard Permissions](/docs/admin/permissions)).

## 3. Turn On AI (Optional)

Server AI starts **off** until an admin configures it:

1. Open **Dashboard → AI Settings** (`/dashboard/<id>/ai`) and enable AI.
2. Pick which features are on ([Chat](/docs/ai/overview), [Server Knowledge](/docs/ai/knowledge), [Catch Up](/docs/ai/overview), [Automation](/docs/server/engagement/automation), [Server Setup](/docs/ai/overview), [Support](/docs/server/support/desks)).
3. In **Channels & Memory**, choose which channels Chino may read.
4. In **Permissions & Links**, set who can use each feature ([Access Levels & Guest Chat](/docs/ai/access-guests)).

## 4. Need Help?

- Use the **Ask Chino** assistant on `/docs` to search documentation or jump to dashboard pages.
- Submit a bug report or feature request with [`/report`](/docs/reference/commands) in Discord or on `/feedback` (see [Bug Reports, Feedback & Tickets](/docs/support/tickets)).
