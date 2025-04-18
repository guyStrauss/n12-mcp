from http import HTTPStatus

from requests_mock.mocker import Mocker

import n12
from tests import dataset


def test_list_articles(main_page: str, requests_mock: Mocker) -> None:
    requests_mock.get(n12.URL, text=main_page)
    articles = n12.get_main_page()

    assert articles == dataset.ARTICLES


def test_list_articles_not_found(requests_mock: Mocker) -> None:
    requests_mock.get(n12.URL, status_code=HTTPStatus.NOT_FOUND)
    articles = n12.get_main_page()
    assert articles == []


def test_list_articles_html_error(requests_mock: Mocker) -> None:
    requests_mock.get(n12.URL, text="Not HTML")
    articles = n12.get_main_page()
    assert articles == []


def test_read_article(requests_mock: Mocker, article_page: str) -> None:
    requests_mock.get(dataset.ARTICLE_URL, text=article_page)
    page = n12.read_article(dataset.ARTICLE_URL)
    assert page != ""


def test_read_article_fail(requests_mock: Mocker) -> None:
    requests_mock.get(dataset.ARTICLE_URL, status_code=HTTPStatus.NOT_FOUND)
    page = n12.read_article(dataset.ARTICLE_URL)
    assert page == "Something Went Wrong"
