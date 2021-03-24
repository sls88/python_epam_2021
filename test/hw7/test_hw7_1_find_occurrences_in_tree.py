"""TEST Homework 7.1."""
from typing import Any

import pytest

from hw.hw7.hw7_1_tree import find_occurrences


@pytest.mark.parametrize(
    ("tree", "element", "expected_result"),
    [
        (
            {
                "first": ["RED", "BLUE"],
                "second": {"simple_key": ["simple", "list", "of", "RED", "valued"]},
                "third": {
                    "abc": "BLUE",
                    "jhl": "RED",
                    "complex_key": {
                        "key1": "value1",
                        "key2": "RED",
                        "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
                    },
                },
                "fourth": "RED",
            },
            "RED",
            6,
        ),
        (
            {
                "first": ["RED", True],
                "second": {"simple_key": ["simple", "list", "of", "RED", "valued"]},
                "third": {
                    "abc": "BLUE",
                    "jhl": "RED",
                    "complex_key": {
                        True: "value1",
                        "key2": "RED",
                        "key3": ["a", "lot", "of", "values", {"nested_key": True}],
                    },
                },
                "fourth": "RED",
            },
            True,
            3,
        ),
        ({0: 0}, 0, 2),
        ({0: 0}, 7, 0),
        ({0: 0}, "", 0),
    ],
)
def test_find_occurrences(tree: dict, element: Any, expected_result: int):
    actual_result = find_occurrences(tree, element)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("tree", "element", "expected_result"),
    [
        ({"key": None}, None, 1),
    ],
)
def test_none_negative(tree: dict, element: Any, expected_result: int):
    with pytest.raises(TypeError):
        find_occurrences(tree, element)
