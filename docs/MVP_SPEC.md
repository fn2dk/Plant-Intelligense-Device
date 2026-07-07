# MVP Specification

## Version 0.1

The first MVP must prove that one engineering PDF can become structured data.

## Scope

Included:

- Upload one P&ID PDF.
- Classify pages.
- Detect legend pages.
- Extract text tags from embedded PDF text.
- Create placeholder graph.
- Expose API endpoints.
- Prepare SQL schema.

Excluded for now:

- User login.
- Production OCR.
- Full OpenAI Vision integration.
- Full symbol detection.
- Full isolation calculations.
- CMMS integration.

## Acceptance criteria

- Backend starts with `uvicorn app.main:app --reload`.
- `/api/documents/analyze` accepts a PDF.
- API returns page classifications.
- API returns detected tags.
- `/api/graph/demo` returns nodes and edges.
- `/api/isolation/demo/P-101A` returns a human-verification isolation proposal.

