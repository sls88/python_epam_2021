"""TEST Homework 10.1."""
import json
import os
from collections import namedtuple
from pathlib import Path
from unittest.mock import patch

import pytest
from bs4 import BeautifulSoup

from hw.hw10.hw10_sip500_2 import centrobank, code_name_price, companies
from hw.hw10.hw10_sip500_2 import p_e, potential_profit, write_files, year_growth


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
def res():
    return (
        [{"1": 1}, {"2": 2}],
        [{"4": 4}, {"6": 6}],
        [{"8": 8}, {"10": 10}],
        [{"12": 12}, {"14": 14}],
    )


@pytest.fixture()
def paths():
    return (
        Path("test/hw10/1.json"),
        Path("test/hw10/2.json"),
        Path("test/hw10/3.json"),
        Path("test/hw10/4.json"),
    )


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


@pytest.mark.asyncio
async def test_write_files(res):
    path1, path2, path3, path4 = (
        Path("1.json"),
        Path("2.json"),
        Path("3.json"),
        Path("4.json"),
    )
    try:
        await write_files(res, Path(path1), Path(path2), Path(path3), Path(path4))
        with open(path1) as f:
            actual_result = json.load(f)
            expected_result = res[0]
        with open(path2) as f:
            actual_result2 = json.load(f)
            expected_result2 = res[1]
        with open(path3) as f:
            actual_result3 = json.load(f)
            expected_result3 = res[2]
        with open(path4) as f:
            actual_result4 = json.load(f)
            expected_result4 = res[3]
        assert actual_result == expected_result
        assert actual_result2 == expected_result2
        assert actual_result3 == expected_result3
        assert actual_result4 == expected_result4
    finally:
        os.remove(path1)
        os.remove(path2)
        os.remove(path3)
        os.remove(path4)
