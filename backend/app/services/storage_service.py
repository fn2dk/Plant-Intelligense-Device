from pathlib import Path

from fastapi import UploadFile


class StorageService:
    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)

    async def save_upload(self, document_id: str, file: UploadFile) -> Path:
        document_dir = self.base_dir / document_id
        document_dir.mkdir(parents=True, exist_ok=True)
        safe_name = file.filename or "uploaded.pdf"
        destination = document_dir / safe_name
        content = await file.read()
        destination.write_bytes(content)
        return destination

    def document_dir(self, document_id: str) -> Path:
        path = self.base_dir / document_id
        if not path.exists():
            raise FileNotFoundError(f"Document not found: {document_id}")
        return path
