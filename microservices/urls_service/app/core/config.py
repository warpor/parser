import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DB = os.getenv("DB")
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

    def get_database_url(self) -> str:
        return f"{self.DB}://{self.DB_HOST}:{self.DB_PORT}"

    def get_broker_url(self) -> str:
        return (f"{self.BROKER_PROTOCOL}://{self.BROKER_USER}:"
                f"{self.BROKER_PASS}@{self.BROKER_HOST}:{self.BROKER_PORT}")


settings = Settings()
