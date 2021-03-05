"""TEST Homework 2.5."""

import string
from typing import Any, List, Sequence

import pytest


from hw.hw2.hw5 import custom_range


@pytest.mark.parametrize(
    ("expected_result", "seq", "args"),
    [
        (["a", "b", "c", "d", "e", "f"], string.ascii_lowercase, "g"),
        (
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
            string.ascii_lowercase,
            ("g", "p"),
        ),
        (["p", "n", "l", "j", "h"], string.ascii_lowercase, ("p", "g", -2)),
        (
            ["z", "x", "v", "t", "r", "p", "n", "l", "j", "h"],
            string.ascii_lowercase,
            ("g", "step=-2"),
        ),
        ([None, {}, "l"], [1, 3, "l", {}, None, True, ["4"]], (None, 3, -1)),
        ([2, 3, 4, 5, 6], (1, 2, 3, 4, 5, 6, 7, 8), (2, 7)),
        ([2, 5], (1, 2, 3, 4, 5, 6, 7, 8), (2, 7, "step=3")),
        ([2, 5], (1, 2, 3, 4, 5, 6, 7, 8), (2, 7, 3)),
    ],
)
def test_custom_range(expected_result: List, seq: Sequence, args: Any):
    if len(args) == 1:
        actual_result = custom_range(seq, args)
    elif len(args) == 2:
        if str(args[1]).startswith("step="):
            actual_result = custom_range(seq, args[0], step=int(args[1][5:]))
        else:
            actual_result = custom_range(seq, *args)
    else:
        if str(args[2]).startswith("step="):
            actual_result = custom_range(seq, args[0], args[1], int(args[2][5:]))
        else:
            actual_result = custom_range(seq, *args)

    assert actual_result == expected_result
