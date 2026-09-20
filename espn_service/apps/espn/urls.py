"""URL configuration for ESPN app."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.espn.views import (
    EventViewSet,
    InjuryViewSet,
    NewsArticleViewSet,
    TeamViewSet,
    TransactionViewSet,
)

app_name = "espn"

router = DefaultRouter()
router.register(r"teams", TeamViewSet, basename="team")
router.register(r"events", EventViewSet, basename="event")
router.register(r"news", NewsArticleViewSet, basename="news")
router.register(r"injuries", InjuryViewSet, basename="injury")
router.register(r"transactions", TransactionViewSet, basename="transaction")

urlpatterns = [
    path("", include(router.urls)),
]
