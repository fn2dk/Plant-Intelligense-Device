# Architecture

The platform is built around a shared processing pipeline:

```text
Document ingestion
→ Page classification
→ Legend extraction
→ OCR
→ Symbol detection
→ Connection tracing
→ Graph generation
→ Validation
→ Engineering actions
```

Each diagram type is implemented as a profile or plugin. The core system does not hardcode P&ID-only behaviour.

## Core design decision

The main asset is the Engineering Knowledge Graph, not the uploaded PDF.

Documents are data sources. The graph is the operational model.
