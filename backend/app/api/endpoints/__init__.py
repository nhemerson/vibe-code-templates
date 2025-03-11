from fastapi import APIRouter

from app.api.endpoints import items, health

# Main API router
api_router = APIRouter()

# Include routers from endpoint modules
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(items.router, prefix="/items", tags=["items"]) 