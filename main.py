from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Transaction Reconciliation API",
    description="Multi-agent system for reconciling transaction data from CSV and TXT files",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")

