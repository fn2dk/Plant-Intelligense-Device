from dataclasses import dataclass, field
from typing import Any


@dataclass
class EngineeringObject:
    object_id: str
    object_type: str
    tag: str | None = None
    properties: dict[str, Any] = field(default_factory=dict)


@dataclass
class EngineeringRelationship:
    source_id: str
    target_id: str
    relationship_type: str
    confidence: float
    properties: dict[str, Any] = field(default_factory=dict)
