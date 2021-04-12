"""TEST Homework 9.1."""
from pathlib import Path
from typing import List, Union

import pytest

from hw.hw9.hw_9_1 import merge_sorted_files


@pytest.fixture()
def different_lengths() -> List[Union[Path, str]]:
    paths = ("test/hw9/test_task1/1_1_1_1.txt", "test/hw9/test_task1/1_2_3.txt")
    return [Path(el) for el in paths]


@pytest.fixture()
def equal_sequences() -> List[Union[Path, str]]:
    paths = ("test/hw9/test_task1/11.txt", "test/hw9/test_task1/22.txt")
    return [Path(el) for el in paths]


@pytest.fixture()
def f1_2_3i4_5_6() -> List[Union[Path, str]]:
    paths = ("test/hw9/test_task1/1_2_3.txt", "test/hw9/test_task1/4_5_6.txt")
    return [Path(el) for el in paths]


@pytest.fixture()
def f1_3_5i2_4_6() -> List[Union[Path, str]]:
    paths = ("test/hw9/test_task1/1_3_5.txt", "test/hw9/test_task1/2_4_6.txt")
    return [Path(el) for el in paths]


@pytest.fixture()
def triple_seq() -> List[Union[Path, str]]:
    paths = (
        "test/hw9/test_task1/1_4_7.txt",
        "test/hw9/test_task1/2_5_8.txt",
        "test/hw9/test_task1/3_6_9.txt",
    )
    return [Path(el) for el in paths]


def test_different_lengths(different_lengths):
    with merge_sorted_files(different_lengths) as f:
        actual_result = list(f)

    assert actual_result == [1, 1, 1, 1, 1, 2, 3]


def test_equality_of_sequences_1_1_1i1_1_1(equal_sequences):
    with merge_sorted_files(equal_sequences) as f:
        actual_result = list(f)

    assert actual_result == [1, 1, 1, 1, 1, 1]


def test_1_2_3i4_5_6(f1_2_3i4_5_6):
    with merge_sorted_files(f1_2_3i4_5_6) as f:
        actual_result = list(f)

    assert actual_result == [1, 2, 3, 4, 5, 6]


def test_1_3_5i2_4_6(f1_3_5i2_4_6):
    with merge_sorted_files(f1_3_5i2_4_6) as f:
        actual_result = list(f)

    assert actual_result == [1, 2, 3, 4, 5, 6]


def test_triple_seq_1_4_7i2_5_8i3_6_9(triple_seq):
    with merge_sorted_files(triple_seq) as f:
        actual_result = list(f)

    assert actual_result == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        with merge_sorted_files(["ggg.ty", "kkk.ru"]) as f:
            list(f)


def test_for(f1_2_3i4_5_6):
    with merge_sorted_files(f1_2_3i4_5_6) as f:
        actual_result = [i for i in f if i < 5]

    assert actual_result == [1, 2, 3, 4]
