from pydantic import BaseModel, Field


class PageClassification(BaseModel):
    page_number: int
    page_type: str
    confidence: float = Field(ge=0.0, le=1.0)
    reason: str


class DetectedComponent(BaseModel):
    component_id: str
    tag: str | None = None
    component_type: str
    page_number: int
    bbox: list[float]
    confidence: float = Field(ge=0.0, le=1.0)
    source: str


class AnalysisResponse(BaseModel):
    document_id: str
    status: str
    page_classifications: list[PageClassification]
    detected_components: list[DetectedComponent]
    next_actions: list[str]
