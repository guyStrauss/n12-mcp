import re
from http import HTTPStatus

import bs4
import requests
from bs4 import BeautifulSoup
from loguru import logger
from pydantic import HttpUrl

from models import ArticleEntry

URL = "https://www.n12.co.il"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "DNT": "1",
    "Referer": "https://www.n12.co.il/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

MAIN_ARTICLES = "grid-ordering main1"
METADATA_ATTRIBUTE = "data-domo-click"
ARTICLE_URL = re.compile(r'"clicked_item_url"\s*:\s*"([^"]+)"')
ALL_ENTRIES = 3
PARTIAL_ENTRIES = 2


def get_main_page() -> list[ArticleEntry]:
    results = []

    response = requests.get(URL, headers=HEADERS, timeout=30)
    if response.status_code != HTTPStatus.OK:
        return []

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


def read_article(article_url: str | HttpUrl) -> str:
    response = requests.get(article_url, headers=HEADERS, timeout=30)
    if response.status_code != HTTPStatus.OK:
        return "Something Went Wrong"
    soup = BeautifulSoup(response.content, "html.parser")
    texts = soup.find_all("p")
    return "\n".join([paragraph.text for paragraph in texts])
