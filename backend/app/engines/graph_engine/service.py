class GraphEngine:
    """Builds engineering relationships.

    MVP returns a deterministic demo graph. Real graph extraction comes after connection tracing.
    """

    def build_demo_graph(self) -> dict:
        nodes = [
            {"id": "P-101A", "type": "pump", "label": "Pump P-101A"},
            {"id": "XV-101", "type": "valve", "label": "Valve XV-101"},
            {"id": "F-101", "type": "filter", "label": "Filter F-101"},
            {"id": "T-101", "type": "tank", "label": "Tank T-101"},
            {"id": "DV-101", "type": "drain", "label": "Drain DV-101"},
        ]
        edges = [
            {"from": "T-101", "to": "XV-101", "relationship": "CONNECTED_TO"},
            {"from": "XV-101", "to": "F-101", "relationship": "CONNECTED_TO"},
            {"from": "F-101", "to": "P-101A", "relationship": "CONNECTED_TO"},
            {"from": "P-101A", "to": "DV-101", "relationship": "HAS_DRAIN"},
        ]
        return {"nodes": nodes, "edges": edges, "status": "demo_graph"}
