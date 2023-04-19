from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from starlette import status

import settings
from database.UserBase import UserBase
from security.bearer_cookie import oauth2_scheme
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
        print(e)
        raise credentials_exception
    return payload