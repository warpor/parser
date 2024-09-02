from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorCollection
from pydantic import AnyHttpUrl

from app.repositories.pages.pages_protocol import PagesRepositoryProtocol
from app.schemas.pages_schemas import PageInfoGet


class PagesRepositoryMongodb(PagesRepositoryProtocol):

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def get_pages(self, url: str | None = None,
                        title: str | None = None) -> list[PageInfoGet]:
        try:
            query = {}
            if url:
                query["url"] = {"$regex": f".*{url}.*", "$options": "i"}
            if title:
                query["title"] = {"$regex": f".*{title}.*", "$options": "i"}
            cursor = self.collection.find(query)

            pages = []
            async for page in cursor:
                pages.append(PageInfoGet(url=page["url"], title=page["title"]))

            return pages
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving pages: {e}")

    async def get_page_html(self, url: AnyHttpUrl) -> str | None:
        try:
            document = await self.collection.find_one({"url": str(url)})
            return document.get("html", None)
        except Exception as e:
            raise HTTPException(status_code=500,
                                detail=f"Error retrieving page HTML content: {e}")
