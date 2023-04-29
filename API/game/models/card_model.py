from enum import Enum

from pydantic import BaseModel

from game.models.stats_model import StatsModel
from game.models.suit_model import SuitModel


class CardState(Enum):
    up = True
    reversed = False


class CardModel(BaseModel):
    id: int
    value: int
    name: str
    suit: SuitModel
    state: CardState
    stats: StatsModel
    description: str
