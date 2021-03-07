"""TEST Homework 2.2."""

from typing import List, Tuple

import pytest

from hw.hw2.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([2], (2, 2)),
    ],
)
def test_major_and_minor_elem(value: List, expected_result: Tuple[int, int]):
    actual_result = major_and_minor_elem(value)

    assert actual_result == expected_result
