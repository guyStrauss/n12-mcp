from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def main_page() -> str:
    with Path("pages/main_page.html").open("r") as f:
        return f.read()


@pytest.fixture(scope="session")
def article_page() -> str:
    with Path("pages/single_article.html").open("r") as f:
        return f.read()
