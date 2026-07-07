from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.document import DocumentUploadResponse
from app.services.storage_service import StorageService

router = APIRouter()
storage = StorageService(base_dir=Path("uploads"))


@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)) -> DocumentUploadResponse:
    filename = file.filename or "uploaded.pdf"
    if not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported in v0.3.")

    document_id = str(uuid4())
    stored_path = await storage.save_upload(document_id=document_id, file=file)
    return DocumentUploadResponse(
        document_id=document_id,
        filename=filename,
        content_type=file.content_type or "application/pdf",
        stored_path=str(stored_path),
    )
