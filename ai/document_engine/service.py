from pathlib import Path

from pypdf import PdfReader

from backend.app.schemas.analysis import PageClassification


class DocumentEngine:
    """Classifies document pages for the first MVP.

    Current implementation uses text heuristics. Later versions will add PDF
    rendering, title-block detection and vision-model classification.
    """

    def classify_pages(self, pdf_path: Path) -> list[PageClassification]:
        reader = PdfReader(str(pdf_path))
        results: list[PageClassification] = []

        for index, page in enumerate(reader.pages, start=1):
            text = (page.extract_text() or "").lower()
            page_type = "drawing"
            reason = "Defaulted to drawing page."
            confidence = 0.55

            if "legend" in text or "legende" in text:
                page_type = "legend"
                reason = "Page text contains legend marker."
                confidence = 0.85
            elif "component list" in text:
                page_type = "component_list"
                reason = "Page text contains component list marker."
                confidence = 0.85
            elif "p&id" in text or "pid" in text:
                page_type = "pid_drawing"
                reason = "Page text contains P&ID marker."
                confidence = 0.75

            results.append(
                PageClassification(
                    page_number=index,
                    page_type=page_type,
                    confidence=confidence,
                    reason=reason,
                )
            )

        return results
