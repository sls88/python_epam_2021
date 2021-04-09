"""TEST Homework 9.1."""
from pathlib import Path
from typing import List, Union

import pytest

from hw.hw9.hw_9_1 import merge_sorted_files


def p() -> str:
    return "test/hw9/test_task1/"


@pytest.mark.parametrize(
    ("paths", "expected_result"),
    [
        ([Path(p() + i) for i in ("1_2_3.txt", "4_5_6.txt")], [1, 2, 3, 4, 5, 6]),
        ([Path(p() + i) for i in ("1_3_5.txt", "2_4_6.txt")], [1, 2, 3, 4, 5, 6]),
        (
            [Path(p() + i) for i in ("1_4_7.txt", "2_5_8.txt", "3_6_9.txt")],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ),
        ([Path(p() + i) for i in ("4_5_6.txt", "1_1_1_1.txt")], [1, 1, 1, 4, 5, 6]),
    ],
)
def test_backspace_recursion_variant(
    paths: List[Union[Path, str]], expected_result: List
):
    actual_result = list(merge_sorted_files(paths))

    assert actual_result == expected_result


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        list(merge_sorted_files(["ggg.ty", "kkk.ru"]))
