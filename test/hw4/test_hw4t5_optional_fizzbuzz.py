"""TEST Homework 4.5."""

from typing import List

import pytest

from hw.hw4.Homework_4_task5 import fizzbuzz_var1, fizzbuzz_var2


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (
            16,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
                "16",
            ],
        ),
        (1, ["1"]),
    ],
)
def test_fizzbuzz_var1(value: int, expected_result: List[str]):
    actual_result = list(fizzbuzz_var1(value))

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (
            16,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
                "16",
            ],
        ),
        (1, ["1"]),
    ],
)
def test_fizzbuzz_var2(value: int, expected_result: List[str]):
    actual_result = list(fizzbuzz_var2(value))

    assert actual_result == expected_result
