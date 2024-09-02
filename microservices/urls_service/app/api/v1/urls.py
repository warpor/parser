from typing import Annotated

from app.dependencies.services_dependencies import get_pages_service, get_parser_service
from app.schemas.pages_schemas import PageInfoGet
from app.schemas.parser_schemas import ParserPost
from app.services.pages_service import PagesService
from app.services.parser_service import ParserService
from fastapi import APIRouter, Depends
from pydantic import AnyHttpUrl

router = APIRouter()


@router.get("/pages", tags=["pages"])
async def get_pages(
        pages_service: Annotated[PagesService, Depends(get_pages_service)],
        title: str | None = None,
        url: str | None = None) -> list[PageInfoGet]:
    return await pages_service.get_pages(title=title, url=url)


@router.get("/page_html", tags=["pages"])
async def get_page_html(
        pages_service: Annotated[PagesService, Depends(get_pages_service)],
        url: AnyHttpUrl) -> str | None:
    return await pages_service.get_page_html(url=url)


@router.post("/parse_page", tags=["parser"])
async def parse_page(
        parser_service: Annotated[ParserService, Depends(get_parser_service)],
        parser_post: ParserPost) -> dict[str, str]:
    await parser_service.add_start_url_to_queue(parser_post)
    return {"message": "Start url add to queue"}
