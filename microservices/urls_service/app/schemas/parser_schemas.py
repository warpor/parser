from typing import Annotated

from pydantic import BaseModel, AnyHttpUrl, Field


class ParserPost(BaseModel):
    url: AnyHttpUrl
    concurrent_page_loads: Annotated[int, Field(default=1, ge=1)]
    depth: Annotated[int, Field(default=0, ge=0)]
