from pathlib import Path

from fastapi import UploadFile


class StorageService:
    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)

    async def save_upload(self, document_id: str, file: UploadFile) -> Path:
        document_dir = self.base_dir / document_id
        document_dir.mkdir(parents=True, exist_ok=True)

        suffix = Path(file.filename or "uploaded.pdf").suffix or ".pdf"
        target_path = document_dir / f"source{suffix}"

        with target_path.open("wb") as buffer:
            while chunk := await file.read(1024 * 1024):
                buffer.write(chunk)

        return target_path
