from enum import Enum

from pydantic import BaseModel


class Suits(Enum):
    major = "Major Arcana"
    swords = 'Swords'
    wands = 'Wands'
    cups = 'Cups'
    pentacles = 'Pentacles'


class SuitModel(BaseModel):
    name: Suits
    description = "There is no description today, lad"

