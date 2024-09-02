from motor.motor_asyncio import AsyncIOMotorCollection

from app.repositories.pages_protocol import PagesRepositoryProtocol
from app.schemas.pages_schemas import PageToDb


class PagesRepositoryMongodb(PagesRepositoryProtocol):

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def insert_pages(self, pages: set[PageToDb]) -> None:
        try:
            await self.collection.insert_many(
                (page.dict() for page in pages), ordered=False)
        except Exception:
            pass
