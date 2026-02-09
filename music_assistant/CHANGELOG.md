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


# [2.7.6] - 30.01.2026

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


