from app.dependencies.repositories_dependencies import (pages_repository,
                                                        parser_repository)
from app.services.pages_service import PagesService
from app.services.parser_service import ParserService

pages_service = PagesService(
    pages_repository)

parser_service = ParserService(
    parser_repository)


def get_pages_service() -> PagesService:
    return pages_service


def get_parser_service() -> ParserService:
    return parser_service
