"""Homework 3.4."""


def is_armstrong(number: int) -> bool:
    """Detect if a number is Armstrong number.

    Args:
        number: number

    Returns:
        The return value. True if is Armstrong number

    """
    a = list(map(int, str(number)))
    return sum(list(map(lambda x: x ** 3, a))) == number
