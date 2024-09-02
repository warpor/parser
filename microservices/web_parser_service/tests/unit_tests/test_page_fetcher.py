from unittest.mock import Mock

import pytest
from aiohttp import ClientSession, ClientResponse
from aioresponses import aioresponses
from app.core.page_fetcher import PageFetcher


@pytest.mark.asyncio
async def test_get_html_success(fetcher: PageFetcher) -> None:
    with aioresponses() as mock:
        url = "https://example.com"
        html_content = "<html><body>Test</body></html>"

        mock.get(url, status=200,
                 headers={"Content-Type": "text/html"}, body=html_content)

        async with ClientSession() as session:
            result = await fetcher.get_html(session, url)

        assert result == html_content


@pytest.mark.asyncio
async def test_get_invalid_html() -> None:
    fetcher = PageFetcher()

    with aioresponses() as mock:
        url = "https://example.com"

        mock.get(url, status=200,
                 headers={"Content-Type": "application/json"}, body='{}')

        async with ClientSession() as session:
            result = await fetcher.get_html(session, url)

        assert result is None


@pytest.mark.asyncio
async def test_get_html_failure() -> None:
    fetcher = PageFetcher()

    with aioresponses() as mock:
        url = "https://example.com"

        mock.get(url, status=500)

        async with ClientSession() as session:
            result = await fetcher.get_html(session, url)

        assert result is None


def test_check_html_success(fetcher: PageFetcher) -> None:
    response = Mock(spec=ClientResponse)
    response.status = 200
    response.headers = {"Content-Type": "text/html"}

    assert fetcher.check_html(response) is True


def test_check_html_non_html_content_type(fetcher: PageFetcher) -> None:
    response = Mock(spec=ClientResponse)
    response.status = 200
    response.headers = {"Content-Type": "application/json"}

    assert fetcher.check_html(response) is False


def test_check_html_non_success_status(fetcher: PageFetcher) -> None:
    response = Mock(spec=ClientResponse)
    response.status = 404
    response.headers = {"Content-Type": "text/html"}

    assert fetcher.check_html(response) is False
