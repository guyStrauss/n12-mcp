import re

import bs4
import requests
from bs4 import BeautifulSoup
from loguru import logger

from models import ArticleEntry

URL = "https://www.n12.co.il"
MAIN_ARTICLES = "grid-ordering main1"
METADATA_ATTRIBUTE = "data-domo-click"
ARTICLE_URL = re.compile(r'"clicked_item_url"\s*:\s*"([^"]+)"')
ALL_ENTRIES = 3
PARTIAL_ENTRIES = 2


def get_main_page() -> list[ArticleEntry]:
    results = []
    with requests.get(URL, timeout=30) as response:
        soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find("ul", {"class": MAIN_ARTICLES})
    if not articles:
        logger.error("Something went wrong while parsing page")
        return []
    for article in articles.children:
        if isinstance(article, bs4.NavigableString):
            continue

        if article.get("class") == ["news-iframe"]:
            continue
        info, *_ = article.text.split("|")
        info = re.split(r"\n+", info.strip())
        if len(info) == ALL_ENTRIES:
            title, subtitle, author = info
        elif len(info) == PARTIAL_ENTRIES:
            title, author = info
            subtitle = None
        else:
            logger.error("Something went wrong while parsing article")
            continue
        metadata = article.get(METADATA_ATTRIBUTE, "")
        url = ARTICLE_URL.search(metadata)
        if url is None:
            logger.error("Failed to extract url")
            continue
        url = url.group(1)
        results.append(
            ArticleEntry(
                title=title,
                subtitle=subtitle,
                author=author,
                url=url,
            )
        )
    return results
