import hashlib


def compute_file_hash(file):
    sha256 = hashlib.sha256()

    for chunk in file.chunks():
        sha256.update(chunk)

    file.seek(0)

    return sha256.hexdigest()
