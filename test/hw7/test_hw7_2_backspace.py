"""TEST Homework 7.2."""
import pytest

from hw.hw7.hw7_2_backspace import backspace_compare, backspace_compare2


@pytest.mark.parametrize(
    ("first", "second", "expected_result"),
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("##a#c", "####c", True),
        ("a##", "###", True),
        ("", "", True),
        ("a", "b", False),
    ],
)
def test_backspace_recursion_variant(first: str, second: str, expected_result: bool):
    actual_result = backspace_compare(first, second)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("first", "second", "expected_result"),
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("##a#c", "####c", True),
        ("a##", "###", True),
        ("", "", True),
        ("a", "b", False),
    ],
)
def test_backspace_second_variant(first: str, second: str, expected_result: bool):
    actual_result = backspace_compare2(first, second)

    assert actual_result == expected_result
