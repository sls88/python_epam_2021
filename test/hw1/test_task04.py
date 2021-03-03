"""TEST Homework 1.4."""

from typing import List

import pytest

from hw.hw1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected_result"),
    [
        ([-1, -2], [2, 1], [0, 2], [2, -1], 2),
        ([0, 1, 0], [0, 1, 5], [-2, -3, 2], [2, 1, -1], 9),
        ([0, 1, 0, 2], [0, 1, 5, -1], [-2, -3, 2, 0], [2, 1, -1, -2], 29),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
