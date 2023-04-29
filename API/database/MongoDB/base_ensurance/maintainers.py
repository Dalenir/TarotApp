import pandas as pd
from motor.motor_asyncio import AsyncIOMotorCollection
from pydantic import BaseModel

from database.MongoDB.basic_mongo import Mongo


# I created a different maintainers for each collection because I want to be flexible in refill methods


class Index(BaseModel):
    name: str
    unique: bool


class IndexMaintainer:
    collection: AsyncIOMotorCollection
    indexes: list[Index]

    async def ensure_indexes(self):
        for index in self.indexes:
            await self.collection.create_index(index.name, unique=index.unique)


class StaticMaintainer:
    collection: AsyncIOMotorCollection

    async def refill(self):
        raise NotImplementedError("You must inherit this class and implement this method")


class CardsMaintainer(StaticMaintainer, IndexMaintainer):
    collection = Mongo().cards_collection
    indexes = [
        Index(name="Name", unique=True),
    ]

    async def refill(self):
        await self.collection.database.drop_collection(self.collection.name)
        cards = pd.read_csv('./assets/cards.csv') \
            .set_index('id') \
            .to_dict('index')
        ready_data = [dict(**cards[card], _id=card) for card in cards]
        await self.collection.insert_many(ready_data)


class FieldMaintainer(StaticMaintainer):
    collection = Mongo().fields_collection

    async def refill(self):
        await self.collection.database.drop_collection(self.collection.name)
        fields = pd.read_csv('./assets/fields.csv') \
            .set_index('id') \
            .to_dict('index')
        ready_data = [dict(**fields[field], _id=field) for field in fields]
        await self.collection.insert_many(ready_data)


class UserMaintainer(IndexMaintainer):
    collection = Mongo().users_collection

    indexes = [
        Index(name="email", unique=True),
        Index(name="username", unique=True),
    ]
