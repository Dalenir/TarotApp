from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pydantic import BaseModel


class StaticMongoCollection(ABC):
    name: str

    @abstractmethod
    async def refill_from_csv(self, db_connection: AsyncIOMotorDatabase):
        pass


class StaticMongoDatabase(BaseModel):
    name: str
    collections: set[StaticMongoCollection]

    def __init__(self, name: str, collections: set[StaticMongoCollection]):
        super().__init__(name=name, collections=collections)


    async def refill(self, client: AsyncIOMotorClient):
        db_connection = client[self.name]
        for collection in self.collections:
            await collection.refill_from_csv(db_connection)

    class Config:
        arbitrary_types_allowed = True


# TODO: Maybe it's a good idea to merge collection classes into one class with generic refill_from_csv method.
 # + I do not think now that static data csv will be that different.
 # + Less clutter.
 # - refill_from_csv will will require more args and will be more complicated to understand what's going on.


class StaticCards(StaticMongoCollection):
    name = 'cards'

    async def refill_from_csv(self, db_connection: AsyncIOMotorDatabase):
        cards = pd.read_csv('./assets/cards.csv') \
            .set_index('id') \
            .to_dict('index')
        ready_data = [dict(**cards[card], _id=card) for card in cards]
        await db_connection[self.name].insert_many(ready_data)


class StaticFields(StaticMongoCollection):
    name = 'fields'

    async def refill_from_csv(self, db_connection: AsyncIOMotorDatabase):
        fields = pd.read_csv('./assets/fields.csv') \
            .set_index('id') \
            .to_dict('index')
        ready_data = [dict(**fields[field], _id=field) for field in fields]
        await db_connection[self.name].insert_many(ready_data)
