import re
from pathlib import Path

from app.schemas.analysis import DetectedComponent, LegendItem


TAG_TYPE_PATTERNS: list[tuple[str, str]] = [
    (r"\bP-?\d{2,4}[A-Z]?\b", "pump"),
    (r"\bXV-?\d{2,4}\b", "actuated_valve"),
    (r"\bBV-?\d{2,4}\b", "ball_valve"),
    (r"\bGBV-?\d{2,4}\b", "gate_or_globe_valve"),
    (r"\bCV-?\d{2,4}\b", "check_valve"),
    (r"\bPI-?\d{2,4}\b", "pressure_indicator"),
    (r"\bPIT-?\d{2,4}\b", "pressure_transmitter"),
    (r"\bFIT-?\d{2,4}\b", "flow_transmitter"),
    (r"\bFIC-?\d{2,4}\b", "flow_controller"),
    (r"\bTIT-?\d{2,4}[A-Z]?\b", "temperature_transmitter"),
    (r"\bAIT-?\d{2,4}[A-Z]?\b", "analyzer_transmitter"),
    (r"\bLS-?\d{2,4}\b", "level_switch"),
    (r"\bT-?\d{2,4}\b", "tank"),
    (r"\bF-?\d{2,4}[A-Z]?\b", "filter"),
    (r"\bRO-?\d{2,4}\b", "reverse_osmosis_unit"),
    (r"\bUV-?\d{2,4}\b", "uv_unit"),
]


class SymbolEngine:
    """First-pass component detector based on engineering tag patterns.

    v0.2 detects tags from extracted text. Later versions will connect these
    tags to symbol coordinates and drawing geometry.
    """

    def detect_components(
        self,
        document_path: Path,
        legend: list[LegendItem],
        page_text: dict[int, str],
    ) -> list[DetectedComponent]:
        components: list[DetectedComponent] = []

        for page_number, text in page_text.items():
            for pattern, component_type in TAG_TYPE_PATTERNS:
                for match in re.finditer(pattern, text):
                    tag = match.group(0).replace(" ", "")
                    components.append(DetectedComponent(
                        tag=tag,
                        component_type=component_type,
                        page_number=page_number,
                        confidence=0.70,
                        source="deterministic_tag_pattern",
                    ))

        # Deduplicate: keep first occurrence
        unique: dict[str, DetectedComponent] = {}
        for component in components:
            unique.setdefault(component.tag, component)

        return sorted(unique.values(), key=lambda item: item.tag)
