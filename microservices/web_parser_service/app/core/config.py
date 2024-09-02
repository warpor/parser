import json
import os
from typing import Any

from dotenv import load_dotenv


def get_config_json(config_path: str = 'config.json') -> dict:
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {}


class Settings:
    DB: str | None = os.getenv("DB")
    DB_HOST: str | None = os.getenv("DB_HOST")
    DB_PORT: str | None = os.getenv("DB_PORT")
    DB_NAME: str | None = os.getenv("DB_NAME")
    DB_COLLECTION: str | None = os.getenv("DB_COLLECTION")

    BROKER_PROTOCOL: str | None = os.getenv("BROKER_PROTOCOL")
    BROKER_HOST: str | None = os.getenv("BROKER_HOST")
    BROKER_PORT: str | None = os.getenv("BROKER_PORT")

    BROKER_USER: str | None = os.getenv("BROKER_DEFAULT_USER")
    BROKER_PASS: str | None = os.getenv("BROKER_DEFAULT_PASS")
    BROKER_START_URLS_QUEUE: str | None = os.getenv("BROKER_START_URLS_QUEUE")

    request_timeout_in_seconds: int
    max_timeout_is_seconds: int
    retries_count: int
    mongo_batch_size: int
    headers: dict[str, str]

    def __init__(self, app_config: dict[str, Any]):
        self.request_timeout_in_seconds = app_config.get(
            "request_timeout_in_seconds", 5)
        self.max_timeout_is_seconds = app_config.get("max_timeout_is_seconds", 30)
        self.retries_count = app_config.get("retries_count", 1)
        self.mongo_batch_size = app_config.get("mongo_batch_size", 100)
        self.headers = app_config.get("headers", {})

    def get_database_url(self) -> str:
        return f"{self.DB}://{self.DB_HOST}:{self.DB_PORT}"

    def get_broker_url(self) -> str:
        return (f"{self.BROKER_PROTOCOL}://{self.BROKER_USER}:"
                f"{self.BROKER_PASS}@{self.BROKER_HOST}:{self.BROKER_PORT}")


load_dotenv()
config_json = get_config_json()
settings = Settings(config_json)
