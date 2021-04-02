"""TEST Homework 8.1."""

import pytest

from hw.hw8.Hw8_1_class_wrapper import KeyValueStorage


@pytest.fixture()
def good_data() -> str:
    return "test/hw8/task1_good_data.txt"


@pytest.fixture()
def bad_data_incorrect_key() -> str:
    return "test/hw8/task1_bad_data1.txt"


def test_bad_data_incorrect_key(bad_data_incorrect_key: str):
    with pytest.raises(KeyError, match="Invalid"):
        KeyValueStorage(bad_data_incorrect_key)


def test_key_not_exist(good_data: str):
    storage = KeyValueStorage(good_data)
    with pytest.raises(ValueError, match="The key"):
        storage["nick_name"]


def test_attr_not_exist(good_data: str):
    storage = KeyValueStorage(good_data)
    with pytest.raises(AttributeError, match="The attribute"):
        storage.nick_name


def test_good_data(good_data: str):
    storage = KeyValueStorage(good_data)
    actual_result1 = storage["name"]
    actual_result2 = storage.song
    actual_result3 = storage.power

    assert actual_result1 == "kek"
    assert actual_result2 == "shadilay"
    assert actual_result3 == int(9001)
