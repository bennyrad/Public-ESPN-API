# Public ESPN API: NFL-Focused Reference

This repository is now maintained as a lean reference for building NFL data products on top of ESPN public endpoints.

Scope today:

- NFL endpoint docs and examples
- Global endpoint references that are still useful in NFL workflows
- A trimmed Django reference service under [espn_service/README.md](espn_service/README.md)

## Disclaimer

These APIs are undocumented and unofficial.

- They can change without notice.
- Availability can vary by endpoint and season.
- Use responsibly and follow applicable terms.

## Repository Layout

- NFL and global docs: [docs/sports/football.md](docs/sports/football.md), [docs/sports/_global.md](docs/sports/_global.md)
- Response patterns and payload examples: [docs/response_schemas.md](docs/response_schemas.md)
- NFL-oriented service blueprint: [espn_service/README.md](espn_service/README.md)

## Quick Start Endpoints

```bash
# NFL scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

# NFL teams
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"

# NFL standings (use /apis/v2/)
curl "https://site.api.espn.com/apis/v2/sports/football/nfl/standings"

# NFL injuries
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/injuries"

# NFL transactions
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/transactions"
```

## Endpoint Families You Will Use Most

### Site API v2

Best for scoreboard, teams, standings, injuries, transactions, and summary views.

Pattern:

```text
https://site.api.espn.com/apis/site/v2/sports/football/nfl/{resource}
```

### Core API v2

Best for matchup depth (odds, plays, predictor, competition-level details).

Pattern:

```text
https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/{resource}
```

### CDN Core

Best for richer live game packages when available.

Pattern:

```text
https://cdn.espn.com/core/nfl/{resource}?xhr=1
```

## Suggested NFL Data Pipeline

1. Ingest and refresh teams weekly.
2. Ingest scoreboard frequently (hourly or better during active windows).
3. Capture injuries and transactions on separate cadences.
4. Enrich selected games with core odds and play data.
5. Cache aggressively and store raw payloads for replay/debug.

## Service Reference

The Django service is intentionally a blueprint, not a final product.

- Read [espn_service/README.md](espn_service/README.md) for current API routes and ingestion triggers.
- Reuse the client and ingestion patterns in your new dedicated NFL repository.

## What Changed

This repository was reduced from multi-sport focus to NFL-first reference usage.

- NHL service removed
- ESPN service trimmed to NFL-relevant patterns
- Root docs flow simplified around football and global references

## License

MIT. See [LICENSE](LICENSE).
