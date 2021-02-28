"""Homework 1.2.

"""

from collections.abc import Sequence


def fib(n: int):
    """Short description.

    Args:
        n: input number of sequence

    Returns: return fibonacci count
                    Type: int

    """
    if not n:
        return 0
    elif n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def check_fib(seq: Sequence[int]) -> bool:
    """Short description.

    Args:
        seq: input sequence

    Returns: return True: fibonacci sequence, False: not fibonacci sequence

    """
    try:
        for i in range(len(seq)):
            if fib(i) != seq[i]:
                return False
    except TypeError:
        print("Incorrect data type")
        return False
    return True
