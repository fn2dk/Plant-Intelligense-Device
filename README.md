# Plant Intelligense Device

Engineering Intelligence Platform.

## v0.3 upload-ready milestone

This version gives Anders a working local MVP where he can upload a PDF from the browser and receive a first structured analysis result.

## What works in v0.3

- FastAPI backend
- Browser upload UI
- PDF upload endpoint
- Local document storage
- Analysis endpoint
- Embedded PDF text extraction
- Page classification
- Legend page detection
- Engineering tag detection
- Basic analysis result display in the frontend

## Start backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## Start frontend

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

Upload a P&ID PDF from the web page.

## Important

This is still deterministic v0.3 logic. It does not yet render drawing images or detect symbol coordinates. That comes in v0.4.
