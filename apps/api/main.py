from fastapi import FastAPI
from apps.api.routers import health, documents, ingestion

app = FastAPI(
    title="Legal RAG Ingestion Service",
    description="API for ingesting, processing, and indexing legal documents.",
    version="1.0.0",
)

app.include_router(health.router, prefix="/api/v1/health",tags=["Health"])
app.include_router(documents.router, prefix="/api/v1/documents",tags=["Documents"])
app.include_router(ingestion.router, prefix="/api/v1/ingestion",tags=["Ingestion"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Legal RAG Ingestion Service API",
        "docs_url": "/docs"
    }
