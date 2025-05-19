from fastapi import FastAPI
from app.routes import router as journal_router

app = FastAPI()

app.include_router(journal_router, prefix="/journals", tags=["journals"])
