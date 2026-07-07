import re
from pathlib import Path
from uuid import uuid4

from backend.app.schemas.analysis import DetectedComponent

TAG_PATTERN = re.compile(r"\b([A-Z]{1,4}-?\d{2,4}[A-Z]?(?:/[A-Z])?)\b")

TAG_TYPE_PREFIXES = {
    "P": "pump",
    "XV": "on_off_valve",
    "BV": "ball_valve",
    "GV": "gate_valve",
    "CV": "check_valve",
    "PI": "pressure_indicator",
    "PIT": "pressure_transmitter",
    "FIT": "flow_transmitter",
    "FIC": "flow_controller",
    "TIT": "temperature_transmitter",
    "AIT": "analyzer_transmitter",
    "LS": "level_switch",
    "T": "tank",
    "F": "filter",
    "RO": "reverse_osmosis",
    "UV": "uv_unit",
}


class SymbolEngine:
    """Detects engineering components.

    First implementation extracts likely tags from OCR text. Coordinate boxes are
    placeholders until PDF coordinate extraction and computer vision are added.
    """

    def detect_components(
        self,
        pdf_path: Path,
        legend: dict,
        ocr_text: dict[int, str],
    ) -> list[DetectedComponent]:
        components: list[DetectedComponent] = []
        seen: set[tuple[int, str]] = set()

        for page_number, text in ocr_text.items():
            for match in TAG_PATTERN.finditer(text):
                tag = match.group(1)
                key = (page_number, tag)
                if key in seen:
                    continue
                seen.add(key)
                prefix = re.match(r"[A-Z]+", tag.replace("-", ""))
                component_type = "unknown_component"
                if prefix:
                    component_type = TAG_TYPE_PREFIXES.get(prefix.group(0), component_type)

                components.append(
                    DetectedComponent(
                        component_id=str(uuid4()),
                        tag=tag,
                        component_type=component_type,
                        page_number=page_number,
                        bbox=[0.0, 0.0, 0.0, 0.0],
                        confidence=0.45,
                        source="ocr_tag_regex_stub",
                    )
                )

        return components[:250]
