import os
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # API
    API_V1_STR: str = "/api/v1"
    
    # Project metadata
    PROJECT_NAME: str = "Svelte + FastAPI Template"
    PROJECT_DESCRIPTION: str = "A modern web application template with Svelte, FastAPI, and Tailwind"
    VERSION: str = "0.1.0"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",  # Svelte dev server
        "http://localhost:3000",
        "http://localhost",
    ]


# Create global settings object
settings = Settings() 