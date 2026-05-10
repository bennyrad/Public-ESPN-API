# ESPN API Documentation

> Comprehensive reference for the unofficial ESPN API — endpoints, parameters, league slugs, response schemas, and a working Django service.

---

## 📁 File Index

### Root
| File | Description |
|------|-------------|
| [README.md](../README.md) | Full documentation — base URLs, endpoint patterns, fantasy, betting, specialized endpoints |
| [CHANGELOG.md](../CHANGELOG.md) | History of all documented changes |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | How to contribute endpoints, fixes, and code |

### Sports Reference (`docs/sports/`)

Each file covers leagues & competitions, API endpoints, Site API resources, and curl examples for that sport.

| File | Sport | Key Leagues |
|------|-------|-------------|
| [_global.md](sports/_global.md) | All Sports | Every v2 endpoint — full WADL listing |
| [football.md](sports/football.md) | 🏈 Football | NFL, NCAAF, CFL, UFL, XFL |
| [basketball.md](sports/basketball.md) | 🏀 Basketball | NBA, WNBA, NCAAM, NCAAW, NBL, FIBA |
| [soccer.md](sports/soccer.md) | ⚽ Soccer | EPL, La Liga, Bundesliga, MLS, UCL, 260+ leagues |
| [baseball.md](sports/baseball.md) | ⚾ Baseball | MLB, NCAAB, WBC, Caribbean/Winter Leagues |
| [hockey.md](sports/hockey.md) | 🏒 Hockey | NHL, NCAAH, Olympics |
| [golf.md](sports/golf.md) | ⛳ Golf | PGA TOUR, LPGA, LIV, DP World Tour, TGL |
| [tennis.md](sports/tennis.md) | 🎾 Tennis | ATP, WTA |

### API Reference
| File | Description |
|------|-------------|
| [response_schemas.md](response_schemas.md) | Example JSON responses for scoreboard, teams, roster, injuries, game summary, athlete, odds, standings, Now API |

### Domain Routing Guide

> All domains below were **live-verified via browser HTTP tests on 2026-03-26** — all returned HTTP 200 OK.

| Domain | Use for | Verified Response Keys |
|--------|---------|----------------------|
| `site.api.espn.com/apis/site/v2/` | Scoreboard, teams, news, injuries, transactions, statistics, groups, draft, summary, rankings | `leagues`, `season`, `week`, `events` (scoreboard); `header`, `articles` (news); `uid`, `children` (standings) |
| `site.api.espn.com/apis/v2/` | **Standings only** — site/v2 returns a stub | `uid`, `id`, `name`, `abbreviation`, `children` |
| `site.web.api.espn.com/apis/common/v3/` | Athlete stats, gamelog, overview, splits (`statistics/byathlete`) | `leagues`, `season`, `day`, `events` (same as site.api) |
| `cdn.espn.com/core/` | Full game packages — drives, plays, odds (requires `?xhr=1`) | Varies by sport |
| `now.core.api.espn.com/v1/` | Real-time news feed — filter by `sport=`, `league=`, `team=` | `resultsCount`, `resultsLimit`, `resultsOffset`, `headlines[]` |
| `sports.core.api.espn.com/v2/` | Core data — events, odds, play-by-play, athletes, coaches | Leagues: `$ref`, `id`, `name`, `season`, `teams`, `athletes`; Collections: `count`, `pageIndex`, `pageSize`, `items[]` |

**Sport-specific exceptions:**
- ⛳ **Golf / 🎾 Tennis scoreboard** → slug required: `pga`, `lpga`, `atp`, `wta` (not numeric IDs)

---

## 🚀 Quick Links

| Data | Endpoint |
|------|----------|
| Scoreboard | `https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/scoreboard` |
| Teams | `https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/teams` |
| Standings | `https://site.api.espn.com/apis/v2/sports/{sport}/{league}/standings` |
| Game summary | `https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/summary?event={id}` |
| Full game package | `https://cdn.espn.com/core/{sport}/game?xhr=1&gameId={id}` |
| Athlete overview | `https://site.web.api.espn.com/apis/common/v3/sports/{sport}/{league}/athletes/{id}/overview` |
| Athlete stats | `https://site.web.api.espn.com/apis/common/v3/sports/{sport}/{league}/athletes/{id}/stats` |
| Stats leaderboard | `https://site.web.api.espn.com/apis/common/v3/sports/{sport}/{league}/statistics/byathlete` |
| Real-time news | `https://now.core.api.espn.com/v1/sports/news?sport=football` |
| Core API | `https://sports.core.api.espn.com/v2/sports/{sport}/leagues/{league}/...` |

