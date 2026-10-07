# [2.10.5-24six.1] - 07.10.2026

Music Assistant 2.10.5 with the 24six provider.

- Upstream release: https://github.com/music-assistant/server/releases/tag/2.10.5
- Container image: `ghcr.io/tikotzky/server:2.10.5-24six.1`
- Python package version: `2.10.5+24six.1`

## 24six changes on top of upstream

- Fix release notes listing changes that did not ship in a stable patch release (#6672)
- Only allow releases to be started from the dev branch (stable) (#6674)
- Pick provider mappings by availability and priority in _select_provider_id (stable) (#6679)
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
- Add a script that moves the 24six fork to the latest upstream stable
- Sync dependencies before checking a rebased 24six branch


# [2.10.4-24six.1] - 24.09.2026

Music Assistant 2.10.4 with the 24six provider.

- Upstream release: https://github.com/music-assistant/server/releases/tag/2.10.4
- Container image: `ghcr.io/tikotzky/server:2.10.4-24six.1`
- Python package version: `2.10.4+24six.1`

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


# [2.10.3-24six.1] - 14.09.2026

Music Assistant 2.10.3 with the 24six provider.

- Upstream release: https://github.com/music-assistant/server/releases/tag/2.10.3
- Container image: `ghcr.io/tikotzky/server:2.10.3-24six.1`
- Python package version: `2.10.3+24six.1`

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
