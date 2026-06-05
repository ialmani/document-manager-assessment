from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import FileVersion
from .serializers import FileVersionSerializer


class FileVersionViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """
      Read-only API for browsing file versions owned by the
      authenticated user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = FileVersionSerializer
    lookup_field = "id"

    def get_queryset(self):
        """
        Restrict queries to the authenticated user's files.
        This prevents users from accessing documents uploaded by others.
        """
        return FileVersion.objects.filter(user=self.request.user)

