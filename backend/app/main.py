from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload import router as upload_router
from app.routes.tailor import router as tailor_router

app = FastAPI(
    title="Resume Tailor API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # your Vite origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(tailor_router, prefix="/tailor", tags=["tailor"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}