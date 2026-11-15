# Server Automation (Workflows)

Build **Trigger → Conditions → Actions** rules in [`/automate`](/docs/reference/commands) or **Dashboard → Workflows** (`/dashboard/<id>/automation`).

<!-- TODO: Put screenshot of `/dashboard/<id>/automation` visual workflow builder here. -->
## Triggers, Conditions & Actions

| Part | Supported options |
|---|---|
| **Triggers** | Member joins, Message sent, Reaction added, Role changed, Schedule (`5` to `10,080` minutes) |
| **Condition Fields** | Message content, User, Channel, Role, Emoji, Is bot, Role direction |
| **Operators** | Equals, Contains, Starts with, Regex, In list |
| **Actions** | Send message, Add role, Create reminder |

## Drafting with AI & Testing

- **AI Rule Draft:** Describe what you want in [`/automate`](/docs/reference/commands) (`draft`) or `/dashboard/<id>/chat` (`Automation` mode). Chino outputs a validated rule card with **Create (turned off)**, **Create and turn on**, or **Discard**.
- **Simulator & Diffs:** Test rules against sample events and compare rule revisions in `/dashboard/<id>/automation`.

## Limits & Rate Caps

| Limit | Cap |
|---|---|
| Max rules per server | **25** |
| Max conditions / actions per rule | **8** conditions / **5** actions |
| Max text length / rule name | **1,900** chars / **80** chars |
| Max delay | **30 days** (43,200 minutes) |
| Default rate limits | **300/hr** (`member_join`, `role_change`), **60/hr** (`message`, `reaction`, `schedule`), ceiling **600/hr** |
