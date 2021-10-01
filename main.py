import os
import uuid
from fastapi import FastAPI, UploadFile, File
from starlette.responses import JSONResponse
from accessory_functions import save_upload_file_tmp, create_upload_file
# from starlette.staticfiles import StaticFiles
# from starlette.templating import Jinja2Templates
from celery_worker import create_task
from models import get_hash_by_id

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")


@app.get("/get_hash_by_id/{hash_id}")
async def show_hash(hash_id: str):
    file_hash = get_hash_by_id(hash_id)
    print(file_hash[0])

    return JSONResponse({
        "file_id": hash_id,
        "md5_hash": file_hash[0]
    })


@app.post("/uploadfile/")
async def create_file(file: UploadFile = File(...)):

    file_name = create_upload_file(file)
    temp_path = "/app/" + file_name
    file_id = str(uuid.uuid4())
    create_task.delay(file_path=temp_path, file_id=file_id)

    return JSONResponse({"file_id": file_id})

