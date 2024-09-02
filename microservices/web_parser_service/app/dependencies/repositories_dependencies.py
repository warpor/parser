from app.dependencies.tools_dependecies import get_database
from app.repositories.pages_mongodb import PagesRepositoryMongodb
from app.repositories.pages_protocol import PagesRepositoryProtocol

pages_repository = PagesRepositoryMongodb(
    collection=get_database().get_database_collection())


def get_pages_repository() -> PagesRepositoryProtocol:
    return pages_repository
