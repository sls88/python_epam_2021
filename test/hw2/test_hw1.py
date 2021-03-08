"""TEST Homework 2.1."""

from typing import List

import pytest

from hw.hw2.hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (
            "test/hw2/test_hw1/data.txt",
            [
                "Schöpfungsmacht",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "politisch-strategischen",
                "Selbstverständlich",
                "Werkstättenlandschaft",
                "résistance-Bewegungen",
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
            ],
        ),
        (
            "test/hw2/test_hw1/data_f1.txt",
            [
                "ak",
                "ab",
                "aabb",
                "aaabbb",
                "cccccg",
                "gf",
                "hb",
                "abc",
                "sdf",
                "sssssdg",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(value: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ("test/hw2/test_hw1/data.txt", "›"),
        ("test/hw2/test_hw1/data_f1.txt", "k"),
    ],
)
def test_get_rarest_char(value: str, expected_result: str):
    actual_result = get_rarest_char(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ("test/hw2/test_hw1/data.txt", 5475),
        ("test/hw2/test_hw1/data_f1.txt", 11),
    ],
)
def test_count_punctuation_chars(value: str, expected_result: int):
    actual_result = count_punctuation_chars(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ("test/hw2/test_hw1/data.txt", 2972),
        ("test/hw2/test_hw1/data_f1.txt", 0),
        ("test/hw2/test_hw1/data_f4.txt", 3),
    ],
)
def test_count_non_ascii_chars(value: str, expected_result: int):
    actual_result = count_non_ascii_chars(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ("test/hw2/test_hw1/data.txt", "ä"),
        ("test/hw2/test_hw1/data_f1.txt", "empty sequence"),
        ("test/hw2/test_hw1/data_f4.txt", "Ü"),
    ],
)
def test_get_most_common_non_ascii_char(value: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(value)

    assert actual_result == expected_result
