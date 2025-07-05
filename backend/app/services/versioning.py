import sqlite3
import uuid
from datetime import datetime

# Table: versions(resume_id, version_id, job_desc_id, latex, timestamp)
conn = sqlite3.connect('metadata.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS versions(
    resume_id TEXT, version_id TEXT PRIMARY KEY,
    job_desc_id TEXT, latex TEXT, timestamp TEXT
)""")
conn.commit()

def init_latex_template(text: str) -> str:
    # basic LaTeX template
    header = r"""\\documentclass{article}
\\begin{document}
"""
    body = text.replace("\n", "\\\\\n")
    footer = r"""\\end{document}"""
    return f"{header}{body}{footer}"


def create_version(resume_id: str, latex: str, job_desc_id: str=None) -> str:
    version_id = str(uuid.uuid4())
    ts = datetime.utcnow().isoformat()
    cur.execute(
        'INSERT INTO versions VALUES(?, ?, ?, ?, ?)',
        (resume_id, version_id, job_desc_id, latex, ts)
    )
    conn.commit()
    return version_id


def get_metadata(resume_id: str, version_id: str) -> dict:
    cur.execute(
        'SELECT job_desc_id, timestamp FROM versions WHERE resume_id=? AND version_id=?',
        (resume_id, version_id)
    )
    row = cur.fetchone()
    return {"job_desc_id": row[0], "timestamp": row[1], "version_id": version_id} if row else {}