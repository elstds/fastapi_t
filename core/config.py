from pydantic_settings import BaseSettings
from pathlib import Path

BASEDIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    db_url: str = f'sqlite+aiosqlite:///{BASEDIR}/app.db'
    db_echo: bool = True

settings = Settings()
