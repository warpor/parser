from pydantic import AnyHttpUrl, BaseModel


class PageInQueue(BaseModel):
    url: str
    depth: int

    def __lt__(self, other: 'PageInQueue') -> bool:
        return self.depth > other.depth

    class Config:
        frozen = True


class PageToDb(BaseModel):
    url: str
    title: str
    html: str

    class Config:
        frozen = True


class PagePost(BaseModel):
    url: AnyHttpUrl
    concurrent_page_loads: int
    depth: int
