from pydantic import BaseModel, Field
from typing import List, Optional
import uuid

class UploadRequest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="UUID for the resume")
    file_url: str  # S3 or MinIO PDF/DOCX URL

class TailorRequest(BaseModel):
    resume_id: str  # Should be a UUID string
    job_description: str

class TailorResponse(BaseModel):
    version_id: str
    llm_response: str
    latex_resume: str
    metadata: dict