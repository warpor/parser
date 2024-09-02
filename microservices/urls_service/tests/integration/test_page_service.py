import time

import pytest
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_get_page_html_integration(parser_post: dict, client: TestClient) -> None:
    response = client.post("/parse_page", json=parser_post)
    assert response.status_code == 200

    processed = False
    for _ in range(10):
        response = client.get("/page_html", params={"url": parser_post["url"]})
        if response.status_code == 200:
            processed = True
            break
        time.sleep(1)

    assert processed, "Message was not processed within the expected time"
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_pages(parser_post: dict, client: TestClient) -> None:
    response = client.post("/parse_page", json=parser_post)
    assert response.status_code == 200

    processed = False
    for _ in range(10):
        response = client.get("/pages", params={"url": parser_post["url"]})
        if response.status_code == 200:
            processed = True
            break
        time.sleep(1)

    assert processed, "Message was not processed within the expected time"
    print(response.json())
    assert response.status_code == 200
