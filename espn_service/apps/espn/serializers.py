"""Serializers for ESPN data models."""

from rest_framework import serializers

from apps.espn.models import (
    Competitor,
    Event,
    Injury,
    NewsArticle,
    Team,
    Transaction,
    Venue,
)


class LeagueMinimalSerializer(serializers.Serializer):
    slug = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    abbreviation = serializers.CharField(read_only=True)


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = [
            "id", "espn_id", "name", "city", "state", "country",
            "is_indoor", "capacity", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class TeamSerializer(serializers.ModelSerializer):
    league = LeagueMinimalSerializer(read_only=True)
    primary_logo = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = [
            "id", "espn_id", "uid", "slug", "abbreviation", "display_name",
            "short_display_name", "name", "nickname", "location", "color",
            "alternate_color", "is_active", "is_all_star", "logos", "primary_logo",
            "league", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class TeamListSerializer(serializers.ModelSerializer):
    league_slug = serializers.CharField(source="league.slug", read_only=True)
    sport_slug = serializers.CharField(source="league.sport.slug", read_only=True)
    primary_logo = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = [
            "id", "espn_id", "abbreviation", "display_name", "short_display_name",
            "location", "color", "primary_logo", "league_slug", "sport_slug", "is_active",
        ]


class TeamMinimalSerializer(serializers.ModelSerializer):
    primary_logo = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = [
            "id", "espn_id", "abbreviation", "display_name",
            "short_display_name", "location", "color", "primary_logo",
        ]


class CompetitorSerializer(serializers.ModelSerializer):
    team = TeamMinimalSerializer(read_only=True)
    score_int = serializers.IntegerField(read_only=True)

    class Meta:
        model = Competitor
        fields = [
            "id", "team", "home_away", "score", "score_int",
            "winner", "line_scores", "records", "statistics", "leaders", "order",
        ]


class EventSerializer(serializers.ModelSerializer):
    league = LeagueMinimalSerializer(read_only=True)
    venue = VenueSerializer(read_only=True)
    competitors = CompetitorSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "id", "espn_id", "uid", "date", "name", "short_name",
            "season_year", "season_type", "season_slug", "week",
            "status", "status_detail", "clock", "period", "attendance",
            "broadcasts", "links", "league", "venue", "competitors",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class EventListSerializer(serializers.ModelSerializer):
    venue_name = serializers.CharField(source="venue.name", read_only=True, allow_null=True)
    competitors = CompetitorSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "id", "espn_id", "date", "name", "short_name", "status", "status_detail",
            "venue_name", "competitors",
        ]


# ---------------------------------------------------------------------------
# New model serializers — added in audit expansion
# ---------------------------------------------------------------------------


class NewsArticleSerializer(serializers.ModelSerializer):
    """Serializer for NewsArticle model."""

    league_slug = serializers.CharField(source="league.slug", read_only=True, allow_null=True)
    sport_slug = serializers.CharField(source="league.sport.slug", read_only=True, allow_null=True)
    thumbnail = serializers.CharField(read_only=True)

    class Meta:
        model = NewsArticle
        fields = [
            "id", "espn_id", "headline", "description", "published",
            "last_modified", "type", "categories", "images", "links",
            "thumbnail", "league_slug", "sport_slug", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class NewsArticleListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for news article lists."""

    league_slug = serializers.CharField(source="league.slug", read_only=True, allow_null=True)
    sport_slug = serializers.CharField(source="league.sport.slug", read_only=True, allow_null=True)
    thumbnail = serializers.CharField(read_only=True)

    class Meta:
        model = NewsArticle
        fields = [
            "id", "espn_id", "headline", "description", "published",
            "type", "thumbnail", "league_slug", "sport_slug",
        ]


class InjurySerializer(serializers.ModelSerializer):
    """Serializer for Injury model."""

    league_slug = serializers.CharField(source="league.slug", read_only=True)
    sport_slug = serializers.CharField(source="league.sport.slug", read_only=True)
    team_abbreviation = serializers.CharField(
        source="team.abbreviation", read_only=True, allow_null=True
    )

    class Meta:
        model = Injury
        fields = [
            "id", "athlete_espn_id", "athlete_name", "position",
            "status", "status_display", "description", "injury_type",
            "injury_date", "return_date",
            "league_slug", "sport_slug", "team_abbreviation",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for Transaction model."""

    league_slug = serializers.CharField(source="league.slug", read_only=True)
    sport_slug = serializers.CharField(source="league.sport.slug", read_only=True)
    team_abbreviation = serializers.CharField(
        source="team.abbreviation", read_only=True, allow_null=True
    )

    class Meta:
        model = Transaction
        fields = [
            "id", "espn_id", "date", "description", "type",
            "athlete_name", "athlete_espn_id",
            "league_slug", "sport_slug", "team_abbreviation",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
