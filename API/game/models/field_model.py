from enum import Enum

from pydantic import BaseModel

from game.models.card_model import CardModel


class FieldModel(BaseModel):
    number: int
    description: str = 'There is no description here too, lad. Stop looking/'
    card: CardModel | None = None
