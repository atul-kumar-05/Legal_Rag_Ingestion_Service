from fastapi import APIRouter
from schemas.upload import PresignedUrlRequest, PresignedUrlResponse
from services.upload_service 

router = APIRouter()


@router.post("/uploads/presigned", response_model=PresignedUrlResponse)
async def get_presigned_url(request: PresignedUrlRequest):
    
