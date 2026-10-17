
from fastapi import APIRouter
router = APIRouter()
@router.get("/v1/health")
def health() -> dict[str, str]:
    return {"status": "Server is Running"}