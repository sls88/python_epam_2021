"""TEST Homework 4.1."""
from collections import namedtuple
from unittest.mock import patch

import pytest

from hw.hw4.Homework_4_task2 import count_dots_on_i


def test_response_ok():
    with patch("requests.get") as fake_get:
        fake_response = namedtuple("Response", "text status")
        fake_get.return_value = fake_response(text="dataidataidatai", status=200)
        assert count_dots_on_i("www.www.www") == 3


def test_response_ok_0i():
    with patch("requests.get") as fake_get:
        fake_response = namedtuple("Response", "text status")
        fake_get.return_value = fake_response(text="", status=200)
        assert count_dots_on_i("https://habr.com/ru/post/330034/") == 0


def test_connection_error():
    with patch("requests.exceptions.ConnectionError"):
        with pytest.raises(ValueError, match="Unreachable"):
            count_dots_on_i("sss")


def test_timeout_error():
    with patch("requests.exceptions.TimeoutError"):
        with pytest.raises(ValueError, match="Unreachable"):
            count_dots_on_i("sssa")
