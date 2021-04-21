"""TEST Homework 10.1."""
import json
import os
from collections import namedtuple
from pathlib import Path
from unittest.mock import patch

import pytest
from bs4 import BeautifulSoup

from hw.hw10.hw10_sip500 import StockStat, centrobank, code_name_price, companies
from hw.hw10.hw10_sip500 import p_e, potential_profit, write_files, year_growth


@pytest.fixture()
def data_1_of_10_pages_companies():
    with open("test/hw10/html1.html") as f:
        return f.read()


@pytest.fixture()
def data_page_company():
    with open("test/hw10/html2.html") as f:
        return BeautifulSoup(f.read(), "html.parser")


def xml_sberbank():
    with open("test/hw10/asp.xml", "rb") as f:
        return f.read()


@pytest.fixture()
def test_json_resource():
    res = tuple([{str(i): i}, {str(i + 1): i + 1}] for i in range(1, 8, 2))
    obj = StockStat(*res)
    return obj, res


@pytest.fixture()
def paths():
    paths = ("price.json", "p_e.json", "profit.json", "growth.json")
    return tuple(Path(el) for el in paths)


def test_code_name_price(data_page_company):
    actual_result = code_name_price(data_page_company)
    expected_result = ("ADBE", "Adobe Inc.", 524.68)

    assert actual_result == expected_result


def test_p_e(data_page_company):
    actual_result = p_e(data_page_company)
    expected_result = 47.10

    assert actual_result == expected_result


def test_potential_profit(data_page_company):
    actual_result = potential_profit(data_page_company)
    expected_result = 65.09

    assert actual_result == expected_result


def test_companies(data_1_of_10_pages_companies):
    actual_result = companies(data_1_of_10_pages_companies)[:3]
    expected_result = [
        "https://markets.businessinsider.com/stocks/mmm-stock",
        "https://markets.businessinsider.com/stocks/aos-stock",
        "https://markets.businessinsider.com/stocks/abt-stock",
    ]

    assert actual_result == expected_result


def test_year_growth(data_1_of_10_pages_companies):
    actual_result = year_growth(data_1_of_10_pages_companies)[:3]
    expected_result = ["33.89%", "66.24%", "39.18%"]

    assert actual_result == expected_result


def test_centrobank():
    with patch("requests.get") as fake_get:
        fake_response = namedtuple("Response", "content")
        fake_get.return_value = fake_response(content=xml_sberbank())
        assert centrobank() == 76.2491


def read_file(path):
    with open(path) as f:
        return json.load(f)


@pytest.mark.asyncio
async def test_write_files(test_json_resource, paths):
    res = test_json_resource
    obj_stock_stat = res[0]
    tuple_lists = res[1]
    try:
        await write_files(obj_stock_stat, *paths)
        actual_result = [read_file(i) == j for i, j in zip(paths, tuple_lists)]
        assert actual_result == [True, True, True, True]
    finally:
        for path in paths:
            os.remove(path)
