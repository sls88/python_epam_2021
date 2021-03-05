"""Homework 1.2."""

from typing import Sequence


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


def check_fibonacci(data: Sequence[int]) -> bool:
    """Check if a sequence is a fibonacci sequence.

    Args:
        data: sequence

    Returns:
        The return value. True if the sequence is Fibonacci sequence

    """
    for i in range(len(data)):
        if fib(i) != data[i]:
            return False
    return True
