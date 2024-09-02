from app.dependencies.tools_dependecies import get_database, get_rabbit_sender
from app.repositories.pages.pages_mongodb import PagesRepositoryMongodb
from app.repositories.pages.pages_protocol import PagesRepositoryProtocol
from app.repositories.parser.parser_protocol import ParserRepositoryProtocol
from app.repositories.parser.parser_rabbit import ParserRepositoryRabbit

pages_repository = PagesRepositoryMongodb(
    collection=get_database().get_database_collection())

parser_repository = ParserRepositoryRabbit(get_rabbit_sender())


def get_pages_repository() -> PagesRepositoryProtocol:
    return pages_repository


def get_parser_repository() -> ParserRepositoryProtocol:
    return parser_repository
