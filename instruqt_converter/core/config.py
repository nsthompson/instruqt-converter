import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Configuration Options - Load Environment Variables
    INSTRUQT_API_URL: str = os.environ.get("INSTRUQT_API_URL")
    INSTRUQT_API_KEY: str = os.environ.get("INSTRUQT_API_KEY")
    INSTRUQT_ORG_SLUG: str = os.environ.get("INSTRUQT_ORG_SLUG")


config = Settings()
