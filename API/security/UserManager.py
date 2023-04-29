from fastapi import Depends, HTTPException
from jose import JWTError
from starlette import status
from starlette.websockets import WebSocket

from database.MongoDB.user_database import UserBase
from schemas.user import MongoUser
from security.bearer_cookie import oauth2_scheme, websocket_auth_test
from security.jwt_home_brew import JWTBrew, get_jwt_brew
from utilts import CryptoMan


async def authenticate(username: str, password: str, database: UserBase):
    user = await database.get_user(username)
    if not user:
        return
    if not CryptoMan.verify_password(password, user.password_hash):
        return
    return user


async def get_current_user(token: str = Depends(oauth2_scheme), jwt_manager: JWTBrew = Depends(get_jwt_brew)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt_manager.decode_access_token(token)

    except (JWTError, ValueError) as e:
        raise credentials_exception
    return payload


async def register_user(username: str, password: str, email: str, database: UserBase = UserBase):
    if await database.get_user(username):
        return False
    password_hash = CryptoMan.get_password_hash(password)
    await database.set_user(user=MongoUser(username=username,
                                           email=email,
                                           password_hash=password_hash))
    return True


async def get_current_user_websocket(websocket: WebSocket, token=Depends(websocket_auth_test)):
    return 'bah'
