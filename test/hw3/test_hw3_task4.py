"""TEST Homework 3.4."""

import pytest

from hw.hw3.hw3_task4 import is_armstrong


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (153, True),
        (10, False),
        (0, True),
    ],
)
def test_is_armstrong(value: int, expected_result: bool):
    actual_result = is_armstrong(value)

    assert actual_result == expected_result
