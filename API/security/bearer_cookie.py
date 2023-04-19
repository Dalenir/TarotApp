# from fastapi.openapi.models import OAuth2
from fastapi import HTTPException
from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel, OAuthFlowPassword
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED
from typing import Dict

from security.jwt_home_brew import JWTBrew, get_jwt_brew
from security.tokens.jwt_config_shema import JWTBrewSettings


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
            self,
            tokenUrl: str,
            jwt_manager: JWTBrew,
            scheme_name: str = None,
            scopes: Dict[str, str] = None,
            auto_error: bool = True,
    ):
        self.jwt_manager: JWTBrew = jwt_manager
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password=OAuthFlowPassword(tokenUrl=tokenUrl, refreshUrl=None, scopes=scopes))
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request):
        authorization: str = request.cookies.get(self.jwt_manager.settings.access_cookie_name)
        csrf_cookie_token: str = request.cookies.get(self.jwt_manager.settings.csrf_cookie_name)
        form_data = await request.form()
        csrf_form_token: str = form_data.get(self.jwt_manager.settings.csrf_form_name)
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer" or csrf_cookie_token != csrf_form_token:
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="auth_token", jwt_manager=get_jwt_brew())
