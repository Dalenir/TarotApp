import uuid
from datetime import timedelta, datetime
from functools import lru_cache

from jose import jwt
from fastapi import Request, Depends
from fastapi import Response

from schemas.security_schemas import TokenPayload, TokenType
from schemas.user import User
from security.tokens.jwt_config_shema import TokenLocation, CookieSameSite, JWTBrewSettings
from security.tokens.jwt_configs import jwt_cookie_csrf
from settings import Settings, get_settings, main_settings


class JWTBrew:

    def __init__(self, settings: JWTBrewSettings, req: Request = None, res: Response = None):
        self.settings = settings
        self._request = req
        self._response = res

    def secure_token(self, token: str):
        if TokenLocation.COOKIES in self.settings.token_location:
                self._response.set_cookie(
                    key=self.settings.access_cookie_name,
                    value=token,
                    max_age=50,
                    httponly=True,
                    secure=self.settings.secure_cookies,
                    samesite=self.settings.cookie_samesite.value
                )
                if self.settings.cookie_csrf_protect:
                    self._response.set_cookie(
                        key=self.settings.csrf_cookie_name,
                        value=JWTBrew.create_csrf_token(),
                        max_age=50,
                        httponly=False,
                        secure=self.settings.secure_cookies,
                        samesite=self.settings.cookie_samesite.value
                    )
        elif TokenLocation.HEADER in self.settings.token_location:
            self._request.headers = {self.settings.access_cookie_name: token}
        elif TokenLocation.QUERY in self.settings.token_location:
            self._request.query_params = {self.settings.access_cookie_name: token}



    @staticmethod
    def create_csrf_token():
        return uuid.uuid4().hex


    @staticmethod
    def create_access_token(user: User,
                              expires_delta: timedelta = None,
                              token_type: TokenType = TokenType.access,
                              settings: Settings = get_settings()):
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_TIME)
        token = TokenPayload(exp=int(expire.timestamp()), sub=user.username, type=token_type, payer=user.is_payer)
        encoded_jwt = jwt.encode(token.dict(), settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str, settings: Settings = get_settings()):
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])


@lru_cache()
def get_jwt_brew(req: Request = None, res: Response = None):
    return JWTBrew(
        jwt_cookie_csrf,
        req=req,
        res=res
    )
