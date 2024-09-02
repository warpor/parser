import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DB = os.getenv("DB")
    DB_HOST: str | None = os.getenv("DB_HOST")
    DB_PORT: str | None = os.getenv("DB_PORT")
    DB_NAME: str | None = os.getenv("DB_NAME")
    DB_COLLECTION: str | None = os.getenv("DB_COLLECTION")

    def get_database_url(self) -> str:
        return f"{self.DB}://{self.DB_HOST}:{self.DB_PORT}"


settings = Settings()
