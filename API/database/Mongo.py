import asyncio

import motor.motor_asyncio as motor
import pandas as pd
from pymongo.errors import BulkWriteError

from settings import main_settings, Settings


class Mongo:
    mongo_client: motor.AsyncIOMotorClient
    cards_collection = motor.AsyncIOMotorCollection
    users_collection = motor.AsyncIOMotorCollection

    def __init__(self):
        self.mongo_client = motor.AsyncIOMotorClient(host=main_settings.MONGO_HOST,
                                                     port=main_settings.MONGO_PORT,
                                                     username=main_settings.MONGO_INITDB_ROOT_USERNAME,
                                                     password=main_settings.MONGO_INITDB_ROOT_PASSWORD)
        self.cards_collection = self.mongo_client.static.cards
        self.users_collection = self.mongo_client.user_data.users


    async def database_setup(self, settings: Settings):
        await self.users_collection.create_index('username', unique=True)
        update_static_data = settings.UPDATE_STATIC

        if update_static_data:
            await self.make_update_static_data()


    async def make_update_static_data(self):
        self.mongo_client.drop_database('static')

        cards = pd.read_csv('./assets/cards.csv') \
            .set_index('id') \
            .to_dict('index')
        card_list = [dict(**cards[card], _id=card) for card in cards]
        cards_collection = self.cards_collection
        try:
            await cards_collection.insert_many(card_list)
        except BulkWriteError:
            print('base is full, dummy')
