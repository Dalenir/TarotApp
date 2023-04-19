import os

import pandas as pd
import motor.motor_asyncio
from pymongo.errors import BulkWriteError


async def make_update_static_data():
    client = motor.motor_asyncio.AsyncIOMotorClient(host=os.getenv('MONGO_HOST'),
                                                    port=27001,
                                                    username=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
                                                    password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'))
    client.drop_database('static')

    cards = pd.read_csv('./assets/cards.csv')\
            .set_index('id')\
            .to_dict('index')
    card_list = [dict(**cards[card], _id=card) for card in cards]
    cards_collection: motor.motor_asyncio.AsyncIOMotorCollection = client.static.cards
    try:
        await cards_collection.insert_many(card_list)
    except BulkWriteError:
        print('base is full, dummy')

