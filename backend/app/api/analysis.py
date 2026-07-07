from fastapi import APIRouter, HTTPException

from app.orchestrator.analysis_orchestrator import AnalysisOrchestrator
from app.schemas.analysis import AnalysisResponse

router = APIRouter()
orchestrator = AnalysisOrchestrator()


@router.post("/{document_id}", response_model=AnalysisResponse)
def analyze_document(document_id: str) -> AnalysisResponse:
    try:
        return orchestrator.analyze(document_id=document_id)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
