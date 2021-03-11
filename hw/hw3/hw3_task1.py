"""Homework 3.1."""

from typing import Any, Callable, Tuple


def cache(times: int) -> Callable:
    """Set call limit.

    Args:
        times: call limit.

    Returns:
        The return value. function cache_func
    """

    def cache_func(func: Callable) -> Callable:
        """Cache the result of the function, return from the cache if the function is called again.

        Args:
            func: the function to cache.

        Returns:
            The return value. function
        """
        results = {}
        count = 0

        def function(*args: Tuple[Any]) -> Any:
            """Cache the result of the function, return from the cache if the function is called again.

            Args:
                *args: arguments

            Returns:
                The return value. results[args] or if the function is called 'times' times: cache_func(func)(*args)
            """
            nonlocal count
            if args not in results:
                results[args] = func(*args)
            if count <= times:
                count += 1
                return results[args]
            else:
                count = 0
                return cache_func(func)(*args)

        return function

    return cache_func
