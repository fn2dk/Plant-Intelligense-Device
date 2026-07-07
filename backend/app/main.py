from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.documents import router as documents_router
from app.api.analysis import router as analysis_router

app = FastAPI(
    title="Engineering Intelligence Platform API",
    version="0.1.0",
    description="Backend foundation for Project Atlas.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(documents_router, prefix="/documents", tags=["documents"])
app.include_router(analysis_router, prefix="/analysis", tags=["analysis"])
