"""Serializers for ingest API endpoints."""

from rest_framework import serializers


class IngestScoreboardRequestSerializer(serializers.Serializer):
    """Request serializer for scoreboard ingestion."""

    date = serializers.CharField(
        max_length=8,
        required=False,
        allow_blank=True,
        help_text="Date in YYYYMMDD format (optional, defaults to today)",
    )

    def validate_date(self, value: str) -> str | None:
        if not value:
            return None
        value = value.strip()
        if len(value) != 8 or not value.isdigit():
            raise serializers.ValidationError("Date must be in YYYYMMDD format (e.g., '20241215')")
        return value


class IngestTeamsRequestSerializer(serializers.Serializer):
    """Request serializer for teams ingestion."""
    pass


class IngestNewsRequestSerializer(serializers.Serializer):
    """Request serializer for news ingestion."""

    limit = serializers.IntegerField(
        default=50, min_value=1, max_value=200, help_text="Number of articles to fetch (default 50)"
    )


class IngestInjuriesRequestSerializer(serializers.Serializer):
    """Request serializer for injury ingestion."""
    pass


class IngestTransactionsRequestSerializer(serializers.Serializer):
    """Request serializer for transaction ingestion."""
    pass


class IngestionResultSerializer(serializers.Serializer):
    """Serializer for ingestion results."""

    created = serializers.IntegerField(help_text="Number of new records created")
    updated = serializers.IntegerField(help_text="Number of existing records updated")
    errors = serializers.IntegerField(help_text="Number of records that failed to process")
    total_processed = serializers.IntegerField(help_text="Total records processed (created + updated)")
    details = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_null=True,
        help_text="Optional details about the ingestion",
    )
