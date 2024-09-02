import asyncio
from asyncio import PriorityQueue

import aiohttp
from aiohttp import ClientSession, ClientError

from app.core.page_fetcher import PageFetcher
from app.core.logger import logger
from app.core.config import settings
from app.core.page_parser import PageParser
from app.dependencies.page_fetcher_dependecies import get_page_fetcher
from app.dependencies.page_parser_dependecies import get_page_parser
from app.dependencies.services_dependencies import get_pages_service
from app.schemas.pages_schemas import PageInQueue, PagePost, PageToDb
from app.services.pages_service import PagesService


class Crawler:
    page_parser: PageParser
    pages_service: PagesService
    queue: PriorityQueue[tuple[int, PageInQueue]]
    visited_pages: set[PageToDb]
    page_fetcher: PageFetcher
    page_post: PagePost | None

    def __init__(self) -> None:
        self.page_fetcher = get_page_fetcher()
        self.page_parser = get_page_parser()
        self.pages_service = get_pages_service()
        self.queue = PriorityQueue()
        self.visited_pages = set()
        self.page_post = None

    async def __parse(self, session: ClientSession, max_depth: int) -> None:
        work_item: PageInQueue
        while True:
            _, work_item = await self.queue.get()
            if max_depth >= work_item.depth:
                await self.__process_page(work_item, session)
            self.queue.task_done()

    async def __process_page(self, work_item: PageInQueue,
                             session: ClientSession) -> None:
        try:
            html = await asyncio.wait_for(
                self.page_fetcher.get_html(session, work_item.url),
                timeout=settings.max_timeout_is_seconds)
            if html:
                await self.__process_html(html, work_item)

        except asyncio.TimeoutError:
            logger.warn(f"Timeout error for URL: {work_item.url}")

        except ClientError as e:
            logger.warn(f"Request error for URL: {work_item.url}. Exception: {str(e)}")

        except Exception as e:
            logger.error(f"Unexpected error for URL:"
                         f" {work_item.url}. Exception {str(e)}")

    async def __process_html(self, html: str, work_item: PageInQueue) -> None:
        title, links = self.page_parser.parse(html,
                                              work_item.url)
        await self.__add_new_links_to_queue(links, work_item.depth)
        await self.__mark_visited_page(PageToDb(url=work_item.url,
                                                title=title, html=html))

    async def __add_new_links_to_queue(
            self, links: list[str], parent_page_depth: int) -> None:
        for link in links:
            priority = - (parent_page_depth + 1)
            await self.queue.put(
                (priority,
                 PageInQueue(url=link, depth=parent_page_depth + 1)))

    async def __mark_visited_page(
            self, visited_page: PageToDb) -> None:
        self.visited_pages.add(visited_page)
        if (len(self.visited_pages)) > settings.mongo_batch_size:
            await self.__batch_add()

    async def __batch_add(self) -> None:
        temp = self.visited_pages.copy()
        self.visited_pages.clear()
        await self.pages_service.insert_pages(temp)
        logger.info(f"Added to mongodb {len(temp)} "
                    f"pages. Initial page: {self.page_post}")

    async def __parse_urls(self, concurrent_page_loads: int, depth: int) -> None:
        conn = aiohttp.TCPConnector(limit_per_host=concurrent_page_loads,
                                    verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            workers = [asyncio.create_task(self.__parse(session, depth))
                       for _ in range(concurrent_page_loads)]
            await self.queue.join()
            [w.cancel() for w in workers]

    async def start_crawler(self, page_post: PagePost) -> None:
        logger.info(f"Starting crawler {page_post}")
        print("here")
        self.page_post = page_post
        self.queue.put_nowait((0, PageInQueue(url=str(page_post.url), depth=0)))
        await self.__parse_urls(page_post.concurrent_page_loads, page_post.depth)
        await self.pages_service.insert_pages(self.visited_pages)
        logger.info(f"Stopped crawler {page_post}")
