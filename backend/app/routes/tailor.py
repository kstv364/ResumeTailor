from fastapi import APIRouter, HTTPException
from app.models import TailorRequest, TailorResponse
from app.services import embedder, llm_client, versioning
import re

router = APIRouter()

import re

def improved_clean_latex_response(response: str) -> str:
    """
    Cleans and fixes LLM LaTeX response:
    - Removes escaped newlines
    - Converts '*' bullets to '\item'
    - Wraps '\item' lines correctly inside 'itemize' environments
    - Cleans redundant spaces
    - Removes Markdown fences if present
    """
    # Step 1: Clean Markdown fences if any
    response = re.sub(r"^```latex", "", response)
    response = re.sub(r"```$", "", response)
    response = response.strip()

    # Step 2: Replace escaped newlines with actual newlines
    response = response.replace('\\n', '\n')

    # Step 3: Convert '*' bullets to '\item'
    response = re.sub(r'^\s*\*\s+', r'\\item ', response, flags=re.MULTILINE)

    # Step 4: Wrap all \item sequences inside itemize environments
    def wrap_items(match):
        block = match.group(0)
        return '\\begin{itemize}\n' + block + '\n\\end{itemize}'

    # This finds blocks of consecutive \item lines and wraps them
    response = re.sub(r'(?:\\item .+\n)+', wrap_items, response)

    # Step 5: Clean extra spaces
    response = re.sub(r' +', ' ', response)

    # Step 6: Validate start and end
    if not response.startswith(r'\documentclass'):
        raise ValueError("The LaTeX document must start with \\documentclass.")
    if not response.endswith(r'\end{document}'):
        raise ValueError("The LaTeX document must end with \\end{document}.")

    return response


@router.post("/", response_model=TailorResponse)
async def tailor_resume(body: TailorRequest):
    try:
        # fetch latest resume text
        resume_text = embedder.fetch_resume(body.resume_id)
        # write the resume text to a .md file for debugging
      
        # generate updated LaTeX based on previous template and new JD
        llm_response = await llm_client.generate_latex_resume(resume_text, body.job_description)
        with open("debug_resume.md", "w") as f:
            f.write(llm_response)
        # create new version linked to this JD
        updated_latex = improved_clean_latex_response(llm_response)
        version_id = versioning.create_version(body.resume_id, updated_latex, job_desc_id=body.job_description)
        metadata = versioning.get_metadata(body.resume_id, version_id)
        return TailorResponse(
            version_id=version_id,
            llm_response=llm_response,
            latex_resume=updated_latex,
            metadata=metadata
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))