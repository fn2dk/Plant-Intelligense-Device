from pathlib import Path

from app.schemas.analysis import PageClassification


class DocumentEngine:
    """Classifies engineering PDF pages using deterministic text signals."""

    def classify_pages(self, document_path: Path, page_text: dict[int, str]) -> list[PageClassification]:
        classifications: list[PageClassification] = []

        for page_number, text in page_text.items():
            text_lower = text.lower()

            if "legend" in text_lower or "legende" in text_lower:
                page_type = "legend"
                confidence = 0.90
                reason = "Page text contains legend/legende."
            elif "component list" in text_lower:
                page_type = "component_list"
                confidence = 0.90
                reason = "Page text contains component list."
            elif "p&id" in text_lower or "pid" in text_lower:
                page_type = "pid"
                confidence = 0.80
                reason = "Page text contains P&ID/PID."
            elif "single line" in text_lower or "sld" in text_lower:
                page_type = "sld"
                confidence = 0.75
                reason = "Page text contains SLD/single line signal."
            else:
                page_type = "unknown"
                confidence = 0.40
                reason = "No strong deterministic signal found."

            classifications.append(PageClassification(
                page_number=page_number,
                page_type=page_type,
                confidence=confidence,
                reason=reason,
            ))

        return classifications
