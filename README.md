# Plant Intelligense Device

Engineering Intelligence Platform foundation.

This project is built as a flexible platform for understanding engineering diagrams, not as a simple PDF viewer.

## Version 0.2 focus

v0.2 introduces a first real PDF ingestion pipeline:

- Upload PDF
- Store document
- Classify pages
- Extract embedded PDF text
- Detect likely legend pages
- Extract engineering tags
- Return a structured analysis result

The first target is P&ID analysis. The architecture is prepared for electrical diagrams, SLDs, loop diagrams, IO diagrams and cable diagrams.

## Local backend start

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Core rule

The drawing legend is the primary source of truth for project-specific symbols, line colours and line types.
