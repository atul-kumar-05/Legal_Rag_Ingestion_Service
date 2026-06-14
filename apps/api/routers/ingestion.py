from fastapi import APIRouter

router = APIRouter()

@router.get("/status/{job_id}", summary="Get ingestion job status")
async def get_ingestion_status(job_id: str):
    return {
        "job_id": job_id,
        "status": "pending",
        "progress": 0.0
    }
