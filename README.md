# Legal RAG Ingestion Service

## Directory Structure

```
├── alembic/
├── apps/
│   ├── api/
│   │   ├── dependencies.py
│   │   ├── main.py                  # FastAPI entry point
│   │   ├── middleware/
│   │   └── routers/
│   │       ├── documents.py         # Upload API
│   │       ├── health.py
│   │       └── ingestion.py
│   └── worker/
│       └── main.py                  # Worker entry point
├── core/
├── docker/
├── infra/
├── ingestion/
│   ├── chunking/
│   ├── deduplication/
│   ├── embeddings/
│   ├── normalization/
│   ├── parsers/
│   ├── persistence/
│   ├── sources/
│   ├── structure/
│   └── validation/
├── schemas/
├── storage/
│   ├── object_store/
│   ├── postgres/
│   └── qdrant/
└── tests/
```

## How to Run the Project

Since the project uses `uv` for fast package and virtual environment management:

### 1. Activate the Virtual Environment

In your PowerShell terminal, activate the environment:
```powershell
.venv\Scripts\Activate.ps1
```
*(Note: If you run into Execution Policy restrictions in PowerShell, you can run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first, or run `.venv\Scripts\activate.bat` in Command Prompt.)*

### 2. Install Dependencies

If you need to install additional dependencies in the future:
```bash
uv pip install -r requirements.txt
```

### 3. Run the API Server

Start the FastAPI development server using `uvicorn`:
```bash
uvicorn apps.api.main:app --reload
```

Once running:
- **API Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Health Check**: [http://127.0.0.1:8000/api/v1/health/health](http://127.0.0.1:8000/api/v1/health/health)
- **Upload Endpoint**: [http://127.0.0.1:8000/api/v1/documents/upload](http://127.0.0.1:8000/api/v1/documents/upload)

