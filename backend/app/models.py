from pydantic import BaseModel
from typing import List, Optional

class UploadRequest(BaseModel):
    id: str
    file_url: str  # S3 or MinIO PDF/DOCX URL

class TailorRequest(BaseModel):
    resume_id: str
    job_description: str

class TailorResponse(BaseModel):
    version_id: str
    latex_resume: str
    metadata: dict