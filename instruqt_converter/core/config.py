import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Configuration Options - Load Environment Variables
    INSTRUQT_API_URL: Optional[str] = os.environ.get("INSTRUQT_API_URL")
    INSTRUQT_API_KEY: Optional[str] = os.environ.get("INSTRUQT_API_KEY")
    INSTRUQT_ORG_SLUG: Optional[str] = os.environ.get("INSTRUQT_ORG_SLUG")


config = Settings()
