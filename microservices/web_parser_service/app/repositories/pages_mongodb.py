from app.core.logger import logger
from app.repositories.pages_protocol import PagesRepositoryProtocol
from app.schemas.pages_schemas import PageToDb
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo.errors import BulkWriteError


class PagesRepositoryMongodb(PagesRepositoryProtocol):

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def insert_pages(self, pages: set[PageToDb]) -> None:
        try:
            await self.collection.insert_many(
                (page.dict() for page in pages), ordered=False)
        except BulkWriteError as e:
            write_errors: list = e.details.get("writeErrors", [])
            for write_error in write_errors:
                error: str = write_error.get("errmsg")
                logger.warning(f"Bulk write warn: {error}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
