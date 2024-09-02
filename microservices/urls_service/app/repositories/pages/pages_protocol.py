from abc import ABC, abstractmethod

from app.schemas.pages_schemas import PageInfoGet
from pydantic import AnyHttpUrl


class PagesRepositoryProtocol(ABC):

    @abstractmethod
    async def get_pages(self, title: str | None = None,
                        url: str | None = None) -> list[PageInfoGet]:
        pass

    @abstractmethod
    async def get_page_html(self, url: AnyHttpUrl) -> str | None:
        pass
