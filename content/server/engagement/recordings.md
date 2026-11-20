# Voice Recordings

Record a voice meeting and play it back per speaker for 7 days. Available in pilot servers only for now.

## Starting and Stopping

- **Who:** `Manage Server`, or anyone granted the **Voice** [dashboard module](/docs/reference/permissions).
- **Where:** [`/record`](/docs/reference/commands) in Discord, or **Dashboard → Recordings** (`/dashboard/<id>/recordings`).
- **Who is recorded:** *Everyone* in the channel (people who join later too), or only the people you pick.
- **Stops** when the host or a manager stops it, or at the time limit.
- **Won't start** if music is playing, too many people are in the channel, or Chino cannot post its notice. Music cannot start while a meeting is recorded.

## Consent

- Chino posts a notice with an **Opt out** button in the voice channel's chat for the whole meeting.
- **Opt out** stops recording you and deletes what was recorded of you in that meeting.
- **Include my voice** off (`/record` → Settings, or the Recordings page) means you are never recorded in that server.

## Listening

- **Who can listen:** the host, server managers and the people in the meeting (unless they opted out).
- **Playback:** every speaker side by side for the whole meeting, with Solo and Mute.
- **Who talks when:** each speaker's timeline marks when they talk, with their total talk time. **Next** and **Previous talk** jump between talks, and **Skip silence** jumps over quiet parts. Shortcuts: Space, arrow keys, N and P.
- **Download** one speaker's file, or tick two or more speakers and **Merge** them into one file. You keep one merged file per meeting; merging again replaces it.
- **Live view:** who is speaking, shown to the host, managers and the people being recorded.
- **Ready message:** turn on *Message me when a recording is ready* to get a DM with a link once it is saved.

## Storage

- Recordings, merged files and everything about them are deleted **7 days** after the meeting.
- Meetings are **not transcribed**, and no meeting audio is sent to an AI. See [Privacy](/docs/privacy/overview).
