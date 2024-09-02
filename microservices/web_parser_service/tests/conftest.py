import pytest

from app.core.page_fetcher import PageFetcher
from app.core.page_parser import PageParser


@pytest.fixture
def sample_html() -> str:
    return """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <a href="http://example.com/page1">Page 1</a>
            <a href="http://example.com/page2">Page 2</a>
        </body>
    </html>
    """


@pytest.fixture()
def parser() -> PageParser:
    return PageParser()


@pytest.fixture()
def fetcher() -> PageFetcher:
    return PageFetcher()


@pytest.fixture()
def url() -> str:
    return "https://example.com"
