"""Homework 1.2."""

import logging
from collections import Sequence


def fib(n: int) -> int:
    """Find the fibonacci number.

    Args:
        n: number of sequence

    Returns:
        The return value. fibonacci count

    """
    if not n:
        return 0
    elif n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def check_fib(seq: Sequence[int]) -> bool:
    """Check if a sequence is a fibonacci sequence.

    Args:
        seq: sequence

    Returns:
        The return value. True if the sequence is Fibonacci sequence

    """
    try:
        for i in range(len(seq)):
            if fib(i) != seq[i]:
                return False
    except TypeError:
        logging.error("Incorrect data type")
        return False
    return True
