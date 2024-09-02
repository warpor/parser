from pydantic import AnyHttpUrl, BaseModel


class PageInfoGet(BaseModel):
    title: str
    url: AnyHttpUrl


class PageHtmlGet(BaseModel):
    html: str
