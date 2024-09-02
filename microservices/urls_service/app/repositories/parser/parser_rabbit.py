from fastapi import HTTPException

from app.repositories.parser.parser_protocol import ParserRepositoryProtocol
from app.schemas.parser_schemas import ParserPost
from app.tools.rabbit import RabbitSender


class ParserRepositoryRabbit(ParserRepositoryProtocol):

    def __init__(self, sender: RabbitSender):
        self.sender = sender

    async def add_start_url_to_queue(self, parser_post: ParserPost) -> None:
        try:
            await self.sender.rabbit_router.broker.publish(
                parser_post, self.sender.start_urls_queue, persist=True)
        except Exception as e:
            raise HTTPException(status_code=500,
                                detail=f"Error adding message to broker: {e}")
