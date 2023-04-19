from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from database.UserBase import UserBase
from security import UserManager
from security.UserManager import get_current_user
from security.jwt_home_brew import JWTBrew, get_jwt_brew
from settings import Settings, get_settings
from schemas.user import User, MongoUser

router = APIRouter()


@router.post("/auth_token", response_model=str)
async def login_for_access_token(jwt_manager: JWTBrew = Depends(get_jwt_brew),
                                 form_data: OAuth2PasswordRequestForm = Depends(),
                                 settings: Settings = Depends(get_settings),
                                 database: UserBase = Depends(UserBase)):
    user: MongoUser = await UserManager.authenticate(
        username=form_data.username,
        password=form_data.password,
        database=database
    )
    if not user:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
    else:
        access_token = jwt_manager.create_access_token(username=user.username,
                                                       expires_delta=timedelta(minutes=settings.JWT_EXPIRATION_TIME),
                                                       settings=settings
                                                       )
        jwt_manager.secure_token('bearer ' + access_token)
        return 'Sucsessfully authenticated!'


@router.post("/protected_endpoint/")
async def card_test(csrf_token: Annotated[str, Form()], user: User = Depends(get_current_user, use_cache=False)):
    return {"message": user}
