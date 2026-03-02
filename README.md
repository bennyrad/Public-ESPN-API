# ESPN Public API Documentation

> **Disclaimer:** This is documentation for ESPN's undocumented public API. I am not affiliated with ESPN. Use responsibly and follow ESPN's terms of service.

---

## ☕ Support This Project

If this documentation has saved you time, consider supporting ongoing development and maintenance:

| Platform | Link |
|----------|------|
| ☕ Buy Me a Coffee | [buymeacoffee.com/pseudo_r](https://buymeacoffee.com/pseudo_r) |
| 💖 GitHub Sponsors | [github.com/sponsors/Kloverdevs](https://github.com/sponsors/Kloverdevs) |
| 💳 PayPal Donate | [PayPal (CAD)](https://www.paypal.com/donate/?business=H5VPFZ2EHVNBU&no_recurring=0&currency_code=CAD) |

Every contribution helps keep this project updated as ESPN changes their API.

---

## 📱 Real-World Apps Built With This API

These apps are live examples of what you can build using this documentation and the included Django service:

### 🏀 [Sportly: Basketball Live](https://play.google.com/store/apps/details?id=com.sportly.basketball)
> Real-time NBA, college basketball, and international leagues — scores, standings, player stats, and live game tracking.

[![Get it on Google Play](https://img.shields.io/badge/Google_Play-Sportly_Basketball-3DDC84?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.sportly.basketball)

### ⚽ [Sportly: Soccer Live](https://play.google.com/store/apps/details?id=com.sportly.soccer)
> Premier League, La Liga, Bundesliga, Serie A, MLS, and more — live scores, tables, fixtures, and news.

[![Get it on Google Play](https://img.shields.io/badge/Google_Play-Sportly_Soccer-3DDC84?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.sportly.soccer)

### 🏒 Sportly: NHL & Hockey *(coming soon)*
> Live NHL scores, standings, game stats, and hockey data across leagues.

`com.sportly.hockey` — Currently in internal testing

### 🏈 Sportly: American Football *(coming soon)*
> NFL scores, standings, play-by-play, and college football coverage.

`com.sportly.football` — Currently in internal testing

### ⚾ Sportly: Baseball *(coming soon)*
> MLB scores, box scores, standings, and baseball stats.

`com.sportly.baseball` — Currently in internal testing


## Table of Contents

- [Overview](#overview)
- [Base URLs](#base-urls)
- [Quick Start](#quick-start)
- [Sports Coverage](#sports-coverage)
- [API Endpoint Patterns](#api-endpoint-patterns)
- [Fantasy Sports API](#fantasy-sports-api)
- [Betting & Odds](#betting--odds)
- [Parameters Reference](#parameters-reference)
- [ESPN Service (Django Implementation)](#espn-service-django-implementation)

---

## Overview

ESPN provides undocumented APIs that power their website and mobile apps. These endpoints return JSON data for scores, teams, players, statistics, and more across all major sports.

**Coverage:** 17 sports · 139 leagues · 370 v2 endpoints · 79 v3 endpoints  
*(Mapped from the ESPN WADL at `sports.core.api.espn.com/v2/application.wadl` and `sports.core.api.espn.com/v3/application.wadl`)*

### Important Notes

- **Unofficial:** These APIs are not officially supported and may change without notice
- **No Authentication Required:** Most endpoints are publicly accessible
- **Rate Limiting:** Be respectful — no official limits published, but excessive requests may be blocked
- **Best Practice:** Implement caching and error handling in your applications

---

## Base URLs

| Domain | Version | Purpose |
|--------|---------|---------|
| `site.api.espn.com` | v2/v3 | Scores, news, teams, standings (site-facing) |
| `sports.core.api.espn.com` | v2 | Athletes, stats, odds, play-by-play, detailed data |
| `sports.core.api.espn.com` | v3 | Athletes, leaders (richer schema) |
| `site.web.api.espn.com` | v3 | Search, athlete profiles |
| `cdn.espn.com` | — | CDN-optimized live data |
| `fantasy.espn.com` | v3 | Fantasy sports leagues |
| `now.core.api.espn.com` | — | Real-time news feeds |

---

## Quick Start

```bash
# NFL Scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

# NBA Teams
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams"

# MLB Scores for a Specific Date
curl "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates=20241215"

# NHL Standings
curl "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/standings"
```

---

## Sports Coverage

Each sport has its own detailed endpoint reference document:

| Sport | Slug | # Leagues | Documentation |
|-------|------|-----------|---------------|
| 🏉 Australian Football | `australian-football` | 1 | [docs/sports/australian_football.md](docs/sports/australian_football.md) |
| ⚾ Baseball | `baseball` | 13 | [docs/sports/baseball.md](docs/sports/baseball.md) |
| 🏀 Basketball | `basketball` | 15 | [docs/sports/basketball.md](docs/sports/basketball.md) |
| 🏏 Cricket | `cricket` | varies | [docs/sports/cricket.md](docs/sports/cricket.md) |
| 🏑 Field Hockey | `field-hockey` | 1 | [docs/sports/field_hockey.md](docs/sports/field_hockey.md) |
| 🏈 Football | `football` | 5 | [docs/sports/football.md](docs/sports/football.md) |
| ⛳ Golf | `golf` | 9 | [docs/sports/golf.md](docs/sports/golf.md) |
| 🏒 Hockey | `hockey` | 6 | [docs/sports/hockey.md](docs/sports/hockey.md) |
| 🥍 Lacrosse | `lacrosse` | 4 | [docs/sports/lacrosse.md](docs/sports/lacrosse.md) |
| 🥊 MMA | `mma` | 25+ | [docs/sports/mma.md](docs/sports/mma.md) |
| 🏎️ Racing | `racing` | 5 | [docs/sports/racing.md](docs/sports/racing.md) |
| 🏉 Rugby | `rugby` | 24 | [docs/sports/rugby.md](docs/sports/rugby.md) |
| 🏉 Rugby League | `rugby-league` | 1 | [docs/sports/rugby_league.md](docs/sports/rugby_league.md) |
| ⚽ Soccer | `soccer` | 24 | [docs/sports/soccer.md](docs/sports/soccer.md) |
| 🎾 Tennis | `tennis` | 2 | [docs/sports/tennis.md](docs/sports/tennis.md) |
| 🏐 Volleyball | `volleyball` | 2 | [docs/sports/volleyball.md](docs/sports/volleyball.md) |
| 🤽 Water Polo | `water-polo` | 2 | [docs/sports/water_polo.md](docs/sports/water_polo.md) |

> For global and cross-sport endpoints, see [docs/sports/_global.md](docs/sports/_global.md).

---

## API Endpoint Patterns

### Site API (Scores, Teams, Standings)

```
GET https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/{resource}
```

| Resource | Description |
|----------|-------------|
| `scoreboard` | Live & scheduled events with scores |
| `teams` | All teams in the league |
| `teams/{id}` | Single team detail |
| `teams/{id}/roster` | Team roster |
| `teams/{id}/schedule` | Team schedule |
| `standings` | League standings |
| `news` | Latest news articles |
| `rankings` | Rankings (college sports) |
| `summary?event={id}` | Full game summary |

### Core API v2 (Athletes, Stats, Events, Odds)

```
GET https://sports.core.api.espn.com/v2/sports/{sport}/leagues/{league}/{resource}
```

| Resource | Description |
|----------|-------------|
| `athletes` | Full athlete list with pagination |
| `athletes/{id}` | Single athlete |
| `athletes/{id}/statistics` | Career stats |
| `athletes/{id}/statisticslog` | Game-by-game log |
| `athletes/{id}/eventlog` | Event history |
| `athletes/{id}/contracts` | Contract info |
| `athletes/{id}/awards` | Awards |
| `athletes/{id}/seasons` | Seasons played |
| `athletes/{id}/records` | Career records |
| `athletes/{id}/hotzones` | Hot zones (baseball) |
| `athletes/{id}/vsathlete/{opponentId}` | Head-to-head stats |
| `events` | Events with full detail |
| `events/{id}/competitions/{id}/odds` | Betting odds |
| `events/{id}/competitions/{id}/probabilities` | Win probabilities |
| `events/{id}/competitions/{id}/plays` | Play-by-play |
| `seasons` | Season list |
| `seasons/{year}/teams` | Teams in a season |
| `seasons/{year}/draft` | Draft data |
| `seasons/{year}/futures` | Futures odds |
| `standings` | League standings |
| `teams` | Teams (detailed) |
| `venues` | Venues/stadiums |
| `leaders` | Statistical leaders |
| `rankings` | Rankings |
| `franchises` | Franchise history |

### Core API v3 (Richer Schema)

```
GET https://sports.core.api.espn.com/v3/sports/{sport}/{league}/{resource}
```

| Resource | Description |
|----------|-------------|
| `athletes` | Athletes (enriched schema) |
| `leaders` | Statistical leaders |

---

## Common League Slugs

### 🏈 Football (sport: `football`)

| League | Slug |
|--------|------|
| NFL | `nfl` |
| College Football | `college-football` |
| CFL | `cfl` |
| UFL | `ufl` |
| XFL | `xfl` |

### 🏀 Basketball (sport: `basketball`)

| League | Slug |
|--------|------|
| NBA | `nba` |
| WNBA | `wnba` |
| NBA G League | `nba-development` |
| NCAA Men's | `mens-college-basketball` |
| NCAA Women's | `womens-college-basketball` |
| NBL | `nbl` |
| FIBA World Cup | `fiba` |

### ⚾ Baseball (sport: `baseball`)

| League | Slug |
|--------|------|
| MLB | `mlb` |
| NCAA Baseball | `college-baseball` |
| World Baseball Classic | `world-baseball-classic` |
| Dominican Winter League | `dominican-winter-league` |

### 🏒 Hockey (sport: `hockey`)

| League | Slug |
|--------|------|
| NHL | `nhl` |
| NCAA Men's | `mens-college-hockey` |
| NCAA Women's | `womens-college-hockey` |

### ⚽ Soccer (sport: `soccer`)

| League | Slug |
|--------|------|
| FIFA World Cup | `fifa.world` |
| UEFA Champions League | `uefa.champions` |
| English Premier League | `eng.1` |
| Spanish LALIGA | `esp.1` |
| German Bundesliga | `ger.1` |
| Italian Serie A | `ita.1` |
| French Ligue 1 | `fra.1` |
| MLS | `usa.1` |
| Liga MX | `mex.1` |
| NWSL | `usa.nwsl` |
| UEFA Europa League | `uefa.europa` |
| FIFA Women's World Cup | `fifa.wwc` |

### ⛳ Golf (sport: `golf`)

| Tour | Slug |
|------|------|
| PGA TOUR | `pga` |
| LPGA | `lpga` |
| DP World Tour | `eur` |
| LIV Golf | `liv` |
| PGA TOUR Champions | `champions-tour` |
| Korn Ferry Tour | `ntw` |

### 🏎️ Racing (sport: `racing`)

| Series | Slug |
|--------|------|
| Formula 1 | `f1` |
| IndyCar | `irl` |
| NASCAR Cup | `nascar-premier` |
| NASCAR Xfinity | `nascar-secondary` |
| NASCAR Truck | `nascar-truck` |

### 🎾 Tennis (sport: `tennis`)

| Tour | Slug |
|------|------|
| ATP | `atp` |
| WTA | `wta` |

---

## Fantasy Sports API

Base URL: `https://fantasy.espn.com/apis/v3/games/{sport}/seasons/{year}`

### Game Codes

| Sport | Code |
|-------|------|
| Football | `ffl` |
| Basketball | `fba` |
| Baseball | `flb` |
| Hockey | `fhl` |

### League Endpoints

```bash
# Get league data (public leagues)
GET /apis/v3/games/ffl/seasons/2024/segments/0/leagues/{league_id}

# With views
?view=mTeam
?view=mRoster
?view=mMatchup
?view=mSettings
?view=mDraftDetail
```

### Authentication (Private Leagues)

Private leagues require cookies: `espn_s2` and `SWID`

---

## Betting & Odds

Base: `sports.core.api.espn.com/v2/sports/{sport}/leagues/{league}`

| Endpoint | Description |
|----------|-------------|
| `/events/{id}/competitions/{id}/odds` | Game odds |
| `/events/{id}/competitions/{id}/probabilities` | Win probabilities |
| `/seasons/{year}/futures` | Season futures |
| `/seasons/{year}/types/{type}/teams/{id}/ats` | ATS records |

**Betting Provider IDs:**

| Provider | ID |
|----------|----|
| Caesars | 38 |
| Bet365 | 2000 |
| DraftKings | 41 |

---

## Parameters Reference

### Common Query Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `dates` | Filter by date | `20241215` or `20241201-20241231` |
| `week` | Week number | `1` through `18` |
| `seasontype` | Season type | `1`=preseason, `2`=regular, `3`=postseason |
| `season` | Year | `2024` |
| `limit` | Results limit | `100`, `1000` |
| `page` | Page number | `1` |
| `groups` | Conference ID | `8` (SEC) |
| `enable` | Include extra data | `roster,stats,projection` |
| `active` | Active filter | `true` / `false` |

### Season Types

| Type | Value |
|------|-------|
| Preseason | 1 |
| Regular Season | 2 |
| Postseason | 3 |
| Off Season | 4 |

### College Football Conference IDs (`groups` param)

| Conference | ID |
|------------|----|
| SEC | 8 |
| Big Ten | 5 |
| ACC | 1 |
| Big 12 | 4 |
| Mountain West | 17 |
| Top 25 | 80 |

---

## ESPN Service (Django Implementation)

This repository includes a production-ready Django REST API that wraps ESPN's endpoints.

### Features

- Full support for **17 sports** and **139 leagues**
- Data ingestion and persistence (teams, events, competitors, athletes, venues)
- Clean REST API with filtering and pagination
- Background jobs (Celery)
- Docker support
- OpenAPI documentation via drf-spectacular

### Quick Start

```bash
cd espn_service
docker compose up --build

# API: http://localhost:8000
# Docs: http://localhost:8000/api/docs/
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Health check |
| `/api/v1/ingest/teams/` | POST | Ingest ESPN teams |
| `/api/v1/ingest/scoreboard/` | POST | Ingest ESPN events |
| `/api/v1/teams/` | GET | List teams |
| `/api/v1/teams/{id}/` | GET | Team details |
| `/api/v1/teams/espn/{espn_id}/` | GET | Team by ESPN ID |
| `/api/v1/events/` | GET | List events |
| `/api/v1/events/{id}/` | GET | Event details |
| `/api/v1/events/espn/{espn_id}/` | GET | Event by ESPN ID |

### ESPN Client Methods

The `ESPNClient` in `clients/espn_client.py` provides methods covering all major endpoints:

| Category | Methods |
|----------|---------|
| Scoreboard | `get_scoreboard()` |
| Teams | `get_teams()`, `get_team()`, `get_team_roster()`, `get_core_teams()` |
| Events | `get_event()`, `get_core_events()` |
| Standings | `get_standings()`, `get_core_standings()` |
| News | `get_news()` |
| Rankings | `get_rankings()` |
| Athletes | `get_athletes()`, `get_athlete()`, `get_athlete_statistics()`, `get_athletes_v3()` |
| Seasons | `get_seasons()` |
| Betting | `get_odds()`, `get_win_probabilities()` |
| Play Data | `get_plays()` |
| Statistics | `get_leaders()`, `get_leaders_v3()` |
| Venues | `get_venues()` |
| Metadata | `get_league_info()` |

### Example Usage

```bash
# Ingest NBA teams
curl -X POST http://localhost:8000/api/v1/ingest/teams/ \
  -H "Content-Type: application/json" \
  -d '{"sport": "basketball", "league": "nba"}'

# Ingest EPL matches
curl -X POST http://localhost:8000/api/v1/ingest/scoreboard/ \
  -H "Content-Type: application/json" \
  -d '{"sport": "soccer", "league": "eng.1"}'

# Query teams
curl "http://localhost:8000/api/v1/teams/?league=nba&search=Lakers"

# Query events
curl "http://localhost:8000/api/v1/events/?league=nfl&date=2024-12-15"
```

See [espn_service/README.md](espn_service/README.md) for full service documentation.

---

## Contributing

Found a new endpoint? Please open an issue or PR!

## License

MIT License — See LICENSE file

---

*Last Updated: March 2026 · 17 sports · 139 leagues · 370 v2 + 79 v3 endpoints*
