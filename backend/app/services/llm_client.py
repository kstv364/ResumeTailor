import httpx
from app.utils import OLLAMA_URL, OLLAMA_MODEL

async def generate_latex_resume(resume_text: str, job_desc: str) -> str:

    prompt = (
        "You are an AI assistant that updates and returns LaTeX resume template. "
        "Given the candidate's original resume and a job description, modify the LaTeX content to best match the JD. "
        "The Original Resume text can be LaTeX code or plain text, but the output returned must be the content to a valid latex file."
        "Don't return any invalid latex characters or escape sequences even if the input has them."
        "Preserve the format of the input resume, including sections, subsections, and itemize environments. All points should be in itemize blocks."
        "The output returned should be a valid LaTeX document that can be compiled without errors."
        f"\n################ Original Resume Text:\n{resume_text}\n########### Job Description:\n{job_desc}\n"
    )

    return await _call_ollama(prompt)

async def _call_ollama(prompt: str) -> str:
    # Ollama API expects a JSON payload similar to OpenAI chat
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(OLLAMA_URL, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        return data['response']