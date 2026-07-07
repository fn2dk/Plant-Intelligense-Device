from pathlib import Path
from typing import Any

from backend.app.schemas.analysis import PageClassification


class LegendEngine:
    """Extracts project-specific legend information.

    The legend is the primary source of truth. This stub returns page references
    and known categories. Later versions will crop symbols and create a learned
    symbol library for each project.
    """

    def extract_legend(self, pdf_path: Path, pages: list[PageClassification]) -> dict[str, Any]:
        legend_pages = [page.page_number for page in pages if page.page_type == "legend"]
        return {
            "pdf_path": str(pdf_path),
            "legend_pages": legend_pages,
            "status": "stub",
            "expected_outputs": [
                "symbols",
                "line_colours",
                "line_styles",
                "component_meanings",
                "project_specific_overrides",
            ],
        }
