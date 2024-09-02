from abc import ABC, abstractmethod

from app.schemas.parser_schemas import ParserPost


class ParserRepositoryProtocol(ABC):

    @abstractmethod
    async def add_start_url_to_queue(self, parser_post: ParserPost) -> None:
        pass
