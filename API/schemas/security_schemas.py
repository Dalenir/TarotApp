from datetime import timedelta
from enum import Enum

from pydantic import BaseModel


class TokenType(Enum):
    access = "access"
    refresh = "refresh"


class TokenPayload(BaseModel):
    type: TokenType = None  # type of the token
    sub: str = None  # subject
    exp: int = None  # expiration
    fresh: bool = None  # is the token fresh?
    scopes: list[str] = None  # scopes of the token

    class Config:
        use_enum_values = True