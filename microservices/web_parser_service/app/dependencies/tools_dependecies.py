from app.tools.mongodb import DataBase, mongo_db
from app.tools.rabbit import RabbitConsumer, rabbit_consumer


def get_database() -> DataBase:
    return mongo_db


def get_rabbit_consumer() -> RabbitConsumer:
    return rabbit_consumer
