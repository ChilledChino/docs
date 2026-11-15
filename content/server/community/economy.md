# Economy, Shop & Quests

Run a server currency (**ChinoCoins**) with a role-integrated shop and rotating daily quests.

![Economy shop and daily quests](/images/feature_economy_shop_quest.webm)

## Member Commands

| Command | What it does |
|---|---|
| [`/daily`](/docs/reference/commands) | Claim your daily ChinoCoins reward |
| [`/work`](/docs/reference/commands) | Work a shift to earn ChinoCoins (on cooldown) |
| [`/pay`](/docs/reference/commands) `<user> <amount>` | Transfer ChinoCoins to another member |
| [`/rob`](/docs/reference/commands) `<user>` | Attempt to steal ChinoCoins (risks a penalty on failure) |
| [`/profile`](/docs/reference/commands) `[user]` | View balance, quest progress, and badges |
| [`/inventory`](/docs/reference/commands) `[user]` | View owned shop items |
| [`/quests`](/docs/reference/commands) | View today's active server quests and progress |
| [`/economy`](/docs/reference/commands) | All-in-one panel (`wallet`, `inventory`, `shop`, `settings`) |

## Shop & Quests Admin

Configure in [`/economy`](/docs/reference/commands) (`settings`) or **Dashboard → Economy / Shop / Quests** (`/dashboard/<id>/economy`, `/shop`, `/quests`):

- **Rates:** Starting balance, per-message coin rate, daily reward amount, and quest reward amount.
- **Shop Items:** Create items with prices, stock/inventory caps, and optional **role bindings** (for up to date limits, see [Pricing and Limits](/docs/reference/pricing)).
- **Daily Quests:** Rotating daily pool for activities like winning quizzes, running commands, and spending coins (for up to date limits, see [Pricing and Limits](/docs/reference/pricing)).
- **Inventory Admin:** Inspect or adjust member balances and items from the dashboard.
