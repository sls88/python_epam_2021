"""TEST Homework 3.3."""

from typing import Any, List, Tuple

import pytest

from hw.hw3.hw3_task3 import make_filter


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (
            (
                {"name": "polly", "type": "bird"},
                [
                    {
                        "name": "Bill",
                        "last_name": "Gilbert",
                        "occupation": "was here",
                        "type": "person",
                    },
                    {
                        "is_dead": True,
                        "kind": "parrot",
                        "type": "bird",
                        "name": "polly",
                    },
                ],
            ),
            [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}],
        ),
        (
            (
                {"name": "Bill"},
                [
                    {
                        "name": "Bill",
                        "last_name": "Gilbert",
                        "occupation": "was here",
                        "type": "person",
                    },
                    {
                        "is_dead": True,
                        "kind": "parrot",
                        "type": "bird",
                        "name": "polly",
                    },
                ],
            ),
            [
                {
                    "name": "Bill",
                    "last_name": "Gilbert",
                    "occupation": "was here",
                    "type": "person",
                }
            ],
        ),
        (
            (
                {"name": "Bill", "kind": "parrot"},
                [
                    {
                        "name": "Bill",
                        "last_name": "Gilbert",
                        "occupation": "was here",
                        "type": "person",
                    },
                    {
                        "is_dead": True,
                        "kind": "parrot",
                        "type": "bird",
                        "name": "polly",
                    },
                ],
            ),
            [
                {
                    "name": "Bill",
                    "last_name": "Gilbert",
                    "occupation": "was here",
                    "type": "person",
                },
                {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
            ],
        ),
    ],
)
def test_filter_class(value: Tuple[Any], expected_result: List[Any]):
    actual_result = make_filter(**value[0]).apply(value[1])

    assert actual_result == expected_result
