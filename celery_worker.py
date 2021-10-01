from accessory_functions import make_hash
import os
from celery import Celery
from dotenv import load_dotenv
from models import create_crypto

load_dotenv(".env")

celery = Celery(__name__)

celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name="making_hash")
def create_task(file_path: str, file_id: str) -> None:
    with open(file_path, "rb") as file:
        result = file.read()
    file_hash = make_hash(result)
    os.remove(file_path)
    create_crypto(file_id=file_id, file_hash=file_hash)
