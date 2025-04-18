from mcp.server import FastMCP
from pydantic import HttpUrl

import n12
from models import ArticleEntry

mcp = FastMCP("N12-News")


@mcp.tool()
def list_articles() -> list[ArticleEntry]:
    return n12.get_main_page()


@mcp.tool()
def read_article(article_url: str | HttpUrl) -> str:
    return n12.read_article(article_url)


if __name__ == "__main__":
    mcp.run(transport="stdio")
