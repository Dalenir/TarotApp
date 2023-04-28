import asyncio

import motor.motor_asyncio as motor
import pandas as pd
from pymongo.errors import BulkWriteError

from database.StaticMongo import StaticMongoDatabase
from settings import main_settings, Settings, static_mongo


#  TODO: Reimagine Mongo class and make an object for each collection



class Mongo:
    mongo_client: motor.AsyncIOMotorClient
    cards_collection = motor.AsyncIOMotorCollection
    users_collection = motor.AsyncIOMotorCollection
    fields_collection = motor.AsyncIOMotorCollection

    def __init__(self):
        self.mongo_client = motor.AsyncIOMotorClient(host=main_settings.MONGO_HOST,
                                                     port=main_settings.MONGO_PORT,
                                                     username=main_settings.MONGO_INITDB_ROOT_USERNAME,
                                                     password=main_settings.MONGO_INITDB_ROOT_PASSWORD)
        self.cards_collection = self.mongo_client.static.cards
        self.users_collection = self.mongo_client.user_data.users
        self.fields_collection = self.mongo_client.static.fields

class BaseStarter(Mongo):

    def __init__(self, static_db: StaticMongoDatabase = static_mongo,
):
        super().__init__()
        self.static_db = static_db


    async def database_setup(self, ensure_indexes: bool = False, refill_static_data: bool = False):
        if ensure_indexes:
            await self.ensure_indexes()
        if refill_static_data:
            await self.refill_static_data()



    async def ensure_indexes(self):
        await self.users_collection.create_index('username', unique=True)
        await self.users_collection.create_index('email', unique=True)
        await self.cards_collection.create_index('No', unique=False)


    async def refill_static_data(self):
        self.mongo_client.drop_database(self.static_db.name)
        await self.static_db.refill(self.mongo_client)
