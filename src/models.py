import pydantic


class ArticleEntry(pydantic.BaseModel):
    title: str
    subtitle: str | None
    author: str
    url: pydantic.HttpUrl
