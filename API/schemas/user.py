from typing import Any

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    is_payer: bool = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs: Any) -> None:
        cls._id = kwargs.get("_id")
        cls.password_hash = kwargs.get("password_hash")


class MongoUser(User):
    _id: str | None = None
    password_hash: str  | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

