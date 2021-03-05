"""TEST Homework 2.4."""

from typing import Callable

import pytest

from hw.hw2.hw4 import cache, func


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (func(100, 200), cache(func(100, 200))),
        (func(500, 800), cache(func(500, 800))),
    ],
)
def test_cache(value: Callable, expected_result: Callable):
    actual_result = cache(value)

    assert actual_result == expected_result
