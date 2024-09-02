from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from app.core.config import settings


class DataBase:
    def __init__(self, database_url: str, database_name: str,
                 database_collection: str) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(database_url)
        self.collection: AsyncIOMotorCollection \
            = self.client[database_name][database_collection]

    def get_database_collection(self) -> AsyncIOMotorCollection:
        return self.collection

    def close_connection(self) -> None:
        self.client.close()


mongo_db = DataBase(settings.get_database_url(),
                    settings.DB_NAME, settings.DB_COLLECTION)
