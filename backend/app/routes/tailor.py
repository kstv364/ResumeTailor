from fastapi import APIRouter, HTTPException
from app.models import TailorRequest, TailorResponse
from app.services import embedder, llm_client, versioning
import re

router = APIRouter()

import re

def perfect_clean_latex_response(raw_response: str) -> str:
    """
    Post-processes the LLM LaTeX response:
    - Removes markdown code fences
    - Fixes escaped newlines
    - Converts '*' bullets to '\item'
    - Wraps orphaned bullet points in itemize environments
    - Leaves existing itemize blocks untouched
    - Returns valid LaTeX ready for Overleaf
    """
    # Step 1: Remove markdown fences
    latex_code = raw_response.strip()
    latex_code = re.sub(r"^```latex", "", latex_code)
    latex_code = re.sub(r"```$", "", latex_code)
    latex_code = latex_code.strip()

    # Step 2: Replace all \n with actual newlines
    latex_code = latex_code.replace('\\n', '\n')

    # Step 3: Replace markdown-style bullets '*' with '\item '
    latex_code = re.sub(r'^\s*\*\s+', r'\\item ', latex_code, flags=re.MULTILINE)

    # Step 4: Find and wrap consecutive orphan \item blocks inside itemize environments
    def wrap_items(match):
        items_block = match.group(0)
        return '\\begin{itemize}\n' + items_block.strip() + '\n\\end{itemize}'

    # Match any sequence of consecutive \item lines (allowing blank lines in between)
    latex_code = re.sub(r'(?:\\item .+\n)+', wrap_items, latex_code)

    # Step 5: Clean double spaces
    latex_code = re.sub(r' +', ' ', latex_code)

    # Step 6: Validate document structure
    if not latex_code.startswith(r'\documentclass'):
        raise ValueError("The document does not start with \\documentclass.")
    if not latex_code.endswith(r'\end{document}'):
        raise ValueError("The document does not end with \\end{document}.")

    return latex_code


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
        updated_latex = perfect_clean_latex_response(llm_response)
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