from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.api.v1.urls import router
from app.dependencies.tools_dependecies import get_rabbit_sender
from app.tools.mongodb import mongo_db


@asynccontextmanager
async def lifespan(app_instance: FastAPI) -> AsyncGenerator:
    rabbit_sender = get_rabbit_sender()
    async with (rabbit_sender.rabbit_router.lifespan_context(app_instance),
                mongo_db.connect_to_database()):
        await rabbit_sender.declare_queue()
        yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)
