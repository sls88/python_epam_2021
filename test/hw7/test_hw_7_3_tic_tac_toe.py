"""TEST Homework 7.3."""
from typing import List

import pytest

from hw.hw7.hw_7_3_tic_tac_toe import tic_tac_toe_checker


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished!"),
        ([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], "unfinished!"),
        ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
        ([["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]], "x wins!"),
        ([["o", "x", "o"], ["-", "o", "x"], ["x", "x", "o"]], "o wins!"),
        ([["x", "o", "x"], ["x", "o", "o"], ["o", "x", "x"]], "draw!"),
        ([["-", "-", "-"], ["o", "o", "o"], ["x", "x", "x"]], "draw!"),
        ([["x", "o", "-"], ["x", "o", "-"], ["x", "o", "-"]], "draw!"),
    ],
)
def test_tic_tac_toe_checker(value: List[List[str]], expected_result: str):
    actual_result = tic_tac_toe_checker(value)

    assert actual_result == expected_result
