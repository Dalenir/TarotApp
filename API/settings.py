from enum import Enum
from functools import lru_cache

from pydantic import BaseSettings


class AppMode(Enum):
    DEV = 'Development'
    PROD = 'Production'

class Settings(BaseSettings):
    API_PORT: int
    DOCKER: bool
    DEBUG_MODE: bool
    UPDATE_STATIC: bool
    MONGO_HOST: str
    MONGO_PORT: int = 27001
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    APP_MODE: AppMode
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION_TIME: int = 15
    REDIS_PORT: int
    REDIS_PASS: str
    cache_database: int = 0

    class Config:
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str):
            if field_name == 'APP_MODE':
                match raw_val:
                    case AppMode.DEV.value:
                        return AppMode.DEV
                    case AppMode.PROD.value:
                        return AppMode.PROD
            return cls.json_loads(raw_val)

@lru_cache()
def get_settings():
    return Settings()


main_settings = get_settings()
