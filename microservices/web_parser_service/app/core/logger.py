import logging


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/web_parser.log')
        ]
    )


logger = logging.getLogger(__name__)
