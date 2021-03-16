"""TEST Homework 4.1."""

import os

import pytest

from hw.hw4.Homework_4_task1 import read_magic_number


def create_test_data(path: str, line: str) -> None:
    with open(path, "w") as file:
        if line:
            for stri in line:
                file.write(stri)
        else:
            file.write(line)


@pytest.mark.parametrize(
    ("path", "line"),
    [
        ("data1.txt", "2"),
        ("data1.txt", "1"),
    ],
)
def test_read_magic_number_is_true(path: str, line: str):
    create_test_data(path, line)

    actual_result = read_magic_number(path)
    os.remove(path)
    assert actual_result is True


@pytest.mark.parametrize(
    ("path", "line"),
    [
        ("data1.txt", "555"),
        ("data1.txt", "0"),
        ("data1.txt", "-1"),
    ],
)
def test_read_magic_number_is_false(path: str, line: str):
    create_test_data(path, line)

    actual_result = read_magic_number(path)
    os.remove(path)
    assert actual_result is False


@pytest.mark.parametrize(
    ("path", "line"),
    [("data1.txt", "213gth"), ("data1.txt", "1-1"), ("data1.txt", "")],
)
def test_read_magic_number_exceptions(path: str, line: str):
    create_test_data(path, line)
    with pytest.raises(ValueError, match="The case of"):
        read_magic_number(path)
    os.remove(path)


@pytest.mark.parametrize(
    ("path", "line"),
    [
        ("", "777"),
    ],
)
def test_read_magic_number_file_exist(path: str, line: str):
    with pytest.raises(ValueError, match="The case of"):
        read_magic_number(path)
