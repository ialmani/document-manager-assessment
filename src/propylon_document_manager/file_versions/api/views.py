from django.shortcuts import render
from django.http import FileResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import FileVersion
from .serializers import FileVersionSerializer
from ..utils import compute_file_hash


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


class DocumentView(APIView):
    """
    Handles uploads and downloads for versioned documents.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, file_url):
        uploaded_file = request.FILES.get("file")

        if uploaded_file is None:
            return Response(
                {"detail": "No file provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        latest_version = (
            FileVersion.objects.filter(
                user=request.user,
                file_url=file_url,
            )
            .order_by("-version_number")
            .first()
        )

        # Revision 0 represents the first uploaded version.
        next_version = 0 if latest_version is None else latest_version.version_number + 1

        file_version = FileVersion.objects.create(
            user=request.user,
            file_name=uploaded_file.name,
            file_url=file_url,
            file=uploaded_file,
            version_number=next_version,
            # SHA-256 hash supports content-addressable storage lookups.
            content_hash=compute_file_hash(uploaded_file),
        )

        return Response(
            FileVersionSerializer(file_version).data,
            status=status.HTTP_201_CREATED,
        )

    def get(self, request, file_url):
        revision = request.query_params.get("revision")

        versions = FileVersion.objects.filter(
            user=request.user,
            file_url=file_url,
        )

        if revision is not None:
            file_version = get_object_or_404(
                versions,
                version_number=revision,
            )
        else:
            file_version = versions.order_by("-version_number").first()

            if file_version is None:
                return Response(
                    {"detail": "File not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

        return FileResponse(
            file_version.file.open("rb"),
            as_attachment=True,
            filename=file_version.file_name,
        )


class ContentAddressableStorageView(APIView):
    """
    Retrieves a file by its SHA-256 content hash.

    This supports Content Addressable Storage, where the file
    is addressed by its contents instead of its document URL.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, content_hash):
        file_version = get_object_or_404(
            FileVersion.objects.filter(user=request.user),
            content_hash=content_hash,
        )

        return FileResponse(
            file_version.file.open("rb"),
            as_attachment=True,
            filename=file_version.file_name,
        )


class DocumentVersionsView(APIView):
    """
    Lists all versions of a document owned by the
    authenticated user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, file_url):
        versions = (
            FileVersion.objects.filter(
                user=request.user,
                file_url=file_url,
            )
            .order_by("version_number")
        )

        return Response(
            FileVersionSerializer(
                versions,
                many=True,
            ).data,
            status=status.HTTP_200_OK,
        )


class DocumentVersionsView(APIView):
    """
    Lists all versions for a document URL owned by the authenticated user.
    Used by the frontend View Versions modal.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, file_url):
        versions = FileVersion.objects.filter(
            user=request.user,
            file_url=file_url,
        ).order_by("version_number")

        return Response(
            FileVersionSerializer(versions, many=True).data,
            status=status.HTTP_200_OK,
        )
