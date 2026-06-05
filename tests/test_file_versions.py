import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from propylon_document_manager.file_versions.models import FileVersion, User
from rest_framework.test import APIClient


def test_file_versions():
    """
    Verify that a document version can be created and associated
    with the correct user.
    """
    user = User.objects.create(
        email="johndoe@gmail.com",
        password='password123'
    )

    file_name = "new_file"
    file_version = 1

    uploaded_file = SimpleUploadedFile(
        "new_file.pdf",
        b"test content",
    )

    FileVersion.objects.create(
        user=user,
        file_name=file_name,
        file_url="documents/new_file.pdf",
        file=uploaded_file,
        version_number=file_version,
        content_hash="testhash123",
    )

    files = FileVersion.objects.all()
    assert files.count() == 1
    assert files[0].file_name == file_name
    assert files[0].version_number == file_version
    assert files[0].user == user
