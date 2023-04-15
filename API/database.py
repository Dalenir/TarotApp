import motor.motor_asyncio

from settings import main_settings


class Mongo:
    mongo_client = motor.motor_asyncio.AsyncIOMotorClient(host=main_settings.MONGO_HOST,
                                                          port=main_settings.MONGO_PORT,
                                                          username=main_settings.MONGO_INITDB_ROOT_USERNAME,
                                                          password=main_settings.MONGO_INITDB_ROOT_PASSWORD)
    cards_collection = mongo_client.static.cards
