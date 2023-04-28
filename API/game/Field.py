from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from database.Mongo import Mongo
from game.models.field_model import FieldModel


class Field(FieldModel):

    # TODO: Here is good example why I need separate classes for collections with easy access

    async def base_fill(self, mongo_client: Mongo = Mongo()):
        field_collection = mongo_client.fields_collection
        field_data = (await field_collection.aggregate(pipeline=[
                        {"$match": {"_id": 3}},
                        {"$project": {
                            'description': "$meaning",
                            'name': '$name'
                            }
                            }
                        ]).to_list(length=None))[0]
        self.description = field_data['description']
        self.name = field_data['name']
        return self