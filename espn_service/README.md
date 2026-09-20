# ESPN Service (NFL-Focused Reference)

This service is a lean Django reference for pulling and storing NFL data from ESPN public endpoints.

It is intentionally scoped to NFL workflows:

- Team and schedule refresh
- Scoreboard and event snapshots
- League news
- Injuries and transactions

## What This Is For

Use this as a blueprint when building a new NFL betting/data project:

- endpoint patterns
- ingestion architecture
- model normalization strategy
- refresh cadence ideas

## Current Scope

- Sport slug: `football`
- League slug: `nfl`

## API Endpoints (Service)

- `GET /healthz`
- `GET /api/v1/teams/`
- `GET /api/v1/events/`
- `GET /api/v1/news/`
- `GET /api/v1/injuries/`
- `GET /api/v1/transactions/`

Ingestion endpoints:

- `POST /api/v1/ingest/teams/`
- `POST /api/v1/ingest/scoreboard/`
- `POST /api/v1/ingest/news/`
- `POST /api/v1/ingest/injuries/`
- `POST /api/v1/ingest/transactions/`

## ESPN Endpoints Used

Site API:

- `/apis/site/v2/sports/football/nfl/scoreboard`
- `/apis/site/v2/sports/football/nfl/teams`
- `/apis/site/v2/sports/football/nfl/news`
- `/apis/site/v2/sports/football/nfl/injuries`
- `/apis/site/v2/sports/football/nfl/transactions`

Core API helpers kept for matchup/betting expansion:

- event detail
- competition odds
- competition plays
- predictor

## Run (Docker)

```bash
cd espn_service
cp .env.example .env
docker compose up --build
```

## Run (Local)

```bash
cd espn_service
python -m venv .venv
source .venv/bin/activate
pip install -e .
python manage.py migrate
python manage.py runserver
```

## Suggested Migration Path To New Repo

1. Copy the client contract in `clients/espn_client.py`.
2. Copy ingestion services in `apps/ingest/services.py`.
3. Keep only models you need for your betting feature set.
4. Rebuild tests in the new repo around your chosen data schema.
