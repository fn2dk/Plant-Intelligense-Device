from __future__ import annotations

import fitz
from pydantic import BaseModel

from app.engines.legend_engine.service import LegendEngine
from app.engines.ocr_engine.service import OcrEngine

class PageClassification(BaseModel):
    page_number: int
    page_type: str
    confidence: float
    reason: str

class DocumentEngine:
    """Coordinates first-pass PDF analysis.

    This engine deliberately keeps AI providers behind abstractions.
    The MVP starts deterministic: text extraction and simple rules.
    Later, OpenAI Vision, PaddleOCR and OpenCV can be plugged into the same flow.
    """

    def analyze_pdf(self, filename: str, content: bytes) -> dict:
        doc = fitz.open(stream=content, filetype="pdf")
        pages: list[dict] = []
        classifications: list[PageClassification] = []

        for index, page in enumerate(doc):
            text = page.get_text("text") or ""
            page_number = index + 1
            classification = self._classify_page(page_number, text)
            classifications.append(classification)
            pages.append({
                "page_number": page_number,
                "width": page.rect.width,
                "height": page.rect.height,
                "text_preview": text[:1200],
                "classification": classification.model_dump(),
            })

        legend_pages = [p for p in pages if p["classification"]["page_type"] == "legend"]
        legend_result = LegendEngine().extract_legend(legend_pages)
        text_result = OcrEngine().extract_tags_from_pages(pages)

        return {
            "filename": filename,
            "page_count": len(doc),
            "pages": pages,
            "legend": legend_result,
            "detected_tags": text_result,
            "next_steps": [
                "Add PDF rendering thumbnails for page-level visual analysis.",
                "Add OpenAI Vision provider for symbol and legend interpretation.",
                "Add OpenCV line and color extraction.",
                "Persist detected objects in database.",
            ],
        }

    def _classify_page(self, page_number: int, text: str) -> PageClassification:
        lower = text.lower()
        if "legend" in lower or "legende" in lower:
            return PageClassification(page_number=page_number, page_type="legend", confidence=0.92, reason="Legend keyword found")
        if "component list" in lower:
            return PageClassification(page_number=page_number, page_type="component_list", confidence=0.90, reason="Component List keyword found")
        if "p&id" in lower or "pid" in lower:
            return PageClassification(page_number=page_number, page_type="drawing", confidence=0.86, reason="P&ID/PID keyword found")
        return PageClassification(page_number=page_number, page_type="unknown", confidence=0.35, reason="No strong classifier match")
