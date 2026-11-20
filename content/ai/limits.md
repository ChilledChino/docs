# Usage Limits & Fair Use

Limits keep AI usage fair across users, servers, and guests. View your personal usage meters in **Chat Settings → Usage** and server meters in **Dashboard → Usage & Limits** (`/dashboard/<id>/ai-usage`).

## Plan Allowances

- **Per-Person Limits:** Your plan sets your **daily window allowance**, **concurrent requests**, **requests per minute**, **max steps**, **max tool calls**, and **max answer length**. For up to date data, see [Pricing and Limits](/docs/reference/pricing).
- **Per-Server Background Allowance:** Background AI features (like AI music autoplay or scheduled report summaries) use the **server's** allowance, not yours.
- **Failed Requests:** If a request fails through no fault of yours, it is not counted against your limit.

## Misuse Pauses

Chino refuses requests that are illegal, harmful, harassing, about private data, or attempt to override its rules (including prompt-injection attempts). Refused requests add up as points: enough of them earns a **warning**, and more earns a **pause** of your AI access. The exact numbers are in [Misuse pauses](/docs/reference/pricing#misuse-pauses).

Being asked *about* a hostile message in a channel never penalizes the person who asked.

## Guest Caps

Guests (not signed in) have strict caps per session, per visitor address, and across all guests, for normal chat and for the Docs Assistant (`/docs`). See [Guests](/docs/reference/pricing#guests-not-signed-in) for the current numbers.

Signed-in users have a separate Docs Assistant allowance that does not consume their normal AI chat quota.

## AI Activity Log (`/me/studio`)

Signed-in users can view paginated audit metadata of their own AI requests (timestamp, feature, model alias, tokens, duration, status) at `/me/studio`. Prompts and answers are never stored there.
