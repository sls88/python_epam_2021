"""Homework 2.3."""

from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Return all possible lists of K items where the first element is from the first list, the second is from the second and so one.

    Args:
        *args: sequences

    Returns:
        The return value. sequence of all possible lists

    """
    exp_comb = []
    if len(args) == 1:
        return [*args]
    for number_lst in range(len(args) - 1):
        for i in args[number_lst]:
            for j in args[number_lst + 1]:
                exp_comb.append([i, j])
    return exp_comb
