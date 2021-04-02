"""TEST Homework 8.2."""
import os
import sqlite3

import pytest

from hw.hw8.Hw8_2_sqlite3 import TableData


@pytest.fixture()
def database() -> None:
    con = sqlite3.connect("db_test.sqlite")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE presidents(name VARCHAR(15), val_1 INT, val_2 VARCHAR(20));"
    )
    cur.execute(
        "INSERT INTO presidents(name, val_1, val_2) VALUES ('Big Man Tyrone', 101, 'Kekistan');"
    )
    cur.execute(
        "INSERT INTO presidents(name, val_1, val_2) VALUES ('Yeltsin', 999, 'Russia');"
    )
    cur.execute(
        "INSERT INTO presidents(name, val_1, val_2) VALUES ('Trump', 1337, 'US');"
    )
    con.commit()
    con.close()


def test_len(database: None):
    presidents = TableData(database_name="db_test.sqlite", table_name="presidents")
    actual_result = len(presidents)
    os.remove("db_test.sqlite")

    assert actual_result == 3


def test_single_data_row(database: None):
    presidents = TableData(database_name="db_test.sqlite", table_name="presidents")
    actual_result = presidents["Yeltsin"]
    os.remove("db_test.sqlite")

    assert actual_result == ("Yeltsin", 999, "Russia")


def test_in_operator(database: None):
    presidents = TableData(database_name="db_test.sqlite", table_name="presidents")
    actual_result = "Yeltsin" in presidents
    actual_result2 = "Ivanov" in presidents
    os.remove("db_test.sqlite")

    assert actual_result is True
    assert actual_result2 is False


def test_iteration_protocol(database: None):
    presidents = TableData(database_name="db_test.sqlite", table_name="presidents")
    actual_result = [president["name"] for president in presidents]
    os.remove("db_test.sqlite")

    assert actual_result == ["Big Man Tyrone", "Trump", "Yeltsin"]


def test_last_result(database: None):
    presidents = TableData(database_name="db_test.sqlite", table_name="presidents")
    con = sqlite3.connect("db_test.sqlite")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO presidents(name, val_1, val_2) VALUES ('Marks', 404, 'USSR');"
    )
    con.commit()
    con.close()
    actual_result = presidents["Marks"]
    os.remove("db_test.sqlite")
    assert actual_result == ("Marks", 404, "USSR")


def test_key_not_exist(database: None):
    presidents = TableData(database_name="db_test.sqlite", table_name="presidents")
    try:
        with pytest.raises(KeyError, match="The name"):
            presidents["Petrov"]
    finally:
        os.remove("db_test.sqlite")
