from fastapi import Depends

from app.dependencies.repositories_dependencies import get_pages_repository
from app.repositories.pages_protocol import PagesRepositoryProtocol
from app.schemas.pages_schemas import PageToDb


class PagesService:
    pages_repository: PagesRepositoryProtocol

    def __init__(self,
                 pages_repository: PagesRepositoryProtocol
                 = Depends(get_pages_repository)) -> None:
        self.pages_repository = pages_repository

    async def insert_pages(self, pages: set[PageToDb]) -> None:
        if pages:
            await self.pages_repository.insert_pages(pages)
