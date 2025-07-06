from fastapi import APIRouter, HTTPException
from app.models import UploadRequest
from app.services import parser, embedder, versioning
from uuid import uuid4

router = APIRouter()

@router.post("/")
async def upload_document(body: UploadRequest):
    try:
        # generate id server-side
        resume_id = str(uuid4())
        # parse file
        text = parser.parse_file(body.file_url)
        # initial LaTeX resume generation
        latex = versioning.init_latex_template(text)
        # store text, embedding, and version metadata
        embedder.store_resume(resume_id, text)
        
        version_id = versioning.create_version(resume_id, latex, job_desc_id=None)
        return {"status": "uploaded", "resume_id": resume_id, "version_id": version_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))