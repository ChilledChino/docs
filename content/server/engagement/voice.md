# Managed Voice Channels

Let members create their own temporary voice rooms on demand by joining a "Join to Create" generator channel.

<!-- TODO: Put screenshot of [`/voice`](/docs/reference/commands) panel + `/dashboard/<id>/voice-channels` here. -->
## Setup (Admins)

Configure in [`/configure`](/docs/reference/commands) (`voice`) or **Dashboard → Voice Channels** (`/dashboard/<id>/voice-channels`):

- Pick one or more **Join-to-Create** voice channels and their parent category.
- Set default bitrates, user limits, permissions, and plan caps (for up to date data, see [Pricing and Limits](/docs/reference/pricing)).
- Empty temporary channels are deleted automatically when the last member leaves.

## Room Owner Controls ([`/voice`](/docs/reference/commands))

Channel owners manage their room using [`/voice`](/docs/reference/commands):

| Section | Actions |
|---|---|
| **My Voice** (`myvoice`) | Rename room, set user limit, lock/unlock, hide/unhide, adjust bitrate, kick a member |
| **Blacklist** (`voice-blacklist`) | Block specific members from joining your room |
| **Sessions** (`voice-sessions`) | View and manage active voice sessions |
