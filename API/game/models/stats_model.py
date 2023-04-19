from pydantic import BaseModel


class StatsModel(BaseModel):
    good: int
    luck: int
    order: int
    wild: bool
