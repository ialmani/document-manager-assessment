from django.conf import settings
from django.urls import path

from rest_framework.routers import DefaultRouter, SimpleRouter

from propylon_document_manager.file_versions.api.views import FileVersionViewSet, DocumentView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("file_versions", FileVersionViewSet,  basename="file-version")

app_name = "api"

urlpatterns = [
    *router.urls,
    path(
        "documents/<path:file_url>",
        DocumentView.as_view(),
        name="document",
    ),
]
