from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health_check():
    """
    Health check endpoint.
    Returns status information about the API.
    """
    return {
        "status": "ok",
        "message": "API is running"
    } 