# AI Resume Scanner using RAG and LLMs

An intelligent AI-powered Resume Screening and Candidate Matching System built using Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), Semantic Search, and Vector Databases.

This project automates resume analysis, candidate ranking, and job matching using modern Generative AI technologies instead of traditional keyword-based ATS systems.

---

# Project Overview

Traditional Applicant Tracking Systems (ATS) rely heavily on exact keyword matching, which often rejects highly qualified candidates due to wording differences.

This project solves that problem using:

- Retrieval-Augmented Generation (RAG)
- Semantic Similarity Search
- Vector Embeddings
- Large Language Models
- NLP-based Resume Parsing

The system intelligently understands resume content, extracts important candidate information, compares resumes with job descriptions semantically, and generates AI-powered recruiter feedback.

---

# Key Features

- Resume Upload and Parsing
- PDF Resume Text Extraction
- Semantic Candidate Matching
- AI-Powered Candidate Ranking
- Vector Database Integration
- Embedding Generation using Sentence Transformers
- RAG-Based Contextual Evaluation
- FastAPI REST APIs
- Dockerized Deployment
- Scalable Backend Architecture
- Recruiter-Friendly AI Feedback

---

# Problem Statement

Recruiters receive thousands of resumes for every job opening. Manual resume screening is:

- Time-consuming
- Error-prone
- Difficult to scale
- Dependent on keyword matching

Traditional ATS systems fail to understand contextual meaning.

Example:

Job Description:
"Looking for Python Backend Engineer with cloud deployment experience"

Resume:
"Built scalable APIs using FastAPI and deployed services on AWS"

Traditional ATS may reject this profile because exact keywords are missing.

This AI Resume Scanner uses semantic understanding to identify strong candidates intelligently.

---

# Architecture

```text
                +--------------------+
                |   Recruiter UI     |
                +----------+---------+
                           |
                           v
                +--------------------+
                |    FastAPI API     |
                +----------+---------+
                           |
        -----------------------------------------
        |                |                      |
        v                v                      v
+---------------+  +-------------+   +----------------+
| Resume Parser |  | Embeddings  |   | Job Processor  |
+---------------+  +-------------+   +----------------+
                           |
                           v
                +--------------------+
                | Vector Database    |
                |  FAISS / ChromaDB  |
                +----------+---------+
                           |
                           v
                +--------------------+
                |    RAG Pipeline    |
                +----------+---------+
                           |
                           v
                +--------------------+
                |      LLM Engine    |
                +----------+---------+
                           |
                           v
                +--------------------+
                | Candidate Ranking  |
                +--------------------+
```

---

# Tech Stack

## Backend

- Python
- FastAPI
- LangChain
- Sentence Transformers
- FAISS
- NumPy

## Frontend

- React.js
- Axios

## AI / NLP

- RAG (Retrieval-Augmented Generation)
- Semantic Search
- Vector Embeddings
- LLM Integration

## DevOps

- Docker
- Docker Compose

---

# Project Workflow

## Step 1 — Resume Upload

Recruiters upload candidate resumes in PDF format.

## Step 2 — Resume Parsing

The system extracts raw text using PDF parsers.

## Step 3 — Text Cleaning

Resume content is cleaned and normalized.

## Step 4 — Chunking

Large resume text is split into smaller chunks for efficient retrieval.

## Step 5 — Embedding Generation

Sentence Transformers convert resume text into vector embeddings.

## Step 6 — Vector Storage

Embeddings are stored in FAISS vector database.

## Step 7 — Job Description Processing

Job descriptions are embedded using the same embedding model.

## Step 8 — Semantic Search

The system retrieves semantically relevant resume chunks.

## Step 9 — RAG Evaluation

Relevant context is passed to the LLM for intelligent evaluation.

## Step 10 — Candidate Ranking

Candidates receive AI-generated scores and recommendations.

---

# Folder Structure

```text
resume-scanner-rag/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── rag/
│   ├── embeddings/
│   ├── vector_db/
│   └── models/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   └── services/
│
├── docker/
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/pramodm27/ResumeScanner-RAG.git

cd ResumeScanner-RAG
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\\Scripts\\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend will run at:

```text
http://localhost:8000
```

Swagger API Docs:

```text
http://localhost:8000/docs
```

---

# Docker Setup

## Build and Run Containers

```bash
docker-compose up --build
```

---

# API Endpoints

## Upload Resume

```http
POST /upload-resume
```

Uploads candidate resume and generates AI match result.

---

# Example API Response

```json
{
  "filename": "resume.pdf",
  "match_result": {
    "score": 75,
    "matched_skills": [
      "python",
      "fastapi",
      "docker"
    ]
  }
}
```

---

# Core AI Concepts Used

## Retrieval-Augmented Generation (RAG)

Retrieves relevant resume information before generating AI evaluation.

## Vector Embeddings

Converts text into numerical vectors representing semantic meaning.

## Semantic Search

Matches resumes based on contextual similarity instead of exact keywords.

## Large Language Models (LLMs)

Generates recruiter-friendly evaluations and recommendations.

---

# Real-World Challenges Solved

## Problem: Poor Keyword Matching

Solution:
Semantic similarity search using embeddings.

## Problem: Resume Formatting Issues

Solution:
Robust PDF parsing pipeline.

## Problem: Slow Search Performance

Solution:
FAISS vector indexing.

## Problem: AI Hallucination

Solution:
Context grounding using RAG.

---

# Future Enhancements

- Multi-language resume support
- AI interview question generation
- ATS integration
- LinkedIn profile analysis
- Resume improvement suggestions
- Cloud deployment on AWS/GCP
- Kubernetes orchestration
- Real-time recruiter dashboard

---

# Learning Outcomes

This project demonstrates:

- End-to-end RAG pipeline development
- Production-grade backend engineering
- FastAPI API development
- Vector database implementation
- Semantic search systems
- LLM application integration
- Docker deployment
- AI system architecture design

---

# Use Cases

- Recruitment Automation
- AI Hiring Platforms
- Talent Screening Systems
- HR Tech Solutions
- Smart ATS Platforms

---

# Why This Project is Valuable

This project combines:

- Generative AI
- NLP
- Backend Engineering
- Vector Databases
- Semantic Search
- LLM Orchestration

It demonstrates practical implementation of modern AI engineering concepts used in real-world intelligent systems.

---

# Author

Pramod Srinivas

GitHub:
https://github.com/pramodm27

---

# License

This project is licensed under the MIT License.
