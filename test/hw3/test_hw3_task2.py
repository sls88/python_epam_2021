"""TEST Homework 3.2."""

import datetime
from typing import Any, Tuple

import pytest

from hw.hw3.hw3_task2 import fast_calculate, sum_more_fast_slow_calculate


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (500, (1024259, datetime.timedelta(seconds=60))),
    ],
)
def test_fast_calculate(value: int, expected_result: Tuple[Any]):
    actual_result = fast_calculate(value)

    assert actual_result[0] == expected_result[0]
    assert actual_result[1] < expected_result[1]


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [(500, 1024259)],
)
def test_sum_more_fast_slow_calculate(value: int, expected_result: int):
    actual_result = sum_more_fast_slow_calculate(value)

    assert actual_result == expected_result
