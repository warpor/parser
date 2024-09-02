from app.core.config import settings
from faststream.rabbit import RabbitQueue
from faststream.rabbit.fastapi import RabbitBroker


class RabbitConsumer:

    def __init__(self, rabbit_broker: RabbitBroker, start_urls_queue: RabbitQueue):
        self.rabbit_broker = rabbit_broker
        self.start_urls_queue = start_urls_queue


print(settings.get_broker_url())
print(settings.BROKER_START_URLS_QUEUE)
rabbit_consumer = RabbitConsumer(
    RabbitBroker(settings.get_broker_url()),
    RabbitQueue(settings.BROKER_START_URLS_QUEUE, durable=True))
