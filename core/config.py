import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Configuration Options
    INSTRUQT_API_URL: str = os.environ.get('INSTRUQT_API_URL')
    INSTRUQT_API_KEY: str = os.environ.get('INSTRUQT_API_KEY')
    INSTRUQT_ORG_SLUG: str = os.environ.get('INSTRUQT_ORG_SLUG')


config = Settings()
