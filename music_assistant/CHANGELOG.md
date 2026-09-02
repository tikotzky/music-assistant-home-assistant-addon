# [2.10.1-24six.1] - 02.09.2026

Music Assistant 2.10.1 with the 24six provider.

- Upstream release: https://github.com/music-assistant/server/releases/tag/2.10.1
- Container image: `ghcr.io/tikotzky/server:2.10.1-24six.1`
- Python package version: `2.10.1+24six.1`

## 24six changes on top of upstream

- Add 24six provider scaffold with manifest, strings, icons and constants
- Add 24six API client with session persistence and re-auth
- Add 24six parsers for music, podcast and radio items
- Add 24six setup flow and provider implementation
- Add 24six provider tests
- Add a Stories section to the 24six provider
- Log 24six profile permissions and listing page sizes at debug level
- Restore the 24six profile permissions from a stored session
- Apply the fixes from running 24six against the live API
- Fail fast on 24six client errors instead of retrying them
- Mirror the 24six home screens and add radio now-playing
- Stop offering artist library edits for 24six
- Parse the 24six Retry-After header safely
- Cap and cache 24six category browsing
- Align the 24six provider with the project standards
- Ask 24six's AI recommendation engine for similar tracks, like the app
- Seed 24six similar-track lookups with the tracks the listener stayed with
- Add a self-contained release workflow for the 24six fork
- Target the fork when publishing a 24six release


# [2.7.6] - 09.02.2026

## ⚠️ Important Notes

As of this release, when running Music Assistant in combination with Home Assistant 2026.2+, the Home Assistant sidebar will now automatically hide. To go back to Home Assistant, click the HA icon on the bottom left of the screen.

---
## 📦 Stable Release

_Changes since [2.7.5](https://github.com/music-assistant/server/releases/tag/2.7.5)_

### 🐛 Bugfixes

- Prevent duplicate airplay player creation leaving player in invalid state (by @kdkavanagh in #2955)
- Fix issues with progress bar jumps and time overflow  (by @MarvinSchenkel in #2959)
- fix(spotify_connect): ignore trailing sink event to prevent playback thrashing (by @prydie in #2976)
- fix(alexa): Fix issue with language on alexa skills for french and germany (by @vlacour97 in #2982)
- fix: Add support for AAC streaming route for universal groups (by @rccoleman in #2990)
- fix(Tidal): Remove unnecessary deduping of recomendation rows (by @jozefKruszynski in #3006)
- Increase cache for local playlist tracks (by @MarvinSchenkel in #3007)
- Fix announcement for Sonos Play:1's (by @MarvinSchenkel in #3009)
- Fix chime validation for player groups (by @MarvinSchenkel in #3013)
- Fixes for the AirPlay provider (by @marcelveldt in #3014)
- Fix player sources in Sonos S1 (by @MarvinSchenkel in #3030)
- Fix Sonos looping announcements (by @MarvinSchenkel in #3032)
- Fix IndexError when Deezer track has no media available (by @sfortis in #3038)
- Fix Sqeezelite playing next enqueued song after announcement. (by @MarvinSchenkel in #3039)
- Fix not being able to ungroup dynamic group members (by @MarvinSchenkel in #3040)
- Radio Paradise. Switch to simple API (by @OzGav in #3046)
- Remove corrupt player configurations (by @marcelveldt in #3051)
- Fix announcement loops for Sonos S1 (by @MarvinSchenkel in #3053)

### 🧰 Maintenance and dependency bumps

- Add PTH107 mypy rule (by @OzGav in #2933)
- Add Spanish and Italian to Alexa language commands (by @alams154 in #3005)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @alams154, @jozefKruszynski, @kdkavanagh, @marcelveldt, @prydie, @rccoleman, @sfortis, @vlacour97


# [2.7.5] - 17.01.2026

## 📦 Stable Release

_Changes since [2.7.4](https://github.com/music-assistant/server/releases/tag/2.7.4)_

### 🧰 Maintenance and dependency bumps

- use instance_id instead of domain on provider level logging (by @fmunkes in #2943)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@fmunkes
