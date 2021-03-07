"""TEST Homework 1.5."""

from typing import List

import pytest

from hw.hw1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("value", "k", "expected_result"),
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1, -3, 5, 3, 6, 7], 4, 21),
        ([1, 3, -1, -3, 5, 3, 6], 4, 11),
    ],
)
def test_find_maximal_subarray_sum(value: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(value, k)

    assert actual_result == expected_result
