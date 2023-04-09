from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PORT: int
    DOCKER: bool
    DEBUG_MODE: bool


@lru_cache()
def get_settings():
    return Settings()


main_settings = get_settings()
