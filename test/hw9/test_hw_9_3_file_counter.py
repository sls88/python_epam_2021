"""TEST Homework 9.3."""
from pathlib import Path

import pytest

from hw.hw9.Homework_9_3_file_counter import universal_file_counter


@pytest.fixture()
def good_path() -> Path:
    return Path("test/hw9/test_task3")


@pytest.fixture()
def bad_path() -> Path:
    return Path("111222333")


def test_count_tokens(good_path):
    extension = "txt"
    counting_function = str.split
    actual_result = universal_file_counter(good_path, extension, counting_function)

    assert actual_result == 6


def test_count_lines(good_path):
    extension = "txt"
    actual_result = universal_file_counter(good_path, extension)

    assert actual_result == 4


def test_nonexistent_extension(good_path):
    nonexistent_extension = "H.D.D."
    actual_result = universal_file_counter(good_path, nonexistent_extension)

    assert actual_result == 0


def test_incorrect_extension(good_path):
    extension = "png"
    with pytest.raises(TypeError):
        universal_file_counter(bad_path, extension)


def test_nonexistent_directory(bad_path):
    extension = "txt"
    with pytest.raises(FileNotFoundError, match="nonexistent"):
        universal_file_counter(bad_path, extension)


def test_incorrect_function(good_path):
    extension = "txt"
    incorrect_function = str.replace
    with pytest.raises(TypeError):
        universal_file_counter(bad_path, extension, incorrect_function)
