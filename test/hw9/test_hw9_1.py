"""TEST Homework 9.1."""
from pathlib import Path
from typing import List, Union

import pytest

from hw.hw9.hw_9_1 import merge_sorted_files, merge_sorted_inf_seq


@pytest.fixture()
def double_path() -> List[Union[Path, str]]:
    path1 = Path("test/hw9/test_task1/double1.txt")
    path2 = Path("test/hw9/test_task1/double2.txt")
    return [path1, path2]


@pytest.fixture()
def different_lengths() -> List[Union[Path, str]]:
    path1 = Path("test/hw9/test_task1/double1.txt")
    path2 = Path("test/hw9/test_task1/broken.txt")
    return [path1, path2]


@pytest.fixture()
def triple_path() -> List[Union[Path, str]]:
    path1 = Path("test/hw9/test_task1/file1.txt")
    path2 = Path("test/hw9/test_task1/file2.txt")
    path3 = Path("test/hw9/test_task1/file3.txt")
    return [path1, path2, path3]


def test_merge_sorted_files(double_path):
    actual_result = list(merge_sorted_files(double_path))

    assert actual_result == [1, 2, 3, 4, 5, 6]


def test_different_lengths(different_lengths):
    actual_result = list(merge_sorted_files(different_lengths))

    assert actual_result == [1, 1, 3, 1, 5, 1]


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        list(merge_sorted_files(["ggg.ty", "kkk.ru"]))


def test_merge_sorted_inf_seq(triple_path, double_path):
    actual_result = list(merge_sorted_inf_seq(triple_path))
    actual_result2 = list(merge_sorted_inf_seq(double_path))

    assert actual_result == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert actual_result2 == [1, 2, 3, 4, 5, 6]


def test_diff_lengths_sorted_inf_seq_func(different_lengths):
    actual_result = list(merge_sorted_inf_seq(different_lengths))

    assert actual_result == [1, 1, 3, 1, 5, 1]
