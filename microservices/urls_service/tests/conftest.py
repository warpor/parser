from unittest.mock import Mock, AsyncMock

import pytest
from fastapi.testclient import TestClient

from app.dependencies.repositories_dependencies import get_pages_repository
from app.repositories.pages.pages_protocol import PagesRepositoryProtocol
from app.services.pages_service import PagesService
from main import app


@pytest.fixture
def mock_pages_repository() -> Mock:
    mock_repo = Mock(spec=PagesRepositoryProtocol)
    mock_repo.get_pages = AsyncMock()
    mock_repo.get_page_html = AsyncMock()
    return mock_repo


@pytest.fixture
def pages_service(mock_pages_repository: Mock) -> PagesService:
    return PagesService(pages_repository=mock_pages_repository)


@pytest.fixture
def pages_repository() -> PagesRepositoryProtocol:
    return get_pages_repository()


@pytest.fixture()
def parser_post() -> dict:
    return {"url": "http://test_server:5000/",
            "concurrent_page_loads": 1,
            "depth": 1}


@pytest.fixture(scope="module")
def client() -> TestClient:
    with TestClient(app) as client:
        yield client
