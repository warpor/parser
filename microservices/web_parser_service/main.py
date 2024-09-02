from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fast_depends import Depends
from faststream import FastStream, ContextRepo

from app.core.crawler import Crawler
from app.core.logger import setup_logging
from app.dependencies.tools_dependecies import get_rabbit_consumer
from app.schemas.pages_schemas import PagePost


@asynccontextmanager
async def lifespan(context: ContextRepo) -> AsyncGenerator:
    setup_logging()
    yield


rabbit_consumer = get_rabbit_consumer()
broker = rabbit_consumer.rabbit_broker

app = FastStream(rabbit_consumer.rabbit_broker, lifespan=lifespan)


@broker.subscriber(rabbit_consumer.start_urls_queue)
async def handle_msg(
        crawler_start_info: PagePost,
        crawler: Crawler = Depends(Crawler),
) -> None:
    await crawler.start_crawler(crawler_start_info)
