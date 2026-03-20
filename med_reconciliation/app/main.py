from fastapi import FastAPI
from app.routes.ingestion import router as ingest_router
from app.routes.reports import router as report_router

app = FastAPI()

app.include_router(ingest_router)
app.include_router(report_router)