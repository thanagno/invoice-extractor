import os
from fastapi import APIRouter, UploadFile
from app.pipelines.inference_pipeline import run_inference

router = APIRouter()

@router.post("/process-invoice/")
async def process_invoice(file: UploadFile):
    """Process the uploaded file to extract invoice details."""
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = run_inference(file_path)
    os.remove(file_path)
    return result