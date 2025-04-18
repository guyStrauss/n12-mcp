from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def main_page() -> str:
    with Path("pages/single_article.html").open() as f:
        return f.read()


@pytest.fixture(scope="session")
def article_page() -> str:
    with Path("pages/article_page.html").open() as f:
        return f.read()
