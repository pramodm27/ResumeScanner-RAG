from fastapi import FastAPI, UploadFile, File
from backend.services.resume_parser import extract_text
from backend.embeddings.embedder import generate_embedding
from backend.vector_db.faiss_store import store_vector
from backend.rag.matcher import match_resume

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Scanner RAG API Running"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    text = await extract_text(file)
    embedding = generate_embedding(text)
    store_vector(embedding)
    result = match_resume(text)

    return {
        "filename": file.filename,
        "match_result": result
    }