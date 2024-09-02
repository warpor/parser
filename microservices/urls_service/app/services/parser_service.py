from app.repositories.parser.parser_protocol import ParserRepositoryProtocol
from app.schemas.parser_schemas import ParserPost


class ParserService:
    parser_repository: ParserRepositoryProtocol

    def __init__(self,
                 parser_repository: ParserRepositoryProtocol) -> None:
        self.parser_repository = parser_repository

    async def add_start_url_to_queue(self, parser_post: ParserPost) -> None:
        await self.parser_repository.add_start_url_to_queue(parser_post)
