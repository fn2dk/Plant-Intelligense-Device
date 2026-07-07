class LegendEngine:
    """Extracts project-specific symbol rules from legend pages.

    The legend is the primary source of truth. Generic symbol libraries must never override it.
    """

    def extract_legend(self, legend_pages: list[dict]) -> dict:
        raw_text = "\n".join(page.get("text_preview", "") for page in legend_pages)
        known_terms = [
            "pump", "centrifugal pump", "ball valve", "check valve", "butterfly valve",
            "electric motor", "on-site measurement", "measuring line", "main current",
            "branch current", "heat tracing", "drain", "inlet/outlet"
        ]
        detected = [term for term in known_terms if term in raw_text.lower()]
        return {
            "legend_page_count": len(legend_pages),
            "detected_terms": detected,
            "primary_source_of_truth": True,
            "status": "rule_based_placeholder",
        }
