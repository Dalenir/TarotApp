from enum import Enum

from pydantic import BaseModel

from game.models.card_model import CardModel


class FieldModel(BaseModel):
    number: int
    name: str = 'Generic name'
    description: str = 'Generic description'
    card: CardModel | None = None
