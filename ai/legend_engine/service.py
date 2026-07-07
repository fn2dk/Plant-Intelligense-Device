from pathlib import Path

from app.schemas.analysis import LegendItem, PageClassification


KNOWN_LEGEND_TERMS = [
    "pump",
    "centrifugal pump",
    "valve",
    "ball valve",
    "check valve",
    "butterfly valve",
    "safety valve",
    "tank",
    "vessel",
    "filter",
    "heat exchanger",
    "measurement",
    "electric motor",
    "drain",
    "inlet/outlet",
    "main current",
    "branch current",
    "measuring line",
    "air",
]


class LegendEngine:
    """Extracts first-pass legend terms from pages classified as legend."""

    def extract_legend(
        self,
        document_path: Path,
        pages: list[PageClassification],
        page_text: dict[int, str],
    ) -> list[LegendItem]:
        legend_pages = {page.page_number for page in pages if page.page_type == "legend"}
        items: list[LegendItem] = []

        for page_number in legend_pages:
            text_lower = page_text.get(page_number, "").lower()
            for term in KNOWN_LEGEND_TERMS:
                if term in text_lower:
                    items.append(LegendItem(
                        name=term,
                        page_number=page_number,
                        confidence=0.65,
                        source="deterministic_legend_keyword",
                    ))

        # Deduplicate by name/page
        unique: dict[tuple[str, int], LegendItem] = {}
        for item in items:
            unique[(item.name, item.page_number)] = item

        return list(unique.values())
