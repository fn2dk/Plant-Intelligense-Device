import re

TAG_PATTERN = re.compile(r"\b[A-Z]{1,5}[-]?[0-9]{2,4}[A-Z]?\b")

class OcrEngine:
    """Text and tag extraction abstraction.

    Current MVP uses embedded PDF text. Later this engine should add PaddleOCR for scanned drawings.
    """

    def extract_tags_from_pages(self, pages: list[dict]) -> dict:
        tags = []
        for page in pages:
            text = page.get("text_preview", "")
            for match in TAG_PATTERN.finditer(text):
                tags.append({
                    "tag": match.group(0),
                    "page_number": page["page_number"],
                    "source": "embedded_pdf_text",
                    "confidence": 0.70,
                })
        unique = list({(t["tag"], t["page_number"]): t for t in tags}.values())
        return {"count": len(unique), "items": unique[:300]}
