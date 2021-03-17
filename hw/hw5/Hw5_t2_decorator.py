"""Homework 5.2."""

from typing import Any, Callable, Dict, Tuple


def wrap(func: Callable) -> Callable:
    """Copy function attributes to wrapper class.

    Args:
        f: original function.

    Returns:
        The return value. wrapper class
    """

    class Wrapper:
        """Override methods in a wrapper class."""

        __doc__ = func.__doc__
        __name__ = func.__name__

        def __init__(self, func: Callable):
            self.func = func

        def __call__(self, *args: Tuple[Any], **kwargs: Dict[Any, Any]):
            pass

        def __add__(self, other: Any) -> Any:
            return other

    Wrapper.__original_func = func
    return Wrapper
