from contextlib import asynccontextmanager
from typing import AsyncGenerator

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from app.core.config import settings


class DataBase:
    database_url: str
    database_name: str
    database_collection: str
    client: AsyncIOMotorClient
    collection: AsyncIOMotorCollection

    def __init__(self, database_url: str,
                 database_name: str, database_collection: str) -> None:
        self.database_url = database_url
        self.database_name = database_name
        self.database_collection = database_collection
        self.client = AsyncIOMotorClient(self.database_url)
        self.collection = self.client[self.database_name][self.database_collection]

    @asynccontextmanager
    async def connect_to_database(self) -> AsyncGenerator:
        try:
            yield self.collection
        finally:
            if self.client is not None:
                self.client.close()

    def get_database_collection(self) -> AsyncIOMotorCollection:
        return self.collection


mongo_db = DataBase(settings.get_database_url(),
                    settings.DB_NAME, settings.DB_COLLECTION)
