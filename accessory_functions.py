import hashlib
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from fastapi import UploadFile


def make_hash(fileb: bytes) -> str:
    return hashlib.md5(fileb).hexdigest()


def save_upload_file_tmp(upload_file: UploadFile) -> str:
    try:
        suffix = Path(upload_file.filename).suffix
        prefix = "/service/"
        with NamedTemporaryFile(delete=False, suffix=suffix, prefix=prefix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = tmp.name
    finally:
        upload_file.file.close()
    return tmp_path


def create_upload_file(uploaded_file: UploadFile):
    file_location = f"service/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return uploaded_file.filename
