import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING

from config import settings


async def create_initial_migration():
    client = AsyncIOMotorClient(settings.get_database_url())
    db = client[settings.DB_NAME]
    collection = db[settings.DB_COLLECTION]

    await collection.create_index([('url', ASCENDING)], unique=True)


if __name__ == '__main__':
    asyncio.run(create_initial_migration())
