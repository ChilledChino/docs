# Dashboard Permissions (RBAC)

Control exactly who can view or change each part of Chino in **Dashboard → Permissions** (`/dashboard/<id>/permissions`).

<!-- TODO: Put screenshot of `/dashboard/<id>/permissions` Role Grants & Why can't I? tabs here. -->
## 3-Level Access

| Level | What it allows |
|---|---|
| **None** | No access to the module's dashboard pages or Discord panel sections |
| **Read** | Can view settings, lists, and Discord panels; all edits/mutations are blocked |
| **Write** | Full configuration and action access inside that module |

- **Server Owner, `Administrator`, and `Manage Server`:** Always have full `Write` access to everything.
- **Delegable Modules:** Most [modules](/docs/reference/permissions) can be granted to specific **roles** or **individual members**.
- **Manage Server Only:** Sensitive [modules](/docs/reference/permissions) (such as Permissions, Audit log, and Plan) can never be delegated.
- **Discord Panel Parity:** Discord panels (`/configure`, `/mod`, etc.) enforce the exact same `Read` / `Write` grants.

See [Permissions Reference](/docs/reference/permissions) for the live list of modules, dashboard pages, and commands.

## Diagnostic Tools

- **My Access:** View your own effective `Write` / `Read` / `None` badge per module.
- **View As:** Preview what a specific role sees before saving changes.
- **Why Can't I?:** Select any module to get a step-by-step trace of why access was granted or denied.
