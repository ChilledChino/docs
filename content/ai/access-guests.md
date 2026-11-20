# Access Levels & Guest Chat

Admins control who can use each AI feature in **Dashboard → Permissions & Links** (`/dashboard/<id>/ai-access`).

<!-- TODO: Put screenshot of `/dashboard/<id>/ai-access` + public guest chat link here. -->
## Per-Feature Access Levels

| Feature | Default (new servers) | Allowed levels |
|---|---|---|
| **Chat** | Members | *Admins only* (+ allow-list), *Members* |
| **Catch Up** | Members | *Admins only* (+ allow-list), *Members* |
| **Server Knowledge** | Members | *Admins only* (+ allow-list), *Members*, *Public* ([details](/docs/ai/knowledge)) |
| **Automation** | Admins only | *Admins only* (locked) |
| **Server Setup** | Admins only | *Admins only* (locked) |

- **Admins** means the server owner, `Administrator`, `Manage Server`, or anyone granted the **AI** [dashboard module](/docs/reference/permissions).
- **Allow-list:** When set to *Admins only*, you can still allow specific roles or members.
- **Public:** Only **[Server Knowledge](/docs/ai/knowledge)** can be opened to the public. Doing so requires `Manage Server` and is audited.

## Public Share Links & Guests

- **Share Link (`/chat/<slug>`):** Opening [Server Knowledge](/docs/ai/knowledge) to *Public* generates a random, unguessable slug that does not expose your server ID. Admins can rotate or revoke it at any time.
- **Plain Guest Chat (`/chat`):** Guests not in a server can chat without server tools or server data.
- **Verification:** Guests pass a **Cloudflare Turnstile** check and receive a 24-hour signed session scoped to one server (or none).
- **Guest Restrictions:**
  - Shorter messages than signed-in members ([Messages and pictures](/docs/reference/pricing#messages-and-pictures)).
  - No images, no personal tools, no server channel tools, and no chat history saving.
