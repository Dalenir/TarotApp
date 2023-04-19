from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PORT: int
    DOCKER: bool
    DEBUG_MODE: bool
    UPDATE_STATIC: bool
    MONGO_HOST: str
    MONGO_PORT: int = 27001
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str


@lru_cache()
def get_settings():
    return Settings()


main_settings = get_settings()
