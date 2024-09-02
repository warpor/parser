from faststream.rabbit import RabbitQueue
from faststream.rabbit.fastapi import RabbitRouter

from app.core.config import settings


class RabbitSender:

    def __init__(self, rabbit_router: RabbitRouter, start_urls_queue: RabbitQueue):
        self.rabbit_router = rabbit_router
        self.start_urls_queue = start_urls_queue

    async def declare_queue(self) -> None:
        await self.rabbit_router.broker.declare_queue(self.start_urls_queue)


rabbit_sender = RabbitSender(RabbitRouter(
    settings.get_broker_url(), include_in_schema=False),
    RabbitQueue(settings.BROKER_START_URLS_QUEUE, durable=True))
