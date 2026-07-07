# MVP Specification

## Objective

Prove that the system can turn one P&ID PDF into structured engineering objects.

## Scope

Included:

- PDF upload
- Page classification
- Legend detection
- OCR extraction
- Tag extraction
- Component records
- Basic API

Excluded from MVP 0.1:

- authentication
- production database hosting
- full symbol computer vision
- approved isolation procedure generation
- SCADA or CMMS integration

## Acceptance criteria

- A PDF can be uploaded through the API.
- The document can be analysed through the API.
- The response returns page classifications.
- The response returns detected component-like tags.
- Each detected item has a component type, page number, source and confidence score.
