import logging

from app.core.config import settings


def setup_logging() -> None:
    if not settings.TESTS_MODE:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/web_parser.log')
            ]
        )


logger = logging.getLogger(__name__)
