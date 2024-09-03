from aiohttp import ClientSession, ClientResponse
from aiohttp.web_exceptions import HTTPError
from app.core.config import settings
from app.core.logger import logger
from tenacity import retry, stop_after_attempt, wait_random


class PageFetcher:
    headers: dict[str, str] | None = None

    def __init__(self, headers: dict[str, str] | None = None):
        self.headers = headers

    @retry(
        stop=stop_after_attempt(settings.retries_count),
        reraise=True,
        wait=wait_random(min=1, max=10)
    )
    async def get_html(self, session: ClientSession, url: str) -> str | None:
        async with session.get(url, headers=self.headers,
                               timeout=settings.request_timeout_in_seconds) as response:
            if self.check_html(response, url):
                return await response.text()
            logger.warning(f"Can't fetch html from {url}")
            return None

    @staticmethod
    def check_status(response: ClientResponse, url: str) -> bool:
        if response.status == 404 or response.status >= 500:
            logger.warning(f"Incorrect status code: {response.status} from {url}")
            return False
        if not 200 <= response.status < 300:
            raise HTTPError(reason=f"Incorrect status code {response.status}")
        return True

    @staticmethod
    def check_content_type(response: ClientResponse) -> bool:
        content_type = response.headers.get("Content-Type", "").lower()
        return "html" in content_type

    @staticmethod
    def check_html(response: ClientResponse, url: str) -> bool:
        return (PageFetcher.check_status(response, url)
                and PageFetcher.check_content_type(response))
