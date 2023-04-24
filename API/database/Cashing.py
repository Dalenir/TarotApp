from settings import get_settings, Settings
import redis.asyncio as redis

class RedCache:

    def __init__(self, main_key: str, settings: Settings = get_settings()):
        self.main_key = main_key
        self.redis = redis.Redis(host='TarotRedis',
                                 port=settings.REDIS_PORT,
                                 db=settings.cache_database,
                                 password=settings.REDIS_PASS,
                                 decode_responses=True)
        
    async def get(self, key: str) -> str:
        return await self.redis.get(f'{self.main_key}:{key}')

    async def set(self, key: str, value: str, expire: int = 300):
        await self.redis.set(f'{self.main_key}:{key}', value, ex=expire)

    async def delete(self, key: str):
        await self.redis.delete(f'{self.main_key}:{key}')