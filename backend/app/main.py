from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.tailor import router as tailor_router

app = FastAPI(
    title="Resume Tailor API",
    version="0.1.0"
)

app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(tailor_router, prefix="/tailor", tags=["tailor"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}