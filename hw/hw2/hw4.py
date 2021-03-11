"""Homework 2.4."""

from typing import Any, Callable, Tuple


def func(a: int, b: int) -> int:
    """Find (a ** b) ** 2.

    Args:
        a: number
        b: number

    Returns:
        The return value. return (a ** b) ** 2
    """
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    """Cache the result of the function, return from the cache if the function is called again.

    Args:
        function: the function to cache.

    Returns:
        The return value. ranged list of elements
    """
    results = {}

    def function(*some: Tuple[Any]) -> Any:
        """Cache the result of the function, return from the cache if the function is called again.

        Args:
            *some: arguments

        Returns:
            The return value. func(*some) or results[some]
        """
        if some not in results:
            results[some] = func(*some)
        return results[some]

    return function
