from fastapi import APIRouter, UploadFile, File

from app.engines.document_engine.service import DocumentEngine
from app.engines.graph_engine.service import GraphEngine
from app.engines.isolation_engine.service import IsolationEngine

router = APIRouter()

@router.post("/documents/analyze")
async def analyze_document(file: UploadFile = File(...)):
    content = await file.read()
    result = DocumentEngine().analyze_pdf(filename=file.filename, content=content)
    return result

@router.get("/graph/demo")
def demo_graph():
    return GraphEngine().build_demo_graph()

@router.post("/isolation/demo/{component_tag}")
def demo_isolation(component_tag: str):
    graph = GraphEngine().build_demo_graph()
    return IsolationEngine().generate_demo_isolation(graph=graph, component_tag=component_tag)
