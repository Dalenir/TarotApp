from enum import Enum

from pydantic import BaseModel


class TokenLocation(Enum):
    COOKIES = 'cookies'
    HEADER = 'header'
    QUERY = 'query'


class CookieSameSite(Enum):
    LAX = 'lax'
    STRICT = 'strict'
    NONE = 'none'


class JWTBrewSettings(BaseModel):

    access_cookie_name = 'access_token'
    refresh_cookie_name = 'refresh_token'
    csrf_cookie_name = 'csrf_token'
    csrf_form_name = 'csrf_token'
    csrf_header_name: str = 'X-CSRFToken'
    token_location: set[TokenLocation]
    secure_cookies: bool = False
    cookie_csrf_protect: bool = True
    cookie_samesite: CookieSameSite
