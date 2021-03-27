"""TEST Homework 7.1."""
from typing import Any, Dict

import pytest

from hw.hw7.hw7_1_tree import find_occurrences


@pytest.fixture()
def example_tree1() -> Dict:
    return {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
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
    }


@pytest.fixture()
def example_tree2() -> Dict:
    return {
        True: ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", True, "values", {"nested_key": True}],
            },
        },
        "fourth": True,
    }


def test_example_from_the_task(example_tree1):
    actual_result = find_occurrences(example_tree1, "RED")

    assert actual_result == 6


def test_another_type(example_tree2):
    actual_result = find_occurrences(example_tree2, True)

    assert actual_result == 4


@pytest.mark.parametrize(
    ("tree", "element", "expected_result"),
    [
        ({0: 0}, 0, 2),
        ({0: 0}, 7, 0),
        ({0: 0}, "", 0),
    ],
)
def test_find_occurrences(tree: Dict, element: Any, expected_result: int):
    actual_result = find_occurrences(tree, element)

    assert actual_result == expected_result


def test_none_negative():
    tree = {"key": None}
    element = None
    with pytest.raises(TypeError):
        find_occurrences(tree, element)
