"""TEST Homework 1.2.

"""
from collections.abc import Sequence

import pytest
from epam_python_2021.hw.hw1.check_fib import check_fib


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5], True),
        ([0, 1, 1, 2, 3, 5, 6], False),
        ([0, 1, 1, "t", 3, 5, 6], False),
        ((0, 1, 1, 2, 3, 5), True),
        ((0, 1, 1, 2, 3, 5, 6), False),
        ("c", False),
        ("cc", False),
        ("ccc", False),
        ("[0, 1, 1, 2, 3, 5]", False),
        (None, False),
        ([0], True),
        (["0"], False),
    ],
)
def test_check_fib(value: Sequence[int], expected_result: bool):
    actual_result = check_fib(value)

    assert actual_result == expected_result
