from abc import ABC, abstractmethod

from app.schemas.pages_schemas import PageToDb


class PagesRepositoryProtocol(ABC):

    @abstractmethod
    async def insert_pages(self, pages: set[PageToDb]) -> None:
        pass
