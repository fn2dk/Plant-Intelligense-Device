class IsolationEngine:
    """Generates isolation proposals.

    Safety rule: output is never approved automatically.
    """

    def generate_demo_isolation(self, graph: dict, component_tag: str) -> dict:
        valves = [n for n in graph["nodes"] if n["type"] == "valve"]
        drains = [n for n in graph["nodes"] if n["type"] == "drain"]
        return {
            "target_component": component_tag,
            "status": "proposal_requires_human_verification",
            "valves_to_close": valves,
            "drains_to_open_or_verify": drains,
            "affected_edges": graph["edges"],
            "warnings": [
                "Demo isolation only. Real isolation requires verified graph connectivity.",
                "Check for trapped pressure, bypasses, check valves and stored energy.",
            ],
        }
