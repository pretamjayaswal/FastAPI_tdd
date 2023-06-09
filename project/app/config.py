
import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger('uvicorn')

class Settings(BaseSettings):
    environment: str = os.getenv('ENVIRONMENT','dev')
    testing: bool = os.getenv('TESTING', 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")

# lru cache to execute fet_settings only once
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from env....")
    return Settings()

