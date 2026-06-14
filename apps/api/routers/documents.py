from fastapi import APIRouter, UploadFile, File, HTTPException, status

router = APIRouter()

@router.post("/upload", summary="Upload a document for ingestion")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a legal document (PDF, TXT, DOCX, etc.) to initiate the ingestion process.
    """
    # Placeholder validation
    allowed_extensions = {".pdf", ".txt", ".docx", ".doc"}
    import os
    _, ext = os.path.splitext(file.filename)
    if ext.lower() not in allowed_extensions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file format. Supported formats: {', '.join(allowed_extensions)}"
        )
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "received",
        "message": "File received successfully. Starting ingestion queue process."
    }
