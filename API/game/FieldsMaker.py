from motor.motor_asyncio import AsyncIOMotorCollection

from database.MongoDB.basic_mongo import Mongo
from game.models.card_model import CardModel
from game.models.field_model import FieldModel


# Seems logic to inherit it from same parent class as CardMaker, but maybe I will remake it to bulk Fields creation
# because fields are needed only in bulk.


class FieldsMaker:
    collection: AsyncIOMotorCollection

    def __init__(self, collection: AsyncIOMotorCollection = Mongo().fields_collection):
        self.collection = collection

    async def get_field(self, field_number: int, card: CardModel):
        field_data = (await self.collection.aggregate(pipeline=[
            {"$match": {"_id": field_number}},
            {"$project": {
                'description': "$meaning",
                'name': '$name'
            }
            }
        ]).to_list(length=None))[0]
        return FieldModel(name=field_data['name'],
                          description=field_data['description'],
                          number=field_number,
                          card=card)
