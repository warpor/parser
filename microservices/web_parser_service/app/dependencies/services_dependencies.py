from app.dependencies.repositories_dependencies import pages_repository
from app.services.pages_service import PagesService

pages_service = PagesService(
    pages_repository)


def get_pages_service() -> PagesService:
    return pages_service
