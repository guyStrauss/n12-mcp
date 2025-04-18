from mcp.server.fastmcp import FastMCP

from src import n12
from src.models import ArticleEntry

mcp = FastMCP("N12-News")


@mcp.tool("Get Articles")
def get_articles() -> list[ArticleEntry]:
    return n12.get_main_page()
