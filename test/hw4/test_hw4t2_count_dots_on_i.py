"""TEST Homework 4.2."""
from collections import namedtuple
from unittest.mock import patch

import pytest
import requests
from requests import ConnectionError, Timeout

from hw.hw4.Homework_4_task2 import count_dots_on_i


class TestErrors:
    def connection_error(self):
        raise ConnectionError

    def timeout_error(self):
        raise Timeout


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


def test_connection_error(monkeypatch):
    monkeypatch.setattr(requests, "get", TestErrors.connection_error)
    with pytest.raises(ValueError, match="Unreachable"):
        count_dots_on_i("https://docs.python.org/")


def test_timeout_error(monkeypatch):
    monkeypatch.setattr(requests, "get", TestErrors.timeout_error)
    with pytest.raises(ValueError, match="Unreachable"):
        count_dots_on_i("https://docs.python.org/")
