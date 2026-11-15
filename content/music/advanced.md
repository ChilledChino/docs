# Crossfade, Autoplay & Lyrics

## Crossfade & Automix

Blend transitions smoothly between queued tracks with [`/crossfade`](/docs/reference/commands) or from the [`/music` Web DJ](/docs/music/web-dj):

- **Duration:** `1` to `12` seconds.
- **Automix:** Smoothly transitions compatible tracks when crossfade is active.

## Autoplay

Keep the music going after the queue ends with [`/autoplay`](/docs/reference/commands):

| Mode | How it picks tracks |
|---|---|
| `ai` | Picks related tracks based on your recent queue (uses the server's background AI allowance) |
| `spotify` | Uses Spotify recommendations |

## Synced Lyrics

Run [`/lyrics`](/docs/reference/commands) (for the current track or a search query):

- Displays a public, live-updating card with a **3,800-character sliding window** around the active line.
- Supports word/syllable-level timing with adaptive pacing to respect Discord rate limits.

## Audio Effects

Open [`/music`](/docs/reference/commands) → **Effects** (requires being in the same voice channel):

| Category | Effects |
|---|---|
| **Tone** | Bass boost (`0–300`), Low pass (`0–900`), Subwoofer |
| **Spatial** | 8D (`off`/`light`/`moderate`/`heavy`), Karaoke, Chorus |
| **Time & Pitch** | Nightcore, Vaporwave, Speed (`0.2–2.0x`), Pitch (`0.2–3.0x`), Rate (`0.2–3.0x`) |
| **Modulation** | Vibrato, Phaser, Wah-wah |
| **Distortion** | Distort, Glitch, Bitcrusher |

![Synced lyrics and music effects](/images/feature_lyrics_music.webm)
