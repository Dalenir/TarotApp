import copy
from enum import Enum

import roman
from pydantic import BaseModel

from game.models.stats_model import StatsModel
from game.models.suit_model import SuitModel, Suits


class CardState(Enum):
    up = True
    reversed = False


class CardModel(BaseModel):
    id: int
    value: int
    visual_value: str
    name: str
    suit: SuitModel
    state: CardState
    stats: StatsModel
    description: str
