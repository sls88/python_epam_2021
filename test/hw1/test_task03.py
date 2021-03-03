"""TEST Homework 1.3."""

from typing import Tuple

import pytest

from hw.hw1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ("test/hw1/test_task03/some_file.txt", (-53, 123524)),
        ("test/hw1/test_task03/some_file1.txt", (0, 36356)),
        ("test/hw1/test_task03/some_file2.txt", (1, 1)),
        ("test/hw1/test_task03/some_file3.txt", (-8, 19)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
