# Engineering Intelligence Platform

Working product name: **Plant Intelligense Device**  
Architecture name: **Project Atlas**

This repository contains the foundation for a flexible Engineering Diagram Intelligence Platform.

The platform is not a PDF viewer. It converts engineering documents into structured objects, relationships, and a searchable Engineering Knowledge Graph.

## First MVP

The first MVP is a single-drawing P&ID analysis pipeline:

1. Upload a PDF.
2. Classify pages.
3. Detect legend pages.
4. Extract OCR text.
5. Detect symbols and component tags.
6. Store components with coordinates and confidence scores.
7. Build basic relationships.
8. Render clickable overlays.
9. Prepare an AI-assisted isolation proposal.

## Long-term diagram profiles

- P&ID
- SLD
- Electrical schematics
- Control diagrams
- IO diagrams
- Loop diagrams
- Cable diagrams
- Excel component registers
- CMMS / maintenance systems

## Safety principle

AI-generated isolation plans are proposals only. A qualified person must verify them before operational use.

## Repository layout

```text
backend/       FastAPI backend and API services
frontend/      React/Next.js frontend foundation
ai/            AI and computer-vision engines
plugins/       Diagram profiles and rule sets
database/      PostgreSQL schema and migrations
docs/          Architecture, requirements and roadmap
tests/         System-level tests
datasets/      Test documents and sample outputs
examples/      Example payloads and expected results
```

## Local backend start

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```
