from fastapi import FastAPI
from app.schemas import UserRequest
from app.graph import run_graph

app = FastAPI(
    title="Warden Task Orchestrator",
    description="A LangGraph-based planning agent for routing tasks across Warden agents.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "Warden Task Orchestrator",
        "status": "running"
    }

@app.post("/analyze")
def analyze(request: UserRequest):
    return run_graph(request.query)
