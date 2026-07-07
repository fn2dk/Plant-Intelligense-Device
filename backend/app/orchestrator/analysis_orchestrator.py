from pathlib import Path

from app.schemas.analysis import AnalysisResponse, AnalysisStats
from ai.document_engine.service import DocumentEngine
from ai.legend_engine.service import LegendEngine
from ai.ocr_engine.service import OcrEngine
from ai.symbol_engine.service import SymbolEngine


class AnalysisOrchestrator:
    """Coordinates the first functional MVP analysis pipeline."""

    def __init__(self, upload_root: Path = Path("uploads")) -> None:
        self.upload_root = upload_root
        self.document_engine = DocumentEngine()
        self.legend_engine = LegendEngine()
        self.ocr_engine = OcrEngine()
        self.symbol_engine = SymbolEngine()

    def analyze(self, document_id: str) -> AnalysisResponse:
        document_dir = self.upload_root / document_id
        if not document_dir.exists():
            raise FileNotFoundError(f"Document not found: {document_id}")

        document_path = document_dir / "source.pdf"
        if not document_path.exists():
            raise FileNotFoundError(f"No PDF found for document: {document_id}")

        ocr_result = self.ocr_engine.extract_text(document_path)
        pages = self.document_engine.classify_pages(document_path, ocr_result.page_text)
        legend_items = self.legend_engine.extract_legend(document_path, pages, ocr_result.page_text)
        components = self.symbol_engine.detect_components(document_path, legend_items, ocr_result.page_text)

        legend_page_count = len([page for page in pages if page.page_type == "legend"])

        return AnalysisResponse(
            document_id=document_id,
            status="analysis_v0_3_completed",
            stats=AnalysisStats(
                page_count=len(pages),
                legend_page_count=legend_page_count,
                component_count=len(components),
                extracted_character_count=len(ocr_result.full_text),
            ),
            page_classifications=pages,
            legend_items=legend_items,
            detected_components=components[:300],
            extracted_text_preview=ocr_result.full_text[:2000],
            next_actions=[
                "v0.4: render PDF pages to PNG for coordinate-aware analysis.",
                "v0.4: create image overlays for clickable components.",
                "v0.5: add OpenCV geometry and line tracing.",
            ],
        )
