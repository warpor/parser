from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.services.pages_service import PagesService


@pytest.mark.asyncio
async def test_get_page_html_not_found(pages_service: PagesService,
                                       mock_pages_repository: Mock) -> None:
    url = "https://example.com"
    mock_pages_repository.get_page_html.return_value = None

    with pytest.raises(HTTPException) as e:
        await pages_service.get_page_html(url)

    assert e.value.status_code == 404


@pytest.mark.asyncio
async def test_get_page_html_success(pages_service: PagesService,
                                     mock_pages_repository: Mock) -> None:
    url = "https://example.com"
    expected_html = "<html><body>Example Content</body></html>"
    mock_pages_repository.get_page_html.return_value = expected_html

    result = await pages_service.get_page_html(url)

    assert result == expected_html
