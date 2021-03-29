"""TEST Homework 7.1."""
import json
from typing import Any, Dict

import pytest

from hw.hw7.hw7_1_tree import find_occurrences


@pytest.fixture(scope="session")
def example_tree1() -> Dict:
    with open("test/hw7/example_tree1.json", "r") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def example_tree2() -> Dict:
    with open("test/hw7/example_tree2.json", "r") as f:
        return json.load(f)


def test_example_from_the_task(example_tree1):
    actual_result = find_occurrences(example_tree1, "RED")

    assert actual_result == 6


def test_another_type(example_tree2):
    actual_result = find_occurrences(example_tree2, True)

    assert actual_result == 3


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
