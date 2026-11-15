# Settings Backup & Revisions

Back up, transfer, and roll back server configurations from **Dashboard → Plan & Backup** (`/dashboard/<id>/insights`).

<!-- TODO: Put screenshot of `/dashboard/<id>/insights` Share Settings export/import here. -->
## Export & Import (Share Settings)

- **Export:** Downloads your server's configuration as `chino-settings-<guildId>.json`.
- **Import:** Paste exported JSON to run a **dry-run verification** first, then apply valid sections. Each [module](/docs/reference/permissions)'s section is permission-checked against your RBAC grants.

## Revision History, Drafts & Rollback

Supported [modules](/docs/reference/permissions) maintain a revision history:

- **Drafts:** Save work-in-progress changes without affecting the live server, or discard drafts anytime.
- **Publish:** Publish a draft with an optional audit note.
- **Diff & Rollback:** Inspect diffs between any two past revisions (up to 50 recent entries) and roll back to a previous revision in one click.
