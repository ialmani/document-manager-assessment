from rest_framework import serializers
from ..models import FileVersion

class FileVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileVersion
        fields = [
            "id",
            "file_name",
            "file_url",
            "version_number",
            "content_hash",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "file_name",
            "file_url",
            "version_number",
            "content_hash",
            "created_at",
        ]
