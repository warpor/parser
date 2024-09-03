from unittest.mock import Mock

import pytest
from aiohttp import ClientSession, ClientResponse
from aioresponses import aioresponses
from app.core.page_fetcher import PageFetcher


@pytest.mark.asyncio
async def test_get_html_success(fetcher: PageFetcher, url: str) -> None:
    with aioresponses() as mock:
        html_content = "<html><body>Test</body></html>"

        mock.get(url, status=200,
                 headers={"Content-Type": "text/html"}, body=html_content)

        async with ClientSession() as session:
            result = await fetcher.get_html(session, url)

        assert result == html_content


@pytest.mark.asyncio
async def test_get_invalid_html(fetcher: PageFetcher, url: str) -> None:
    with aioresponses() as mock:
        mock.get(url, status=200,
                 headers={"Content-Type": "application/json"}, body='{}')

        async with ClientSession() as session:
            result = await fetcher.get_html(session, url)

        assert result is None


@pytest.mark.asyncio
async def test_get_html_not_found(fetcher: PageFetcher, url: str) -> None:
    with aioresponses() as mock:
        mock.get(url, status=404)

        async with ClientSession() as session:
            result = await fetcher.get_html(session, url)

        assert result is None


@pytest.mark.asyncio
async def test_get_html_server_error(fetcher: PageFetcher, url: str) -> None:
    with aioresponses() as mock:
        mock.get(url, status=500)

        async with ClientSession() as session:
            result = await fetcher.get_html(session, url)

        assert result is None


def test_check_html_success(fetcher: PageFetcher, url: str) -> None:
    response = Mock(spec=ClientResponse)
    response.status = 200
    response.headers = {"Content-Type": "text/html"}

    assert fetcher.check_status(response, url) is True


def test_check_html_non_html_content_type(fetcher: PageFetcher, url: str) -> None:
    response = Mock(spec=ClientResponse)
    response.status = 200
    response.headers = {"Content-Type": "application/json"}

    assert fetcher.check_content_type(response) is False


def test_check_html_non_success_status(fetcher: PageFetcher, url: str) -> None:
    response = Mock(spec=ClientResponse)
    response.status = 404
    response.headers = {"Content-Type": "text/html"}

    assert fetcher.check_status(response, url) is False
