from motor.motor_asyncio import AsyncIOMotorCollection

from database.MongoDB.basic_mongo import Mongo
from schemas.user import MongoUser


class UserBase:
    collection: AsyncIOMotorCollection = Mongo().users_collection

    async def set_user(self, user: MongoUser):
        return (await self.collection.insert_one(user.dict())).inserted_id

    async def get_user(self, username: str):
        user_dict = await self.collection.find_one({"username": username})
        if user_dict:
            return MongoUser(**user_dict)

    async def update_user(self, user: MongoUser):
        return await self.collection.update_one({"username": user.username}, {"$set": user.dict()})

    async def delete_user(self, username: str):
        return await self.collection.delete_one({"username": username})
