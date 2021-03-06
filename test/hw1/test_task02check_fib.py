"""TEST Homework 1.2."""

from typing import Sequence

import pytest

from hw.hw1.task02check_fib import check_fibonacci


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([0, 1, 1, 2, 3, 5], True),
        ([0, 1, 1, 2, 3, 5, 6], False),
        ((0, 1, 1, 2, 3, 5), True),
        ((0, 1, 1, 2, 3, 5, 6), False),
        ([0], True),
    ],
)
def test_check_fibonacci(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
