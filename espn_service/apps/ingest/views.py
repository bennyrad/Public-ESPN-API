"""Views for ingestion API endpoints."""

import structlog
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.ingest.serializers import (
    IngestionResultSerializer,
    IngestInjuriesRequestSerializer,
    IngestNewsRequestSerializer,
    IngestScoreboardRequestSerializer,
    IngestTeamsRequestSerializer,
    IngestTransactionsRequestSerializer,
)
from apps.ingest.services import (
    InjuryIngestionService,
    NewsIngestionService,
    ScoreboardIngestionService,
    TeamIngestionService,
    TransactionIngestionService,
)

logger = structlog.get_logger(__name__)
NFL_SPORT = "football"
NFL_LEAGUE = "nfl"


class IngestScoreboardView(APIView):
    """Endpoint for ingesting scoreboard data from ESPN."""

    @extend_schema(
        tags=["Ingest"],
        summary="Ingest scoreboard data",
        description=(
            "Fetch scoreboard data from ESPN for a specific sport, league, and date, "
            "then upsert the events and competitors into the database."
        ),
        request=IngestScoreboardRequestSerializer,
        responses={
            200: IngestionResultSerializer,
            400: {"description": "Invalid request data"},
            502: {"description": "ESPN API error"},
        },
    )
    def post(self, request: Request) -> Response:
        """Ingest scoreboard data from ESPN."""
        serializer = IngestScoreboardRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        date = serializer.validated_data.get("date")

        logger.info("scoreboard_ingestion_requested", sport=NFL_SPORT, league=NFL_LEAGUE, date=date)

        service = ScoreboardIngestionService()
        result = service.ingest_scoreboard(NFL_SPORT, NFL_LEAGUE, date)
        return Response(IngestionResultSerializer(result.to_dict()).data, status=status.HTTP_200_OK)


class IngestTeamsView(APIView):
    """Endpoint for ingesting team data from ESPN."""

    @extend_schema(
        tags=["Ingest"],
        summary="Ingest teams data",
        description=(
            "Fetch all teams from ESPN for a specific sport and league, "
            "then upsert them into the database."
        ),
        request=IngestTeamsRequestSerializer,
        responses={
            200: IngestionResultSerializer,
            400: {"description": "Invalid request data"},
            502: {"description": "ESPN API error"},
        },
    )
    def post(self, request: Request) -> Response:
        """Ingest teams data from ESPN."""
        serializer = IngestTeamsRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        logger.info("teams_ingestion_requested", sport=NFL_SPORT, league=NFL_LEAGUE)

        service = TeamIngestionService()
        result = service.ingest_teams(NFL_SPORT, NFL_LEAGUE)
        return Response(IngestionResultSerializer(result.to_dict()).data, status=status.HTTP_200_OK)


class IngestNewsView(APIView):
    """Endpoint for ingesting news articles from ESPN."""

    @extend_schema(
        tags=["Ingest"],
        summary="Ingest news articles",
        description=(
            "Fetch news articles from ESPN for a specific sport and league, "
            "then upsert them into the database."
        ),
        request=IngestNewsRequestSerializer,
        responses={
            200: IngestionResultSerializer,
            400: {"description": "Invalid request data"},
            502: {"description": "ESPN API error"},
        },
    )
    def post(self, request: Request) -> Response:
        """Ingest news articles from ESPN."""
        serializer = IngestNewsRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        limit = serializer.validated_data.get("limit", 50)

        logger.info("news_ingestion_requested", sport=NFL_SPORT, league=NFL_LEAGUE, limit=limit)

        service = NewsIngestionService()
        result = service.ingest_news(NFL_SPORT, NFL_LEAGUE, limit=limit)
        return Response(IngestionResultSerializer(result.to_dict()).data, status=status.HTTP_200_OK)


class IngestInjuriesView(APIView):
    """Endpoint for ingesting league injury reports from ESPN."""

    @extend_schema(
        tags=["Ingest"],
        summary="Ingest injury report",
        description=(
            "Fetch the current league injury report from ESPN and refresh the database snapshot. "
            "This is a full replacement — all prior entries for the league are deleted then re-inserted."
        ),
        request=IngestInjuriesRequestSerializer,
        responses={
            200: IngestionResultSerializer,
            400: {"description": "Invalid request data"},
            502: {"description": "ESPN API error"},
        },
    )
    def post(self, request: Request) -> Response:
        """Ingest injury report from ESPN."""
        serializer = IngestInjuriesRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        logger.info("injuries_ingestion_requested", sport=NFL_SPORT, league=NFL_LEAGUE)

        service = InjuryIngestionService()
        result = service.ingest_injuries(NFL_SPORT, NFL_LEAGUE)
        return Response(IngestionResultSerializer(result.to_dict()).data, status=status.HTTP_200_OK)


class IngestTransactionsView(APIView):
    """Endpoint for ingesting league transactions from ESPN."""

    @extend_schema(
        tags=["Ingest"],
        summary="Ingest transactions",
        description=(
            "Fetch the latest transactions from ESPN for a specific sport and league, "
            "then upsert them into the database."
        ),
        request=IngestTransactionsRequestSerializer,
        responses={
            200: IngestionResultSerializer,
            400: {"description": "Invalid request data"},
            502: {"description": "ESPN API error"},
        },
    )
    def post(self, request: Request) -> Response:
        """Ingest transactions from ESPN."""
        serializer = IngestTransactionsRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        logger.info("transactions_ingestion_requested", sport=NFL_SPORT, league=NFL_LEAGUE)

        service = TransactionIngestionService()
        result = service.ingest_transactions(NFL_SPORT, NFL_LEAGUE)
        return Response(IngestionResultSerializer(result.to_dict()).data, status=status.HTTP_200_OK)
