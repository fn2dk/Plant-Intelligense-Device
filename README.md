# Engineering Intelligence Platform

Working repository name: Plant-Intelligense-Device-
Internal project name: Atlas

This project is a flexible Engineering Diagram Intelligence Platform. It is designed to ingest technical documents such as P&IDs, SLDs, electrical schematics, loop diagrams, cable diagrams and component lists, then convert them into an Engineering Knowledge Graph.

The first MVP focuses on one uploaded P&ID PDF and proves the core pipeline:

Document ingestion -> Page classification -> Legend extraction -> OCR -> Symbol detection -> Connection tracing -> Graph generation -> Interactive overlay -> Engineering actions.

## First MVP

The first target is a single-drawing P&ID intelligence demo.

It must:

- Upload a PDF.
- Render the PDF in the browser.
- Classify pages as drawing, legend, component list or other.
- Extract tags and text.
- Create detected engineering objects.
- Store coordinates and confidence scores.
- Expose objects through an API.
- Prepare the structure for isolation planning and Excel component register matching.

## Architecture

- Backend: Python FastAPI
- Frontend: Next.js / React
- Database: PostgreSQL / Supabase-compatible SQL
- PDF rendering: PDF.js in frontend, PyMuPDF in backend
- OCR: PaddleOCR later, simple OCR abstraction now
- AI/Vision: pluggable provider later
- Graph: relational MVP now, Neo4j-ready model later

## Safety

Any generated isolation plan is an engineering proposal only and must be verified by a qualified human before operational use.
