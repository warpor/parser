from app.tools.mongodb import DataBase, mongo_db
from app.tools.rabbit import RabbitSender, rabbit_sender


def get_database() -> DataBase:
    return mongo_db


def get_rabbit_sender() -> RabbitSender:
    return rabbit_sender
