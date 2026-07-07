from pathlib import Path

from app.schemas.analysis import AnalysisResponse
from ai.document_engine.service import DocumentEngine
from ai.legend_engine.service import LegendEngine
from ai.ocr_engine.service import OcrEngine
from ai.symbol_engine.service import SymbolEngine


class AnalysisOrchestrator:
    """Coordinates the first MVP analysis pipeline.

    The orchestrator deliberately calls specialised services instead of using one
    large prompt. This keeps the architecture flexible for P&ID, SLD and
    electrical diagram profiles.
    """

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

        pdf_files = list(document_dir.glob("*.pdf"))
        if not pdf_files:
            raise FileNotFoundError(f"No PDF found for document: {document_id}")

        document_path = pdf_files[0]
        ocr_result = self.ocr_engine.extract_text(document_path)
        pages = self.document_engine.classify_pages(document_path, ocr_result.page_text)
        legend_items = self.legend_engine.extract_legend(document_path, pages, ocr_result.page_text)
        components = self.symbol_engine.detect_components(document_path, legend_items, ocr_result.page_text)

        return AnalysisResponse(
            document_id=document_id,
            status="analysis_v0_2_completed",
            page_classifications=pages,
            legend_items=legend_items,
            detected_components=components,
            extracted_text_preview=ocr_result.full_text[:2000],
            next_actions=[
                "Add PDF page rendering for vision/image analysis.",
                "Add OpenCV line colour and geometry detection.",
                "Add symbol bounding boxes and click coordinates.",
                "Build graph edges between detected components.",
            ],
        )
