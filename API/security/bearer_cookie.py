# from fastapi.openapi.models import OAuth2
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel, OAuthFlowPassword
from fastapi.security.utils import get_authorization_scheme_param
from starlette import status
from starlette.exceptions import WebSocketException
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED
from typing import Dict

from starlette.websockets import WebSocket

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
        if form_data:
            csrf_notcookie_token: str = form_data.get(self.jwt_manager.settings.csrf_form_name)
        else:
            headers = request.headers
            csrf_notcookie_token = headers.get(self.jwt_manager.settings.csrf_header_name)
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer" or csrf_cookie_token != csrf_notcookie_token:
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


def websocket_auth_test(websocket: WebSocket, jwt_brew: JWTBrew = Depends(get_jwt_brew)):
    authorization: str = websocket.cookies.get(jwt_brew.settings.access_cookie_name)
    csrf_cookie_token: str = websocket.cookies.get(jwt_brew.settings.csrf_cookie_name)
    csrf_notcookie_token = websocket.headers.get(jwt_brew.settings.csrf_header_name)
    scheme, param = get_authorization_scheme_param(authorization)
    if not authorization or scheme.lower() != "bearer" or csrf_cookie_token != csrf_notcookie_token:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    else:
        return param




oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="auth_token", jwt_manager=get_jwt_brew())
