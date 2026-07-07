# Backend

Run locally:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open API docs:

http://127.0.0.1:8000/docs
