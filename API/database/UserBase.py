from database.Mongo import Mongo
from schemas.user import User, MongoUser


class UserBase(Mongo):

    def __init__(self):
        super().__init__()

    async def set_user(self, user: MongoUser):
        return (await self.users_collection.insert_one(user.dict())).inserted_id

    async def get_user(self, username: str):
        user_dict = await self.users_collection.find_one({"username": username})
        if user_dict:
            return MongoUser(**user_dict)

    async def update_user(self, user: MongoUser):
        return await self.users_collection.update_one({"username": user.username}, {"$set": user.dict()})

    async def delete_user(self, username: str):
        return await self.users_collection.delete_one({"username": username})
