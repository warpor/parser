from app.core.config import settings
from app.core.page_fetcher import PageFetcher

page_fetcher = PageFetcher(settings.headers)


def get_page_fetcher() -> PageFetcher:
    return page_fetcher
