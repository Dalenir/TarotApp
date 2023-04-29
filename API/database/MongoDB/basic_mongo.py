from motor import motor_asyncio as motor

from settings import main_settings


# I really don't like this approach, but I need base to run in separate loop before main one, so I have a little
# choices here. If you have better idea, please let me know. All other solutions seeems overcomplicated.
# TODO: Maybe move maintainers to separate script?

class Mongo:
    def __init__(self):
        self.client = motor.AsyncIOMotorClient(host=main_settings.MONGO_HOST,
                                               port=main_settings.MONGO_PORT,
                                               username=main_settings.MONGO_INITDB_ROOT_USERNAME,
                                               password=main_settings.MONGO_INITDB_ROOT_PASSWORD)

        self.cards_collection: motor.AsyncIOMotorCollection = self.client.static.cards
        self.fields_collection: motor.AsyncIOMotorCollection = self.client.static.fields
        self.users_collection: motor.AsyncIOMotorCollection = self.client.user_data.users
