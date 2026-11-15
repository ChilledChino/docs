# Autoroles & Role Menus

Manage join roles and self-assignable role menus in [`/configure`](/docs/reference/commands) (`roles`, `joinroles`) or **Dashboard → Onboarding & XP → Roles & Menus** (`/dashboard/<id>/roles`).

![Role menus and auto-roles](/images/feature_roles_and_menu.webm)

## Autoroles (Roles on Join)

- Automatically assign one or more roles as soon as a member joins.
- Plan limits apply (for up to date data, see [Pricing and Limits](/docs/reference/pricing)).

## Self-Role Menus

- **Reaction & Button Menus:** Build role menus and publish them to any text channel, or edit/repair existing menu messages.
- **Allow / Block Lists:** Restrict which roles can use a menu ([plan limits](/docs/reference/pricing) apply).
- **Hierarchy Safety Checks:** Chino validates role assignability upfront and flags roles that are `@everyone`, bot-managed, above Chino's highest role, or blocked by missing `Manage Roles`.
