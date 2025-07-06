import requests
import pdfplumber
from io import BytesIO
from docx import Document
from urllib.parse import urlparse

def parse_file(file_url: str) -> str:
    resp = requests.get(file_url)
    data = resp.content
    # Use urlparse to get the path and check extension
    path = urlparse(file_url).path
    if path.endswith('.pdf'):
        return _parse_pdf(data)
    elif path.endswith('.docx'):
        return _parse_docx(data)
    else:
        raise ValueError("Unsupported file type")


def _parse_pdf(data: bytes) -> str:
    text = []
    with pdfplumber.open(BytesIO(data)) as pdf:
        for p in pdf.pages:
            text.append(p.extract_text() or "")
    return "\n".join(text)


def _parse_docx(data: bytes) -> str:
    doc = Document(BytesIO(data))
    return "\n".join([para.text for para in doc.paragraphs])