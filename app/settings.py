import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """App settings which used across the app."""

    title: str = "My API Docs"
    contact: dict = {
        "name": "example.com",
        "url": "https://example.com",
        "email": "hello@example.com",
    }
    description: str = "🚀 A clean, scalable FastAPI starter template to kickstart your next backend project.  🔧 Includes modular structure, environment configs, and production-ready setup."
    version: str = "1.0.0"
    openapi_tags: list[dict] = [
        {
            "name": "default",
            "description": "⚙️ General purpose endpoints used for health checks ✅, system info ℹ️, or default routing 📡.",
        },
        # add more tags as needed
    ]

    cors_origins: list[str] = ["*"]
    env: str = os.getenv("ENV", "local")  # "local" | "dev" | "stg" | "prd"
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", 8000))
    debug: bool = True if env == "local" else False


settings = Settings()
