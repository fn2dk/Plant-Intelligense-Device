from pathlib import Path

from pypdf import PdfReader


class OcrEngine:
    """Extracts text from engineering documents.

    Current implementation uses embedded PDF text through pypdf. Later versions
    will add PaddleOCR for rasterized drawings and technical tag recognition.
    """

    def extract_text(self, pdf_path: Path) -> dict[int, str]:
        reader = PdfReader(str(pdf_path))
        return {
            index: page.extract_text() or ""
            for index, page in enumerate(reader.pages, start=1)
        }
