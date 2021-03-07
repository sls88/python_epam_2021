"""Homework 1.4.

Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import itertools
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Find the maximum number of tuples.

    Given four lists A, B, C, D of integer values,
    calculates  how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

    Args:
        a, b, c, d: sequences

    Returns:
        The return value. amount of tuples, where A [i] + B [j] + C [k] + D [l] is zero.

    """
    sp1 = [i + j for i, j in itertools.product(a, b)]
    sp2 = [i + j for i, j in itertools.product(c, d)]
    amount_comb = 0
    for i, j in itertools.product(sp1, sp2):
        if i + j == 0:
            amount_comb += 1
    return amount_comb
