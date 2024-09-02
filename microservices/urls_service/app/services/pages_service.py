from app.repositories.pages.pages_protocol import PagesRepositoryProtocol
from app.schemas.pages_schemas import PageInfoGet
from fastapi import HTTPException
from pydantic import AnyHttpUrl


class PagesService:
    pages_repository: PagesRepositoryProtocol

    def __init__(self,
                 pages_repository: PagesRepositoryProtocol) -> None:
        self.pages_repository = pages_repository

    async def get_pages(self, url: str | None = None,
                        title: str | None = None) -> list[PageInfoGet]:
        return await self.pages_repository.get_pages(url, title)

    async def get_page_html(self, url: AnyHttpUrl) -> str:
        html = await self.pages_repository.get_page_html(url)

        if not html:
            raise HTTPException(status_code=404, detail="Page not found")

        return html
