from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


@dataclass
class OcrResult:
    page_text: dict[int, str]
    full_text: str


class OcrEngine:
    """Text extraction service.

    v0.3 uses embedded PDF text through pypdf.
    Later versions will add PaddleOCR for scanned drawings.
    """

    def extract_text(self, document_path: Path) -> OcrResult:
        reader = PdfReader(str(document_path))
        page_text: dict[int, str] = {}

        for index, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            page_text[index] = text

        return OcrResult(
            page_text=page_text,
            full_text="\n\n".join(page_text.values()),
        )
