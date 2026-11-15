# Usage Limits & Fair Use

Limits keep AI usage fair across users, servers, and guests. View your personal usage meters in **Chat Settings → Usage** and server meters in **Dashboard → Usage & Limits** (`/dashboard/<id>/ai-usage`).

## Plan Allowances

- **Per-Person Limits:** Your plan sets your **daily window allowance**, **concurrent requests**, **requests per minute**, **max steps**, **max tool calls**, and **max answer length**. For up to date data, see [Pricing and Limits](/docs/reference/pricing).
- **Per-Server Background Allowance:** Background AI features (like AI music autoplay or scheduled report summaries) use the **server's** allowance, not yours.
- **Failed Requests:** If a request fails through no fault of yours, it is not counted against your limit.

## Misuse Pauses

Chino refuses requests that are illegal, harmful, harassing, about private data, or attempt to override its rules (including prompt-injection attempts):

| Points in 24 hours | Action |
|---|---|
| **3 points** | Warning |
| **6 points** | AI access paused for **24 hours** (or until cleared by bot staff) |

Being asked *about* a hostile message in a channel never penalizes the person who asked.

## Guest Caps

Guests (not signed in) have strict daily caps. Defaults:

| Scope | Normal Chat | Docs Assistant (`/docs`) |
|---|---|---|
| Per session | **10 / day** | **5 / day** |
| Per visitor address | **30 / day** | **10 / day** |
| All guests combined | **500 / day** | **300 / day** |
| Guests outside servers | **100 / day** | - |

Signed-in users have a separate **30 / day** allowance for the Docs Assistant that does not consume their normal AI chat quota.

## AI Activity Log (`/me/studio`)

Signed-in users can view paginated audit metadata of their own AI requests (timestamp, feature, model alias, tokens, duration, status) at `/me/studio`. Prompts and answers are never stored there.
