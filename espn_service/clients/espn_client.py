"""Lean ESPN API client focused on NFL data workflows.

This client keeps only the endpoint helpers needed by the current ingestion
services plus common NFL betting dashboard needs (odds, plays, predictor,
athlete stats).
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any

import httpx
import structlog
from django.conf import settings
from tenacity import RetryError, retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from apps.core.exceptions import ESPNClientError, ESPNNotFoundError, ESPNRateLimitError

logger = structlog.get_logger(__name__)


class ESPNEndpointDomain(str, Enum):
    """Supported ESPN domains."""

    SITE = "site"        # site.api.espn.com
    CORE = "core"        # sports.core.api.espn.com
    SITE_V2 = "site_v2"  # site.api.espn.com/apis/v2
    CDN = "cdn"          # cdn.espn.com/core


SPORT_NAMES: dict[str, str] = {
    "football": "Football",
}

LEAGUE_INFO: dict[str, tuple[str, str]] = {
    "nfl": ("National Football League", "NFL"),
}


@dataclass
class ESPNResponse:
    """Normalized response wrapper."""

    data: dict[str, Any]
    status_code: int
    url: str

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300


class ESPNClient:
    """HTTP client for ESPN data endpoints."""

    def __init__(
        self,
        site_api_url: str | None = None,
        core_api_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        user_agent: str | None = None,
    ) -> None:
        config = getattr(settings, "ESPN_CLIENT", {})

        self.site_api_url = (site_api_url or config.get("SITE_API_BASE_URL", "https://site.api.espn.com")).rstrip("/")
        self.core_api_url = (core_api_url or config.get("CORE_API_BASE_URL", "https://sports.core.api.espn.com")).rstrip("/")
        self.cdn_url = config.get("CDN_API_BASE_URL", "https://cdn.espn.com").rstrip("/")

        self.timeout = timeout or config.get("TIMEOUT", 30.0)
        self.max_retries = max_retries or config.get("MAX_RETRIES", 3)
        self.retry_backoff = config.get("RETRY_BACKOFF", 1.0)
        self.user_agent = user_agent or config.get("USER_AGENT", "ESPN-Service/1.0")

        self._client: httpx.Client | None = None

    @property
    def client(self) -> httpx.Client:
        if self._client is None or self._client.is_closed:
            self._client = httpx.Client(
                timeout=httpx.Timeout(self.timeout),
                headers={"User-Agent": self.user_agent, "Accept": "application/json"},
                follow_redirects=True,
            )
        return self._client

    def close(self) -> None:
        if self._client is not None and not self._client.is_closed:
            self._client.close()
            self._client = None

    def __enter__(self) -> "ESPNClient":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()

    def _get_base_url(self, domain: ESPNEndpointDomain) -> str:
        if domain == ESPNEndpointDomain.SITE:
            return self.site_api_url
        if domain == ESPNEndpointDomain.SITE_V2:
            return self.site_api_url
        if domain == ESPNEndpointDomain.CDN:
            return self.cdn_url
        return self.core_api_url

    def _build_url(self, domain: ESPNEndpointDomain, path: str) -> str:
        return f"{self._get_base_url(domain)}/{path.lstrip('/')}"

    def _handle_response(self, response: httpx.Response, url: str) -> ESPNResponse:
        if response.status_code == 404:
            raise ESPNNotFoundError(f"ESPN resource not found: {url}")
        if response.status_code == 429:
            raise ESPNRateLimitError("ESPN API rate limit exceeded")
        if response.status_code >= 500:
            raise ESPNClientError(f"ESPN server error: {response.status_code}")
        if response.status_code >= 400:
            raise ESPNClientError(f"ESPN API error: {response.status_code}")

        try:
            payload = response.json()
        except Exception as exc:
            raise ESPNClientError(f"Failed to parse ESPN response: {exc}") from exc

        return ESPNResponse(data=payload, status_code=response.status_code, url=url)

    def _request_with_retry(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
    ) -> ESPNResponse:
        @retry(
            retry=retry_if_exception_type((httpx.TransportError, ESPNClientError)),
            stop=stop_after_attempt(self.max_retries),
            wait=wait_exponential(multiplier=self.retry_backoff, min=1, max=10),
            reraise=True,
        )
        def _do_request() -> ESPNResponse:
            response = self.client.request(method, url, params=params)
            return self._handle_response(response, url)

        try:
            return _do_request()
        except RetryError as exc:
            raise ESPNClientError(f"ESPN request failed after {self.max_retries} retries") from exc
        except (ESPNNotFoundError, ESPNRateLimitError):
            raise
        except httpx.TransportError as exc:
            raise ESPNClientError(f"ESPN connection error: {exc}") from exc

    def get(
        self,
        path: str,
        domain: ESPNEndpointDomain = ESPNEndpointDomain.SITE,
        params: dict[str, Any] | None = None,
    ) -> ESPNResponse:
        return self._request_with_retry("GET", self._build_url(domain, path), params=params)

    # ------------------------------------------------------------------
    # Site API v2 endpoints (core ingestion + dashboard basics)
    # ------------------------------------------------------------------

    def get_scoreboard(
        self,
        sport: str,
        league: str,
        date: str | datetime | None = None,
        limit: int | None = None,
    ) -> ESPNResponse:
        params: dict[str, Any] = {}
        if date:
            params["dates"] = date.strftime("%Y%m%d") if isinstance(date, datetime) else date
        if limit is not None:
            params["limit"] = limit
        return self.get(f"/apis/site/v2/sports/{sport}/{league}/scoreboard", ESPNEndpointDomain.SITE, params)

    def get_teams(self, sport: str, league: str, limit: int = 100) -> ESPNResponse:
        return self.get(
            f"/apis/site/v2/sports/{sport}/{league}/teams",
            ESPNEndpointDomain.SITE,
            {"limit": limit},
        )

    def get_team(self, sport: str, league: str, team_id: str) -> ESPNResponse:
        return self.get(f"/apis/site/v2/sports/{sport}/{league}/teams/{team_id}", ESPNEndpointDomain.SITE)

    def get_team_roster(self, sport: str, league: str, team_id: str) -> ESPNResponse:
        return self.get(
            f"/apis/site/v2/sports/{sport}/{league}/teams/{team_id}/roster",
            ESPNEndpointDomain.SITE,
        )

    def get_event(self, sport: str, league: str, event_id: str) -> ESPNResponse:
        return self.get(
            f"/apis/site/v2/sports/{sport}/{league}/summary",
            ESPNEndpointDomain.SITE,
            {"event": event_id},
        )

    def get_news(self, sport: str, league: str, limit: int = 25) -> ESPNResponse:
        return self.get(
            f"/apis/site/v2/sports/{sport}/{league}/news",
            ESPNEndpointDomain.SITE,
            {"limit": limit},
        )

    def get_standings(self, sport: str, league: str, season: int | None = None) -> ESPNResponse:
        params: dict[str, Any] = {}
        if season is not None:
            params["season"] = season
        return self.get(f"/apis/v2/sports/{sport}/{league}/standings", ESPNEndpointDomain.SITE_V2, params)

    def get_league_injuries(self, sport: str, league: str) -> ESPNResponse:
        return self.get(f"/apis/site/v2/sports/{sport}/{league}/injuries", ESPNEndpointDomain.SITE)

    def get_team_injuries(self, sport: str, league: str, team_id: str) -> ESPNResponse:
        return self.get(
            f"/apis/site/v2/sports/{sport}/{league}/teams/{team_id}/injuries",
            ESPNEndpointDomain.SITE,
        )

    def get_league_transactions(self, sport: str, league: str) -> ESPNResponse:
        return self.get(f"/apis/site/v2/sports/{sport}/{league}/transactions", ESPNEndpointDomain.SITE)

    # ------------------------------------------------------------------
    # Core API v2 endpoints (matchups / betting-oriented)
    # ------------------------------------------------------------------

    def get_league_info(self, sport: str, league: str) -> ESPNResponse:
        return self.get(f"/v2/sports/{sport}/leagues/{league}", ESPNEndpointDomain.CORE)

    def get_core_event(self, sport: str, league: str, event_id: str) -> ESPNResponse:
        return self.get(
            f"/v2/sports/{sport}/leagues/{league}/events/{event_id}",
            ESPNEndpointDomain.CORE,
        )

    def get_competition_odds(
        self,
        sport: str,
        league: str,
        event_id: str,
        competition_id: str | None = None,
    ) -> ESPNResponse:
        comp_id = competition_id or event_id
        return self.get(
            f"/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{comp_id}/odds",
            ESPNEndpointDomain.CORE,
        )

    def get_competition_plays(
        self,
        sport: str,
        league: str,
        event_id: str,
        competition_id: str | None = None,
        limit: int = 300,
    ) -> ESPNResponse:
        comp_id = competition_id or event_id
        return self.get(
            f"/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{comp_id}/plays",
            ESPNEndpointDomain.CORE,
            {"limit": limit},
        )

    def get_game_predictor(
        self,
        sport: str,
        league: str,
        event_id: str,
        competition_id: str | None = None,
    ) -> ESPNResponse:
        comp_id = competition_id or event_id
        return self.get(
            f"/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{comp_id}/predictor",
            ESPNEndpointDomain.CORE,
        )

    # ------------------------------------------------------------------
    # CDN helper endpoints
    # ------------------------------------------------------------------

    def get_cdn_gamepackage(self, sport: str, event_id: str, view: str = "game") -> ESPNResponse:
        return self.get(
            f"/core/{sport}/{view}",
            ESPNEndpointDomain.CDN,
            {"xhr": 1, "gameId": event_id},
        )


_default_client: ESPNClient | None = None


def get_espn_client() -> ESPNClient:
    """Return a shared ESPN client instance."""
    global _default_client
    if _default_client is None:
        _default_client = ESPNClient()
    return _default_client
