from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from sentence_transformers import SentenceTransformer
from app.utils import VECTOR_DB_URL
import sqlite3

# Initialize DB and vector store
client = QdrantClient(url=VECTOR_DB_URL)
model = SentenceTransformer('all-MiniLM-L6-v2')
COLLECTION = 'resumes'
conn = sqlite3.connect('metadata.db', check_same_thread=False)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS resumes(id TEXT PRIMARY KEY, text TEXT)')
conn.commit()


def store_resume(resume_id: str, text: str):
    # store raw text
    cur.execute('INSERT OR REPLACE INTO resumes VALUES(?, ?)', (resume_id, text))
    conn.commit()
    # embed and store
    vec = model.encode(text).tolist()
    client.upsert(collection_name=COLLECTION, points=[PointStruct(id=resume_id, vector=vec, payload={'text': text})])


def fetch_resume(resume_id: str) -> str:
    cur.execute('SELECT text FROM resumes WHERE id=?', (resume_id,))
    row = cur.fetchone()
    return row[0] if row else ''