import httpx
from app.utils import OLLAMA_URL, OLLAMA_MODEL

async def generate_latex_resume(resume_text: str, job_desc: str) -> str:
    prompt = (
        "You are an AI assistant that updates a LaTeX resume template. "
        "Given the candidate's original resume and a job description, modify the LaTeX content to best match the JD. The Resume text can be latexcode or plain text, but the output must be valid LaTeX code. "
        f"################Original Resume Text:\n{resume_text}\n###########Job Description:\n{job_desc}\n"
        "Return only the complete LaTeX code that can be direcgtly rendered."
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