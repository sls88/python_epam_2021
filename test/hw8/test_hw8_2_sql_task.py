"""TEST Homework 8.2."""
import os
import sqlite3
from contextlib import contextmanager


import pytest

from hw.hw8.Hw8_2_sqlite3 import TableData


@pytest.fixture()
def path() -> str:
    return "test/hw8/db_test.sqlite"


@contextmanager
def test_db(path: str) -> None:
    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        with open("test/hw8/SQL_commands.sql") as f:
            cur.executescript(f.read())
        con.commit()
        con.close()
        yield
    finally:
        os.remove(path)


def test_len(path: str):
    with test_db(path):
        with TableData(database_name=path, table_name="presidents") as presidents:
            actual_result = len(presidents)

    assert actual_result == 3


def test_single_data_row(path: str):
    with test_db(path):
        with TableData(database_name=path, table_name="presidents") as presidents:
            actual_result = presidents["Yeltsin"]

    assert actual_result == ("Yeltsin", 999, "Russia")


def test_in_operator(path: str):
    with test_db(path):
        with TableData(database_name=path, table_name="presidents") as presidents:
            actual_result = "Yeltsin" in presidents
            actual_result2 = "Ivanov" in presidents

    assert actual_result is True
    assert actual_result2 is False


def test_iteration_protocol(path: str):
    with test_db(path):
        with TableData(database_name=path, table_name="presidents") as presidents:
            actual_result = [president["name"] for president in presidents]
            actual_result2 = [president["name"] for president in presidents]
            actual_result3 = [president["age"] for president in presidents]

    assert actual_result == ["Big Man Tyrone", "Trump", "Yeltsin"]
    assert actual_result2 == ["Big Man Tyrone", "Trump", "Yeltsin"]
    assert actual_result3 == [101, 1337, 999]


def test_last_result(path: str):
    with test_db(path):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO presidents(name, age, country) VALUES ('Marks', 404, 'USSR');"
        )
        con.commit()
        con.close()
        with TableData(database_name=path, table_name="presidents") as presidents:
            actual_result = presidents["Marks"]

    assert actual_result == ("Marks", 404, "USSR")


def test_key_not_exist(path: str):
    with test_db(path):
        with TableData(database_name=path, table_name="presidents") as presidents:
            with pytest.raises(KeyError, match="The name"):
                presidents["Petrov"]
