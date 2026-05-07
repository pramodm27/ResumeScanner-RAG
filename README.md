# AI Resume Scanner using RAG

## Run Backend

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## Run Docker

```bash
docker-compose up --build
```

## API

POST /upload-resume

Upload PDF resumes and receive AI matching score.