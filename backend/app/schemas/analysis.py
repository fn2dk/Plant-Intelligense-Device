from pydantic import BaseModel, Field


class PageClassification(BaseModel):
    page_number: int
    page_type: str
    confidence: float
    reason: str


class DetectedComponent(BaseModel):
    tag: str
    component_type: str
    page_number: int | None = None
    confidence: float = 0.5
    source: str = "text_pattern"


class LegendItem(BaseModel):
    name: str
    page_number: int
    confidence: float = 0.5
    source: str = "legend_text"


class AnalysisStats(BaseModel):
    page_count: int
    legend_page_count: int
    component_count: int
    extracted_character_count: int


class AnalysisResponse(BaseModel):
    document_id: str
    status: str
    stats: AnalysisStats
    page_classifications: list[PageClassification] = Field(default_factory=list)
    legend_items: list[LegendItem] = Field(default_factory=list)
    detected_components: list[DetectedComponent] = Field(default_factory=list)
    extracted_text_preview: str = ""
    next_actions: list[str] = Field(default_factory=list)
