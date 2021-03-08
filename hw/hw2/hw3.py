"""Homework 2.3."""

import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Return all possible lists of K items where the first element is from the first list, the second is from the second and so one.

    Args:
        *args: sequences

    Returns:
        The return value. sequence of all possible lists

    """
    return [
        [*j]
        for i in range(len(args) - 1)
        for j in itertools.product(args[i], args[i + 1])
    ]
