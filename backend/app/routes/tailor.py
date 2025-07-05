from fastapi import APIRouter, HTTPException
from app.models import TailorRequest, TailorResponse
from app.services import embedder, llm_client, versioning

router = APIRouter()

@router.post("/", response_model=TailorResponse)
async def tailor_resume(body: TailorRequest):
    try:
        # fetch latest resume text
        resume_text = embedder.fetch_resume(body.resume_id)
        # generate updated LaTeX based on previous template and new JD
        updated_latex = await llm_client.generate_latex_resume(resume_text, body.job_description)
        # create new version linked to this JD
        version_id = versioning.create_version(body.resume_id, updated_latex, job_desc_id=body.job_description)
        metadata = versioning.get_metadata(body.resume_id, version_id)
        return TailorResponse(
            version_id=version_id,
            latex_resume=updated_latex,
            metadata=metadata
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))